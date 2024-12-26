"""Hello unit test module."""

from buildkite_sdk.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello buildkite-sdk"
