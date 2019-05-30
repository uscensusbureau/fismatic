import itertools


def flatten(list_of_lists):
    # https://stackoverflow.com/a/13498063/358804
    return list(itertools.chain(*list_of_lists))
