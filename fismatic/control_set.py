from collections import Counter
from . import helpers
from . import similarity


class ControlSet:
    def __init__(self, controls):
        self._controls = controls

    def get_implementations_by_id(self):
        """The ID (key) is the control name + part."""
        result = {}

        for control in self._controls:
            for part, imp in control.implementation.items():
                key = ": ".join([control.name, part])
                result[key] = imp

        return result

    def get_implementations(self):
        """Returns a list of strings."""
        return self.get_implementations_by_id().values()

    def num_controls(self):
        return len(self._controls)

    def num_implementations(self):
        return len(self.get_implementations())

    def num_unique_implementations(self):
        return len(set(self.get_implementations()))

    def num_identical_implementations(self):
        return self.num_implementations() - self.num_unique_implementations()

    def implementation_token_counts(self):
        implementations = self.get_implementations()
        return [
            # based on
            # https://stackoverflow.com/a/41425016/358804
            sum(1 if not (token.is_stop or token.is_punct) else 0 for token in imp)
            for imp in implementations
        ]

    def num_tokens(self):
        return sum(self.implementation_token_counts())

    def similarity_matrix(self):
        implementations_by_id = self.get_implementations_by_id()
        return similarity.generate_diffs_with_labels(implementations_by_id)

    def entities(self):
        """Returns a list of spaCy Entities."""
        implementations = self.get_implementations()
        return helpers.flatten(imp.ents for imp in implementations)

    def top_entities(self, top=20):
        """Returns the most common entities across the controls."""
        entities = [e.text for e in self.entities()]
        # https://www.youtube.com/watch?v=YrFOAhT4Azk
        counter = Counter(entities)
        return counter.most_common(top)

    def _is_proper_noun(self, span):
        # https://spacy.io/api/annotation#pos-tagging
        return span.root.tag_ in ["NNP", "NNPS"]

    def proper_noun_chunks(self):
        implementations = self.get_implementations()
        return helpers.flatten(
            [
                [chunk.text for chunk in imp.noun_chunks if self._is_proper_noun(chunk)]
                for imp in implementations
            ]
        )

    def top_proper_noun_chunks(self, top=20):
        """Returns the most common proper noun chunks across the controls."""
        chunks = self.proper_noun_chunks()
        counter = Counter(chunks)
        return counter.most_common(top)
