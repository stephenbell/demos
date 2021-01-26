from poetry_demo import __version__
from poetry_demo import simple_demo


def test_version():
    """Test the version"""
    assert __version__ == "0.1.0"


def test_name():
    assert simple_demo.PERSON == "stephen"
