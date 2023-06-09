from __future__ import annotations

import json
from zlib import crc32

import pytest

import ManimExtra.utils.hashing as hashing
from ManimExtra import Square

ALREADY_PROCESSED_PLACEHOLDER = hashing._Memoizer.ALREADY_PROCESSED_PLACEHOLDER


@pytest.fixture(autouse=True)
def reset_already_processed():
    hashing._Memoizer.reset_already_processed()


def test_JSON_basic():
    o = {"test": 1, 2: 4, 3: 2.0}
    o_serialized = hashing.get_json(o)
    assert isinstance(o_serialized, str)
    assert o_serialized == str({"test": 1, "2": 4, "3": 2.0}).replace("'", '"')


def test_JSON_with_object():
    class Obj:
        def __init__(self, a):
            self.a = a
            self.b = 3.0
            self.c = [1, 2, "test", ["nested list"]]
            self.d = {2: 3, "2": "salut"}

    o = Obj(2)
    o_serialized = hashing.get_json(o)
    assert (
        str(o_serialized)
        == '{"a": 2, "b": 3.0, "c": [1, 2, "test", ["nested list"]], "d": {"2": 3, "2": "salut"}}'
    )


def test_JSON_with_function():
    def test(uhu):
        uhu += 2
        return uhu

    o_serialized = hashing.get_json(test)
    dict_o = json.loads(o_serialized)
    assert "code" in dict_o
    assert "nonlocals" in dict_o
    assert (
        str(o_serialized)
        == r'{"code": "    def test(uhu):\n        uhu += 2\n        return uhu\n", "nonlocals": {}}'
    )


def test_JSON_with_function_and_external_val():
    external = 2

    def test(uhu):
        uhu += external
        return uhu

    o_ser = hashing.get_json(test)
    external = 3
    o_ser2 = hashing.get_json(test)
    assert json.loads(o_ser2)["nonlocals"] == {"external": 3}
    assert o_ser != o_ser2


def test_JSON_with_method():
    class A:
        def __init__(self):
            self.a = self.method
            self.b = 3

        def method(self, b):
            b += 3
            return b

    o_ser = hashing.get_json(A())
    dict_o = json.loads(o_ser)
    assert dict_o["a"]["nonlocals"] == {}


def test_JSON_with_wrong_keys():
    def test():
        return 3

    class Test:
        def __init__(self):
            self.a = 2

    a = {(1, 2): 3}
    b = {Test(): 3}
    c = {test: 3}
    for el in [a, b, c]:
        o_ser = hashing.get_json(el)
        dict_o = json.loads(o_ser)
        # check if this is an int (it meant that the lkey has been hashed)
        assert int(list(dict_o.keys())[0])


def test_JSON_with_circular_references():
    B = {1: 2}

    class A:
        def __init__(self):
            self.b = B

    B["circular_ref"] = A()
    o_ser = hashing.get_json(B)
    dict_o = json.loads(o_ser)
    assert dict_o["circular_ref"]["b"] == ALREADY_PROCESSED_PLACEHOLDER


def test_JSON_with_big_np_array():
    import numpy as np

    a = np.zeros((1000, 1000))
    o_ser = hashing.get_json(a)
    assert "TRUNCATED ARRAY" in o_ser


def test_JSON_with_tuple():
    o = [(1, [1])]
    o_ser = hashing.get_json(o)
    assert o_ser == "[[1, [1]]]"


def test_JSON_with_object_that_is_itself_circular_reference():
    class T:
        def __init__(self) -> None:
            self.a = None

    o = T()
    o.a = o
    hashing.get_json(o)


def test_hash_consistency():
    def assert_two_objects_produce_same_hash(obj1, obj2, debug=False):
        """
        When debug is True, if the hashes differ an assertion comparing (element-wise) the two objects will be raised,
        and pytest will display a nice difference summary making it easier to debug.
        """
        json1 = hashing.get_json(obj1)
        hashing._Memoizer.reset_already_processed()
        json2 = hashing.get_json(obj2)
        hashing._Memoizer.reset_already_processed()
        hash1 = crc32(repr(json1).encode())
        hash2 = crc32(repr(json2).encode())
        if hash1 != hash2 and debug:
            dict1 = json.loads(json1)
            dict2 = json.loads(json2)
            assert dict1 == dict2
        assert hash1 == hash2, f"{obj1} and {obj2} have different hashes."

    assert_two_objects_produce_same_hash(Square(), Square())
    s = Square()
    assert_two_objects_produce_same_hash(s, s.copy())
