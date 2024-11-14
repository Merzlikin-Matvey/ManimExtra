import typing

from manim import AnnularSector, VGroup, Tex
from manim.constants import *
from manim.utils.color import *

import numpy as np
import typing

PIE_CHART_COLORS = [
    RED,
    GREEN,
    BLUE,
    MAROON,
    YELLOW,
    TEAL
]


class PieChartSector(AnnularSector):
    """
    A sector of a pie chart.

    Parameters
    ----------
    value : float
        The value of the sector.
    percent : float
        The percentage of the sector.
    label : str
        The label of the sector.
    """
    def __init__(self, value, percent, label, *args, **kwargs):
        self.value = value
        self.percent = percent
        self.label = label
        angle = percent / 100 * 2 * PI
        super().__init__(angle=angle + 0.0075, *args, **kwargs)


class PieChart(VGroup):
    """
    A pie chart.

    Parameters
    ----------
    data : Union[dict, tuple]
        The data of the pie chart. If it is a dictionary, the keys are the labels and the values are the values.
        If it is a tuple, the first element is the labels and the second element is the values.
    labels : Optional[List[str]]
        The labels of the pie chart.
    label_buff : float, optional
        The buffer between the label and the sector. Default to 0.85.
    colors : List[Union[str, Tuple[float, float, float]]], optional
        The colors of the sectors. Default to PIE_CHART_COLORS.
    inner_radius : float, optional
        The inner radius of the sectors. Default to 1.
    outer_radius : float, optional
        The outer radius of the sectors. Default to 2.
    """
    def __init__(self,
                 data,
                 labels=None,
                 label_buff: float = 0.85,
                 colors=PIE_CHART_COLORS,
                 inner_radius=1,
                 outer_radius=2,
                 ):
        if isinstance(data, dict):
            labels = list(data.keys())
            values = list(data.values())
        elif isinstance(data, tuple):
            labels, values = data
        else:
            labels = labels if labels else [i for i in range(len(data))]
            values = data

        n = len(values)
        sum_values = sum(values)
        sum_angle = 0

        self.values = values
        self.labels = VGroup()
        self.sectors = VGroup()

        if n > len(colors):
            raise ValueError(f"Too many values for pie chart. Maximum is {len(PIE_CHART_COLORS)}")

        for i in range(n):
            val = values[i]
            angle = val / sum_values * 2 * PI

            sector = PieChartSector(
                value=val,
                percent=100 * val / sum_values,
                label=labels[i],
                color=colors[i],
                inner_radius=inner_radius,
                outer_radius=outer_radius
            ).rotate(about_point=ORIGIN, angle=sum_angle)

            label = Tex(labels[i]).move_to(RIGHT * sector.outer_radius).rotate(
                about_point=ORIGIN, angle=(sum_angle + angle / 2)).rotate(-(sum_angle + angle / 2)).shift(
                label_buff * np.array(
                    [np.cos(sum_angle + angle / 2), np.sin(sum_angle + angle / 2), 0]))

            sum_angle += angle

            self.sectors.add(sector)
            self.labels.add(label)

        super().__init__(self.sectors, self.labels)

    def get_labels(self):
        return self.labels

    def get_sectors(self):
        return self.sectors

    def get_sector(self, value=None, label=None):
        """
        Get a sector by value or label.

        :param value:
        :param label:
        :return:
        """
        for sector in self.sectors:
            if value:
                if sector.value == value:
                    return sector
            if label:
                if sector.label == label:
                    return sector
        raise ValueError("No sector with that value or label found")
