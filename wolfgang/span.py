from wolfgang.vector import Vector

class Span:
  # @param vector [List<Vector>] The spanning set of vectors.
  def __init__(self, vectors):
    self.vectors = vectors

  # @return [Integer] The number of vectors in the spanning set.
  def __len__(self):
    return len(self.vectors)

  # @param dimension [Integer] The dimension of the real space to use.
  # @return [Span] A basis for R^(dimension).
  # @raise [ValueError] If dimension is non-positive.
  @staticmethod
  def real_basis(dimension):
    if dimension <= 0:
      raise ValueError('Dimension of span must be positive.')
    vectors = []
    for i in xrange(dimension):
      vector = Vector([0] * dimension)
      vector[i] = 1
      vectors.append(vector)
    return Span(vectors)
