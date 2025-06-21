import sys
from pathlib import Path

src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from shutil import copytree

from stat_to_pub import delete_all_contents

PUBLIC = "public/"
STATIC = "static/"

public = Path(PUBLIC).resolve()
static = Path(STATIC).resolve()


def main():
    if not public.exists():
        raise ValueError(f"Error: '{public}' path does not exist.")

    if not static.exists():
        raise ValueError(f"Error: '{static}' path does not exist.")

    delete_all_contents(public)

    copytree(static, public, dirs_exist_ok=True)


if __name__ == "__main__":
    main()
