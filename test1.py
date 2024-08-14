import pytest


def test1(cache: pytest.Cache):
    cache.mkdir("foo")


def test2(cache: pytest.Cache):
    cache.mkdir("bar")
