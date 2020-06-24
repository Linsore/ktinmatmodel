from fenics import *
from mshr import *
import numpy as np
import sympy
import matplotlib.pyplot as mplot
import matplotlib.tri as tri
import matplotlib.gridspec as gridspec
from sympy.printing import ccode
sympy.init_printing()
import sympy.functions.elementary.trigonometric as sym_trig


def gradient(u):
    return sympy.diff(u, x), sympy.diff(u, y)


def laplass(u):
    return sympy.diff(u, x,x) + sympy.diff(u, y,y)


x, y, a, t = sympy.symbols('x[0], x[1], a, t')

u_e = x**2 + y**2 + t

def teploprov(u_e, step):
    x, y, a, t = sympy.symbols('x[0], x[1], a, t')
    #шаг
    dt = step
    # Площади функций
    domain = Circle(Point(0, 0), 1)
    mesh = generate_mesh(domain, 20)
    V = FunctionSpace(mesh, 'P', 2)
    u_D = Expression(ccode(u_e), degree=2, t=0)

    # Определение границ
    def boundary(x, on_boundary):
        if on_boundary:
            if x[1] < 0:
                return True
            else:
                return False
        else:
            return False

    bc = DirichletBC(V, u_D, boundary)

    u_n = interpolate(u_D, V)
    u = TrialFunction(V)
    v = TestFunction(V)
    sympy.diff(u_e, t)
    f = Expression(ccode(sympy.diff(u_e, t) - a * laplass(u_e)), a = 1, degree = 2, t = 0)
    h = Expression(
        '{0} * x[0] / sqrt(x[0]*x[0] + x[1]*x[1]) + {1} * x[1] / sqrt(x[0]*x[0] + x[1]*x[1])'.format(
            ccode(gradient(u_e)[0]), ccode(gradient(u_e)[1])
        ), degree = 2, t = 0
    )

    F = u*v*dx + dt*dot(grad(u), grad(v))*dx - (u_n + dt*f)*v*dx - dt * v * h * ds
    a, L = lhs(F), rhs(F)
    u = Function(V)
    t=0
    # Решение на времни t
    for n in range(step):
        t += dt
        u_D.t = t
        h.t = t
        f.t = t
        solve(a == L, u, bc)
        u_e = interpolate(u_D, V)
        error = np.abs(u_e.vector().get_local()- u.vector().get_local()).max()
        print(' t = ', t, ',max error = ', error, 'L2 error = ', errornorm(u_e, u, 'L2'))

        u_n.assign(u)

    n = mesh.num_vertices()
    d = mesh.geometry().dim()
    mesh_coordinates = mesh.coordinates().reshape((n, d))
    triangles = np.asarray([cell.entities(0) for cell in cells(mesh)])
    triangulation = tri.Triangulation(mesh_coordinates[:, 0], mesh_coordinates[:, 1], triangles)
    plt.figure()
    gs = gridspec.GridSpec(1, 2)

    ax1 = plt.subplot(gs[0])
    zfaces = np.asarray([u(cell.midpoint()) for cell in cells(mesh)])
    ax1.tripcolor(triangulation, facecolors=zfaces, edgecolors='k')
    ax1.set_title('solution')

    ax2 = plt.subplot(gs[1])
    zfaces = np.asarray([u_e(cell.midpoint()) for cell in cells(mesh)])
    ax2.tripcolor(triangulation, facecolors=zfaces, edgecolors='k')
    ax2.set_title('original')


teploprov((x**2 - y**2) * t, 20)
#teploprov(4*x * t, 20)
#teploprov(x * sym_trig.cos(y) + 6*sym_trig.sin(2*y) *sym_trig.sin(t), 20)
