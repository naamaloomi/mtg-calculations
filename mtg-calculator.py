#!/usr/bin/env/python
# coding=utf-8
from __future__ import unicode_literals

from scipy.stats import hypergeom

deck_size = 60
nr_of_lands = 18
nr_of_target_cards = 8

# Chance to draw 0 out of 4 cards in a 60 card deck when drawing 7 cards.
p0 = hypergeom.cdf(0, 60, 4, 7)

# Chance to draw at least 1 land in opening hand.
p1 = 1 - hypergeom.cdf(0, deck_size, nr_of_lands, 7)

# Chance to draw at least 3 lands by turn 3.
p2 = 1 - \
     hypergeom.cdf(0, deck_size, nr_of_lands, 9) - \
     hypergeom.cdf(1, deck_size, nr_of_lands, 9) - \
     hypergeom.cdf(2, deck_size, nr_of_lands, 9)

# Chance to draw Stoneforge Mystic or Vampiric Tutor in opening hand or
# draw Stoneforge Mystic on the first draw step.
p3 = 1 - hypergeom.cdf(0, deck_size, nr_of_target_cards, 7)
p4 = 1 - hypergeom.cdf(0, 53, 4, 1)
p5 = p3 + p4

# Chance to draw at least 2 lands by first draw.
p6 = 1 - \
     hypergeom.cdf(0, deck_size, nr_of_lands, 8) - \
     hypergeom.cdf(1, deck_size, nr_of_lands, 8)

# Chance to draw  at least 1 of 6 counterspells in a TL deck by turn 3.
p7 = 1 - hypergeom.cdf(0, 50, 6, 10)

print p1
print p2
print p3
print p4
print p5
print p6
print p7
