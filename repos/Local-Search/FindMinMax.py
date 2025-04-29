"""

The class FindMinMax finds the minimum or the maximum value of a list. The constructor initializes the private function compare, 
which points to one of the private static functions minimum(a, b) or maximum(a, b).

"""

class FindMinMax():
    MIN = 0
    MAX = 1

    def __init__(self, data, find=MIN):
        self.__data = data
        self.__compare = self.__maximum if find == self.MAX else self.__minimum


    def find(self):
        m = self.__data[0]

        for value in self.__data:
            if self.__compare(value, m) < 0:
                m = value

        return m

    @staticmethod
    def __minimum(a, b):
        return a - b

    @staticmethod
    def __maximum(a, b):
        return b - a


if __name__ == "__main__":

    numbers = [11, 30, 9, 5, 9, 2, 15, 1, 7]

    finder = FindMinMax(numbers)

    print("Min", finder.find())

    finder = FindMinMax(numbers, FindMinMax.MIN)

    print("Min", finder.find())

    finder = FindMinMax(numbers, FindMinMax.MAX)

    print("Max", finder.find())
