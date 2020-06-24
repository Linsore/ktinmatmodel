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


alfa = 1
x, y, alp = sympy.symbols('x[0], x[1], alpha')
u_e = x**2 + y**2

def poisson(uuu):
    f = -sympy.diff(uuu, x, x) - sympy.diff(uuu, y, y) + alp * uuu
    # Площади функций
    domain = Circle(Point(0, 0), 1)
    mesh = generate_mesh(domain, 20)
    V = FunctionSpace(mesh, 'P', 2)
    # Определение границ
    u_D = Expression(ccode(uuu), degree=2)


    def boundary_D(x, on_boundary):
        if on_boundary:
            if x[1] < 0:
                return True
            else:
                return False
        else:
            return False

    bc = DirichletBC(V, u_D, boundary_D)

    n = FacetNormal(mesh)

    # МКЭ
    u = TrialFunction(V)
    v = TestFunction(V)
    f = Expression(ccode(f), degree = 2, alpha = alfa)
    h = Expression('{0} * x[0] / sqrt(x[0]*x[0] + x[1]*x[1]) + {1} * x[1] / sqrt(x[0]*x[0] + x[1]*x[1])'.format(
        ccode(gradient(uuu)[0]), ccode(gradient(uuu)[1])), degree = 2)

    a = dot(grad(u), grad(v)) * dx + alfa * u * v * dx

    L = f*v*dx + h*v*ds

    # Решение
    u = Function(V)
    solve(a == L, u, bc)
    # Ошибка в норме Л2
    error_L2 = errornorm(u_D, u, 'L2')
    # Максимум норма
    vertex_values_u_D = u_D.compute_vertex_values(mesh)
    vertex_values_u = u.compute_vertex_values(mesh)
    error_max = np.max(np.abs(vertex_values_u_D - vertex_values_u))
    print('error_L2  =', error_L2)
    print('error_max =', error_max)

    n = mesh.num_vertices()
    d = mesh.geometry().dim()
    mesh_coordinates = mesh.coordinates().reshape((n, d))
    triangles = np.asarray([cell.entities(0) for cell in cells(mesh)])
    triangulation = tri.Triangulation(mesh_coordinates[:, 0], mesh_coordinates[:, 1], triangles)
    mplot.figure()
    gs = gridspec.GridSpec(1, 2)

    ax1 = mplot.subplot(gs[0])
    zfaces = np.asarray([u(cell.midpoint()) for cell in cells(mesh)])
    ax1.tripcolor(triangulation, facecolors=zfaces, edgecolors='k')
    ax1.set_title('Решение')

    ax2 = mplot.subplot(gs[1])
    zfaces = np.asarray([u_D(cell.midpoint()) for cell in cells(mesh)])
    ax2.tripcolor(triangulation, facecolors=zfaces, edgecolors='k')
    ax2.set_title('Аналитическое')


poisson(u_e)
#poisson(3*x**2 - 2*y**2)
#poisson(6*x**2 * sym_trig.cos(y) + sym_trig.sin(y))
