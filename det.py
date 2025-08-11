def det3x3(matrix):
    """
    Calculate determinant of a 3x3 matrix.
    matrix: list of lists, e.g.,
    [[a11, a12, a13],
     [a21, a22, a23],
     [a31, a32, a33]]
    """
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("Matrix must be 3x3.")

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    print(f"{a} {b} {c}")
    print(f"{d} {e} {f}")
    print(f"{g} {h} {i}")
    print(f*h)
    one = a * ((e * i) - ( f * h))
    two =    - b * ((d * i) - (f * g))
    three =     + c * ((d * h) - (e * g))
    print(f"{one} {two} {three}")
    return (
       one+two+three
    )

# Example usage:
mat = [
    [-9, -6, 7],
    [-2, -5, 4],
    [3, -9, 5]
]
print("Determinant:", det3x3(mat))
