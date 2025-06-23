from sys import argv
from pathlib import Path
from shutil import copytree
from stat_to_pub import delete_all_contents
from generate_page import generate_pages


def main():
    try:
        basepath = argv[1]
    except IndexError as e:
        basepath = "/"

    DOCS = "./docs/"
    STATIC = "./static/"

    docs = Path(DOCS).resolve()
    static = Path(STATIC).resolve()

    if not docs.exists():
        raise ValueError(f"Error: '{docs}' path does not exist.")

    if not static.exists():
        raise ValueError(f"Error: '{static}' path does not exist.")

    delete_all_contents(docs)

    copytree(static, docs, dirs_exist_ok=True)

    root = Path("./content/").resolve()
    source = Path("./content/").resolve()
    template = Path("./template.html").resolve()
    dest = Path("./docs/").resolve()

    generate_pages(
        root,
        source,
        template,
        dest,
        basepath,
    )


if __name__ == "__main__":
    main()
