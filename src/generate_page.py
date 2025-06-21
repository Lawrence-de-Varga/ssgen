from pathlib import Path
from md_blocks_to_html_node import md_blocks_to_html_node
from decorators import type_check
from blocks_to_html import block_to_block_type, BlockType
from slice_on_delim import starts_with
from md_doc_to_md_blocks import md_doc_to_md_blocks


@type_check([list[str]])
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
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    if not from_path.exists() or not from_path.is_file():
        raise ValueError(f"Error: {from_path} must exist and be a file.")

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

    template.replace("{{ Title }}", title)
    template.replace("{{ Content }}", html)

    if dest_path.exists():
        if not dest_path.is_file():
            raise ValueError(f"Error: if {dest_path} exists it must be a file.")
        with open(dest_path, "w") as dp:
            dp.write(template)
    elif dest_path.parent.exists():
        with open(dest_path, "w") as dp:
            dp.write(template)
    else:
        raise ValueError(f"Error: {dest_path.parent} does not exist.")
