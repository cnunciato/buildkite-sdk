"""Hello unit test module."""

from app_python.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello app-python"
