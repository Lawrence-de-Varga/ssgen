class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        prop_list = [f' {key}="{value}"' for key, value in self.props.items()]
        return "".join(prop_list)

    def __repr__(self):
        return (
            f"TextNode(tag={self.tag}, value={self.value}, children={self.children}, \
                    props={self.props}"
        )


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, children=None, props=props)
        if self.value is None:
            raise ValueError("Leaf nodes must have a value.")

    # @property
    # def children(self):
    #     raise AttributeError("Leaf nodes cannot have children.")

    # @children.setter
    # def children(self, value):
    #     self.children = None
    #     raise AttributeError("LeafNode's cannot have children assigned to them.")

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        if self.props:
            html_props = self.props_to_html()
        else:
            html_props = ""

        if self.tag in ['area', 'base', 'br', 'col', 'embed', 'hr', img',\
                        'input', 'link', 'meta', 'param', 'source', 'track', 'wbr']:
                        return f"<{self.tag}{html_props}/>"
                        
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None:
            raise ValueError("Parent nodes must have children")

        if self.props is not None:
            html_props = self.props_to_html()
        else:
            html_props = ""

        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{html_props}>{children_html}</{self.tag}>"
