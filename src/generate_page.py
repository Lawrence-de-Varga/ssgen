from pathlib import Path
from decorators import type_check
from blocks_to_html import block_to_block_type, BlockType
from slice_on_delim import starts_with


@type_check([list[str]])
def extract_title(blocks: list[str]):
    """
    Takes a list of markdown blocks as
    returned by markdown_to_blocks
    and extracts athe first <h1>/'# '
    heading from it to use as the
    title for the webpage.
    """
    headings = [
        block for block in blocks if block_to_block_type(block) == BlockType.HEADING
    ]

    for heading in headings:
        if starts_with("# ", heading):
            return heading.lstrip("# ")

    raise ValueError(f"Error: no <h1> ('# ') heading block found in {blocks}.")
