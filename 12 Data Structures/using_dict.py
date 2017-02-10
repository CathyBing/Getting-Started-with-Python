ab = {'Swaroop' : 'swaroop@swaroopsh.com',
      'Larry' : 'larry@wall.org',
      'Matsumoto' : 'matz@ruby-lang.org',
      'Spammer' : 'spammer@hotmail.com'
}

print "Swaroop's address is", ab['Swaroop']

del ab['Spammer']
print '\nThere are %d contacts in the address-book\n' % len(ab)

for name, address in ab.items():
      print('Contact {0} at {1}'.format(name, address))

ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
      print "Guido's address is", ab['Guido']
