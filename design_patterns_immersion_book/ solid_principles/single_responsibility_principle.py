# Нарушение SRP: один класс выполняет несколько задач

class Report:
    def __init__(self, data):
        self.data = data

    def calculate(self):
        return sum(self.data)

    def display(self):
        print('Отчет:', self.calculate())


# Исправление SRP: делаем отдельные классы для расчета и вывода

class ReportCalculator:
    def __init__(self, data):
        self.data = data

    def calculate(self):
        return sum(self.data)


class ReportDisplay:
    def __init__(self, report):
        self.report = report

    def display(self):
        print('Отчет:', self.report.calculate())


if __name__ == '__main__':
    data1 = [10, 20, 30]

    report_calculator = ReportCalculator(data1)
    report_display = ReportDisplay(report_calculator)

    report_display.display()
