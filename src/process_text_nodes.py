import extract_md_link_or_image_tag as ex
import slice_on_delim as sd
from decorators import type_check
from textnode import TextNode

"""
FLOW:
MD-text -> sd.mmsplit -> sd.process_split_string
        -> ex.process_nodes  
"""


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


test = """
Learn about **variables** in Python and how to _assign_ values to them. Use `x = 10` for initialization. See this ![Python logo](https://i.imgur.com/python-logo.jpeg) and check the [documentation](https://docs.python.org).
The **James Webb Telescope** captured _astonishing_ images of deep space. Look at this ![nebula image](https://i.imgur.com/space-pic.jpg) and read more on [NASA's site](https://www.nasa.gov).
Make **spaghetti carbonara** with _crispy_ pancetta. Use `fresh eggs` for best results. See the ![finished dish](https://i.imgur.com/pasta-photo.jpg) and get the [full recipe](https://recipes.com/carbonara).
**Deadlifts** are _essential_ for strength training. Maintain proper `form` to avoid injury. Watch this ![exercise demo](https://i.imgur.com/deadlift-vid.gif) and join our [fitness community](https://fitness.org).
Visit **Kyoto** for _breathtaking_ temples. Don't miss `Fushimi Inari` shrine. See this ![temple photo](https://i.imgur.com/kyoto-temple.jpg) and book [flights here](https://travel-japan.com).
**AI models** are becoming _incredibly_ advanced. Try the new `ChatGPT-4` API. Check this ![AI graphic](https://i.imgur.com/ai-visual.png) and read the [announcement](https://openai.com/blog).
"""
