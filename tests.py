import pytest

from utils import object_exception_handler


@pytest.mark.parametrize(
    "error",
    [
        KeyError,
        IndexError,
        NameError,
        SyntaxError,
        TypeError,
        RuntimeError,
        Exception,
    ],
)
def test_Exceptions_decorator(error):
    @object_exception_handler
    def dummy(err):
        raise err

    with pytest.raises(Exception):
        assert dummy(error)
