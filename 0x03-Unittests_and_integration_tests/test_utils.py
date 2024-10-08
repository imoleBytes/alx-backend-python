#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function and understand
its purpose. Play with it in the Python console to make sure you understand.
In this task you will write the first unit test for utils.access_nested_map.
Create a TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method to test
that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for
following inputs:
"""
from typing import (Mapping, Tuple, Union)
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (access_nested_map, get_json, memoize)


class TestAccessNestedMap(unittest.TestCase):
    """Testing the `access_nested_map`"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Tuple[str],
            expected: Union[Mapping, int]
            ) -> None:
        """ main tests happens here"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError"),
        ({"a": 1}, ("a", "b"), "mmmm")
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping,
            path: Tuple, expected: str) -> None:
        """access_nested_map for exception """
        with self.assertRaises(KeyError, msg=expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Tests the get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Mapping) -> None:
        """ Method tests the `get_json` function """

        attrs = {'json.return_value': test_payload}

        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests `memoize` function."""

    def test_memoize(self) -> None:
        """Tests `memoize`'s fn."""

        class TestClass:
            """inner class"""
            def a_method(self):
                """inner method forclass TestClass"""
                return 42

            @memoize
            def a_property(self):
                """ a property func"""
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_func:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_func.assert_called_once()
