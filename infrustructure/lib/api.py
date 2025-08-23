import random


def wrap_string(_cmd):
    """
    Since strings are immutable, a function must return a new string, which then needs to be reassigned to the original variable.
    :param _cmd:
    :return: str
    """
    _cmd += ' wrapped'
    return _cmd


def unique_random_numbers():
    numbers = list(range(100000))
    random.shuffle(numbers)
    for num in numbers:
        yield num


def update_nested_dict(original: dict, new: dict) -> dict:
    """
    Recursively update a nested dictionary.
    :param original: The dictionary to be updated
    :param new: The dictionary with updates
    :return: The updated dictionary
    """
    for key, value in new.items():
        if (
            key in original
            and isinstance(original[key], dict)
            and isinstance(value, dict)
        ):
            # If both are dictionaries, update recursively
            update_nested_dict(original[key], value)
        else:
            # Otherwise, overwrite or add the value
            original[key] = value
    return original


if __name__ == '__main__':

    random_generator = unique_random_numbers()

    for idx, number in enumerate(random_generator, start=1):
        print(number)
        if number % 100 == 0:
            print(f"idx is {idx}")
            break
    else:
        raise RuntimeError("No multiple of 100 found")
