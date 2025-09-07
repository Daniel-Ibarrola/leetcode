from leetcode.decorators import exclamation


@exclamation
def hello_world():
    return "Hello World"


def test_exclamation():
    assert hello_world() == "Hello World!"
