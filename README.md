![Main Logo](assets/logo.png)

<p align="center">
    <a href="https://pypi.org/project/manimextra/">
        <img src="https://img.shields.io/pypi/v/manimextra">
    </a>
    <a href="https://github.com/Merzlikin-Matvey/ManimExtra">
        <img src="https://img.shields.io/github/license/Merzlikin-Matvey/ManimExtra">
    </a>
</p>

<p align="center">
    ManimExtra - Addition to the standard set function in ManimCE
</p>

## Table of Contents:
- [What is it](#what-is-it)
- [Installation](#installation)
- [Examples](#examples)
- [Documentation](#documentation)

## What is it?

ManimExtra provides an advanced feature set for ManimCE.
The library makes it easy to work with geometry by adding 
many classic designs, such as a bisector or an inscribed circle.
There are also many objects 
that'll simplify the work with algebra by adding systems of equations and a trigonometric circle.

## Installation

Installing the library is straightforward. 
If there were no problems with the installation of ManimCE, 
then there'll be no problems here. 
On Windows, you need to write the command

> pip install manimextra

And on Linux/MacOS

> pip3 install manimextra

## Examples

Below are some complex usage examples combining several objects from ManimExtra.

### Example 1: Triangle Centers and Circles

```python
from manim import *
from manimextra import *

class TriangleCentersScene(Scene):
    def construct(self):
        # Define triangle vertices
        A = Dot(3 * LEFT + 2 * DOWN, color=RED)
        B = Dot(2 * LEFT + 3 * UP, color=GREEN)
        C = Dot(3 * RIGHT + 2 * DOWN, color=BLUE)

        # Triangle sides
        sides = VGroup(Line(B, C), Line(A, C), Line(A, B))

        # Centers
        incenter = Incenter(A, B, C).set_color(YELLOW)
        centroid = Centroid(A, B, C).set_color(PURPLE)
        circumcenter = Circumcenter(A, B, C).set_color(ORANGE)

        # Circles
        incircle = Incircle(A, B, C, color=YELLOW, stroke_opacity=0.5)
        circumcircle = Circumcircle(A, B, C, color=ORANGE, stroke_opacity=0.5)

        self.add(A, B, C, sides)
        self.play(FadeIn(incenter), FadeIn(incircle))
        self.play(FadeIn(centroid))
        self.play(FadeIn(circumcenter), FadeIn(circumcircle))
        self.wait()
```

### Example 2: System of Equations Animation

```python
from manim import *
from manimextra import *

class SystemOfEquationsExample(Scene):
    def construct(self):
        system1 = SystemOfEquations(
            MathTex("x + y = 2"),
            MathTex("x - y = 0")
        )
        system2 = SystemOfEquations(
            MathTex("x = 1"),
            MathTex("y = 1")
        )
        self.play(FadeIn(system1))
        self.wait()
        self.play(TransformSystem(system1, system2))
        self.wait()
```

### Example 3: Pie Chart and Unit Circle

```python
from manim import *
from manimextra import *

class PieAndCircleScene(Scene):
    def construct(self):
        pie = PieChart(
            data={"A": 10, "B": 20, "C": 30},
            label_buff=0.7,
            inner_radius=1,
            outer_radius=2
        ).to_edge(LEFT)
        circle = UnitCircle().to_edge(RIGHT)
        circle.add_point(PI / 2, r"\dfrac{\pi}{2}")
        circle.add_point(PI, r"\pi")
        self.play(FadeIn(pie), FadeIn(circle))
        self.wait()
```

## Documentation

Full documentation with API reference and more examples is available at:

- [ManimExtra Documentation](https://merzlikin-matvey.github.io/ManimExtra/)

You can also build the documentation locally by running:

```bash
cd docs
make html
```

and opening `docs/_build/html/index.html` in your browser.