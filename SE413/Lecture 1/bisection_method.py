import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def f(x):
    """
    Define a function (you can change to whatever function you want
    """
    return (x - np.pi)**2 + 4 * np.sin(x)

def visualize(function, minimum, iter_points, limits, npoints=100):
    """
    Quick plot of the function
    """
    x, y = function[0], function[1]
    lam_x = sym.lambdify(x, y)
    x_vals = np.linspace(limits[0], limits[1], num=npoints)
    y_vals = lam_x(x_vals)

    # Some plot configurations
    plt.rc('font', family='serif')
    plt.rc('font', size=11)
    plt.rc('axes', labelsize=11)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, 'r-')
    ax.plot(iter_points[0], iter_points[1], 'og')
    ax.plot(minimum[0], minimum[1], 'sr')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()

def bisection(function, limits, tol=1e-3, max_iter=100):
    """
    :param function: symbolic expression
    :param limits: limits of the function
    :param tol: tolerance to converge
    :return:
    """
    xm_vector = []
    fxm_vector = []
    b = [limits[0], limits[1]]
    if b[0] > b[1]:
        raise Exception('Bracket values must be in ascending order')

    yprime = function.diff(x)
    dfb0 = float(yprime.subs(x, b[0]))
    dfb1 = float(yprime.subs(x, b[1]))

    if not ((np.sign(dfb0) < 0) and (np.sign(dfb1) > 0)):
        raise Exception('Minimum may not be contained in bracket')

    b_size = b[1] - b[0]
    k = 0

    while (b_size > tol) and (k < max_iter):
        k += 1
        xm = (b[1] + b[0])/2
        fxm = float(y.subs(x, xm))
        dfxm = float(yprime.subs(x, xm))

        if dfxm == 0:
            break
        elif dfxm > 0:
            b[1] = xm
            xm_vector.append(xm)
            fxm_vector.append(fxm)
        elif dfxm < 0:
            b[0] = xm
            xm_vector.append(xm)
            fxm_vector.append(fxm)

        b_size = b[1] - b[0]
        minimum = [xm, fxm]
        iter_points = [xm_vector, fxm_vector]

    return minimum, iter_points



#%%
# You are supposed to run the previous box before
x = sym.symbols('x')
y = (x - sym.pi)**2 + 4 * sym.sin(x)
minimum, iter_points = bisection(y, [-10, 10])

function = [x, y]
visualize(function, minimum, iter_points, [-10, 10])

