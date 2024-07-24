import manim
from manim.constants import *

from ..useful_in_development import *
import numpy as np


class Line(manim.Line):
    def __init__(self, start=LEFT, end=manim.RIGHT, auto_dot_to_array=True, **kwargs):
        if auto_dot_to_array:
            start, end = dot_to_array(start, end)
        super().__init__(start, end, **kwargs)

    def is_point_in_line(self, dot):
        dot = dot_to_array(dot)[0]
        x1, y1 = self.get_start()[0], self.get_start()[1]
        x2, y2 = self.get_end()[0], self.get_end()[1]
        x3, y3 = dot[0], dot[1]
        return round(np.linalg.det(np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])), 3) == 0

    def set_length_about_point(self, length, dot):
        dot = dot_to_array(dot)[0]
        A = dot + np.array([length, 0, 0])
        line = Line(dot, A).rotate(about_point=dot, angle=self.get_angle())
        self.put_start_and_end_on(line.get_start(), line.get_end())
        return self
    
    def get_distance(self, dot):
        dot = dot_to_array(dot)[0]
        return Line(dot, self.get_projection(dot)).get_length()

    def equal(self, n=1, buff=0.1, length=0.2, **kwargs):
        return manim.VGroup(*[Line(**kwargs).set_length(length).rotate(
            about_point=Line(**kwargs).set_length(length).get_center(), angle=np.pi / 2) for i in range(n)]).arrange(
            buff=buff, direction=RIGHT).move_to(self.get_center()).rotate(
            about_point=self.get_center(), angle=self.get_angle()).set_z_index(1)

    def paral(self, n=1, buff=0.08, length=0.15, rotate=False, **kwargs):
        elem = manim.VGroup(
            Line(**kwargs).set_length(length).rotate(about_point=Line().set_length(0.2).get_end(),
                                                     angle=PI / 4).shift(0.02 * UR),
            Line(**kwargs).set_length(length).rotate(about_point=Line().set_length(0.2).get_end(),
                                                     angle=-PI / 4).shift(0.02 * DR)
        ).rotate(int(rotate) * np.pi)
        return manim.VGroup(*[elem.copy() for i in range(n)]).arrange(buff=buff, direction=RIGHT).move_to(
            self.get_center()).rotate(about_point=self.get_center(), angle=self.get_angle()).set_z_index(1)

    def inversion(self, circle, **kwargs):
        if self.is_point_in_line(circle.get_center()):
            return Line(self.get_start(), self.get_end(), **kwargs)
        else:
            dot_1 = circle_symmetry(circle, self.point_from_proportion(0.3))
            dot_2 = circle_symmetry(circle, self.point_from_proportion(0.5))
            dot_3 = circle_symmetry(circle, self.point_from_proportion(0.7))
            return Circle().from_three_points(dot_1, dot_2, dot_3, **kwargs)


class Angle(manim.Angle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def from_three_points(A, B, C, auto_dot_to_array=True, **kwargs):
        angle = Angle(Line(B, A), Line(B, C), **kwargs)
        if angle.get_angle_value() > PI:
            angle = Angle(Line(B, C), Line(B, A), **kwargs)
        return angle

    def get_label_center(self, delta=0.25):
        A = self.lines[0].get_end()
        B = self.lines[0].get_start()
        C = self.lines[1].get_end()
        A, B, C = dot_to_array(A, B, C)

        try:
            radius = self.radius
        except AttributeError:
            inter = manim.line_intersection(
                [self.lines[0].get_start(), self.lines[0].get_end()],
                [self.lines[1].get_start(), self.lines[1].get_end()],
            )

            if self.quadrant[0] == 1:
                dist_1 = np.linalg.norm(self.lines[0].get_end() - inter)
            else:
                dist_1 = np.linalg.norm(self.lines[0].get_start() - inter)
            if self.quadrant[1] == 1:
                dist_2 = np.linalg.norm(self.lines[1].get_end() - inter)
            else:
                dist_2 = np.linalg.norm(self.lines[1].get_start() - inter)
            if np.minimum(dist_1, dist_2) < 0.6:
                radius = (2 / 3) * np.minimum(dist_1, dist_2)
            else:
                radius = 0.4

        center = Line(B, Line(A, C).point_from_proportion(((Line(A, C).get_length() * Line(A, B).get_length()) / (
                Line(B, C).get_length() + Line(A, B).get_length())) / Line(A, C).get_length())).set_length_about_point(
            delta + radius, B).get_end()

        return center



class Circle(manim.Circle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def from_three_points(p1, p2, p3, auto_dot_to_array=True, **kwargs):
        if auto_dot_to_array:
            p1, p2, p3 = dot_to_array(p1, p2, p3)
        center = manim.line_intersection(
            manim.perpendicular_bisector([p1, p2]),
            manim.perpendicular_bisector([p2, p3]),
        )
        radius = np.linalg.norm(p1 - center)
        return Circle(radius=radius, **kwargs).shift(center)

    def pow(self, dot):
        dot = dot_to_array(dot)[0]
        return round((pow(self.get_center()[0] - dot[0], 2) + pow(self.get_center()[1] - dot[1], 2)) -
                     self.radius ** 2, 4)

    def is_point_in_circle(self, dot):
        dot = dot_to_array(dot)[0]
        return self.pow(dot) == 0
    
    def get_diametrically_opposite_point(self, dot):
        dot = dot_to_array(dot)[0]
        return self.get_center() + self.get_center() - dot


class Dot(manim.Dot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
