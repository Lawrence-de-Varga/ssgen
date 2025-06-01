from enum import Enum
from htmlnode import LeafNode
from decorators import type_check_decorator


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text="", text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


@type_check_decorator([TextNode])
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise ValueError(f"Invalid TextType: {text_node.text_type}")

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            if not text_node.url:
                raise ValueError("Missing Url for href tag")
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )
        case TextType.IMAGE:
            if not text_node.url:
                raise ValueError("Missing Url for image")
            return LeafNode(
                tag="img", value="", props={"src": text_node.url, "alt": text_node.text}
            )
