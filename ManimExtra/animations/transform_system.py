from manim import AnimationGroup, Transform, FadeIn, FadeOut

from ..algebra.system_of_equations import SystemOfEquations

__all__ = [
    "TransformSystem"
]


class TransformSystem(AnimationGroup):
    def __init__(self, system_1, system_2, **kwargs):
        group = []

        group.append(Transform(system_1.brace, system_2.brace))

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
