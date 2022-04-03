def paraboloid(x1, x2):
    return f"x1 ** 2 + x2 ** 2"


def ackley(x1, x2):
    return f"- 20* exp(- 0.2* sqrt(1 / 2 * (x1 ** 2 + x2 ** 2))) - exp(1 / 2 * (cos( 2 * pi* x1) + cos( 2 * pi* x2))) +  20+ exp(1)"


def bukin(x1, x2):    return f"100 * sqrt(abs(x2 - 0.01 * x1 ** 2)) + 0.01 * abs(x1 + 10)"



def cross_in_tray(x1, x2):
    return f"-0.0001 * (abs(sin(x1) * sin(x2) * exp(abs(100 - sqrt(x1 ** 2 + x2 ** 2) / pi))) + 1) ** 0.1"


def drop_wave(x1, x2):
    return f"- (1 + cos(12 * sqrt(x1 ** 2 + x2 ** 2))) / (0.5 * (x1 ** 2 + x2 ** 2) + 2)"


def eggholder(x1, x2):
    return f"-(x2 + 47) * sin(sqrt(abs(x2 + x1 / 2 + 47))) - x1 * sin(sqrt(abs(x1 - (x2 + 47))))"


def griewank(x1, x2):
    return f"(x1 ** 2 + x2 ** 2) / 4000 - cos(x1 / sqrt(1)) * cos(x2 / sqrt(2)) + 1"


def holder_table(x1, x2):
    return f"-abs(sin(x1) * cos(x2) * exp(abs(1 - sqrt(x1 ** 2 + x2 ** 2) / pi)))"


def levy(x1, x2):
    return f"sin(pi *  1 + (x1 - 1) / 4) ** 2 + ( 1 + (x1 - 1) / 4- 1) ** 2 * (1 + 10 * sin(pi *  1 + (x1 - 1) / 4+ 1) ** 2) + ( 1 + (x2 - 1) / 4- 1) ** 2 * (1 + 10 * sin(2 * pi *  1 + (x2 - 1) / 4) ** 2)"


def levy13(x1, x2):
    return f"sin(3 * pi * x1) ** 2 + (x1 - 1) ** 2 * (1 + sin(3 * pi * x1) ** 2) + (x2 - 1) ** 2 * (1 + sin(2 * pi * x2) ** 2)"


def rastrigin(x1, x2):
    return f"10 * 2 + (x1 ** 2 - 10 * cos(2 * pi * x1)) + (x2 ** 2 - 10 * cos(2 * pi * x2))"


def schaffer(x1, x2):
    return f"0.5 + (sin(x1 ** 2 - x2 ** 2) ** 2 - 0.5) / (1 + 0.001 * (x1 ** 2 + x2 ** 2)) ** 2"


def schwefel(x1, x2):
    return f"418.9829 * 2 - x1 * sin(sqrt(abs(x1))) - x2 * sin(sqrt(abs(x2)))"


def bocharevsky(x1, x2):
    return f"x1 ** 2 + 2 * x2 ** 2 - 0.3 * cos(3 * pi * x1) - 0.4 * cos(4 * pi * x2) + 0.7"


def perm(x1, x2):
    return f"((1 +  0.5) * (x1 ** 1 - 1 / (1) ** 1) + (2 +  0.5) * (x2 ** 1 - 1 / (2) ** 1)) ** 2 + ((1 +  0.5) * (x1 ** 2 - 1 / (1) ** 2) + (2 +  0.5) * (x2 ** 2 - 1 / (2) ** 2)) ** 2"


def diff_power(x1, x2):
    return f"abs(x1) ** 2 + abs(x2) ** 3"


def trid(x1, x2):
    return f"(x1 - 1) ** 2 + (x2 - 1) ** 2 - x1 * x2"


def booth(x1, x2):
    return f"(x1 + 2 * x2 - 7) ** 2 + (2 * x1 + x2 - 5) ** 2"


def matyas(x1, x2):
    return f"0.26 * (x1 ** 2 + x2 ** 2) - 0.48 * x1 * x2"


def mccormick(x1, x2):
    return f"sin(x1 + x2) + (x1 - x2) ** 2 - 1.5 * x1 + 2.5 * x2 + 1"


def zakharov(x1, x2):
    return f"x1 ** 2 + x2 ** 2 + (0.5 * 1 * x1 + 0.5 * 2 * x2) ** 2 + (0.5 * 1 * x1 + 0.5 * 2 * x2) ** 4"


def three_hump(x1, x2):
    return f"2 * x1 ** 2 - 1.05 * x1 ** 4 + x1 ** 6 / 6 + x1 * x2 + x2 ** 2"


def six_hump(x1, x2):
    return f"(4 - 2.1 * x1 ** 2 + x1 ** 4 / 3) * x1 ** 2 + x1 * x2 + (-4 + 4 * x2 ** 2) * x2 ** 2"


def dixon_price(x1, x2):
    return f"(x1 - 1) ** 2 + 2 * (2 * x2 ** 2 - x1) ** 2"


def rosenbrock(x1, x2):
    return f"100 * (x2 - x1 ** 2) ** 2 + (x1 - 1) ** 2"


