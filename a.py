import sympy as sp

# 定义符号变量 x
x = sp.symbols("x")

# 定义表达式
expr = (x - 100) * (x - 1.111) * (x - 3000.113)

# 展开表达式
expanded_expr = sp.expand(expr)

# 将展开后的表达式转换为多项式形式
poly_expr = sp.Poly(expanded_expr, x)

# 获取所有系数列表，从最高次到最低次
coeffs = poly_expr.all_coeffs()

# 输出展开式和系数
print(expr)
print(expanded_expr)
print(" ".join(map(str, coeffs)))
