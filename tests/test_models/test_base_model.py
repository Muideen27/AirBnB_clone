#!/usr/bin/env python3
"""Unittest modul for the BaseClass"""

from models.base_model import BaseModel
from datetime import datetime
import unittest
import uuid
import time
import json

class TestBaseModel(unittest.TestCase):
    """Test case for base model"""
    def setUp(self):
        self.model = BaseModel()


    def test_init(self):
        """Test case for initialization of BaseModel"""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_id(self):
        self.assertIsInstance(self.model.id, str)
        self.assertNotEqual(self.model.id, "")
        self.assertEqual(len(self.model.id), 36)

    def test_created_at(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        expected_str = "[{}] ({}) {}".format(
            type(self.model).__name__, self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        expected_dict = {
            "id": self.model.id,
            "__class__": type(self.model).__name__,
            "created_at": self.model.created_at.isoformat(),
            "updated_at": self.model.updated_at.isoformat()
        }
        self.assertEqual(self.model.to_dict(), expected_dict)

    def test_do_dict_with_args(self):
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)

    def test_to_dict_with_json(self):
        model_dict = self.model.to_dict()
        model_json = json.dumps(model_dict)
        expected_dict = {
            "id": self.model.id,
            "__class__": type(self.model).__name__,
            "created_at": self.model.created_at.isoformat(),
            "updated_at": self.model.updated_at.isoformat()
        }
        self.assertEqual(json.loads(model_json), expected_dict)

