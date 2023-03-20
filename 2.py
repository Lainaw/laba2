str = ''

while(True):
  word = input('Введите слово: ')
  
  if(word == 'stop'):
    break
  
  str += word + ' '

print(str)
