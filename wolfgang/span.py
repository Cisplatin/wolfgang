from wolfgang.vector import Vector

class Span:
  # @param vector [List<Vector>] The spanning set of vectors.
  def __init__(self, vectors):
    self.vectors = vectors

  # @return [Integer] The number of vectors in the spanning set.
  def __len__(self):
    return len(self.vectors)
