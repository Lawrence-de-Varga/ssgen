from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    test = TextNode("Well Well Well", TextType.BOLD, "https://cheese.com")

    print(test)


main()
