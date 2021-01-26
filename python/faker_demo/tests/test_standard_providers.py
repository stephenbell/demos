def test_faker(faker):
    """Assert faker name object isinstance str"""
    assert isinstance(faker.name(), str)
    assert faker.name() == "boo"


def test_something():
    assert isinstance("oooo", str)
