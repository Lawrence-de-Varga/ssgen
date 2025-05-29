import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_init(self):
        # Test basic initialization
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertIsNone(node.props)

        # Test with props
        props = {"class": "greeting", "id": "main"}
        node = LeafNode("a", "Click me", props)
        self.assertEqual(node.props, props)

    # def test_children_property(self):
    #     node = LeafNode("span", "content")
    #     with self.assertRaises(AttributeError) as ctx:
    #         _ = node.children
    #     self.assertEqual(str(ctx.exception), "LeafNode cannot have children")

    #     with self.assertRaises(AttributeError) as ctx:
    #         node.children = ["invalid"]
    #     self.assertEqual(
    #         str(ctx.exception), "LeafNode's cannot have children assigned to them."
    #     )

    def test_to_html(self):
        # Test simple tag
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

        # Test with props
        node = LeafNode(
            "a", "Click here", {"href": "https://www.example.com", "target": "_blank"}
        )
        expected = '<a href="https://www.example.com" target="_blank">Click here</a>'
        self.assertEqual(node.to_html(), expected)

        # Test no tag (raw text)
        node = LeafNode(None, "Just plain text")
        self.assertEqual(node.to_html(), "Just plain text")

    def test_value_required(self):
        # Test empty value
        with self.assertRaises(ValueError) as context:
            LeafNode("p", None)
        self.assertEqual(str(context.exception), "Leaf nodes must have a value.")

        # Test empty string (should be allowed)
        node = LeafNode("p", "")
        self.assertEqual(node.to_html(), "<p></p>")

    def test_props_to_html(self):
        # Test props conversion
        node = LeafNode("div", "Content", {"class": "container", "data-id": "123"})
        expected_props = ' class="container" data-id="123"'
        self.assertEqual(node.props_to_html(), expected_props)

        # Test no props
        node = LeafNode("div", "Content")
        self.assertEqual(node.props_to_html(), "")

    def test_edge_cases(self):
        # Test numeric value (should be converted to string)
        node = LeafNode("span", 42)
        self.assertEqual(node.to_html(), "<span>42</span>")

        # Test boolean value
        node = LeafNode("span", True)
        self.assertEqual(node.to_html(), "<span>True</span>")

        # Test empty tag
        node = LeafNode(None, "Testing an empty tag.")
        self.assertEqual(node.to_html(), node.value)


if __name__ == "__main__":
    unittest.main()
