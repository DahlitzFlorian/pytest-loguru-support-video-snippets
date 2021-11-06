import builtin_logging
import pytest


def test_logging(caplog):
    builtin_logging.func()

    assert "This is a log message." in caplog.text
