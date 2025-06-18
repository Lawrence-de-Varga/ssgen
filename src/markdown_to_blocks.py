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


md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""


bmd = """

# 100-Line Markdown Document

## Section 1: Introduction

This document contains exactly 100 lines of Markdown content.

> "First quote demonstrating blockquote syntax."

## Section 2: Core Elements

### Paragraph Example

This is the first paragraph spanning a single line.

This is the second paragraph on its own line.

```python
# Python code block
def example():
    return True
```

### Unordered List

- First list item
- Second list item
  - Nested item A
  - Nested item B
- Third list item

## Section 3: Ordered Content

1. First numbered item
2. Second numbered item
   1. Nested number A
   2. Nested number B
3. Third numbered item

> "Second quote showing multi-line  
> blockquote formatting."

```javascript
// JavaScript example
console.log("Hello World");
```

## Section 4: Repeating Patterns

- Repeat list item 1
- Repeat list item 2
- Repeat list item 3

1. Repeat number 1
2. Repeat number 2
3. Repeat number 3

```bash
# Shell command
ls -la
```

This paragraph continues the content flow.

> "Third quote demonstrating consistency."

## Section 5: More Examples

### Code Variants

```html
<p>Sample HTML</p>
```

```yaml
config:
  enabled: true
```

### Final Lists

- Final item A
- Final item B
- Final item C

1. Last number 1
2. Last number 2
3. Last number 3

## Section 6: Conclusion

This concludes the 100-line document.

> "Final quote ending the example."

```text
Plain text block to
reach line count
```

# END
"""
