# TODO: Create ORM classes.
#

from sensor import Energy

energy = Energy()
table = []
with open('sample.dat') as sample:
    for row in sample:
        table.append(energy.parse(row))
