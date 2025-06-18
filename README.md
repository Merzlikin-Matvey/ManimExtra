![Main Logo](https://raw.githubusercontent.com/Merzlikin-Matvey/ManimExtra/main/assets/logo.png)

<p align="center">
    <a href="https://pypi.org/project/manimextra/">
        <img src="https://img.shields.io/pypi/v/manimextra" alt="Project Version">
    </a>
    <a href="https://github.com/Merzlikin-Matvey/ManimExtra">
        <img src="https://img.shields.io/github/license/Merzlikin-Matvey/ManimExtra" alt="Project License">
    </a>
    <a>
        <img src="https://github.com/Merzlikin-Matvey/ManimExtra/workflows/Tests/badge.svg" alt="Tests">
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

### Example 1: Feuerbach Theorem
![feuerbach.png](https://raw.githubusercontent.com/Merzlikin-Matvey/ManimExtra/main/assets/feuerbach.png)

```python
from manim import *
from manimextra import *

class FeuerbachTheoremScene(Scene):
    def construct(self):
        A = Dot(2 * DOWN + 4 * LEFT).set_z_index(1)
        B = Dot(2 * UP + 2.5 * LEFT).set_z_index(1)
        C = Dot(2 * DOWN + 4 * RIGHT).set_z_index(1)
        
        AB = Line(A, B, color=BLUE)
        BC = Line(B, C, color=BLUE)
        CA = Line(C, A, color=BLUE)
        
        incircle = Incircle(A, B, C, color=YELLOW)
        nine_point_circle = NinePointCircle(A, B, C, color=GREEN)
        feuerbach = FeuerbachPoint(A, B, C)
        
        
        self.add(A, B, C, AB, BC, CA, incircle, nine_point_circle, feuerbach)
```

### Example 2: System of Equations Animation

![feuerbach.png](https://raw.githubusercontent.com/Merzlikin-Matvey/ManimExtra/main/assets/equaions.gif)


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

### Example 3: Pie Chart 

![piechart.png](https://raw.githubusercontent.com/Merzlikin-Matvey/ManimExtra/main/assets/piechart.png)


```python
from manim import *
from manimextra import *

class PieChartExample(Scene):
    def construct(self):
        pie_chart = PieChart(
            data={"First": 10, "Second": 20, "Third": 30},
            label_buff=0.7,
            inner_radius=1,
            outer_radius=2
        )
        self.add(pie_chart)
```

## Documentation

Full documentation with API reference and more examples is available at:

- [ManimExtra Documentation](https://merzlikin-matvey.github.io/ManimExtra/)

