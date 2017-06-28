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

  def test_length(self):
    self.assertEqual(len(self.vector), 3)

  def test_getitem(self):
    self.assertEqual(self.vector[0], 1)
    self.assertEqual(self.vector[2], 3)
    with self.assertRaises(IndexError):
      self.vector[3]

  def test_setitem(self):
    self.assertEqual(self.vector[0], 1)
    self.vector[0] = 2
    self.assertEqual(self.vector[0], 2)
    with self.assertRaises(IndexError):
      self.vector[3] = 2
    self.vector[0] = 1

  def test_add(self):
    vector_sum = self.vector + Vector([3, 2, 1])
    self.assertEqual(vector_sum, Vector([4, 4, 4]))
    with self.assertRaises(ValueError):
      vector_sum = self.vector + Vector([3, 2])

  def test_subtract(self):
    vector_diff = self.vector - Vector([3, 2, 1])
    self.assertEqual(vector_diff, Vector([-2, 0, 2]))
    with self.assertRaises(ValueError):
      vector_diff = self.vector - Vector([3, 2])

  def test_multiply(self):
    vector_prod = self.vector * 3
    self.assertEqual(vector_prod, Vector([3, 6, 9]))
    vector_prod = 3 * self.vector
    self.assertEqual(vector_prod, Vector([3, 6, 9]))

  def test_negative(self):
    self.assertEqual(-self.vector, Vector([-1, -2, -3]))

  def test_zero_vector(self):
    self.assertEqual(Vector.zero_vector(2), Vector([0, 0]))
    with self.assertRaises(ValueError):
      Vector.zero_vector(0)

  def test_unit_vector(self):
    self.assertEqual(Vector.unit_vector(2), Vector([1, 1]))
    with self.assertRaises(ValueError):
      Vector.unit_vector(0)

  def test_magnitude(self):
    self.assertEqual(round(self.vector.magnitude(), 4), 3.7417)

  def test_dot(self):
    self.assertEqual(self.vector.dot(Vector([1, 2, 1])), 8)

  def test_cross(self):
    cross = Vector([3, -3, 1]).cross(Vector([4, 9, 2]))
    self.assertEqual(cross, Vector([-15, -2, 39]))
    with self.assertRaises(ValueError):
      Vector([1, 2, 3]).cross(Vector([1, 2, 3, 4]))
    with self.assertRaises(ValueError):
      Vector([1, 2, 3, 4]).cross(Vector([1, 2, 3, 4]))

  def test_from_points(self):
    p1, p2 = (1, 2, 6), (2, 0, 2)
    self.assertEqual(Vector.from_points(p1, p2), Vector([1, -2, -4]))
    with self.assertRaises(ValueError):
      Vector.from_points(p1, p1)
    with self.assertRaises(ValueError):
      Vector.from_points(p1, (2, 0))

  def test_parallel(self):
    self.assertTrue(self.vector.parallel(Vector([2, 4, 6])))
    self.assertFalse(self.vector.parallel(Vector([2, 4, 5])))
    with self.assertRaises(ValueError):
      self.vector.parallel(Vector([2, 4]))

  def test_orthogonal(self):
    self.assertTrue(Vector([1, -2, 3]).orthogonal(Vector([5, 4, 1])))
    self.assertFalse(Vector([1, -2, 3]).orthogonal(Vector([5, 4, 2])))
    with self.assertRaises(ValueError):
      self.vector.orthogonal(Vector([2, 4]))

  def test_angle(self):
    self.assertEqual(self.vector.angle(self.vector), 0)
    self.assertEqual(round(Vector([1, 1]).angle(Vector([1, 0])), 4), 0.7854)
    with self.assertRaises(ValueError):
      self.vector.angle(Vector([1, 0]))

if __name__ == '__main__':
  unittest.main()
