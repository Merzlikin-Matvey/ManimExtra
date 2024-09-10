import math

from manim import (
    MathTex,
    VGroup,
    ArcBetweenPoints,
    FadeOut,
    AnimationGroup,
    override_animate,
    FadeIn
)

from manim.utils.color.manim_colors import *

from ..geometry.default import *

__all__ = [
    "UnitCircleLabel",
    "UnitCircle"
]


class UnitCircleLabel(MathTex):
    def __init__(self, direction=RIGHT, repeats=0, fraction=True, **kwargs):
        if (direction == RIGHT).all():
            self.other = False
            if repeats == 0:
                super().__init__(r'0', **kwargs)
            else:
                super().__init__(str(2 * repeats) + r'\pi', **kwargs)
        elif (direction == LEFT).all():
            if repeats == 0:
                super().__init__(r'\pi', **kwargs)
            elif repeats == -1:
                super().__init__(r'-\pi', **kwargs)
            else:
                super().__init__(str(2 * repeats + 1) + r'\pi', **kwargs)

        if fraction:
            if (direction == UP).all():
                if repeats > 0:
                    up_label_text = r'\dfrac{' + str(4 * repeats + 1) + r'\pi}{2}'
                elif repeats == 0:
                    up_label_text = r'\dfrac{\pi}{2}'
                else:
                    up_label_text = r'-\dfrac{' + str(-(4 * repeats + 1)) + r'\pi}{2}'
                super().__init__(up_label_text, **kwargs)
            if (direction == DOWN).all():
                if repeats >= 0:
                    down_label_text = r'\dfrac{' + str(4 * repeats + 3) + r'\pi}{2}'
                elif repeats == -1:
                    down_label_text = r'-\dfrac{\pi}{2}'
                else:
                    down_label_text = r'-\dfrac{' + str(-(4 * repeats + 3)) + r'\pi}{2}'
                super().__init__(down_label_text, **kwargs)

        else:
            if (direction == UP).all():
                super().__init__(str(2 * repeats + 0.5) + r'\pi', **kwargs)
            elif (direction == DOWN).all():
                super().__init__(str(2 * repeats + 1.5) + r'\pi', **kwargs)