def easom(x1, x2):
    return f"-cos(x1) * cos(x2) * exp(-(x1 - pi) ** 2 - (x2 - pi) ** 2)"


def michalewicz(x1, x2):
    return f"-(sin(x1)*sin(x1**2/pi)**(2*10))-(sin(x2)*sin(2*x2**2/pi)**(2*10))"


paraboloid_point_min = "0; 0"
paraboloid_point_start = "-5.12; -5.12"

ackley_point_min = "0; 0"
ackley_point_start = "-32.768; -32.768"

bukin_point_min = "-10; 1"
bukin_point_start = "-15; -3"

cross_in_tray_point_min = "1.3491; 1.3491"
cross_in_tray_point_start = "-10; -10"

drop_wave_point_min = "0; 0"
drop_wave_point_start = "-5.12; -5.12"

eggholder_point_min = "512; 404.2319"
eggholder_point_start = "-512; -512"

griewank_point_min = "0; 0"
griewank_point_start = "-600; -600"

holder_table_point_min = "8.05502; 9.66459"
holder_table_point_start = "-10; -10"

levy_point_min = "1; 1"
levy_point_start = "-10; -10"

levy13_point_min = "1; 1"
levy13_point_start = "-10; -10"

rastrigin_point_min = "0; 0"
rastrigin_point_start = "-5.12; -5.12"

schaffer_point_min = "0; 0"
schaffer_point_start = "-100; -100"

schwefel_point_min = "420.9687; 420.9687"
schwefel_point_start = "-500; -500"

bocharevsky_point_min = "0; 0"
bocharevsky_point_start = "-100; -100"

perm_point_min = "0; 0.5"
perm_point_start = "-2; -2"

diff_power_point_min = "0; 0"
diff_power_point_start = "-1; -1"

trid_point_min = "2; 6"
trid_point_start = "-4; -4"

booth_point_min = "1; 3"
booth_point_start = "-10; -10"

matyas_point_min = "0; 0"
matyas_point_start = "-10; -10"

mccormick_point_min = "-0.54719; -1.54719"
mccormick_point_start = "-1.5; -3"

# powersum_point_min = "None; None"
# powersum_point_start = "0; 0"

zakharov_point_min = "0; 0"
zakharov_point_start = "-5; -5"

three_hump_point_min = "0; 0"
three_hump_point_start = "-5; -5"

six_hump_point_min = "0.0898; -0.7126"
six_hump_point_start = "-3; -2"

dixon_price_point_min = "1; 2 ** (-0.5)"
dixon_price_point_start = "-10; -10"

rosenbrock_point_min = "1; 1"
rosenbrock_point_start = "-5; -5"

easom_point_min = "pi; pi"
easom_point_start = "-100; -100"

michalewicz_point_min = "2.20; 1.57"
michalewicz_point_start = "pi; pi"

funcs_str = {'Paraboloid': [paraboloid, paraboloid_point_min, paraboloid_point_start],
             'Ackley function': [ackley, ackley_point_min, ackley_point_start],
             'Bukin function №6': [bukin, bukin_point_min, bukin_point_start],
             'Cross-in-tray function': [cross_in_tray, cross_in_tray_point_min, cross_in_tray_point_start],
             'Drop-wave function': [drop_wave, drop_wave_point_min, drop_wave_point_start],
             'Eggholder function': [eggholder, eggholder_point_min, eggholder_point_start],
             'Griewank function': [griewank, griewank_point_min, griewank_point_start],
             #'Holder table function': [holder_table, holder_table_point_min, holder_table_point_start],
             'Levy function': [levy, levy_point_min, levy_point_start],
             'Levy №13 function': [levy13, levy13_point_min, levy13_point_start],
             'Rastrigin function': [rastrigin, rastrigin_point_min, rastrigin_point_start],
             'Schaffer function': [schaffer, schaffer_point_min, schaffer_point_start],
             'Schwefel function': [schwefel, schwefel_point_min, schwefel_point_start],
             'Bocharevsky function': [bocharevsky, bocharevsky_point_min, bocharevsky_point_start],
             'Perm 0,d,beta function': [perm, perm_point_min, perm_point_start],
             'Sum of different powers function': [diff_power, diff_power_point_min, diff_power_point_start],
             'Trid function': [trid, trid_point_min, trid_point_start],
             'Booth function': [booth, booth_point_min, booth_point_start],
             'Matyas function': [matyas, matyas_point_min, matyas_point_start],
             'Mccormick function': [mccormick, mccormick_point_min, mccormick_point_start],
             # 'Power sum function': [powersum, powersum_point_min, powersum_point_start],
             'Zakharov function': [zakharov, zakharov_point_min, zakharov_point_start],
             'Three-hump function': [three_hump, three_hump_point_min, three_hump_point_start],
             'Six-hump function': [six_hump, six_hump_point_min, six_hump_point_start],
             'Dixon-price function': [dixon_price, dixon_price_point_min, dixon_price_point_start],
             'Rosenbrock function': [rosenbrock, rosenbrock_point_min, rosenbrock_point_start],
             'Easom function': [easom, easom_point_min, easom_point_start],
             'Michalewicz function': [michalewicz, michalewicz_point_min, michalewicz_point_start]}
