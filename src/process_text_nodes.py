import extract_md_link_or_image_tag as ex
import slice_on_delim as sd
from decorators import type_check
from textnode import TextNode


@type_check([str])
def process_md_paragraph(md_text: str) -> list[TextNode]:
    """
    Takes a md paragraph block containing inline link, image,
    bold, italic and code tags and returns a list of
    TextNode(s) corresponding to the paragraph.
    """
    operand = sd.mmsplit(sd.DELIMS, md_text)
    operand = sd.process_split_string(sd.DELIMS, operand)
    operand = ex.process_nodes(operand)

    return operand
