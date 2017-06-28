# -*- coding: utf-8 -*-
from math import sqrt

class Vector:
  # @param vector [List<Integer>] The value to intialize the vector to.
  def __init__(self, vector):
    self.vector = vector

  # @return [Integer] The number of elements in the vector.
  def __len__(self):
    return len(self.vector)

  # @return [String] A clean representation of the vector.
  def __repr__(self):
    return '⟨{}⟩'.format(', '.join(map(str, self.vector)))

  # @param func [Element -> Element] The function to operate with.
  # @return [Vector] The function applied element-wise to the vector.
  def __map(self, func):
    return Vector(map(func, self.vector))

  # @param other [Vector] The vector to operate on.
  # @param func [Element x Element -> Element] The function to operate with.
  # @return [Vector] The function applied element-wise to the two vectors.
  # @raise [ValueError] If the vectors are not the same size.
  def __operate(self, other, func):
    if len(self) != len(other):
      raise ValueError('Can only operate on two vectors of equal magnitude.')
    return Vector([func(x, y) for x, y in zip(self.vector, other.vector)])

  # @return [Vector] The vector with all elements negated.
  def __neg__(self):
    return self.__map(lambda x: -x)

  # @param other [Vector] The vector to add to.
  # @return [Vector] The sum of the two vectors.
  # @raise [ValueError] If the vectors are not the same size.
  def __add__(self, other):
    return self.__operate(other, lambda x, y: x + y)

  # @param other [Vector] The vector to subtract.
  # @return [Vector] The difference of the two vectors.
  # @raise [ValueError] If the vectors are not the same size.
  def __sub__(self, other):
    return self.__operate(other, lambda x, y: x - y)

  # @param other [Element] The scalar to multiply by.
  # @return [Vector] The scalar multiple of the vector.
  def __mul__(self, other):
    return self.__map(lambda x: x * other)

  # @param other [Element] The scalar to multiply by.
  # @return [Vector] The scalar multiple of the vector.
  def __rmul__(self, other):
    return self.__mul__(other)

  # @param other [Vector] The vector to compare to.
  # @return [Boolean] True if the two are equal (by vector definition).
  def __eq__(self, other):
    return self.vector == other.vector

  # @param other [Vector] The vector to compare to.
  # @return [Boolean] True if the two are inequal (by vector definition).
  def __ne__(self, other):
    return not self.__eq__(other)

  # @param dimension [Integer] The dimension of the vector to return.
  # @param value [Element] The value to set each element to.
  # @return [Vector] The vector with all values as the given value.
  # @raise [ValueError] If dimension is a non-positive value.
  @staticmethod
  def __standard_vector(dimension, value):
    if dimension <= 0:
      raise ValueError('Dimension of vector must be positive.')
    return Vector([value] * dimension)

  # @param dimension [Integer] The dimension of the zero vector to return.
  # @return [Vector] The zero vector with the correct dimensions.
  # @raise [ValueError] If dimension is a non-positive value.
  @staticmethod
  def zero_vector(dimension):
    return Vector.__standard_vector(dimension, 0)

  # @param dimension [Integer] The dimension of the unit vector to return.
  # @return [Vector] The unit vector with the correct dimensions.
  # @raise [ValueError] If dimension is a non-positive value.
  @staticmethod
  def unit_vector(dimension):
    return Vector.__standard_vector(dimension, 1)

  # @return [Element] The magnitude of the vector.
  def magnitude(self):
    return sqrt(sum(map(lambda x: x * x, self.vector)))
