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
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props=props)
        self._children = None

    @property
    def children(self):
        raise AttributeError("Leaf nodes cannot have children.")

    @children.setter
    def children(self, value):
        raise AttributeError("LeafNode's cannot have children assigned to them.")

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf nodes must have a value.")
        if not self.tag:
            return self.value
        if self.props:
            html_props = self.props_to_html()
        else:
            html_props = ""
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"
