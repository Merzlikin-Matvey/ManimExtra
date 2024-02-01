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


def circle_symmetry(circle: manim.Circle, dot) -> tuple:
    x, y, z = dot_to_array(dot)
    x0, y0, z0 = circle.get_center()
    r = circle.get_radius()
    return (
        x0 + ((r ** 2 * (x - x0)) / ((x - x0) ** 2 + (y - y0) ** 2)),
        y0 + ((r ** 2 * (y - y0)) / ((x - x0) ** 2 + (y - y0) ** 2)),
        0
    )
