from manim import (
    AnimationGroup,
    ApplyMethod,
    Transform,
    FadeIn,
    FadeOut
)
from manim.constants import *
import numpy as np

from ..algebra.system_of_equations import SystemOfEquations

__all__ = [
    "TransformSystem",
    "SwapEquations"
]


class TransformSystem(AnimationGroup):
    def __init__(self, system_1, system_2, **kwargs):
        self.system_1 = system_1
        self.system_2 = system_2
        group = [Transform(system_1.brace, system_2.brace)]

        equations_1 = system_1.equations
        equations_2 = system_2.equations

        size_1 = len(equations_1)
        size_2 = len(equations_2)

        if size_1 <= size_2:
            for i in range(size_1):
                group.append(Transform(equations_1[i], equations_2[i]))
            for i in range(size_1, size_2):
                group.append(FadeIn(equations_2[i]))
        else:
            for i in range(size_2):
                group.append(Transform(equations_1[i], equations_2[i]))
            for i in range(size_2, size_1):
                group.append(FadeOut(equations_1[i]))

        super().__init__(*group, **kwargs)

    def clean_up_from_scene(self, scene):
        super().clean_up_from_scene(scene)
        for eq in self.system_1.equations:
            scene.remove(eq)
        scene.remove(self.system_1.brace)
        for eq in self.system_2.equations:
            scene.remove(eq)
        scene.remove(self.system_2.brace)
        scene.add(self.system_2)


class SwapEquations(AnimationGroup):
    def __init__(self, system, i, j, **kwargs):
        self.system = system
        self.i, self.j = min(i, j), max(i, j)
        equations_between = self.system.equations[self.i + 1:self.j]
        delta = self.system.equations[self.i].get_height() - self.system.equations[self.j].get_height()
        super().__init__(
            ApplyMethod(equations_between.shift, delta * UP),
            ApplyMethod(self.system.equations[self.i].shift,
                        (2 * self.system.buff_between_equations + equations_between.get_height() +
                         self.system.equations[self.j].get_height()) * DOWN),
            ApplyMethod(self.system.equations[self.j].shift,
                        (2 * self.system.buff_between_equations + equations_between.get_height() +
                         self.system.equations[self.i].get_height()) * UP),
            **kwargs
        )

    def finish(self):
        self.system.equations[self.i], self.system.equations[self.j] = (
            self.system.equations[self.j], self.system.equations[self.i])


class InsertEquation(AnimationGroup):
    def __init__(self,
                 system: SystemOfEquations,
                 eq,
                 index,
                 direction=DOWN
                 ):
        self.system = system
        self.eq = eq
        self.index = index
        self.direction = direction

        if np.array_equal(direction, DOWN):
            under = system.equations[index:]
            delta = system.buff_between_equations + eq.get_height()
            eq.move_to(
                system.equations[index].get_center() + (
                        system.equations[index].get_height() - eq.get_height()) / 2 * UP +
                (system.equations[index].get_width() - eq.get_width()) / 2 * LEFT
            )

            brace_height = system.brace.get_height() + delta
            brace = system.brace.copy().scale_to_fit_height(brace_height).shift(delta / 2 * DOWN)

            shift_animation = ApplyMethod(under.shift, delta * DOWN)
            transform_brace = Transform(system.brace, brace)
            fade_in_animation = FadeIn(eq)

            super().__init__(
                shift_animation,
                transform_brace,
                fade_in_animation
            )
        elif np.array_equal(direction, UP):
            over = system.equations[:index]
            delta = system.buff_between_equations + eq.get_height()
            eq.move_to(
                system.equations[index].get_center() +
                (system.equations[index].get_height() + eq.get_height()) / 2 * UP +
                + self.system.buff_between_equations * UP +
                (system.equations[index].get_width() - eq.get_width()) / 2 * LEFT
            )

            brace_height = system.brace.get_height() + delta
            brace = system.brace.copy().scale_to_fit_height(brace_height).shift(delta / 2 * UP)

            shift_animation = ApplyMethod(over.shift, delta * UP)
            transform_brace = Transform(system.brace, brace)
            fade_in_animation = FadeIn(eq)

            super().__init__(
                shift_animation,
                transform_brace,
                fade_in_animation
            )
        else:
            under = system.equations[index:]
            over = system.equations[:index]
            delta = (system.buff_between_equations + eq.get_height()) / 2

            shift_under = ApplyMethod(under.shift, delta * DOWN)
            shift_over = ApplyMethod(over.shift, delta * UP)
            eq.move_to(
                system.equations[index].get_center() + (delta * DOWN) +
                (system.equations[index].get_height() + eq.get_height()) / 2 * UP +
                + self.system.buff_between_equations * UP +
                (system.equations[index].get_width() - eq.get_width()) / 2 * LEFT
            )

            brace_height = system.brace.get_height() + delta * 2
            brace = system.brace.copy().scale_to_fit_height(brace_height)

            super().__init__(
                shift_under,
                shift_over,
                Transform(system.brace, brace),
                FadeIn(eq)
            )

    def finish(self):
        self.system.equations.insert(self.index, self.eq)

