from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode, LeafNode


def main():
    test = TextNode("Well Well Well", TextType.HTML, "https://cheese.com")

    print(test)


main()
