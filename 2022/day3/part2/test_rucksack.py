from .rucksack import find_common_item, get_item_value


def test_find_common_item():
    assert find_common_item(["AAAC", "CBBB", "DDCD"]) == "C"


def test_get_item_value():
    assert get_item_value("a") == 1
    assert get_item_value("G") == 33
