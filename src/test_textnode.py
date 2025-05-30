import unittest
from textnode import TextNode, TextType


class TestTextNodeEquality(unittest.TestCase):
    def test_eq_equal_nodes(self):
        node1 = TextNode("Sample text", TextType.TEXT, "https://example.com")
        node2 = TextNode("Sample text", TextType.TEXT, "https://example.com")
        self.assertEqual(node1, node2)

    def test_eq_different_text(self):
        node1 = TextNode("Text 1", TextType.TEXT, "https://example.com")
        node2 = TextNode("Text 2", TextType.TEXT, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_type(self):
        node1 = TextNode("Same text", TextType.BOLD, "https://example.com")
        node2 = TextNode("Same text", TextType.ITALIC, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_different_url(self):
        node1 = TextNode("Same text", TextType.TEXT, "https://example.com/1")
        node2 = TextNode("Same text", TextType.TEXT, "https://example.com/2")
        self.assertNotEqual(node1, node2)

    def test_eq_one_url_none(self):
        node1 = TextNode("Same text", TextType.TEXT, "https://example.com")
        node2 = TextNode("Same text", TextType.TEXT, None)
        self.assertNotEqual(node1, node2)

    def test_eq_both_urls_none(self):
        node1 = TextNode("Same text", TextType.TEXT, None)
        node2 = TextNode("Same text", TextType.TEXT, None)
        self.assertEqual(node1, node2)

    def test_eq_compare_with_non_textnode(self):
        node = TextNode("Text", TextType.TEXT, "https://example.com")
        other_object = "Not a TextNode"
        self.assertNotEqual(node, other_object)

    def test_eq_empty_text(self):
        node1 = TextNode("", TextType.TEXT, "https://example.com")
        node2 = TextNode("", TextType.TEXT, "https://example.com")
        self.assertEqual(node1, node2)

    def test_eq_case_sensitive_text(self):
        node1 = TextNode("TEXT", TextType.TEXT, "https://example.com")
        node2 = TextNode("text", TextType.TEXT, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_case_sensitive_url(self):
        node1 = TextNode("Text", TextType.TEXT, "https://EXAMPLE.com")
        node2 = TextNode("Text", TextType.TEXT, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Test", TextType.CODE, "http://test.com")
        self.assertEqual(repr(node), "TextNode(Test, code, http://test.com)")


if __name__ == "__main__":
    unittest.main()
