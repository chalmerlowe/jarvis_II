# TITLE: asc_desc >> gen_asc_desc.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION: This script generates the data file associated with the
#              following puzzle.

# You are given the file: asc_desc.csv. It contains multiple lines,
# each of which contains a word, an integer and a float.
# 

# Your job is to sort each of the lines using a two-tiered approach:
# sort lines based on the values of the floats in DESCENDING numerical order
#     and sort the lines based on the words in ASCENDING alphabetical order

# With the lines properly sorted, find the 500th line
#     and add the integer value to the float value and submit that 
#     as your answer.

# For example, if given the following values in the csv and asked
#     to sum the values on the 5th line...

# conductions,2,300.001
# fitchews,5,500.002
# mulches,8,700.003
# conductions,3,500.001 
# fitchews,1,600.002
# mulches,5,600.003
# conductions,6,400.001
# mulches,7,500.003

# once sorted, will result in the following:

# conductions,3,500.001 
# conductions,6,400.001
# conductions,2,300.001
# fitchews,1,600.002
# fitchews,5,500.002 <<< fifth line >>> 500.002 + 5 = 505.002
# mulches,8,700.003
# mulches,5,600.003
# mulches,7,500.003

# Submit as your answer: 505.002

# ==============================================================
# Generation code:

from random import choice, randint, random

words = ['abasement', 'accompaniment', 'adjoined', 'agers', 'algerine',
         'ambivalence', 'angelica', 'antiquing', 'aptness', 'arthropod',
         'athletics', 'avidities', 'bailouts', 'barre', 'beck', 'belfry',
         'betide', 'biome', 'blinding', 'boletus', 'bourgeois', 'brickbat',
         'budder', 'busheler', 'calcite', 'canter', 'carpals',
         'cautiousness', 'chalked', 'chervils', 'chowing', 'clanging',
         'clumpier', 'cogitates', 'commercialize', 'conductions',
         'contention', 'cordlike', 'counterfeits', 'crayons', 'crumblier',
         'curtailments', 'dame', 'debris', 'defused', 'deodara', 'dethroned',
         'differ', 'disbuds', 'disregarded', 'doggier', 'dowsing', 'dryness',
         'earful', 'eighths', 'emergent', 'engagements', 'enwomb',
         'espanoles', 'ewers', 'exposals', 'faker', 'feathered', 'ficklest',
         'fitchews', 'flittered', 'fomenters', 'fornical', 'frilling',
         'furnaced', 'gangrening', 'generousness', 'girting', 'goatfish',
         'granddad', 'grosses', 'guttler', 'hamstrings', 'haughty', 'helium',
         'highjack', 'homeliness', 'housecleaning', 'hygeists', 'imaginable',
         'imprecision', 'indecorously', 'infrequently', 'instigator',
         'intolerably', 'isatinic', 'jefes', 'juggler', 'kenos', 'kneads',
         'ladybugs', 'lateraling', 'legmen', 'lightproof', 'livestocks',
         'lores', 'lychees', 'malfeasance', 'marina', 'maybe', 'mensches',
         'midline', 'mintiest', 'misplacing', 'moistful', 'morello',
         'mulches', 'myomas', 'nectaries', 'nimmed', 'nonskiers', 'nylons',
         'off', 'opium', 'ostriches', 'outloves', 'overamplifies',
         'overplaying', 'ozonizing', 'panzers', 'passengers', 'peddles',
         'perfunctory', 'philatelist', 'pillowcases', 'planche',
         'plutonium', 'poplins', 'practises', 'premenopausal', 'primmer',
         'propane', 'puckered', 'puttering', 'quinina', 'rammer',
         'reached', 'rechanneled', 'redocks', 'regales', 'relaunches',
         'repartee', 'resets', 'retirer', 'rhonchus', 'roarings',
         'rowdiest', 'saddling', 'sanserif', 'scanty', 'screed', 'seeding',
         'seriating', 'shebeans', 'showgirls', 'silverware', 'skits',
         'sludgy', 'snobby', 'soma', 'sparker', 'splining', 'squirting',
         'stelar', 'story', 'sturgeon', 'succeed', 'superlain', 'sweep',
         'tabourer', 'targe', 'televiews', 'thallic', 'thudding',
         'titivates', 'tore', 'transcends', 'trilobed', 'tubbers',
         'twirling', 'unchary', 'unfit', 'unneighborly', 'untraced',
         'uraniums', 'vapourers', 'verstes', 'visibly', 'waftage',
         'waterers', 'whams', 'wikiups', 'womby', 'xanthoma', 'zareebas']

def _float(increment):
    '''random float generator
    return a float between 100 and 200
    '''
    
    return round((random() + increment) * 100, 3)

with open('asc_desc.csv', 'w') as fout:
    for line in range(1000):
        word = choice(words[:])
        integer = str(randint(1, 10))
        flt = str(_float(1))
        output = ','.join([word, integer, flt]) + '\n'
        fout.write(output)