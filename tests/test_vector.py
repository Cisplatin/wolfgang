# -*- coding: utf-8 -*-

import unittest

from structures.vector import Vector

class TestVectorClass(unittest.TestCase):
  vector = Vector([1, 2, 3])

  def test_init(self):
    self.assertEqual(self.vector.vector, [1, 2, 3])

  def test_repr(self):
    self.assertEqual(self.vector.__repr__(), '⟨1, 2, 3⟩')

  def test_equality(self):
    self.assertEqual(self.vector, Vector([1, 2, 3]))
    self.assertNotEqual(self.vector, Vector([1, 2, 2]))

  def test_magnitude(self):
    self.assertEqual(len(self.vector), 3)

  def test_add(self):
    vector_sum = self.vector + Vector([3, 2, 1])
    self.assertEqual(vector_sum, Vector([4, 4, 4]))
    with self.assertRaises(ValueError):
      vector_sum = self.vector + Vector([3, 2])

if __name__ == '__main__':
  unittest.main()
