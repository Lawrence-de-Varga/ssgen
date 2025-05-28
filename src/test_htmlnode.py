import unittest
from htmlnode import HTMLNode


class TestHTMLNodePropsToHtml(unittest.TestCase):
    def test_props_to_html_basic(self):
        node = HTMLNode(props={"class": "button", "id": "submit-btn"})
        expected = ' class="button" id="submit-btn"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://example.com"})
        expected = ' href="https://example.com"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty_props(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none_props(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_special_characters(self):
        node = HTMLNode(props={"data-value": "hello&world", "onclick": "alert('test')"})
        expected = ' data-value="hello&world" onclick="alert(\'test\')"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_boolean_attributes(self):
        node = HTMLNode(props={"disabled": "true", "readonly": "readonly"})
        expected = ' disabled="true" readonly="readonly"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_numbers(self):
        node = HTMLNode(props={"tabindex": "1", "value": "42"})
        expected = ' tabindex="1" value="42"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_multiple_spaces(self):
        node = HTMLNode(props={"style": "color: red;  margin: 10px"})
        expected = ' style="color: red;  margin: 10px"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_unicode(self):
        node = HTMLNode(props={"alt": "café", "title": "日本語"})
        expected = ' alt="café" title="日本語"'
        self.assertEqual(node.props_to_html(), expected)


if __name__ == "__main__":
    unittest.main()
