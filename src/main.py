from pathlib import Path
from shutil import copytree
from stat_to_pub import delete_all_contents
from generate_page import generate_pages


def main():
    PUBLIC = "./public/"
    STATIC = "./static/"

    public = Path(PUBLIC).resolve()
    static = Path(STATIC).resolve()

    if not public.exists():
        raise ValueError(f"Error: '{public}' path does not exist.")

    if not static.exists():
        raise ValueError(f"Error: '{static}' path does not exist.")

    delete_all_contents(public)

    copytree(static, public, dirs_exist_ok=True)

    root = Path("./content/").resolve()
    source = Path("./content/").resolve()
    template = Path("./template.html").resolve()
    dest = Path("./public/").resolve()

    generate_pages(
        root,
        source,
        template,
        dest,
    )


if __name__ == "__main__":
    main()
