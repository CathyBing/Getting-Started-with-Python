number = 23
running = True
while running:
    guess = int(raw_input('''Do you know what number I\'m holding? Try and guess!
    Enter your answer here: '''))
    if guess == number:
        print 'Congratualations! You\'ve guessed it!'
        print '(But you\'re not winning any prize!)'
        running = False
    elif guess < number:
        print 'Nope, it\'s a little higher than that.'
    else:
        print 'Nope, it\'s a little lower than that.'
else:
    print 'The guessing is over.'
print 'Done.'