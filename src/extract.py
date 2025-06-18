import re

from decorators import type_check_decorator
from textnode import TextNode, TextType
from collections.abc import Callable
import slice_on_delim as sd


@type_check_decorator([str])
def extract_markdown_images(text: str) -> list[tuple]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


@type_check_decorator([str])
def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


# @type_check_decorator([str])
def split_node_links(node: TextNode):
    text = node.text
    links = dict(extract_markdown_links(text))

    split_text = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    nodes = []
    for string in split_text:
        # If string is a link description create a link node
        if string in links.keys():
            nodes.append(TextNode(string, text_type=TextType.LINK, url=links[string]))
            continue

        # if string is a link, ignore it as it has been added to a previous link node
        if string in links.values():
            continue

        # everything else is presumed to be text
        nodes.append(TextNode(string, text_type=node.text_type, url=node.url))

    return nodes


# @type_check_decorator([str])
def split_node_images(node: TextNode):
    text = node.text
    links = dict(extract_markdown_images(text))

    split_text = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    nodes = []
    for string in split_text:
        # If string is an image description create an image node
        if string in links.keys():
            nodes.append(TextNode(string, text_type=TextType.IMAGE, url=links[string]))
            continue

        # if string is an image link, ignore as it has been dealt with.
        if string in links.values():
            continue

        # everything else is presumed to be text
        nodes.append(TextNode(string, text_type=node.text_type, url=node.url))

    return nodes


def split_nodes(old_nodes: list[TextNode], splitter: Callable) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        new_nodes.extend(splitter(node))

    return new_nodes


def process_nodes(old_nodes: list[TextNode]) -> list[TextNode]:
    pass


a = TextNode(
    "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
    text_type=TextType.TEXT,
)
b = a.text
c = "I **love** cheese. I --really really-- do."
c += b
d = sd.mmsplit(["**", "--"], c)
e = sd.process_split_string(["**", "--"], d)
