def clockwise_rotate_matrix_outer(matrix, rotate=1):

  for rot in range(1, rotate+1):
    outer_loop = []
    # Initialise edge pointers
    top = 0
    bottom = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    prev = matrix[top + 1][left]

    # Move elements of top row one step right
    for i in range(left, right + 1):
      curr = matrix[top][i]
      outer_loop.append(prev)
      matrix[top][i] = prev
      prev = curr

    top += 1

    # Move elements of rightmost column one step downwards
    for i in range(top, bottom + 1):
      curr = matrix[i][right]
      outer_loop.append(prev)
      matrix[i][right] = prev
      prev = curr

    right -= 1

    # Move elements of bottom row one step left
    for i in range(right, left - 1, -1):
      curr = matrix[bottom][i]
      outer_loop.append(prev)
      matrix[bottom][i] = prev
      prev = curr

    bottom -= 1

    # Move elements of leftmost column one step upwards
    for i in range(bottom, top - 1, -1):
      curr = matrix[i][left]
      outer_loop.append(prev)
      matrix[i][left] = prev
      prev = curr

    left += 1
  return matrix


def matrix_print(matrix):
  print "___"*10
  for row in matrix:
    for val in row:
      print '{:4}'.format(val),
    print
  print "___" * 10


matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
print "Current matrix"
matrix_print(matrix)
n = int(input("Rotate count---> "))
matrix = clockwise_rotate_matrix_outer(matrix, n)
print "Final Matrix"
matrix_print(matrix)
