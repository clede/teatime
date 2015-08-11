# Tea timer app
# Jonathan Clede 2015
# Designed for Python 2

import time

teatimes = {'White': 2,
            'Green': 3,
            'Black': 4,
            'Darjeeling': 3,
            'Oolong': 4,
            'Herbal': 6,
            'Pu-Erh': 4 }

print ' '
print 'TEA TYPES:'

for tea in teatimes:
    print '  ',
    print tea

print ' '

entry = ' '

while entry not in teatimes:
    entry = raw_input('ENTER A KIND OF TEA: ')

print entry + ' tea should be steeped for ' + str(teatimes[entry]) + ' minutes.'
seconds = teatimes[entry] * 60

while entry != '':
    entry = raw_input('PRESS ENTER TO START ')

for sec in range(seconds)[::-1]:
    print str(sec) + ' seconds remaining...'
    time.sleep(1)

print 'TEA TIME!'
