import itertools


def flatten(list_of_lists):
    # https://stackoverflow.com/a/13498063/358804
    return list(itertools.chain(*list_of_lists))


def present(span):
    """Accepts a spaCy Span and returns True if the text contains non-whitespace characters."""
    return span and span.text.strip()
