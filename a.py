import sympy as sp
import numpy as np

a = np.array([[1, 3, 1, -4], [-1, -3, 1, 0], [2, 6, 2, -8]])

c = a.T @ a
result = ""
for x in c:
    result += " & ".join(map(str, x)) + " \\\\\n"
print(result)
print(np.linalg.matrix_rank(c))

c = a

result = ""
for x in c:
    result += " & ".join(map(str, x)) + " \\\\\n"
print(result)
print(np.linalg.matrix_rank(c))

c = a @ a.T

result = ""
for x in c:
    result += " & ".join(map(str, x)) + " \\\\\n"
print(result)
print(np.linalg.matrix_rank(c))
