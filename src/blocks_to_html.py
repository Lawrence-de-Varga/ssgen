from decorators import type_check
from htmlnode import HTMLNode

# import markdown_to_blocks as mtb
from markdown_to_blocks import *
from process_text_nodes import *
from textnode import *


def pp(thing):
    idx = 0
    for item in thing:
        print(item)
        print()
        print(block_to_block_type(item))
        print(idx)
        idx += 1
        print(
            "-------------------------------------------------------------------------------------------------------------------"
        )
        print()


with open("../markdown_sample.md") as f:
    mds1 = f.read()
with open("../markdown_sample_2.md") as f:
    mds2 = f.read()
with open("../markdown_sample_3.md") as f:
    mds3 = f.read()
with open("../markdown_sample_4.md") as f:
    mds4 = f.read()
with open("../markdown_sample_5.md") as f:
    mds5 = f.read()
with open("../markdown_sample_6.md") as f:
    mds6 = f.read()
with open("../markdown_sample_7.md") as f:
    mds7 = f.read()
