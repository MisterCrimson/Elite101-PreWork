import time

print('Welcome to start of your chatbot journey!')

name = input('before we get started let me get your name so i we can connect better.  ')

time.sleep(1)
print(f' Hello {name} im called Friday and it is very nice to meet you!')
age = input('my last question for you before we get started is "how old are you?"')

time.sleep(1)
print(f'Wow! I wonder if i will ever be {age}')
time.sleep(1)


print(f'Okay now lets begin {name}, please choose from the following options')
options = ['1.  placeholder A',
           '2.  placeholder B', 
           '3.  placeholder C',
           '4.  exit coversation']
print(options[0])
print(options[1])
print(options[2])
print(options[3])

conversation1 = input('enter the number of your choice here. -->  ') 

if conversation1 == '1' or conversation1 == '1.':
  print('u choose option A')

elif conversation1 == '2' or conversation1 == '2.':
  print('u choose option B')

elif conversation1 == '3' or conversation1 == '3.':
  print('u choose option C')

elif conversation1 == '4' or conversation1 == '4.':
  print('Goodbye and have a great day!')
  time.sleep(1)
  exit()

else:
  print('...Uh oh can you try again  from the start with one of the available numbers?')
