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
        print(f'Incoming call: {self.description_number}')

    def __str__(self) -> str:
        return f'Phone(description_number={self.description_number}, accepted_calls={self.__counter_enter_calls})'

    def get_accepted_calls(self) -> int:
        print(f'number of calls received: {self.__counter_enter_calls}')
        return self.__counter_enter_calls

    def accept_call(self) -> None:
        self.__counter_enter_calls += 1

    def save_numbers(self, the_file: str) -> None:
        with open(the_file, 'a', newline='') as file:
            write_file = csv.writer(file)
            write_file.writerow([self.description_number, self.get_accepted_calls()])


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

print(f'Total number of call operations: {count_obj([p1, p2, p3])}')

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
    def __init__(self, color) -> None:
        self.color = color
        self.set_color(color)
        self.x_coord = 0
        self.y_coord = 0

    def set_color(self, color: str) -> None:
        if color not in ['white', 'black']:
            raise ValueError('incorrect color selected')
        self.color = color

    def change_color(self) -> str:
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'
        return self.color

    def get_color(self) -> str:
        return f'you have chosen a color: {self.change_color()}'

    def _set_validator(self, val1, val2) -> None:
        if val1 in range(0, 8) and val2 in range(0, 8):
            self.x_coord = val1
            self.y_coord = val2
        else:
            raise ValueError('The coordinates of the pieces must be in the board range from 0 to 7')

    def get_step_validation(self) -> str:
        return f"We're in the checkerboard range: {self.x_coord}, {self.y_coord}"

    @abstractmethod
    def _change_place(self, val1, val2) -> None:
        print('Implementation in subclasses')

    def make_step(self, val1, val2) -> None:
        try:
            self._change_place(val1, val2)
        except ValueError as v_e:
            print(f"Figure {self.__class__.__name__} will not reach the cage in one step. Error: {v_e}")


class Pawn(ChessFigures):
    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 3) and val2 in range(0, 3):
            self._set_validator(val1, val2)
        else:
            raise ValueError('The coordinates of the pieces must be in the board range from 0 to 2')

    def get_step_validation(self) -> str:
        return f'Made a move by the pawn with the coordinates: {self.x_coord}, {self.y_coord}'


class Horse(ChessFigures):
    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 6) and val2 in range(0, 6):
            self._set_validator(val1, val2)
        else:
            raise ValueError('The coordinates of the pieces must be in the board range from 0 to 5')

    def get_step_validation(self) -> str:
        return f'Made a move by the horse with the coordinates: {self.x_coord}, {self.y_coord}'


class Officer(ChessFigures):

    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 8) and val2 in range(0, 8):
            self._set_validator(val1, val2)
        else:
            raise ValueError('The coordinates of the pieces must be in the board range from 0 to 7')

    def get_step_validation(self) -> str:
        return f'made a move by the officer with coordinates: {self.x_coord}, {self.y_coord}'


class Tour(ChessFigures):

    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 8) and val2 in range(0, 8):
            self._set_validator(val1, val2)
        else:
            raise ValueError('The coordinates of the pieces must be in the board range from 0 to 7')

    def get_step_validation(self) -> str:
        return f'made a move with coordinates: {self.x_coord}, {self.y_coord}'


class Queen(ChessFigures):

    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 8) and val2 in range(0, 8):
            self._set_validator(val1, val2)
        else:
            raise ValueError('The coordinates of the pieces must be in the board range from 0 to 7')

    def get_step_validation(self) -> str:
        return f'Made a queen move with coordinates: {self.x_coord}, {self.y_coord}'


class King(ChessFigures):

    def _change_place(self, val1, val2) -> None:
        if val1 in range(0, 2) and val2 in range(0, 2):
            self._set_validator(val1, val2)
        else:
            raise ValueError('The coordinates of the pieces must be in the board range from 0 to 1')

    def get_step_validation(self) -> str:
        return f'Made a king move with coordinates: {self.x_coord}, {self.y_coord}'


def figures_list(figures: List[ChessFigures], x_value: int, y_value: int) -> List:
    result = []
    for figure in figures:
        try:
            figure.make_step(x_value, y_value)
            result.append(figure)
        except ValueError as v:
            print(f"Figure {figure.__class__.__name__} will not reach the cage in one step. Error: {v}")
    return result


p = Pawn('white')
h = Horse('black')
of = Officer('black')
t = Tour('black')
q = Queen('black')
k = King('white')

x, y = 2, 4
step_figures = figures_list([p, h, of, t, q, k], x, y)
if not step_figures:
    print(f"None of the pieces can reach the square in one step")
else:
    print("pieces that can reach a square in one step:")
    for f in step_figures:
        if f.x_coord == x and f.y_coord == y:
            print(f"{f.__class__.__name__} - {f.get_step_validation()}")
