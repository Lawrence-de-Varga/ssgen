from decorators import type_check_decorator
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


@type_check_decorator([str])
def markdown_to_blocks(md_string: str) -> list[str]:
    """
    Assumes a well formed markdown string.
    Returns a list of strings coresponding to
    markdown blocks.
    """
    blocks = md_string.split("\n\n")
    blocks = [block.strip() for block in blocks]
    return blocks


md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
