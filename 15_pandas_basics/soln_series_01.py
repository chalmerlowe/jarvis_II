# coding: utf-8
from pandas import Series
restaurant_ratings = Series(range(0, 6))
restaurant_ratings.name = 'ratings'
restaurant_ratings.index = ['mcD', "Wendy's", "BK", 'KFC', "Popeye's", 'Taps and Apps']
