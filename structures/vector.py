# -*- coding: utf-8 -*-

class Vector:
  # @param vector [List<Integer>] The value to intialize the vector to.
  def __init__(self, vector):
    self.vector = vector

  # @return [String] A clean representation of the vector.
  def __repr__(self):
    return '⟨{}⟩'.format(', '.join(map(str, self.vector)))

  # @param other [Any] The object to compare to.
  # @return [Boolean] True if the two are equal (by vector definition).
  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.vector == other.vector
    return False

  # @param other [Any] The object to compare to.
  # @return [Boolean] True if the two are inequal (by vector definition).
  def __ne__(self, other):
    return not self.__eq__(other)
