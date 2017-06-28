# -*- coding: utf-8 -*-

from structures.vector import Vector

# Vector initializes properly
vector = Vector([1, 2, 3])
assert vector.vector == [1, 2, 3]

# Vector prints properly
assert vector.__repr__() == '⟨1, 2, 3⟩'

# Equality is checked correctly
assert vector == Vector([1, 2, 3])
assert vector != Vector([1, 2, 2])
