from .similarity import nlp


def similar_implementations(control_sets, control_name, part, implementation):
    user_implementation = nlp(implementation)

    implementations = [
        cs.get_implementation_for(control_name, part) for cs in control_sets
    ]
    # exclude SSPs that don't have that control+part
    implementations = filter(None, implementations)

    # get the most similar
    return sorted(
        implementations,
        key=lambda imp: imp.similarity(user_implementation),
        reverse=True,
    )
