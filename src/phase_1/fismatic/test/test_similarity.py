import numpy as np
import pandas as pd
from .. import similarity


def test_generate_diffs():
    sources = ["foo", "Foo", "bar"]
    docs = [similarity.nlp(source) for source in sources]
    diffs = similarity.generate_diffs(docs)
    expected = [
        # foo, Foo, bar
        [1.0, 1.0, 0.2],  # foo
        [1.0, 1.0, 0.2],  # Foo
        [0.2, 0.2, 1.0],  # bar
    ]
    np.testing.assert_array_almost_equal(diffs, expected, decimal=2)


def test_similar_controls():
    desc_lkup = ["AC-1", "AC-2", "AC-2 (1)"]
    diffs = pd.DataFrame(
        [
            # AC-1, AC-2, AC-2 (1)
            [1.00, 0.95, 0.00],  # AC-1
            [0.95, 1.00, 0.00],  # AC-2
            [0.00, 0.00, 1.00],  # AC-2 (1)
        ],
        index=desc_lkup,
        columns=desc_lkup,
    )

    very_similar = similarity.similar_controls(diffs)
    assert very_similar == {
        "AC-1": {"AC-2": 0.95},
        "AC-2": {"AC-1": 0.95},
        "AC-2 (1)": {},
    }
