def paraboloid(x):
    return x[0] ** 2 + x[1] ** 2


paraboloid_point_min = [10, 10]
paraboloid_point_start = [0, 0]

funcs = {'paraboloid': [paraboloid, paraboloid_point]}
