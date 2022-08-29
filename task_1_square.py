def new_zone_square(square1: tuple, square2: tuple)-> int:
    '''
    Возращает значение, какой должна быть новая площадь, чтобы в ней поместились старые 2.
    Значения должны быть в одинаковых еденицах измерения
    :param square1: кортеж координат первой площади вида x1,y1,x2,y2
    :param square2: кортеж координат второй площади вида x3,y3,x4,y4
    :return: размер новой площади
    '''
    if square1[0] > square2[0]:  # если первый квадрат находится левее, чем правый
        square1, square2 = square2, square1  # то меняем их местами

    x1, y1, x2, y2 = square1
    x3, y3, x4, y4 = square2
    # Найдем самую длинную сумарную сторону, учитывая пробелы между прямоугольниками
    sum_side_Y = y4 - y1
    sum_side_X = x4 - x1
    # учтем, если одна из сторон больше суммы двух других
    longest_side_X = x2 - x1 if x2 - x1 > x4 - x3 else x4 - x3
    longest_side_Y = y2 - y1 if y2 - y1 > y4 - y3 else y4 - y3
    # считаем какое из этих чисел больше всего и возращаем его квадрат
    sum_side = sum_side_Y if sum_side_Y > sum_side_X else sum_side_X
    longest_side = longest_side_X if longest_side_X > longest_side_Y else longest_side_Y

    return sum_side ** 2 if sum_side > longest_side else longest_side ** 2


def test1_new_zone_square():
    assert new_zone_square((6, 6, 8, 8), (1, 8, 4, 9)) == 49


def test2_new_zone_square():
    assert new_zone_square((1, 1, 6, 2), (1, 3, 3, 5)) == 25


def test3_new_zone_square():
    assert new_zone_square((1, 1, 4, 5), (5, 5, 9, 9)) == 64
