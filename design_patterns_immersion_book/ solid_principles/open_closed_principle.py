# Нарушение OCP: для добавления нового типа отчета нужно менять существующий код

class Report1:
    def __init__(self, data):
        self.data = data

    def generate(self, report_type):
        if report_type == 'summary':
            return self.generate_summary()
        elif report_type == 'detailed':
            return self.generate_detailed()
        else:
            raise ValueError('Неизвестный тип отчета.')

    def generate_summary(self):
        return f'Краткий отчет: {sum(self.data)}'

    def generate_detailed(self):
        return f'Детальный отчет: {', '.join(map(str, self.data))}'


# Если нужно добавить новый тип отчета, например 'statistics', нужно изменить первоначальный код в классе Report1

# Исправление OCP: расширяем класс через наследование, не изменяя существующий код
class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        raise NotImplementedError('Подклассы должны реализовывать этот метод.')


class SummaryReport(Report):
    def generate(self):
        return f'Краткий отчет: {sum(self.data)}'


class DetailedReport(Report):
    def generate(self):
        return f'Детальный отчет: {', '.join(map(str, self.data))}'


class StatisticsReport(Report):
    def generate(self):
        return f'Отчет по статистике: Средний = {sum(self.data) / len(self.data)}'


if __name__ == '__main__':
    data1 = [10, 20, 30]
    report_summary = SummaryReport(data1)
    report_detailed = DetailedReport(data1)
    report_statistics = StatisticsReport(data1)

    print(report_summary.generate())
    print(report_detailed.generate())
    print(report_statistics.generate())
