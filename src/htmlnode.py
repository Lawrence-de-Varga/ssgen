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
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
