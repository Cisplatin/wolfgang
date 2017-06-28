from structures.vector import Vector

# Vector initializes properly
vector = Vector([1, 2, 3])
assert vector.vector == [1, 2, 3]

# Vector prints properly
print vector.__repr__()
