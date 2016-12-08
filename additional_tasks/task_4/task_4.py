from math import sqrt


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "x: " + str(self._x) + ", y: " + str(self._y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


def count_distance(point_1, point_2):
    return sqrt(pow(point_2.get_x() - point_1.get_x(), 2) + pow(point_2.get_y() - point_1.get_y(), 2))


def get_minimal_sum_distance_point(surface):
    min_sum_distance = float('inf')
    min_sum_point = None

    for point in surface:
        other_points = {other_point for other_point in surface if other_point is not point}
        distance_sum = 0
        for other_point in other_points:
            distance = count_distance(point, other_point)
            distance_sum += distance

        if distance_sum < min_sum_distance:
            min_sum_distance = distance_sum
            min_sum_point = point

    return min_sum_point

if __name__ == "__main__":
    test_surface = {Point(12, 2), Point(3, 7), Point(32, 54), Point(13, 43)}
    print(get_minimal_sum_distance_point(surface=test_surface))
