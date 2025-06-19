from decorators import type_check
from enum import Enum
from slice_on_delim import starts_with, ends_with, mstarts_with


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


@type_check([str])
def markdown_to_blocks(md_string: str) -> list[str]:
    """
    Assumes a well formed markdown string.
    Returns a list of strings coresponding to
    markdown blocks.
    """
    blocks = md_string.split("\n\n")
    blocks = [block.strip() for block in blocks]
    return blocks


@type_check([str])
def md_heading_check(md: str) -> bool:
    """
    Returns True if provided string is a markdown heading.
    """
    headings = [
        "# ",
        "## ",
        "### ",
        "#### ",
        "##### ",
        "###### ",
    ]

    if mstarts_with(headings, md):
        return True
    else:
        return False


@type_check([str])
def md_code_check(md: str) -> bool:
    return starts_with("```", md) and ends_with("```", md)


@type_check([str, str])
def md_line_type_check(md: str, check_char: str) -> bool:
    lines = md.split("\n")
    for line in lines:
        if not starts_with(check_char, line.lstrip()):
            return False
    return True


@type_check([str])
def md_quote_check(md: str) -> bool:
    return md_line_type_check(md, ">")


@type_check([str])
def md_ul_check(md: str) -> bool:
    return md_line_type_check(md, "- ")


# Does not account for nested list atm.
@type_check([str])
def md_ol_check(md: str) -> bool:
    lines = md.split("\n")
    idx = 1
    for line in lines:
        if not starts_with(f"{idx}. ", line):
            return False
        idx += 1

    return True


@type_check([str])
def block_to_block_type(md_block: str) -> BlockType:
    """
    Returns the BlockType of a given block.
    """
    if md_heading_check(md_block):
        return BlockType.HEADING
    if md_code_check(md_block):
        return BlockType.CODE
    if md_quote_check(md_block):
        return BlockType.QUOTE
    if md_ul_check(md_block):
        return BlockType.UNORDERED_LIST
    if md_ol_check(md_block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
