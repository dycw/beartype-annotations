from __future__ import annotations

from beartype import beartype


@beartype
def foo(x: int) -> int:
    return x + 1


def test_main():
    assert foo(1) == 2
