#!/usr/bin/python3
"""
Test cases for module Rectangle in models
"""
import unittest
import json
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test Base Class"""

    @classmethod
    def setClass(cls):
        """
        Test object instantiate
        """

        cls.one = Base()
