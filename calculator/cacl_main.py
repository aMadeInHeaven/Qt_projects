from PyQt6.QtWidgets import QApplication, QMainWindow
from calculator.design.calc_design import Ui_MainWindow
from PyQt6.QtCore import Qt
import sys


class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setup(self)
        self.setup1()

        self.real_result = ["0"]

        self.is_equal = False
        self.math_sighns = ["+", "-", "/", "*", "("]

        self.brackets_stack = []

    def setup1(self):
        self.button_0.clicked.connect(lambda: self.write_number("0"))  # Done
        self.button_1.clicked.connect(lambda: self.write_number("1"))  # Done
        self.button_2.clicked.connect(lambda: self.write_number("2"))  # Done
        self.button_3.clicked.connect(lambda: self.write_number("3"))  # Done
        self.button_4.clicked.connect(lambda: self.write_number("4"))  # Done
        self.button_5.clicked.connect(lambda: self.write_number("5"))  # Done
        self.button_6.clicked.connect(lambda: self.write_number("6"))  # Done
        self.button_7.clicked.connect(lambda: self.write_number("7"))  # Done
        self.button_8.clicked.connect(lambda: self.write_number("8"))  # Done
        self.button_9.clicked.connect(lambda: self.write_number("9"))  # Done

        self.plus_button.clicked.connect(lambda: self.write_number("+"))  # Done
        self.minus_button.clicked.connect(lambda: self.write_number("-"))  # Done
        self.multiply_button.clicked.connect(lambda: self.write_number("*"))  # Done
        self.division_button.clicked.connect(lambda: self.write_number("/"))  # Done

        self.percent_button.clicked.connect(self.get_percent)  # Done
        self.bracket_button.clicked.connect(self.brackets)
        self.comma_button.clicked.connect(self.comma)  # Done
        self.negation_button.clicked.connect(self.negation)  # Done

        self.clear_button.clicked.connect(self.clear)  # Done
        self.equal_button.clicked.connect(self.result)  # Done

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        if event.key() == Qt.Key.Key_Backspace:
            if len(self.real_result[-1]) == 1:
                self.real_result.pop()
            else:
                self.real_result[-1] = self.real_result[-1][:-1]
            self.result_label.setText("".join(self.real_result))

    def write_number(self, number):

        if self.result_label.text() == "error, don't do that":
            print(1)
            if number.isdigit():
                self.real_result = [number]
            else:
                self.real_result = ["0"]

            self.result_label.setText("".join(self.real_result))

            '''если при вычислении была ошибка, то обнуляем или записываем вводимое число'''

        elif self.is_equal or self.real_result == ["0"]:
            self.is_equal = False
            if number == ".":
                self.real_result[-1] += "."
            elif number in self.math_sighns:
                self.real_result += [number]
            else:
                if self.real_result != ["0"]:
                    self.real_result[-1] += number
                else:
                    self.real_result = [number]
            self.result_label.setText("".join(self.real_result))

            '''если был получен результат (нажато равно) или на экране просто 0'''

        else:

            if number in self.math_sighns:
                if self.real_result[-1] not in self.math_sighns:
                    self.real_result += [number]

                '''если ввод - мат.знак проверяем, можно ли его вписать и вписываем, если можно'''

            elif number == ".":
                if self.real_result[-1] not in self.math_sighns and "." not in self.real_result[-1]:
                    self.real_result[-1][-1] += "."
                '''если вводят точку, смотрим, можно ли это сделать и вписываем, если можно'''
            else:

                if self.real_result[-1] != "0" and self.real_result[-1] not in self.math_sighns:
                    self.real_result[-1] += number

                elif self.real_result[-1] in self.math_sighns:
                    self.real_result += [number]

                '''проверяем возможность вписать число, если можно вписываем'''

            self.result_label.setText("".join(self.real_result))

    def result(self):

        delta_stack = []
        for sign in self.brackets_stack:
            if delta_stack != []:
                if delta_stack[-1] == "(" and sign == ")":
                    delta_stack.pop()
                else:
                    delta_stack.append(sign)
            else:
                delta_stack.append(sign)

        if delta_stack != []:
            count_open_brackets = delta_stack.count("(")
            self.real_result += [")"] * count_open_brackets

        try:
            res = eval("".join(self.real_result))
            if int(res) == res:

                self.real_result = [str(int(res))]
                self.result_label.setText("".join(self.real_result))
            else:

                self.real_result = [str(round(res, 8))]
                self.result_label.setText("".join(self.real_result))
        except:
            self.result_label.setText("error, don't do that")

        self.is_equal = True
        self.brackets_stack = []

    def get_percent(self):

        if self.result_label.text()[-1] in ["+", "-", "*", "/", "%"]:
            pass
        else:
            self.result_label.setText(self.result_label.text() + "%")
            equasion = self.real_result

            if len(equasion) == 1:
                self.real_result = [str(float(self.real_result[0]) / 100)]

            elif equasion[-2] in ["*", "/"]:
                self.real_result = self.real_result[:-1] + [str(float(self.real_result[-1]) / 100)]

            else:
                prev_number = eval("".join(self.real_result[:-2]))
                print(prev_number)
                self.real_result = [
                    str((float(prev_number) * float(eval("100" + self.real_result[-2] + self.real_result[-1]))) / 100)]

    def clear(self):

        self.real_result = ["0"]
        self.result_label.setText("".join(self.real_result))

        self.is_equal = False
        self.brackets_stack = []

    def brackets(self):
        print(self.brackets_stack)
        if self.real_result[-1] in self.math_sighns:
            self.real_result += ["("]
            self.brackets_stack += ["("]
        elif self.brackets_stack.count("(") > self.brackets_stack.count(")"):
            self.real_result += [")"]
            self.brackets_stack += [")"]
        self.result_label.setText("".join(self.real_result))

    def comma(self):
        print(self.real_result)
        if self.result_label.text() != "error, don't do that":
            if self.real_result[-1].isdigit() and ("." not in self.real_result[-1]):
                self.real_result[-1] += "."
                self.result_label.setText("".join(self.real_result))

    def negation(self):

        if self.real_result[-1] not in self.math_sighns:
            self.real_result[-1] = str(-int(self.real_result[-1]))
            self.result_label.setText("".join(self.real_result))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main_window()
    window.show()

    app.exec()
