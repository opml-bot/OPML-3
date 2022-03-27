import numpy as np


def paraboloid(x):
    return x[0] ** 2 + x[1] ** 2


def ackley(x):
    a = 20
    b = 0.2
    c = 2 * np.pi
    return -a * np.exp(-b * np.sqrt(1 / 2 * (x[0] ** 2 + x[1] ** 2))) - np.exp(
        1 / 2 * (np.cos(c * x[0]) + np.cos(c * x[1]))) + a + np.exp(1)


def bukin(x):
    return 100 * np.sqrt(abs(x[1] - 0.01 * x[0] ** 2)) + 0.01 * abs(x[0] + 10)


def cross_in_tray(x):
    return -0.0001 * (
            abs(np.sin(x[0]) * np.sin(x[1]) * np.exp(abs(100 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi))) + 1) ** 0.1


def drop_wave(x):
    return - (1 + np.cos(12 * np.sqrt(x[0] ** 2 + x[1] ** 2))) / (0.5 * (x[0] ** 2 + x[1] ** 2) + 2)


def eggholder(x):
    return -(x[1] + 47) * np.sin(np.sqrt(abs(x[1] + x[0] / 2 + 47))) - x[0] * np.sin(np.sqrt(abs(x[0] - (x[1] + 47))))


def griewank(x):
    return (x[0] ** 2 + x[1] ** 2) / 4000 - np.cos(x[0] / np.sqrt(1)) * np.cos(x[1] / np.sqrt(2)) + 1


def holder_table(x):
    return -abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(abs(1 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi)))


def levy(x):
    w1 = 1 + (x[0] - 1) / 4
    w2 = 1 + (x[1] - 1) / 4
    return np.sin(np.pi * w1) ** 2 + (w1 - 1) ** 2 * (1 + 10 * np.sin(np.pi * w1 + 1) ** 2) + (w2 - 1) ** 2 * (
                1 + 10 * np.sin(2 * np.pi * w2) ** 2)


def levy13(x):
    return np.sin(3 * np.pi * x[0]) ** 2 + (x[0] - 1) ** 2 * (1 + np.sin(3 * np.pi * x[0]) ** 2) + (x[1] - 1) ** 2 * (
                1 + np.sin(2 * np.pi * x[1]) ** 2)


def rastrigin(x):
    return 10 * 2 + (x[0] ** 2 - 10 * np.cos(2 * np.pi * x[0])) + (x[1] ** 2 - 10 * np.cos(2 * np.pi * x[1]))


def schaffer(x):
    return 0.5 + (np.sin(x[0] ** 2 - x[1] ** 2) ** 2 - 0.5) / (1 + 0.001 * (x[0] ** 2 + x[1] ** 2)) ** 2

def schwefel(x):
    return 418.9829*2 - x[0]*np.sin(np.sqrt(abs(x[0]))) - x[1]*np.sin(np.sqrt(abs(x[1])))

paraboloid_point_min = [0, 0]
paraboloid_point_start = [10, 10]

ackley_point_min = [0, 0]
ackley_point_start = [-32.768, -32.768]

bukin_point_min = [-10, 1]
bukin_point_start = [-15, -3]

cross_in_tray_point_min = [1.3491, 1.3491]
cross_in_tray_point_start = [-10, -10]

drop_wave_point_min = [0, 0]
drop_wave_point_start = [-5.12, -5.12]

eggholder_point_min = [512, 404.2319]
eggholder_point_start = [-512, -512]

griewank_point_min = [0, 0]
griewank_point_start = [-600, -600]

holder_table_point_min = [8.05502, 9.66459]
holder_table_point_start = [-10, -10]

levy_point_min = [1, 1]
levy_point_start = [-10, -10]

levy13_point_min = [1, 1]
levy13_point_start = [-10, -10]

rastrigin_point_min = [0, 0]
rastrigin_point_start = [-5.12, -5.12]

schaffer_point_min = [0, 0]
schaffer_point_start = [-100, -100]

schwefel_point_min = [420.9687, 420.9687]
schwefel_point_start = [-500, -500]

funcs = {'paraboloid': [paraboloid, paraboloid_point_min, paraboloid_point_start],
         'Ackley function': [ackley, ackley_point_min, ackley_point_start],
         'Bukin function №6': [bukin, bukin_point_min, bukin_point_start],
         'Cross-in-tray function': [cross_in_tray, cross_in_tray_point_min, cross_in_tray_point_start],
         'Drop-wave function': [drop_wave, drop_wave_point_min, drop_wave_point_start],
         'Eggholder function': [eggholder, eggholder_point_min, eggholder_point_start],
         'Griewank function': [griewank, griewank_point_min, griewank_point_start],
         'Holder table function': [holder_table, holder_table_point_min, holder_table_point_start],
         'Levy function': [levy, levy_point_min, levy_point_start],
         'Levy №13 function': [levy13, levy13_point_min, levy13_point_start],
         'Rastrigin function': [rastrigin, rastrigin_point_min, rastrigin_point_start],
         'Schaffer function': [schaffer, schaffer_point_min, schaffer_point_start],
         'Schwefel function': [schwefel, schwefel_point_min, schwefel_point_start],}
