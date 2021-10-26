import math
from dataclasses import dataclass
from typing import Callable


@dataclass
class Solution:
    x_0: float
    y_0: float
    x_range: float
    n: float

    def differential_equation(self, x: float, y: float) -> float:
        return math.exp(y) - 2 / x

    def calculate():
        pass


class ExactSolution(Solution):
    c: float
    n_range_min: float
    n_range_max: float
    exact: Callable[[float], float]

    def precalculate(self):
        self.c = (math.pow(math.e, -self.y_0) - self.x_0) / self.x_0 ** 2
        self.exact = lambda x: -math.log(self.c * x ** 2 + x)

    def calculate(self) -> list:
        self.precalculate()

        x = self.x_0
        h = self.x_range / self.n

        data = [(self.x_0, self.y_0)]
        data.append((float("{:.4f}".format(self.x_0)),
                     float("{:.4f}".format(self.y_0))))

        while x < self.x_range:
            x += h
            y = self.exact(x)

            data.append((float("{:.4f}".format(x)), float("{:.4f}".format(y))))
        
        return data

    def calculate_lte(self, points):
        self.precalculate()

        return map(lambda point: (point[0], self.exact(point[0]) - point[1]), points)

    def calculate_gte(self, solution):
        self.precalculate()

        points = []

        old_n = solution.n

        for n in range(self.n_range_min, self.n_range_max + 1):
            solution.n = n
            point = solution.calculate()[-1]
            points.append((n, abs(self.exact(point[0]) - point[1])))

        solution.n = old_n
        
        return points


class EulerSolution(Solution):
    def calculate(self) -> list:
        h = self.x_range / self.n
        x = self.x_0
        y = self.y_0

        data = []
        data.append((float("{:.4f}".format(self.x_0)),
                     float("{:.4f}".format(self.y_0))))

        while x < self.x_range:
            y += h * self.differential_equation(x, y)
            x += h

            data.append((float("{:.4f}".format(x)), float("{:.4f}".format(y))))

        return data


class ImprovedEulerSolution(Solution):
    def calculate(self) -> list:
        h = self.x_range / self.n
        x = self.x_0
        y = self.y_0

        k1: float
        h2 = 0.5 * h

        data = []
        data.append((float("{:.4f}".format(self.x_0)),
                     float("{:.4f}".format(self.y_0))))

        k1 = 0
        while x < self.x_range:
            k1 = h2 * self.differential_equation(x, y)
            y += h * self.differential_equation(x + h2, y + k1)
            x += h

            data.append((float("{:.4f}".format(x)), float("{:.4f}".format(y))))

        return data


class RungeKuttaSolution(Solution):
    def calculate(self) -> list:
        h = self.x_range / self.n
        x = self.x_0
        y = self.y_0

        k1: float
        h2 = 0.5 * h

        data = []
        data.append((float("{:.4f}".format(self.x_0)),
                     float("{:.4f}".format(self.y_0))))

        dy1 = dy2 = dy3 = dy4 = 0
        while x < self.x_range:
            dy1 = h * self.differential_equation(x, y)
            dy2 = h * self.differential_equation(x + h / 2.0, y + dy1 / 2.0)
            dy3 = h * self.differential_equation(x + h / 2.0, y + dy2 / 2.0)
            dy4 = h * self.differential_equation(x + h, y + dy3)

            x += h
            y += (dy1 + 2.0 * (dy2 + dy3) + dy4) / 6.0

            data.append((float("{:.4f}".format(x)), float("{:.4f}".format(y))))

        return data
