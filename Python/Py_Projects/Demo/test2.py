word = 'Please Spell 好 in English: ' 
answer = input(word)
while answer.upper() != 'GOOD':
      if answer.upper() == 'FUCK':
            print('I am done with this SHIT!')
            break
            print('FUCK OFF')
      answer = input('Wrong,\n%s' % word)
else:
      print('Correct!')