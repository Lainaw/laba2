import random

errorCount = 0

def gen_task():
  a = random.randrange(1, 100)
  b = random.randrange(1, 100)
  
  return { "prompt": str(a) + ' + ' + str(b) + " = ", "answer": a + b }

while(True):
  if errorCount < 3:
      task = gen_task()
      answer = input(task['prompt'])
    
      if(int(answer) == task['answer']):
        print('Правильно!')
        pass
      else:
        print('Ответ неверный.')
        errorCount += 1
  else:
    print('Вы набрали 3 ошибки')
    break


