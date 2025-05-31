from textnode import TextType
from collections.abc import Callable


delimiter_to_text_type = {"`": TextType.CODE, "**": TextType.BOLD, "_": TextType.ITALIC}


# TODO: correct it for kwargs, as it is currently treating it
# like a list instead of a dict
def type_check_decorator(param_types: list):
    def decorate(function_to_check):
        def wrapper(*args, **kwargs):
            idx = 0
            for param in param_types:
                if idx in range(len(args)):
                    print(args[0])
                    print(param_types[0])
                    if not isinstance(args[idx], param_types[idx]):
                        print(idx)
                        raise TypeError(
                            f"Arg {idx + 1} must be of type: {param_types[idx]}."
                        )
                    idx += 1
                elif (idx - len(args)) in range(len(kwargs)):
                    if not isinstance(kwargs[idx - len(args)], param_types[idx]):
                        raise TypeError(
                            f"Arg {idx + 1} must be of type: {param_types[idx]}."
                        )
                    idx += 1
            return function_to_check(*args, **kwargs)

        return wrapper

    return decorate


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    pass


@type_check_decorator([str, str])
def slice_on_first_delimiter(delimiter: str, text: str):
    # if not text:
    #     raise ValueError("second argument must be a string.")

    # if not delimiter:
    #     raise ValueError("First argument must be a string.")

    idx = text.find(delimiter)

    if idx == -1:
        return text
    else:
        return idx, text[idx:]
