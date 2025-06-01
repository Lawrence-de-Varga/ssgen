from textnode import TextType
from decorators import type_check_decorator

delimiter_to_text_type = {"`": TextType.CODE, "**": TextType.BOLD, "_": TextType.ITALIC}


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    pass


@type_check_decorator([str, str])
def slice_on_first_delimiter(delimiter: str, text: str):
    idx = text.find(delimiter)

    if idx == -1:
        return text
    else:
        return text[:idx], idx, text[idx:]


# returns True if string starts with sub_string
@type_check_decorator([str, str])
def starts_with(sub_string: str, string: str) -> bool:
    if len(string) < len(sub_string):
        return False

    for idx in range(len(sub_string)):
        if sub_string[idx] != string[idx]:
            return False

    return True


# Same as starts with but checks multiple substrings
@type_check_decorator([list, str])
def mstarts_with(sub_strings: list, string: str) -> str | bool:
    for ss in sub_strings:
        if starts_with(ss, string):
            return ss
    return False


# Similar to .split() but retains the sub_string to split with
# in the returned string
@type_check_decorator([str, str])
def msplit(sub_string: str, string: str) -> list[str]:
    if sub_string == "":
        return string

    if sub_string not in string:
        return string

    split_string: list[str] = []
    current_string: str = ""

    partner = False

    i = 0
    while not i >= len(string):
        if starts_with(sub_string, string[i:]):
            if not partner:
                split_string.append(current_string)
                current_string = sub_string
                partner = not partner
                i += len(sub_string)
            else:
                split_string.append(current_string + sub_string)
                current_string = ""
                partner = not partner
                i += len(sub_string)

        else:
            current_string += string[i]
            i += 1
    split_string.append(current_string)

    return split_string


@type_check_decorator([list, str])
def mmsplit(sub_strings: list[str], string: str) -> list[str]:
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
