
class BarNumberChecks(object):

    def __init__(self):
        self._bar_number_dict = {'A': [2, 4, 6],
                                 'B': [8, 10, 12],
                                 'C': [14, 16, 18],
                                 'D': [20, 22, 24],
                                 'E': [26, 28, 30],
                                 'F': [32, 34, 36],
                                 'G': [38, 40, 42],
                                 'H': [44, 46, 48],
                                 'I': [50, 52, 54],
                                 'J': [56, 58, 60],
                                 'K': [62, 64, 66],
                                 'L': [68, 70, 72],
                                 }

    def __call__(self, segment_name):
        return self.get_barNumbers(segment_name)

    def get_barNumbers(self, segment_name):
        """Allocates bar numbers in integer values depending
           on char representing segment name
         """
        bar_nums = self._bar_number_dict[segment_name]
        return bar_nums


if __name__ == '__main__':

    checks = BarNumberChecks()
    barNums = checks.get_barNumbers('A')
    print(barNums)
