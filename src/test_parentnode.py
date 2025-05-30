import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_init(self):
        # Test basic initialization
        children = [LeafNode("p", "Child node")]
        node = ParentNode("div", children)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, children)
        self.assertIsNone(node.props)

        # Test with props
        props = {"class": "container"}
        node = ParentNode("div", children, props)
        self.assertEqual(node.props, props)

    def test_to_html_simple(self):
        # Single child
        child = LeafNode("span", "hello")
        node = ParentNode("div", [child])
        self.assertEqual(node.to_html(), "<div><span>hello</span></div>")

        # Multiple children
        children = [
            LeafNode("b", "bold"),
            LeafNode(None, "normal"),
            LeafNode("i", "italic"),
        ]
        node = ParentNode("p", children)
        expected = "<p><b>bold</b>normal<i>italic</i></p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_props(self):
        children = [LeafNode("span", "content")]
        node = ParentNode("div", children, {"id": "main", "class": "box"})
        expected = '<div id="main" class="box"><span>content</span></div>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_nested(self):
        # Test nested parent nodes
        inner_child = LeafNode("b", "bold text")
        inner_parent = ParentNode("span", [inner_child])
        outer_parent = ParentNode("div", [inner_parent])

        expected = "<div><span><b>bold text</b></span></div>"
        self.assertEqual(outer_parent.to_html(), expected)

    def test_validation(self):
        # Test missing tag
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("p", "test")]).to_html()
        self.assertEqual(str(context.exception), "Parent nodes must have a tag")

        # Test missing children
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None).to_html()
        self.assertEqual(str(context.exception), "Parent nodes must have children")

        # Test empty children
        with self.assertRaises(ValueError) as context:
            ParentNode("div", []).to_html()
        self.assertEqual(str(context.exception), "Parent nodes must have children")

    def test_edge_cases(self):
        # Test with various child types
        children = [
            LeafNode(None, "raw text"),
            ParentNode("div", [LeafNode("p", "nested")]),
            LeafNode("img", "", {"src": "image.jpg"}),  # self-closing
        ]
        node = ParentNode("section", children)
        expected = (
            '<section>raw text<div><p>nested</p></div><img src="image.jpg"/></section>'
        )
        self.assertEqual(node.to_html(), expected)

    def test_void_elements(self):
        # Test with void elements as children
        children = [LeafNode("br", ""), LeafNode("img", "", {"src": "pic.png"})]
        node = ParentNode("div", children)
        expected = '<div><br/><img src="pic.png"/></div>'
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
