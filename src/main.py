from solutions import EulerSolution, ImprovedEulerSolution, RungeKuttaSolution, ExactSolution
from numpy import arange
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtCore import QLocale
from functools import reduce
import sys


def pyplotify(arrs, el):
    arrs[0].append(el[0])
    arrs[1].append(el[1])

    return arrs


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.locale = QLocale("en")

        self.doubleValidator = QDoubleValidator()
        self.doubleValidator.setLocale(self.locale)

        self.intValidator = QIntValidator()

        self.solutions__figure = plt.figure()
        self.lte_errors__figure = plt.figure()
        self.gte_errors__figure = plt.figure()

        self.setupUi()

    def editBox(self, label: str):
        edit = QLineEdit()
        edit.setValidator(self.doubleValidator)

        label = QLabel(label)

        box = QVBoxLayout()
        box.addWidget(label)
        box.addWidget(edit)

        return edit, box

    def setupUi(self):
        self.setWindowTitle("DE Egor Vlasov")

        euler__solution = EulerSolution(0, 0, 0, 0)
        improved_euler__solution = ImprovedEulerSolution(0, 0, 0, 0)
        runge_kutta__solution = RungeKuttaSolution(0, 0, 0, 0)
        exact__solution = ExactSolution(0, 0, 0, 0)

        x_0__edit, x_0__box = self.editBox("x_0")
        y_0__edit, y_0__box = self.editBox("y_0")
        x_range__edit, x_range__box = self.editBox("x_range")
        n__edit, n__box = self.editBox("n")
        n__edit.setValidator(self.intValidator)
        n_range_min__edit, n_range_min__box = self.editBox("n_range_min")
        n_range_min__edit.setValidator(self.intValidator)
        n_range_max__edit, n_range_max__box = self.editBox("n_range_max")
        n_range_max__edit.setValidator(self.intValidator)

        def x_0__edited():
            val, ok = self.locale.toDouble(x_0__edit.text())

            if not ok:
                print("x_0: ", x_0__edit.text())
                return

            euler__solution.x_0 = val
            improved_euler__solution.x_0 = val
            runge_kutta__solution.x_0 = val
            exact__solution.x_0 = val

        def y_0__edited():
            val, ok = self.locale.toDouble(y_0__edit.text())

            if not ok:
                print("y_0: ", y_0__edit.text())
                return

            euler__solution.y_0 = val
            improved_euler__solution.y_0 = val
            runge_kutta__solution.y_0 = val
            exact__solution.y_0 = val

        def x_range__edited():
            val, ok = self.locale.toDouble(x_range__edit.text())

            if not ok:
                print("x_range: ", x_range__edit.text())
                return

            euler__solution.x_range = val
            improved_euler__solution.x_range = val
            runge_kutta__solution.x_range = val
            exact__solution.x_range = val

        def n__edited():
            val, ok = self.locale.toInt(n__edit.text())

            if not ok:
                print("n: ", n__edit.text())
                return

            euler__solution.n = val
            improved_euler__solution.n = val
            runge_kutta__solution.n = val
            exact__solution.n = val

        def n_range_min__edited():
            val, ok = self.locale.toInt(n_range_min__edit.text())

            if not ok:
                print("n: ", n_range_min__edit.text())
                return

            exact__solution.n_range_min = val

        def n_range_max__edited():
            val, ok = self.locale.toInt(n_range_max__edit.text())

            if not ok:
                print("n: ", n_range_max__edit.text())
                return

            exact__solution.n_range_max = val

        x_0__edit.textEdited.connect(x_0__edited)
        y_0__edit.textEdited.connect(y_0__edited)
        x_range__edit.textEdited.connect(x_range__edited)
        n__edit.textEdited.connect(n__edited)
        n_range_min__edit.textEdited.connect(n_range_min__edited)
        n_range_max__edit.textEdited.connect(n_range_max__edited)

        solutions__canvas = FigureCanvas(self.solutions__figure)
        solutions__toolbar = NavigationToolbar(solutions__canvas, self)

        lte_errors__canvas = FigureCanvas(self.lte_errors__figure)
        lte_errors__toolbar = NavigationToolbar(lte_errors__canvas, self)

        gte_errors__canvas = FigureCanvas(self.gte_errors__figure)
        gte_errors__toolbar = NavigationToolbar(gte_errors__canvas, self)

        calculate__button = QPushButton("Calculate")
        calculate_gte__button = QPushButton("Calculate")

        def calculate():
            euler_points = euler__solution.calculate()
            improved_euler_points = improved_euler__solution.calculate()
            runge_kutta_points = runge_kutta__solution.calculate()
            exact_points = exact__solution.calculate()

            self.solutions__figure.clear()

            ax = self.solutions__figure.add_subplot(111)

            ax.plot(*reduce(pyplotify, euler_points, ([], [])),
                    label="Euler Solution")
            ax.plot(*reduce(pyplotify, improved_euler_points, ([], [])),
                    label="Improved Euler Solution")
            ax.plot(*reduce(pyplotify, runge_kutta_points, ([], [])),
                    label="Runge Kutta Solution")
            ax.plot(*reduce(pyplotify, exact_points, ([], [])),
                    label="Exact Solution")

            ax.legend()

            euler_lte = exact__solution.calculate_lte(euler_points)
            improved_euler_lte = exact__solution.calculate_lte(
                improved_euler_points)
            runge_kutta_lte = exact__solution.calculate_lte(runge_kutta_points)

            self.lte_errors__figure.clear()

            ax = self.lte_errors__figure.add_subplot(111)

            ax.plot(*reduce(pyplotify, euler_lte, ([], [])), label="Euler LTE")
            ax.plot(*reduce(pyplotify, improved_euler_lte, ([], [])),
                    label="Improved Euler LTE")
            ax.plot(*reduce(pyplotify, runge_kutta_lte, ([], [])),
                    label="Runge Kutta LTE")

            ax.legend()

            solutions__canvas.draw()
            lte_errors__canvas.draw()

        def calculate_gte():
            euler_gte = exact__solution.calculate_gte(euler__solution)
            improved_euler_gte = exact__solution.calculate_gte(
                improved_euler__solution)
            runge_kutta_gte = exact__solution.calculate_gte(
                runge_kutta__solution)

            self.gte_errors__figure.clear()

            ax = self.gte_errors__figure.add_subplot(111)

            ax.plot(*reduce(pyplotify, euler_gte, ([], [])), label="Euler GTE")
            ax.plot(*reduce(pyplotify, improved_euler_gte, ([], [])),
                    label="Improved Euler GTE")
            ax.plot(*reduce(pyplotify, runge_kutta_gte, ([], [])),
                    label="Runge Kutta GTE")

            ax.legend()

            gte_errors__canvas.draw()

        calculate__button.clicked.connect(calculate)
        calculate_gte__button.clicked.connect(calculate_gte)

        edit__vbox = QVBoxLayout()
        edit__vbox.addWidget(QLabel("Solutions & LTEs"))
        edit__vbox.addLayout(x_0__box)
        edit__vbox.addLayout(y_0__box)
        edit__vbox.addLayout(x_range__box)
        edit__vbox.addLayout(n__box)
        edit__vbox.addWidget(calculate__button)
        edit__vbox.addStretch(1)
        edit__vbox.addWidget(QLabel("GTEs"))
        edit__vbox.addLayout(n_range_min__box)
        edit__vbox.addLayout(n_range_max__box)
        edit__vbox.addWidget(calculate_gte__button)
        edit__vbox.addStretch(1)

        plot__vbox = QVBoxLayout()
        plot__vbox.addWidget(QLabel("Solutions"))
        plot__vbox.addWidget(solutions__toolbar)
        plot__vbox.addWidget(solutions__canvas)
        plot__vbox.addWidget(QLabel("LTEs"))
        plot__vbox.addWidget(lte_errors__toolbar)
        plot__vbox.addWidget(lte_errors__canvas)

        plot1__vbox = QVBoxLayout()
        plot1__vbox.addWidget(QLabel("GTEs"))
        plot1__vbox.addWidget(gte_errors__toolbar)
        plot1__vbox.addWidget(gte_errors__canvas)

        hbox = QHBoxLayout()
        hbox.addLayout(edit__vbox)
        hbox.addLayout(plot__vbox)
        hbox.addLayout(plot1__vbox)

        self.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())