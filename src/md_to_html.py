from decorators import type_check
from textnode import TextNode, text_node_to_html_node, TextType
from markdown_to_blocks import block_to_block_type, markdown_to_blocks, BlockType
from slice_on_delim import starts_with, ends_with
from htmlnode import ParentNode, HTMLNode, LeafNode
from process_text_nodes import process_md_paragraph


@type_check([str])
def md_doc_to_html_nodes(doc: str) -> ParentNode:
    """
    Takes a markdown document and returns the
    a ParentNode whose children represent
    the whole document as HTML, Leaf and Parent
    nodes.
    """
    blocks = markdown_to_blocks(doc)

    children = []
    for block in blocks:
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            children.append(paragraph_block_to_paragraph_node(block))
            continue
        if block_to_block_type(block) == BlockType.CODE:
            children.append(code_block_to_code_node(block))
            continue
        if block_to_block_type(block) == BlockType.HEADING:
            children.append(heading_block_to_heading_node(block))
            continue
        if block_to_block_type(block) == BlockType.QUOTE:
            children.append(quote_block_to_quote_node(block))
            continue
        if block_to_block_type(block) == BlockType.UNORDERED_LIST:
            children.append(ul_block_to_ul_node(block))
            continue
        if block_to_block_type(block) == BlockType.ORDERED_LIST:
            children.append(ol_block_to_ol_node(block))

    return ParentNode("div", children)


@type_check([str])
def md_paragraph_to_html_nodes(md: str) -> list[HTMLNode]:
    """
    Takes md text with possible inline elements and
    turns it into a list of TextNode and then a list
    of htmlnodes which are then returned.
    """
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
    children = md_paragraph_to_html_nodes(text)
    return ParentNode(heading, children)


@type_check([str])
def quote_block_to_quote_node(block: str) -> ParentNode:
    if not starts_with("> ", block):
        raise ValueError(f"Error: '{block}' is not a valid md quote.")

    text = block.lstrip("> ")
    children = md_paragraph_to_html_nodes(text)
    return ParentNode("blockquote", children)


@type_check([str])
def code_block_to_code_node(block: str) -> LeafNode:
    if not starts_with("```", block) and ends_with("```", block):
        raise ValueError(f"Error: {block} is not a valid md block.")

    text = block.strip("```")
    text_node = TextNode(text, text_type=TextType.CODE)
    child = text_node_to_html_node(text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


@type_check([str])
def paragraph_block_to_paragraph_node(block: str) -> ParentNode:
    children = md_paragraph_to_html_nodes(block)
    return ParentNode("p", children)


@type_check([str])
def ul_block_to_ul_node(block: str) -> ParentNode:
    list_items = block.split("\n")
    list_items = [block.lstrip("- ") for block in list_items]
    p_list = []
    for li in list_items:
        children = md_paragraph_to_html_nodes(li)
        par = ParentNode("li", children)
        p_list.append(par)
    return ParentNode("ul", p_list)


@type_check([str])
def ol_block_to_ol_node(block: str) -> ParentNode:
    list_items = block.split("\n")
    idx = 1
    new_list_items = []
    for li in list_items:
        new_list_items.append(li.lstrip(f"{idx}. "))
        idx += 1

    p_list = []
    for li in new_list_items:
        children = md_paragraph_to_html_nodes(li)
        par = ParentNode("li", children)
        p_list.append(par)
    return ParentNode("ol", p_list)


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


with open("../sample_md/markdown_sample_1.md") as f:
    mds1 = f.read()
with open("../sample_md/markdown_sample_2.md") as f:
    mds2 = f.read()
with open("../sample_md/markdown_sample_3.md") as f:
    mds3 = f.read()
with open("../sample_md/markdown_sample_4.md") as f:
    mds4 = f.read()
with open("../sample_md/markdown_sample_5.md") as f:
    mds5 = f.read()
with open("../sample_md/markdown_sample_6.md") as f:
    mds6 = f.read()
with open("../sample_md/markdown_sample_7.md") as f:
    mds7 = f.read()
with open("../sample_md/site.md") as f:
    site = f.read()


blocks = markdown_to_blocks(mds7)
