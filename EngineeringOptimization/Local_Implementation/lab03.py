import numpy as np
from numpy.linalg import inv
from autograd import grad, hessian

# Let's define an objective function
def obj_f(x):
    f = 0.5 * (x[0]**2 + 20 * x[1]**2)
    return f

# Defining Rosenbrok function
def rosb(x):
    return ((x[0] - 1)**2 + 100 * (x[1] - x[0]**2)**2)

def grad_f(func, x):
    """
    Computes the gradient of a given function @ point x
    """
    return grad(func)(x)

def hess_f(func, x):
    """
    Computes the hessian of a given function @ point x
    """
    return hessian(func)(x)

def armijo(func, x_cur, search_dir, c1, alpha0):
    """
    Verify f(x + alpha p) <= f(x) + c1 alpha grad(f).p
    """
    alpha = alpha0
    x_new = x_cur + alpha * search_dir
    f_cur = func(x_cur)
    f_new = func(x_new)
    grad_cur = grad_f(func, x_cur)
    n_iter = 0

    while f_new > f_cur + c1 * alpha * np.dot(grad_cur, search_dir):
        n_iter += 1
        alpha = alpha/2
        x_new = x_cur + alpha * search_dir
        f_new = func(x_new)

    return alpha, n_iter

def wolfe(func, x_cur, search_dir, c1, c2, alpha0):
    """
    Verify a) f(x+alpha p) <= f(x) + c1 alpha grad(f).T p
           b) grad(f(x + alpha p)).T p >= c2 grad(f).T p
    """
    alpha = alpha0
    x_new = x_cur + alpha * search_dir
    f_cur = func(x_cur)
    f_new = func(x_new)
    grad_cur = grad_f(func, x_cur)
    grad_new = grad_f(func, x_new)
    n_iter = 0

    # Bounds
    lb = 0
    ub = np.inf

    # Check Wolfe conditions
    while True:
        n_iter += 1
        if f_new > f_cur + c1 * alpha * np.dot(grad_cur, search_dir):
            ub = alpha
            alpha = 0.5 * (lb + up)/2
        elif np.dot(grad_new, search_dir) < c2 * np.dot(grad_cur, search_dir)
            lb = alpha
            if np.isinf(ub):
                alpha = 2 * lb
            else:
                alpha = (lb + ub)/2
        else:
            break

        x_new = x_cur + alpha * search_dir
        f_new = func(x_new)
        grad_new = grad_f(func, x_new)

    return alpha, n_iter



def steepest_descent(func, x0, stepRule, c1, c2, alpha0, tol=0.01):
    """
    Computes the steepest descend direction for unconstrained optimization
    """

