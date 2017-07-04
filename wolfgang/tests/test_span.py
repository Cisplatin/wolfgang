# -*- coding: utf-8 -*-
import unittest

from wolfgang.vector import Vector
from wolfgang.span import Span

class TestSpanClass(unittest.TestCase):
  def test_init(self):
    span = Span([Vector.unit_vector(3), Vector([1, 2, 3])])
    self.assertEqual(span.vectors, [Vector.unit_vector(3), Vector([1, 2, 3])])

if __name__ == '__main__':
  unittest.main()
