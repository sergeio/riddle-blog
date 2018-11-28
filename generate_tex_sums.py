"""
Basically, this is code to generate the following:

$ \frac{1}{4} $
$ \frac{1}{8} + \frac{1}{8} = \frac{1}{4} $
$ \frac{1}{8} + \frac{1}{16} $
$ \frac{1}{16} + \frac{1}{32} + \frac{1}{32} = \frac{1}{8} $
$ \frac{1}{16} + \frac{1}{64} $
$ \frac{1}{32} + \frac{1}{128} + \frac{1}{128} = \frac{1}{32} + \frac{1}{64} $
$ \frac{1}{64} + \frac{1}{128} + \frac{1}{256} $
$ \frac{1}{128} + \frac{1}{256} + \frac{1}{512} + \frac{1}{512} = \frac{1}{64} $
$ \frac{1}{128} + \frac{1}{1024} $
$ \frac{1}{256} + \frac{1}{2048} + \frac{1}{2048} = \frac{1}{256} + \frac{1}{1024} $
$ \frac{1}{512} + \frac{1}{2048} + \frac{1}{4096} $

Each line is represents f(x), where sum(f(x), from=2, to=infinity) = the amount
of girls in the country according to the riddle this repository is exploring.

In retrospect, I would have saved a bunch of time just typing it out by hand.
"""
from fractions import Fraction


class SumRow:
    """Logic for representing a row of Fraction sums.

    Takes two numerically equivalent arguments: `fractions` and the same
    fractions', reduced form.  In this context, reducing refers to repeatedly
    summing identical fractions in the fraction list:
    [1/4, 1/8, 1/8, 1/9] -> [1/2, 1/9]
    """

    def __init__(self, fractions, reduced):
        self.fractions = fractions
        self.reduced = reduced

    @staticmethod
    def _repr_fraction(fraction):
        return f'\\frac{{{fraction.numerator}}}{{{fraction.denominator}}}'

    @staticmethod
    def _repr_fraction_list(fraction_list):
        return ' + '.join(SumRow._repr_fraction(x) for x in fraction_list)

    def __repr__(self):
        """Format our fraction sums to be consumed by latex

        Examples:
            $ \frac{1}{4} $
            $ \frac{1}{8} + \frac{1}{8} = \frac{1}{4} $
        """
        strings = [SumRow._repr_fraction_list(f)
                   for f in (self.fractions, self.reduced)]
        if self.fractions == self.reduced:
            return '$ ' + strings[0] + ' $'
        return '$ ' + ' = '.join(strings) + ' $'


def generate_ith_element_of_girl_population_sum(n=10):
    partial_sums = [[Fraction(1, 4)]]
    partial_sums_reduced = [[Fraction(1, 4)]]
    i = 0
    while i < n:
        new = [x / 2 for x in partial_sums_reduced[i]]
        new.append(Fraction(1, 2 ** (i + 3)))
        partial_sums.append(new)
        partial_sums_reduced.append(reduce_fraction_sum(new))
        i += 1
    return partial_sums, partial_sums_reduced


def reduce_fraction_sum(fraction_list):
    """If the fraction list has identical fractions, sum them."""
    if len(fraction_list) == 1:
        return fraction_list
    fraction_list = sorted(fraction_list, reverse=True)
    result = []
    for i in range(len(fraction_list)- 1):
        this = fraction_list[i]
        next_ = fraction_list[i + 1]
        if this == next_:
            to_reduce = fraction_list[:i] + [this * 2] + fraction_list[i + 2:]
            return reduce_fraction_sum(to_reduce)
    return fraction_list


def main():
    for sums, reduced in zip(*generate_ith_element_of_girl_population_sum()):
        print(SumRow(sums, reduced))


if __name__ == '__main__':
    main()
