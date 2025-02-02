> Примеры из книги не совсем подошли, поэтому я решил сам привести описание каждого принципа и соответствующий
> пример кода, который, по моему мнению, будет более понятен и удобен для восприятия!
(Всегда берем в расчет - возможно, мне не хватает уровня для понимания.)

# SOLID

> SOLID — это набор из пяти принципов объектно-ориентированного проектирования, которые помогают создавать программы,
> удобные для дальнейшей доработки и расширения. Эти принципы были предложены Робертом Сесилом Мартином,
> более известным как "Дядя Боб" (Uncle Bob), в начале 2000-х годов. Они стали основой для написания качественного и
> гибкого кода.

## S - Single Responsibility Principle (SRP) (Принцип единственной ответственности)

- Принцип единой ответственности гласит, что класс должен иметь только одну причину для изменения, то есть он должен
- отвечать за одну задачу.
    - **Зачем это нужно?** Если класс выполняет несколько разных задач, при изменении одной из них придется менять весь
      класс, что увеличивает вероятность ошибок.
    - **Пример:** Если у нас есть класс, который одновременно выполняет логику расчётов и выводит данные, то при
      изменении логики вывода нужно будет изменять и расчёты, что нарушает принцип.
- [Файл с реализацией кода - S](https://github.com/COD-e-x/design_patterns_lab/blob/main/design_patterns_immersion_book/solid_principles/single_responsibility_principle.py)

## O - Open/Closed Principle (OCP) (Принцип открытости/закрытости)

- Принцип открытости/закрытости гласит, что классы должны быть открыты для расширения, но закрыты для модификации.
    - **Зачем это нужно?** Это означает, что мы должны иметь возможность добавлять новую функциональность в программу,
      не изменяя уже существующий код, а только расширяя его.
    - **Как это работает?** Мы не должны изменять существующие классы, а должны создавать новые, которые расширяют
      функциональность существующих. Это позволяет минимизировать риски при внесении изменений.
- [Файл с реализацией кода - O](https://github.com/COD-e-x/design_patterns_lab/blob/main/design_patterns_immersion_book/solid_principles/open_closed_principle.py)

## L - Liskov Substitution Principle (LSP) (Принцип подстановки Лисков)

- Принцип подстановки Барбары Лисков гласит: объекты дочерних классов должны быть взаимозаменяемы с объектами их
  базового класса.
    - **Зачем это нужно?** Это обеспечивает предсказуемость поведения программы: мы должны быть уверены, что, заменяя
      объект базового класса объектом дочернего, функциональность программы останется корректной.
    - **Как это работает?** Дочерний класс не должен нарушать ожидания, заданные интерфейсом или поведением базового
      класса.
- [Файл с реализацией кода - L](https://github.com/COD-e-x/design_patterns_lab/blob/main/design_patterns_immersion_book/solid_principles/liskov_substitution_principle.py)

## I - Interface Segregation Principle (ISP) (Принцип разделения интерфейса)

- Принцип разделения интерфейсов гласит: клиенты не должны зависеть от интерфейсов, которые они не используют.
    - **Зачем это нужно?** Если интерфейс содержит методы, которые не нужны некоторым классам, то эти классы будут либо
      нарушать реализацию, либо иметь ненужную зависимость. Это делает код сложным в поддержке и использовании.
    - **Как это работает?** Разделяйте большие интерфейсы на более мелкие, специфичные интерфейсы, которые будут
      содержать только методы, необходимые для конкретного клиента.
- [Файл с реализацией кода - I](https://github.com/COD-e-x/design_patterns_lab/blob/main/design_patterns_immersion_book/solid_principles/interface_segregation_principle.py)

## D - Dependency Inversion Principle (DIP) (Принцип инверсии зависимости)

- Принцип инверсии зависимостей гласит: модули верхнего уровня (логика приложения) не должны зависеть от модулей нижнего
  уровня (детали реализации). Оба типа модулей должны зависеть от абстракций. Абстракции не должны зависеть от деталей,
  но детали должны зависеть от абстракций.
    - **Зачем это нужно?** Чтобы уменьшить связь между модулями и сделать систему более гибкой для изменений.
      Это позволяет заменить одну реализацию другой без необходимости переписывать весь код.
    - **Как это работает?** Верхний уровень взаимодействует с нижним через интерфейсы или абстрактные классы, а не через
      конкретные реализации.
- [Файл с реализацией кода - D](https://github.com/COD-e-x/design_patterns_lab/blob/main/design_patterns_immersion_book/solid_principles/dependency_inversion_principle.py)

