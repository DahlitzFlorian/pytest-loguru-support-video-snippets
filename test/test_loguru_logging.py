import loguru_logging


def test_logging(caplog):
    loguru_logging.func()

    assert "This is a log message." in caplog.text
