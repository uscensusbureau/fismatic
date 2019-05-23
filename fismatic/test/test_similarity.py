import pandas as pd
from pytest import approx
from .. import similarity


def test_generate_diffs():
    diffs = similarity.generate_diffs(["foo", "Foo", "bar"])
    assert approx(diffs) == [
        # foo, Foo, bar
        [1.0, 1.0, 0.0],  # foo
        [1.0, 1.0, 0.0],  # Foo
        [0.0, 0.0, 1.0],  # bar
    ]


def test_similar_controls():
    desc_lkup = ["AC-1", "AC-2", "AC-2 (1)"]
    diffs = pd.DataFrame(
        [
            # AC-1, AC-2, AC-2 (1)
            [1.0, 0.9, 0.0],  # AC-1
            [0.9, 1.0, 0.0],  # AC-2
            [0.0, 0.0, 1.0],  # AC-2 (1)
        ],
        index=desc_lkup,
        columns=desc_lkup,
    )

    very_similar = similarity.similar_controls(diffs)
    assert very_similar == {
        "AC-1": {"AC-2": 0.9},
        "AC-2": {"AC-1": 0.9},
        "AC-2 (1)": {},
    }
