from sympy import parse_expr

print(compile(' -5.12', '<string>', 'eval').co_names)

print(parse_expr(' -5.12'))