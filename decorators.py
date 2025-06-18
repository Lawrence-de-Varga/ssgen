def type_check_decorator(param_types: list):
    def decorate(function_to_check):
        def wrapper(*args, **kwargs):
            idx = 0
            for param in param_types:
                if idx in range(len(args)):
                    if not isinstance(args[idx], param_types[idx]):
                        print(idx)
                        raise TypeError(
                            f"Arg {idx + 1}: {args[idx]} must be of type: {param_types[idx]}, but is of type: {type(args[idx])}."
                        )
                    idx += 1
                elif (idx - len(args)) in range(len(kwargs)):
                    if not isinstance(
                        list(kwargs.values())[idx - len(args)], param_types[idx]
                    ):
                        raise TypeError(
                            f"Arg {idx + 1} must be of type: {param_types[idx]}."
                        )
                    idx += 1
            return function_to_check(*args, **kwargs)

        return wrapper

    return decorate
