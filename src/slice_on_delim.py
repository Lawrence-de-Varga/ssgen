from textnode import TextType, TextNode
from decorators import type_check

delimiter_to_text_type = {
    "`": TextType.CODE,
    "**": TextType.BOLD,
    "*": TextType.ITALIC,
    "_": TextType.ITALIC,
}

DELIMS = ["**", "_", "`", "*"]


# returns True if string starts with sub_string
@type_check([str, str])
def starts_with(sub_string: str, string: str) -> bool:
    if len(string) < len(sub_string):
        return False

    if not sub_string:
        return False

    for idx in range(len(sub_string)):
        if sub_string[idx] != string[idx]:
            return False

    return True


# Same as starts with but checks multiple substrings
@type_check([list, str])
def mstarts_with(sub_strings: list, string: str) -> str | bool:
    for ss in sub_strings:
        if starts_with(ss, string):
            return ss
    return False


@type_check([str, str])
def ends_with(sub_string: str, string: str) -> bool:
    if len(string) < len(sub_string):
        return False

    if not sub_string:
        return False

    string = string[::-1]

    return starts_with(sub_string, string)


@type_check([list, str])
def mcontains(sub_strings: list[str], string: str) -> bool | str:
    """
    Returns True if any element of 'sub_strings' is
    in 'string'.
    """
    for ss in sub_strings:
        if ss in string:
            return ss
    return False


@type_check([list, str])
def mmsplit(sub_strings: list[str], string: str) -> list[str]:
    """
    Same as msplit but takes multiple delimiters to split the string on.
    Intended for use with paired delimiters
    """
    if sub_strings == []:
        return string

    split_string: list[str] = []
    current_string: str = ""
    pairs = []

    i = 0
    while not i >= len(string):
        ss = mstarts_with(sub_strings, string[i:])
        if ss:
            if pairs == [] or ss != pairs[-1]:
                split_string.append(current_string)
                current_string = ss
                pairs.append(ss)
                i += len(ss)
            else:
                split_string.append(current_string + ss)
                current_string = ""
                i += len(ss)
                pairs = pairs[:-1]
        else:
            current_string += string[i]
            i += 1
    split_string.append(current_string)

    return split_string


@type_check([list, list])
def process_split_string(sub_strings: list[str], strings: list[str]) -> list[TextNode]:
    """Takes a list of delimiter strings and a list of strings (from mmsplit)
    and returns a list of TextNode(s) whose TextType is determined
    by the delimiter (or absence thereof).
    NOTE: Currently does not handle nested delimiters .e.g 'I **need to --go-- home** now'
    NOTE: Embedded html code will currently not display correctly, it will be treated as part of
          the final html documents structure rather than code to be displayed literally.
    """
    if not sub_strings:
        raise ValueError("'sub_strings' must not be None.")

    if not strings:
        raise ValueError("'strings' must not be None")

    nodes = []
    for string in strings:
        ss = mcontains(sub_strings, string)
        if not ss:
            nodes.append(TextNode(string, text_type=TextType.TEXT))
        else:
            string = string.replace(ss, "")
            tt = delimiter_to_text_type[ss]
            nodes.append(TextNode(string, tt))

    return nodes
