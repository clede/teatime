# Tea timer app
# Jonathan Clede 2015

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

choice = ' '

while choice not in teatimes:
    choice = raw_input('ENTER A KIND OF TEA: ')

print choice + ' tea should be steeped for ' + str(teatimes[choice]) + ' minutes.'

seconds = teatimes[choice] * 60

for sec in range(seconds)[::-1]:
    print str(sec) + ' seconds remaining...'
    time.sleep(1)

print 'TEA TIME!'
