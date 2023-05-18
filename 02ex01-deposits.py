#!/usr/bin/env python3

"""Calculate deposit percent yield based on time period.

Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...

Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.

Let's implement this.

A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.

Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""


# DONE: add lines to calculate yields for some common periods
#       of time (e.g. 1 month, 1 year, 5 years, 10 years)
# DONE: change the script to output the 1-year percent yield
#       as well
# TODO: (extra) Output only percents if the initial SUM is
#       not known at the moment the script is run


USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()

def growth_calc(per, fixed_period, set_period):
    return (1 + per) ** (set_period / fixed_period)

def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growths = [
    growth_calc(per, fixed_period, set_period),
    growth_calc(per, fixed_period, 1/12),
    growth_calc(per, fixed_period, 1),
    growth_calc(per, fixed_period, 5),
    growth_calc(per, fixed_period, 10)]
    return [initial_sum * growths[0], growths[1:]]


def main(args):
    """Gets called when run as a script."""
    if len(args) != 4 + 1:
        exit(USAGE.format(script=args[0]))

    args = args[1:]
    initial_sum, percent, fixed_period, set_period = map(float, args)

    # same as
    # initial_sum = float(args[0])
    # percent = float(args[1])
    # ...

    res = deposit(initial_sum, percent, fixed_period, set_period)
    print('The total sum for', set_period, 'years is', res[0], end='')
    res = deposit(initial_sum, percent, fixed_period, 1)
    print(' which is', res[0], 'for one year')
    print('Growths for 1m, 1y, 5y and 10y are', res[1])
    
if __name__ == '__main__':
    import sys

    main(sys.argv)
