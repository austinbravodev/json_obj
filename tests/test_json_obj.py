import pytest

from .mocks import json

from json_obj import JSONObj


def test_json_obj():
    json_obj = JSONObj(json)

    assert json_obj.attr == "attr value"
    assert json_obj.nested.attr == "nested attr value"
    assert json_obj.list_attr[2] == 3
    assert json_obj.nested_list.list_attr[2] == 3
    assert json_obj.nested_attr_list[0].attr == "in list"

    json_obj.missing = "present"

    assert json_obj.missing == "present"
    del json_obj.missing

    with pytest.raises(AttributeError):
        json_obj.missing
