
class SequenceGenerator(object):
    "Library of functions for generating musical material"

    __slots__ = ()

    @staticmethod
    def generate_random_pulse_sequence(length):
        """
         Takes an int n as argument
         returns a list of n bits with
         1/-1 values to use as counts
        """

        from random import getrandbits

        bits = getrandbits
        binary_string = "{0:b}".format(bits(length))
        binary_list = [int(x) for x in binary_string]
        rhythm_list = [x if x == 1 else -1 for x in binary_list]
        return rhythm_list
