#!/usr/bin/env python3

import unittest
from parameterized import parameterized, parameterized_class
import utils
from typing import Mapping, List, Union, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """ testing """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected_value: Union[int, Mapping]):
        """ test access"""
        self.assertEqual(utils.access_nested_map(nested_map, path),
                         expected_value)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """ testing access map exceptio  """
        self.assertRaises(KeyError, utils.access_nested_map, nested_map, path)
