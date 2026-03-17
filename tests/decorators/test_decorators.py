from leetcode.decorators import exclamation, add_suffix


@exclamation
def hello_world():
    return "Hello World"


def test_exclamation():
    assert hello_world() == "Hello World!"


@add_suffix("!!!")
def hello_world_again():
    return "Hello World"


def test_add_suffix():
    assert hello_world_again() == "Hello World!!!"