class UnitCircle(VGroup):
    def __init__(self, point=0, radius=1.5, color=BLUE, label_buff=0.2, font_size=32, fractions=True):
        self.circle = Circle(radius=radius, color=color)

        self.labels = VGroup()
        self.dots = VGroup()

        self.other_right_basic_label = False

        repeats = math.floor(point / (2 * np.pi))
        self.repeats = repeats

        self.label_buff = label_buff
        self.font_size = font_size

        right = Dot(self.circle.point_at_angle(0))
        up = Dot(self.circle.point_at_angle(np.pi / 2))
        left = Dot(self.circle.point_at_angle(np.pi))
        down = Dot(self.circle.point_at_angle(3 * np.pi / 2))

        self.right = right
        self.up = up
        self.left = left
        self.down = down

        self.right_label = UnitCircleLabel(direction=RIGHT, repeats=repeats, fraction=fractions,
                                           font_size=font_size).next_to(right, RIGHT, buff=label_buff)
        self.up_label = UnitCircleLabel(direction=UP, repeats=repeats, fraction=fractions, font_size=font_size).next_to(
            up, UP, buff=label_buff)
        self.left_label = UnitCircleLabel(direction=LEFT, repeats=repeats, fraction=fractions,
                                          font_size=font_size).next_to(left, LEFT, buff=label_buff)
        self.down_label = UnitCircleLabel(direction=DOWN, repeats=repeats, fraction=fractions,
                                          font_size=font_size).next_to(down, DOWN, buff=label_buff)

        self.horizontal = Line(self.left, self.right)
        self.vertical = Line(self.down, self.up)

        super().__init__(self.circle, self.labels, self.dots)

    def get_center(self):
        return self.circle.get_center()

    def add_point(self, point, label):
        dot = Dot(self.circle.point_at_angle(point))
        if isinstance(label, str):
            label = MathTex(label, font_size=self.font_size).next_to(dot, Line(self.circle.get_center(),
                                                                               dot).get_unit_vector(),
                                                                     buff=self.label_buff)
        self.dots.add(dot)
        self.labels.add(label)
        return VGroup(dot, label)

    @override_animate(add_point)
    def _add_point_animation(self, point, label, anim_args=None):
        if anim_args is None:
            anim_args = {}
        dot, label = self.add_point(point, label)
        anim = FadeIn(VGroup(dot, label), **anim_args)
        return anim

    def _normalize_labels(self):
        VGroup(self.right, self.up, self.left, self.down, self.right_label, self.up_label, self.left_label,
                 self.down_label).move_to(self.circle.get_center())

    def show_labels(self):
        self._normalize_labels()
        self.add(self.right, self.up, self.left, self.down, self.right_label, self.up_label, self.left_label,
                 self.down_label)
        return self

    def hide_labels(self):
        self.remove(self.right, self.up, self.left, self.down, self.right_label, self.up_label, self.left_label,
                    self.down_label)
        return self

    @override_animate(show_labels)
    def _show_labels_animation(self, anim_args=None):
        self._normalize_labels()
        if anim_args is None:
            anim_args = {}
        anim = AnimationGroup(
            FadeIn(self.right, **anim_args),
            FadeIn(self.up, **anim_args),
            FadeIn(self.left, **anim_args),
            FadeIn(self.down, **anim_args),
            FadeIn(self.right_label, **anim_args),
            FadeIn(self.up_label, **anim_args),
            FadeIn(self.left_label, **anim_args),
            FadeIn(self.down_label, **anim_args)
        )
        return anim

    @override_animate(hide_labels)
    def _hide_labels_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        anim = AnimationGroup(
            FadeOut(self.right, **anim_args),
            FadeOut(self.up, **anim_args),
            FadeOut(self.left, **anim_args),
            FadeOut(self.down, **anim_args),
            FadeOut(self.right_label, **anim_args),
            FadeOut(self.up_label, **anim_args),
            FadeOut(self.left_label, **anim_args),
            FadeOut(self.down_label, **anim_args)
        )
        return anim

    def show_horizontal(self):
        self.add(self.horizontal)
        return self

    def hide_horizontal(self):
        self.remove(self.horizontal)
        return self

    @override_animate(show_horizontal)
    def _show_horizontal_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeIn(self.horizontal, **anim_args)

    @override_animate(hide_horizontal)
    def _hide_horizontal_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeOut(self.horizontal, **anim_args)

    def show_vertical(self):
        self.add(self.vertical)
        return self

    def hide_vertical(self):
        self.remove(self.vertical)
        return self

    @override_animate(show_vertical)
    def _show_vertical_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeIn(self.vertical, **anim_args)

    @override_animate(hide_vertical)
    def _hide_vertical_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return FadeOut(self.vertical, **anim_args)

    def show_axes(self):
        self.add(self.horizontal, self.vertical)
        return self

    def hide_axes(self):
        self.remove(self.horizontal, self.vertical)
        return self

    @override_animate(show_axes)
    def _show_axes_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return AnimationGroup(
            FadeIn(self.horizontal, **anim_args),
            FadeIn(self.vertical, **anim_args)
        )

    @override_animate(hide_axes)
    def _hide_axes_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        return AnimationGroup(
            FadeOut(self.horizontal, **anim_args),
            FadeOut(self.vertical, **anim_args)
        )

    def get_arc(self, start, end, **kwargs):
        return ArcBetweenPoints(self.circle.point_at_angle(start), self.circle.point_at_angle(end),
                                radius=self.circle.get_radius(), **kwargs)

    def get_abscissa_point(self, point):
        alpha = (1 + point) / 2
        return self.horizontal.point_from_proportion(alpha)

    def get_ordinate_point(self, point):
        alpha = (1 + point) / 2
        return self.vertical.point_from_proportion(alpha)

