# -*- coding: utf-8 -*-

class Vector:
  # @param vector [List<Integer>] The value to intialize the vector to.
  def __init__(self, vector):
    self.vector = vector

  # @return [String] A clean representation of the vector.
  def __repr__(self):
    return '⟨{}⟩'.format(' '.join(map(str, self.vector)))
