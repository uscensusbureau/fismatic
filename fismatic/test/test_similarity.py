from .. import similarity


def test_generate_diffs():
    diffs = similarity.generate_diffs(["foo", "Foo", "bar"])
    assert diffs == [
        # foo, Foo, bar
        [1.0, 1.0, 0.0],  # foo
        [1.0, 1.0, 0.0],  # Foo
        [0.0, 0.0, 1.0],  # bar
    ]
