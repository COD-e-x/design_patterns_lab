from itertools import product


class TaxCalculator:
    def get_tax_rate(self, country, state=None, product=None):
        """Публичный метод для получения налоговой ставки в зависимости от страны, штата и товара."""
        if country == 'US' and state:
            return self.__get_us_tax(state)
        elif country == 'EU' and product:
            return self.__get_eu_tax(product, state)
        elif country == 'China' and product:
            return self.__get_china_tax(product)
        else:
            return 0.0

    @staticmethod
    def __get_us_tax(state):
        """Приватный метод для расчёта налоговой ставки для США по штату."""
        state_tax_rates = {
            'CA': 0.0725,  # Калифорния
            'NY': 0.04,    # Нью-Йорк
            'TX': 0.0625,  # Техас
            # Можно легко добавить при необходимости информацию!
        }
        return state_tax_rates.get(state, 0.07)  # Базовая ставка для других штатов 7%

    @staticmethod
    def __get_eu_tax(product, state):
        """Приватный метод для расчёта НДС в ЕС по стране и продукту."""
        country_tax_rates = {
            'Germany': {
                'food': 0.07,
                'electronics': 0.19,
                'clothing': 0.19,
            },
            'France': {
                'food': 0.055,
                'electronics': 0.20,
                'clothing': 0.20,
            },
            'Italy': {
                'food': 0.10,
                'electronics': 0.22,
                'clothing': 0.22,
            },
            # Можно легко добавить при необходимости информацию!
        }
        product_tax_rates = country_tax_rates.get(state, {})
        return product_tax_rates.get(product, 0.20)  # Базовая ставка 20%


    @staticmethod
    def __get_china_tax(product):
        """Приватный метод для расчёта НДС в Китае по продукту."""
        product_tax_rates = {
            'food': 0.13,
            'electronics': 0.17,
            'clothing': 0.10,
            # Можно легко добавить при необходимости информацию!
        }
        return product_tax_rates.get(product, 0.13) # Базовая ставка 13%


class Order:
    def __init__(self,tax_calculator: TaxCalculator, line_items, county, state=None, city=None):
        self.__tax_calculator = tax_calculator
        self.__line_items = line_items
        self.__county = county
        self.__state = state
        self.__city = city

    def get_order_total(self):
        total = 0
        for item in self.__line_items:
            product = item['product']
            price = item['price']
            tax_rate = self.__tax_calculator.get_tax_rate(self.__county, self.__state, product)
            total += price * tax_rate
        return total


if __name__ == '__main__':
    tax_calculator_ = TaxCalculator()
    line_items_ = [
        {'product': 'food', 'price': 1000},
        {'product': 'electronics', 'price': 1000},
    ]
    o = Order(tax_calculator_, line_items_, county='EU', state='France')
    print(o.get_order_total()) # 5.5% от 1000, 20% от 1000 = 255.0