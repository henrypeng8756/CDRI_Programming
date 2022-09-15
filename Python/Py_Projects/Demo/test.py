x = 'Please Spell 快樂 in English:'
answer = input(x)
while answer.upper() != "HAPPY":
      answer = input('Wrong! Please try again!\n%s' % x)
else:
      print('Correct!')
