from decorators import type_check_decorator
from textnode import TextNode, TextType
import re


@type_check_decorator([str])
def extract_markdown_images(text: str) -> list[tuple]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


@type_check_decorator([str])
def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


@type_check_decorator([str])
def split_nodes_link(text: str):
    links = dict(extract_markdown_links(text))
    print(links)

    split_text = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    nodes = []
    for string in split_text:
        if string in links.keys():
            nodes.append(TextNode(string, text_type=TextType.LINK, url=links[string]))
            continue

        if string in links.values():
            continue

        nodes.append(TextNode(string, text_type=TextType.TEXT))

    return nodes


@type_check_decorator([str])
def split_nodes_image(text: str):
    links = dict(extract_markdown_images(text))
    print(links)

    split_text = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    nodes = []
    for string in split_text:
        if string in links.keys():
            nodes.append(TextNode(string, text_type=TextType.IMAGE, url=links[string]))
            continue

        if string in links.values():
            continue

        nodes.append(TextNode(string, text_type=TextType.TEXT))

    return nodes
