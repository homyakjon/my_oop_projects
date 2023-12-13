"""1. Описуємо телефон:

Клас телефону.
У нього мають бути:

Поле для опису номера
Метод, щоб задати номер телефону
Захищене поле для лічильника вхідних дзвінків
Метод, який поверне нам кількість прийнятих дзвінків
Метод прийняти дзвінок, який додає до лічильника одиницю
Створіть три різні об’єкти телефону. Поміняйте всім початковий номер.
Прийміть по кілька дзвінків на кожному (різна кількість)

Напишіть функцію, яка приймає список з об’єктів телефонів,
а повертає загальну кількість прийнятих дзвінків з усіх телефонів.
* Зберігати інформацію про прийняті дзвінки у файл (txt або краще csv)

"""


import csv
from typing import List


class Phone:
    def __init__(self):
        self.description_number: str = ""
        self.__counter_enter_calls: int = 0

    def set_number_phone(self, value: str) -> None:
        self.description_number = value
        print(f'Входящий звонок: {self.description_number}')

    def __str__(self) -> str:
        return f'Phone(description_number={self.description_number}, accepted_calls={self.__counter_enter_calls})'

    def get_accepted_calls(self) -> int:
        print(f'Количество принятых звонков: {self.__counter_enter_calls}')
        return self.__counter_enter_calls

    def accept_call(self) -> None:
        self.__counter_enter_calls += 1

    def save_numbers(self, the_file: str) -> None:
        with open(the_file, 'a', newline='') as file:
            write_file = csv.writer(file)
            write_file.writerow(([self.description_number, self.get_accepted_calls()]))


def count_obj(phones: List[Phone]) -> int:
    result = 0
    for phone in phones:
        result += phone.get_accepted_calls()
    return result


p1 = Phone()
p2 = Phone()
p3 = Phone()

p1.set_number_phone("111-229-445")
p2.set_number_phone("444-555-666")
p3.set_number_phone("777-888-999")

p1.accept_call()
p1.accept_call()
p1.accept_call()
print(str(p1))
p2.accept_call()
p2.accept_call()
p2.accept_call()
p3.accept_call()
p3.accept_call()
p3.accept_call()

print(f'Общее количество принятых звонков: {count_obj([p1, p2, p3])}')

p1.save_numbers("phone1_number.csv")
p2.save_numbers("phone2_number.csv")
p3.save_numbers("phone3_number.csv")


"""2. Опишіть клас для фігури шахів.

Фігура повинна містити такі атрибути:

Колір (білий або чорний)
Місце на дошці (тут є варіанти, або два окремих поля, для опису координат або одне,
але, наприклад, кортеж з двох чисел)
І такі методи як:
Змінити колір (нічого не приймає, тільки змінює колір на протилежний)
Змінити місце на дошці (приймає або дві змінні або один кортеж з двох елементів), 
не забудьте перевірити, що ми не намагаємося поставити фігуру за межі дошки (обидва значення від 0 до 7)
Абстрактний метод перевірки потенційного ходу (деталі нижче)
На даному етапі фігури можуть стояти на одній і ті ж клітині, поки нам це не важливо
Опишіть класи, для пішака, коня, офіцера, тури, ферзя та короля. 
Все що в них потрібно додати - це один метод для перевірки, 
чи можливо за один хід поміняти місце фігури на дошці 
(всі ходять по-різному, пішаки мають ще й відмінність від кольору). 
Метод приймає знову ж таки або дві цифри, або один кортеж. 
І знову ж таки перевіряємо чи не виходить значення за межі дошки 
(оскільки нам потрібен цей функціонал двічі, бажано робити його як окремий захищений метод у батьківському класі).
І функцію, яка приймає список фігур та потенційну нову клітинку, 
а повертає список із фігур. Але тільки тих, які можуть за один хід дістатися цієї клітини.

* Скрізь описати типізації (у функціях, атрибутах та методах)"""


from typing import List
from abc import abstractmethod


