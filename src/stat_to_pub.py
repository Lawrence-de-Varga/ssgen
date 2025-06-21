from decorators import type_check
from pathlib import Path

PUBLIC = "/home/ldv/workspace/github.com/lawrence-de-varga/ssgen/public/"
STATIC = "/home/ldv/workspace/github.com/lawrence-de-varga/ssgen/static/"


public = Path(PUBLIC)
static = Path(STATIC)

if not public.exists():
    raise ValueError(f"Error: '{public}' path does not exist.")

if not static.exists():
    raise ValueError(f"Error: '{static}' path does not exist.")


@type_check([Path])
def delete_all_files(directory: Path):
    """
    Deletes all files in the given directory and
    its sub directories.
    """
    if not directory.exists():
        raise ValueError(f"Error: '{directory}' does not exist.")
    if not directory.is_dir():
        raise ValueError(f"Error: '{directory}' is not a directory.")

    items = directory.iterdir()

    for i in items:
        if i.is_file():
            i.unlink()

    items = directory.iterdir()

    for i in items:
        delete_all_files(i)


@type_check([Path])
def is_empty_dir(directory: Path) -> bool:
    if not directory.exists():
        raise ValueError(f"Error: '{directory}' does not exist.")
    if not directory.is_dir():
        raise ValueError(f"Error: '{directory}' is not a directory.")

    if len(list(directory.iterdir())) == 0:
        return True

    return False


@type_check([Path])
def delete_all_directories(directory: Path):
    """
    Used after delete_all_files to delete all the remaining empty
    directories.
    """
    if not directory.exists():
        raise ValueError(f"Error: '{directory}' does not exist.")
    if not directory.is_dir():
        raise ValueError(f"Error: '{directory}' is not a directory.")

    items = directory.iterdir()

    for i in items:
        if is_empty_dir(i):
            i.rmdir()
            continue
        delete_all_directories(i)
        i.rmdir()


@type_check([Path])
def delete_all_contents(directory: Path):
    if not directory.exists():
        raise ValueError(f"Error: '{directory}' does not exist.")
    if not directory.is_dir():
        raise ValueError(f"Error: '{directory}' is not a directory.")

    try:
        delete_all_files(directory)
    except Exception as e:
        raise Exception(
            f"Error: operation 'delete_all_files' has failed with errror: {e}."
        )

    try:
        delete_all_directories(directory)
    except Exception as e:
        raise Exception(
            f"Error: operation 'delete_all_directories' has failed with errror: {e}."
        )


p = Path("/home/ldv/workspace/github.com/lawrence-de-varga/ssgen/src/testing/")
