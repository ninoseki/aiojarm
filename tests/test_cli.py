from typing import List

import pytest

from aiojarm.cli import default_max_at_once, is_file_input, read_from_file


def test_default_max_at_once():
    v = default_max_at_once()
    assert isinstance(v, int)
    assert v > 0


@pytest.mark.parametrize(
    "values,expected",
    [
        (["example.com"], False),
        (["example.com", "test.com"], False),
        (["README.md"], True),
    ],
)
def test_is_file_input(values: List[str], expected: bool):
    assert is_file_input(values) is expected


def test_read_from_file():
    lines = read_from_file("README.md")
    assert isinstance(lines, list)
    assert isinstance(lines[0], str)
