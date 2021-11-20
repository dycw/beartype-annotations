from __future__ import annotations

from beartype import beartype


@beartype
def foo(x: int | None) -> int:
    return 0 if x is None else (x + 1)


def test_main():
    assert foo(None) == 2
    assert foo(1) == 2
