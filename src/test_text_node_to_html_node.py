import unittest
from textnode import (
    TextNode,
    TextType,
    text_node_to_html_node,
)
from htmlnode import LeafNode
from enum import Enum


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type_text(self):
        node = TextNode("Hello world", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(node), LeafNode(value="Hello world"))

    def test_text_type_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        self.assertEqual(
            text_node_to_html_node(node), LeafNode(tag="b", value="Bold text")
        )

    def test_text_type_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        self.assertEqual(
            text_node_to_html_node(node), LeafNode(tag="i", value="Italic text")
        )

    def test_text_type_code(self):
        node = TextNode("print('Hello')", TextType.CODE)
        self.assertEqual(
            text_node_to_html_node(node), LeafNode(tag="code", value="print('Hello')")
        )

    def test_text_type_link(self):
        node = TextNode("Click me", TextType.LINK, "https://example.com")
        self.assertEqual(
            text_node_to_html_node(node),
            LeafNode(tag="a", value="Click me", props={"href": "https://example.com"}),
        )

    def test_text_type_image(self):
        node = TextNode("logo", TextType.IMAGE, "https://example.com/logo.png")
        self.assertEqual(
            text_node_to_html_node(node),
            LeafNode(
                tag="img",
                value="",
                props={"src": "https://example.com/logo.png", "alt": "logo"},
            ),
        )

    def test_invalid_text_type(self):
        class FakeType(Enum):
            FAKE = "fake"

        node = TextNode("Test", FakeType.FAKE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_link_missing_url(self):
        node = TextNode("Missing URL", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_image_missing_url(self):
        node = TextNode("Missing URL", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(node), LeafNode(value=""))

    def test_whitespace_text(self):
        node = TextNode("   ", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(node), LeafNode(value="   "))

    def test_special_characters(self):
        node = TextNode("<>&'\"", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(node), LeafNode(value="<>&'\""))

    def test_none_text(self):
        node = TextNode(None, TextType.TEXT)
        with self.assertRaises(AttributeError):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
