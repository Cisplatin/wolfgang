# -*- coding: utf-8 -*-

class Vector:
  # @param vector [List<Integer>] The value to intialize the vector to.
  def __init__(self, vector):
    self.vector = vector

  # @return [Integer] The magnitude of the vector.
  def __len__(self):
    return len(self.vector)

  # @return [String] A clean representation of the vector.
  def __repr__(self):
    return '⟨{}⟩'.format(', '.join(map(str, self.vector)))

  # @param other [Vector] The vector to operate on.
  # @param func [Element x Element -> Element] The function to operate with.
  # @return [Vector] The function applied element-wise to the two vectors.
  # @raise [ValueError] If the vectors are not the same size.
  def __operate(self, other, func):
    if len(self) != len(other):
      raise ValueError('Can only operate on two vectors of equal magnitude.')
    return Vector([func(x, y) for x, y in zip(self.vector, other.vector)])

  # @param other [Vector] The vector to add to.
  # @return [Vector] The sum of the two vectors.
  # @raise [ValueError] If the vectors are not the same size.
  def __add__(self, other):
    return self.__operate(other, lambda x, y: x + y)

  # @param other [Vector] The vector to compare to.
  # @return [Boolean] True if the two are equal (by vector definition).
  def __eq__(self, other):
    return self.vector == other.vector

  # @param other [Vector] The vector to compare to.
  # @return [Boolean] True if the two are inequal (by vector definition).
  def __ne__(self, other):
    return not self.__eq__(other)
