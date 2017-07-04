# -*- coding: utf-8 -*-
import unittest

from wolfgang.vector import Vector
from wolfgang.span import Span

class TestSpanClass(unittest.TestCase):
  def test_init(self):
    span = Span([Vector.unit_vector(3), Vector([1, 2, 3])])
    self.assertEqual(span.vectors, [Vector.unit_vector(3), Vector([1, 2, 3])])

  def test_len(self):
    span = Span([Vector.unit_vector(3), Vector([1, 2, 3])])
    self.assertEqual(len(span), 2)

  def test_real_basis(self):
    span = Span.real_basis(3)
    basis = [Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])]
    self.assertEqual(span.vectors, basis)

if __name__ == '__main__':
  unittest.main()
