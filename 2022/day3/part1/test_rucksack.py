from .rucksack import split_compartments, find_common_item, get_item_value


def test_split_compartments():
    assert split_compartments("AAAABBBB") == ("AAAA", "BBBB")


def test_find_common_item():
    assert find_common_item("AAAC", "CBBB") == "C"


def test_get_item_value():
    assert get_item_value("a") == 1
    assert get_item_value("G") == 33
