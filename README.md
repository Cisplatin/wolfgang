# wolfgang

Wolfgang is a small and fast utility for vector manipulation in Python.

## Example

```
from wolfgang import Vector

vector_1 = Vector([1, 2, 3])
vector_2 = Vector.from_points((0, 0, 0), (1, 1, 1))

print vector_1[0] # => 1
print len(vector_2) # => 3

cross_product = vector_1.cross(vector_2)
print cross_product # => ⟨-1, 2, -1⟩
```

For a list of all functions and information on their use and parameters, see
`vector.py <https://github.com/Cisplatin/wolfgang/blob/master/wolfgang/vector.py>_`

## Development

To run all tests, use:

```
python -m unittest discover
```