class ChessFigures:
    def __init__(self, color='') -> None:
        self.color = color
        self.x_coord = 0
        self.y_coord = 0

    def change_color(self) -> str:
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'
        return self.color

    def get_color(self) -> str:
        if self.color not in ['white', 'black']:
            raise ValueError('Цвет выбран неверно')
        return f'Вы выбрали цвет: {self.change_color()}'

    def _set_validator(self, val1, val2) -> None:
        if val1 in range(0, 8) and val2 in range(0, 8):
            self.x_coord = val1
            self.y_coord = val2
        else:
            raise ValueError('Координаты фигур должны быть в диапазоне доски от 0 до 7')

    def get_step_validation(self) -> str:
        return f'Мы находимся в диапазоне шахматной доски: {self.x_coord}, {self.y_coord}'

    @abstractmethod
    def _change_place(self, val1, val2) -> None:
        print('Реализация в подклассах')

    def make_step(self, val1, val2) -> None:
        try:
            self._change_place(val1, val2)
        except ValueError as v_e:
            print(f"Фигура {self.__class__.__name__} не дойдет до клетки за один шаг. Ошибка: {v_e}")


class Pawn(ChessFigures):
    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 3) and val2 in range(0, 3):
            self._set_validator(val1, val2)
        else:
            raise ValueError('Координаты должны быть в диапазоне от 0 до 2')

    def get_step_validation(self) -> str:
        return f'Сделал ход пешкой с координатами: {self.x_coord}, {self.y_coord}'


class Horse(ChessFigures):
    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 6) and val2 in range(0, 6):
            self._set_validator(val1, val2)
        else:
            raise ValueError('Координаты должны быть в диапазоне от 0 до 5')

    def get_step_validation(self) -> str:
        return f'Сделал ход конем с координатами: {self.x_coord}, {self.y_coord}'


class Officer(ChessFigures):

    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 8) and val2 in range(0, 8):
            self._set_validator(val1, val2)
        else:
            raise ValueError('Координаты должны быть в диапазоне от 0 до 7')

    def get_step_validation(self) -> str:
        return f'Сделал ход офицером с координатами: {self.x_coord}, {self.y_coord}'


class Tour(ChessFigures):

    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 8) and val2 in range(0, 8):
            self._set_validator(val1, val2)
        else:
            raise ValueError('Координаты должны быть в диапазоне от 0 до 7')

    def get_step_validation(self) -> str:
        return f'Сделал ход турой с координатами: {self.x_coord}, {self.y_coord}'


class Queen(ChessFigures):

    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 8) and val2 in range(0, 8):
            self._set_validator(val1, val2)
        else:
            raise ValueError('Координаты должны быть в диапазоне от 0 до 7')

    def get_step_validation(self) -> str:
        return f'Сделал ход королевой с координатами: {self.x_coord}, {self.y_coord}'


class King(ChessFigures):

    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 2) and val2 in range(0, 2):
            self._set_validator(val1, val2)
        else:
            raise ValueError('Координаты должны быть в диапазоне от 0 до 1')

    def get_step_validation(self) -> str:
        return f'Сделал ход королем с координатами: {self.x_coord}, {self.y_coord}'


def figures_list(figures: List[ChessFigures], x_value: int, y_value: int) -> List:
    result = []
    for figure in figures:
        try:
            figure.make_step(x_value, y_value)
            result.append(figure)
        except ValueError as v:
            print(f"Фигура {figure.__class__.__name__} не дойдет до клетки за один шаг. Ошибка: {v}")
    return result


p = Pawn()
h = Horse()
of = Officer()
t = Tour()
q = Queen()
k = King()

x, y = 2, 4
step_figures = figures_list([p, h, of, t, q, k], x, y)
if not step_figures:
    print(f"Ни одна из фигур не может дойти до клетки за один шаг")
else:
    print("Фигуры, которые могут дойти до клетки за один шаг:")
    for f in step_figures:
        if f.x_coord == x and f.y_coord == y:
            print(f"{f.__class__.__name__} - {f.get_step_validation()}")
