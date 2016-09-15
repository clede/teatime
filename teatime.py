# Tea timer app
# Jonathan Clede 2016
# Designed for Python 3

import time

# Setup and display list of teas.

teatimes = {'White': 2,
            'Green': 3,
            'Black': 4,
            'Darjeeling': 3,
            'Oolong': 4,
            'Herbal': 6,
            'Pu-Erh': 4 }
print(' ')
print('TEA TYPES:')
for tea in teatimes:
    print(tea)
print(' ')

# Set up the timer and start it.

entry = ' '
while entry not in teatimes:
    entry = input('ENTER A KIND OF TEA: ')

print(entry + ' tea should be steeped for ' + str(teatimes[entry]) + 
      ' minutes.')
seconds = teatimes[entry] * 60

while entry != '':
    entry = input('PRESS ENTER TO START ')

for sec in range(seconds)[::-1]:
    print(str(sec) + ' seconds remaining...')
    time.sleep(1)

print('TEA TIME!')
