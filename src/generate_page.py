from pathlib import Path
from md_blocks_to_html_node import md_blocks_to_html_node
from decorators import type_check
from md_doc_to_md_blocks import block_to_block_type, BlockType
from slice_on_delim import starts_with
from md_doc_to_md_blocks import md_doc_to_md_blocks


@type_check([list])
def extract_title(blocks: list[str]):
    """
    Takes a list of markdown blocks as
    returned by markdown_to_blocks
    and extracts athe first <h1>/'# '
    heading from it to use as the
    title for the webpage.
    """
    try:
        headings = [
            block for block in blocks if block_to_block_type(block) == BlockType.HEADING
        ]
    except TypeError as e:
        raise TypeError(
            f"Error: extract_title requires a list of valid md blocks as strings. {e}"
        )

    for heading in headings:
        if starts_with("# ", heading):
            return heading.lstrip("# ")

    raise ValueError(f"Error: no <h1> ('# ') heading block found in {blocks}.")


@type_check([Path, Path, Path])
def generate_page(from_path, template_path, dest_path) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    if not from_path.exists():
        raise FileNotFoundError(f"Error: '{from_path}' does not exist.")
    if not from_path.is_file():
        raise ValueError(f"Error: {from_path} must be a file.")

    if not template_path.exists():
        raise FileNotFoundError(f"Error: '{template_path}' does not exist.")
    if not template_path.exists() or not template_path.is_file():
        raise ValueError(f"Error: {template_path} must exist and be a file.")

    with open(from_path, "r") as fp:
        md_doc = fp.read()

    with open(template_path, "r") as tp:
        template = tp.read()

    try:
        blocks = md_doc_to_md_blocks(md_doc)
    except Exception as e:
        raise Exception(f"Error: mt_to_blocks failed with error: {e}")

    try:
        html_nodes = md_blocks_to_html_node(blocks)
    except Exception as e:
        raise Exception(f"Error: md_doc_to_html_nodes failed with error: {e}")

    try:
        html = html_nodes.to_html()
    except Exception as e:
        raise Exception(f"Error: htmlnodes.to_html() failed with error: {e}")

    title = extract_title(blocks)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    if dest_path.exists():
        print("writing to existing index.html")
        if not dest_path.is_file():
            raise ValueError(f"Error: if {dest_path} exists it must be a file.")
        with open(dest_path, "w") as dp:
            dp.write(template)
    elif dest_path.parent.exists():
        print("writing new index.html")
        with open(dest_path, "w") as dp:
            dp.write(template)
    else:
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dest_path, "w") as dp:
            dp.write(template)


@type_check([Path, Path, Path])
def generate_pages(root_dir_path, from_dir_path, template_path, dest_dir_path) -> None:
    if not from_dir_path.exists():
        raise FileNotFoundError(f"Error: '{from_dir_path}' does not exist.")
    if not from_dir_path.is_dir():
        raise ValueError(f"Error: '{from_dir_path}' must be a directory.")

    if not root_dir_path.exists():
        raise FileNotFoundError(f"Error: '{root_dir_path}' does not exist.")
    if not root_dir_path.is_dir():
        raise ValueError(f"Error: '{root_dir_path}' must be a directory.")

    if not dest_dir_path.exists():
        raise FileNotFoundError(f"Error: '{dest_dir_path}' does not exist.")
    if not dest_dir_path.is_dir():
        raise ValueError(f"Error: '{dest_dir_path}' must be a directory.")

    if not template_path.exists():
        raise FileNotFoundError(f"Error: '{template_path}' does not exist.")
    if not template_path.is_file():
        raise ValueError(f"Error: '{template_path}' must be a file.")

    for item in from_dir_path.iterdir():
        if item.is_file():
            if item.name == "index.md":
                dest_path = Path(
                    # creates the sub path relative to the root path that will be
                    # copied into dest_dir
                    item.absolute().relative_to(root_dir_path).parent / "index.html"
                )
                # Full path for new 'index.html' file in dest_dir
                dest_path = Path(dest_dir_path / dest_path)

                generate_page(item.absolute(), template_path, dest_path)
            else:
                continue

        else:
            generate_pages(root_dir_path, item, template_path, dest_dir_path)
