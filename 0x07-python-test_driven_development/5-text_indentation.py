#!/usr/bin/python3


"""a function that prints a text with 2 new lines after each of these \
        characters: ., ? and :"""


def text_indentation(text):
    """This function indent text after a given character
    :param: text of type string
    :return: indented text after characters ".", "?" ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join([line.strip(" ") for line in \
                text.split(delim)])
    print(f"{text}", end="")
