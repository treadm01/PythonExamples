import math


class check_prime(object):

    def is_prime(self, number):
        square = int(math.sqrt(number))
        factor_found = False
        for i in range(2, square + 1):  # todo remove multiples of previous numbers? only check odd numbers?
            factor_found = number % i == 0
            if factor_found:
                break
        return not factor_found
