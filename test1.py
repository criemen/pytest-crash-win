import pytest
import logging


def test1(cache: pytest.Cache):
    path = cache.mkdir("foo")
    logging.info(f"test1: {path}")


def test2(cache: pytest.Cache):
    path = cache.mkdir("bar")
    logging.info(f"test2: {path}")
