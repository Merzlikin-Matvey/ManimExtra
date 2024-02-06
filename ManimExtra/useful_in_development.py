import numpy as np
import manim


def dot_to_array(*dots) -> list:
    coordinates = []
    for dot in dots:
        if isinstance(dot, np.ndarray):
            coordinates.append(dot)
        else:
            try:
                coordinates.append(dot.get_center())
            except:
                pass
    return coordinates


def circle_symmetry(circle: manim.Circle, dot) -> np.ndarray:
    x, y, z = dot_to_array(dot)
    x0, y0, z0 = circle.get_center()
    r = circle.get_radius()
    return np.array([
        x0 + ((r ** 2 * (x - x0)) / ((x - x0) ** 2 + (y - y0) ** 2)),
        y0 + ((r ** 2 * (y - y0)) / ((x - x0) ** 2 + (y - y0) ** 2)),
        0
    ])


def distance(A, B) -> float:
    A, B = dot_to_array(A, B)
    return np.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2)

