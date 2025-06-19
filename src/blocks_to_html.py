from decorators import type_check
from textnode import TextNode, text_node_to_html_node, TextType
from markdown_to_blocks import block_to_block_type, markdown_to_blocks, BlockType
from slice_on_delim import starts_with, ends_with
from htmlnode import ParentNode, HTMLNode, LeafNode
from process_text_nodes import process_md_paragraph


@type_check([str])
def md_text_to_html_nodes(md: str) -> list[HTMLNode]:
    tnodes = process_md_paragraph(md)
    html_nodes = [text_node_to_html_node(node) for node in tnodes]
    return html_nodes


@type_check([str])
def heading_block_to_heading_node(block: str) -> ParentNode:
    headings = {
        "# ": "h1",
        "## ": "h2",
        "### ": "h3",
        "#### ": "h4",
        "##### ": "h5",
        "###### ": "h6",
    }

    heading = ""
    for h in headings:
        if starts_with(h, block):
            heading = headings[h]
            md_head = h
    if heading == "":
        raise ValueError(f"Error: '{block}' is not a valid md heading.")

    text = block.lstrip(md_head)
    children = md_text_to_html_nodes(text)
    return ParentNode(heading, children)


@type_check([str])
def quote_block_to_quote_node(block: str) -> ParentNode:
    if not starts_with("> ", block):
        raise ValueError(f"Error: '{block}' is not a valid md quote.")

    text = block.lstrip("> ")
    children = md_text_to_html_nodes(text)
    return ParentNode("blockquote", children)


@type_check([str])
def code_block_to_code_node(block: str) -> LeafNode:
    if not starts_with("```", block) and ends_with("```", block):
        raise ValueError(f"Error: {block} is not a valid md block.")

    text = block.strip("```")
    text_node = TextNode(text, text_type=TextType.CODE)
    leaf_node = text_node_to_html_node(text_node)
    return leaf_node


def pp(thing):
    idx = 0
    for item in thing:
        print(item)
        print()
        print(block_to_block_type(item))
        print(idx)
        idx += 1
        print(
            "-------------------------------------------------------------------------------------------------------------------"
        )
        print()


with open("../markdown_sample.md") as f:
    mds1 = f.read()
with open("../markdown_sample_2.md") as f:
    mds2 = f.read()
with open("../markdown_sample_3.md") as f:
    mds3 = f.read()
with open("../markdown_sample_4.md") as f:
    mds4 = f.read()
with open("../markdown_sample_5.md") as f:
    mds5 = f.read()
with open("../markdown_sample_6.md") as f:
    mds6 = f.read()
with open("../markdown_sample_7.md") as f:
    mds7 = f.read()

blocks = markdown_to_blocks(mds7)
