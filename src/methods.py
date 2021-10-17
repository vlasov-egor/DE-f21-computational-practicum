import math
from dataclasses import dataclass


class NumericalMethod:

    x_0: float
    y_0: float
    x_range: float

    def differential_equation(x_0: float, y_0: float) -> float:
        (math.exp**y_0 - 2 / x_0)

    def get_approximation():
        pass

    def numerical_method():
        pass


class EulerMethod(NumericalMethod):
    def calculate(self) -> list(tuple(float, float)):

        print("Euler Method")
        h = 1
        x = self.x_0
        y = self.y_0

        data = [(self.x_0, self.y_0)]

        print(
            f"""Current x: {float("{:.4f}".format(self.x_0))}\nCurrent y: {float("{:.4f}".format(self.y_0))}"""
        )

        data.append((float("{:.4f}".format(self.x_0),
                           float("{:.4f}".format(self.y_0)))))

        while x < self.x_range:
            y += h * self.differential_equation(x, y)
            x += h

            print(
                f"""Current x: {float("{:.4f}".format(x))}\nCurrent y: {float("{:.4f}".format(y))}"""
            )
            data.append((float("{:.4f}".format(x), float("{:.4f}".format(y)))))

        print("Approximate solution at x = {:.4f} is {:.4f}".format(x, y))
        return data

    def plot():
        pass


class ImprovedEulerMethod(NumericalMethod):
    def calculate(self) -> list(tuple(float, float)):

        print("Improved Euler Method")
        h = 1
        x = self.x_0
        y = self.y_0

        k1: float
        h2 = 0.5 * h

        data = [(self.x_0, self.y_0)]

        print(
            f"""Current x: {float("{:.4f}".format(self.x_0))}\nCurrent y: {float("{:.4f}".format(self.y_0))}"""
        )

        data.append((float("{:.4f}".format(self.x_0),
                           float("{:.4f}".format(self.y_0)))))

        while (x < self.x_range):
            k1 = h2 * self.differential_equation(x, y)
            y += h * self.differential_equation(x + h2, y + k1)
            x += h

            print(
                f"""Current x: {float("{:.4f}".format(x))}\nCurrent y: {float("{:.4f}".format(y))}"""
            )

            data.append((float("{:.4f}".format(x), float("{:.4f}".format(y)))))

        print("Approximate solution at x = {:.4f} is {:.4f}".format(x, y))
        return data

    def get_next():
        pass


class RungeKuttaMethod(NumericalMethod):
    def calculate(self) -> list(tuple(float, float)):

        print("Runge Kutta Method")
        h = 1
        x = self.x_0
        y = self.y_0

        k1: float
        h2 = 0.5 * h

        data = [(self.x_0, self.y_0)]

        print(
            f"""Current x: {float("{:.4f}".format(self.x_0))}\nCurrent y: {float("{:.4f}".format(self.y_0))}"""
        )

        data.append((float("{:.4f}".format(self.x_0),
                           float("{:.4f}".format(self.y_0)))))

        while (x < self.x_range):
            dy1 = h * self.differential_equation(x, y)
            dy2 = h * self.differential_equation(x + h / 2.0, y + dy1 / 2.0)
            dy3 = h * self.differential_equation(x + h / 2.0, y + dy2 / 2.0)
            dy4 = h * self.differential_equation(x + h, y + dy3)

            x += h
            y += (dy1 + 2.0 * (dy2 + dy3) + dy4) / 6.0
            print(
                f"""Current x: {float("{:.4f}".format(x))}\nCurrent y: {float("{:.4f}".format(y))}"""
            )

            data.append((float("{:.4f}".format(x), float("{:.4f}".format(y)))))

        print("Approximate solution at x = {:.4f} is {:.4f}".format(x, y))
        return data

    def get_next():
        pass
