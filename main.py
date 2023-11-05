import time

import list_of_brands as str
import Shoes_list as shoes

counter = 0
def display_brands():
  #used to print out list of clothing brands listed in ./list_of_brands.py
  print("Here are the brands:")
  for brand in str.clothing_brands:
    print(brand)
    time.sleep(0.5)
  time.sleep(1)

#defines product name & prices for it
def inventory_display(brands):
  print("***Our Brand Collection***\n-------------------------\n\n")
  for brand in brands:
    print(f"Brand:{brand[0]} \nPrice:{brand[1]} \nSize:{brand[2]}")
    print("---------------------------------------------\n")

print('Welcome to start of your chatbot journey!')

name = input('before we get started let me get your name so i we can connect better.  ')

time.sleep(1)
print(f' Hello {name} im called Friday and it is very nice to meet you!')
age = int(input('my last question for you before we get started is "how old are you?"'))

time.sleep(1)
if age <= 18:
  time.sleep(0.5)
  print('make sure to work with an adult.')

else:
  time.sleep(0.5)
  print(f'Wow! I wonder if i will ever be {age}')
time.sleep(1)
  
#gives users options between leaving the conversation or continuing to exchange/return an item based on numerical choices
print(f'Okay now lets begin {name}, What are you here for?')
options = ['1.  Return product',
           '2.  Exchange product', 
           '3.  exit coversation']
print(options[0])
print(options[1])
print(options[2])

conversation1 = input('enter the number of your choice here. -->  ') 

if conversation1 == '1' or conversation1 == '1.':
  print('u choose to return an item')

elif conversation1 == '2' or conversation1 == '2.':
  print('u choose to exchange an item')

elif conversation1 == '3' or conversation1 == '3.':
  print('Goodbye and have a great day!')
  time.sleep(1)
  exit()

else:
  print('...Uh oh can you try again  from the start with one of the available numbers?')

#used to specify what clothing item is being dealt with
clothingid = input('please list the type of clothing you want to return here. -->  ')

time.sleep(1)
if clothingid == 'shirt' or clothingid == 'Shirt' :
  ShirtBrands = display_brands()
  print(ShirtBrands)

elif clothingid =='pants' or clothingid == 'Pants' :
  PantsBrands =  display_brands()
  print(PantsBrands)
  
elif clothingid == 'shoes' or clothingid == 'Shoes' :
  ShoeBrands = display_brands()
  print(ShoeBrands)

elif clothingid == 'jacket' or clothingid == 'Jacket' :
  JacketBrands = display_brands()
  print(JacketBrands)

else:
  print('...Uh oh can you try again and pick from a shirt,pants, shoes, or a jacket?')

while counter <= 0:
    
  #used to get the brand of the item from a seperate list
  brandid = input(f"Now may you please enter the brand of the {clothingid} here -->  ")
  time.sleep(0.5)
  
  #used to get the entire product from a seperate list
  if brandid == 'adidas'.lower:
    print(shoes.Adidas_brands[0])
    print(shoes.Adidas_brands[1])
    print(shoes.Adidas_brands[2])
  
  elif brandid == 'nike'.lower:
    print(shoes.Nike_brands[0])
    print(shoes.Nike_brands[1])
    print(shoes.Nike_brands[1])
  
  elif brandid == 'under armour'.lower:
    print(shoes.Under_Armour_brands[0])
    print(shoes.Under_Armour_brands[1])
    print(shoes.Under_Armour_brands[2])
  
  elif brandid == 'vans'.lower:
    print(shoes.Vans_brands[0])
    print(shoes.Vans_brands[1])
    print(shoes.Vans_brands[2])
  
  #used to get cost of the item
  priceid = int(input(f' please enter the price of your {clothingid} here --> $'))
  time.sleep(0.5)
  
  print('we are looking for products that match your current selections' 
  f'{clothingid},from {brandid}, that cost {priceid}.')
  time.sleep(1)
  
  #reintroduce coversation1 and seperate between return or exchange items
  if conversation1 == '1' or conversation1 == '1.':
    print(' we have found related items and are prepared to reimburse you when you come in')
    time.sleep(1)
    exit()
  else:
    print('now lets get into what you would like to exchange your item for')
    time.sleep(.5)
    
  #will be used to compare values of users item and what they want to exchange it for
  clothingid2 = input('please list the clothing product you want to exchange for here. -->  ')
  
  time.sleep(1)
  if clothingid2 == 'shirt' or clothingid2 == 'Shirt' :
    ShirtBrands = display_brands()
    print(ShirtBrands)
  
  elif clothingid2 =='pants' or clothingid2 == 'Pants' :
    PantsBrands =  display_brands()
    print(PantsBrands)
    
  elif clothingid2 == 'shoes' or clothingid2 == 'Shoes' :
    ShoeBrands = display_brands()
    print(ShoeBrands)
  
  elif clothingid2 == 'jacket' or clothingid2 == 'Jacket' :
    JacketBrands = display_brands()
    print(JacketBrands)
  
  brandid2 = input(f"Now may you please enter the brand of the {clothingid} here -->  ")
  time.sleep(0.5)
  
  if brandid2 == 'adidas'.lower:
    print(shoes.Adidas_brands[0])
    print(shoes.Adidas_brands[1])
    print(shoes.Adidas_brands[2])

  elif brandid2 == 'nike'.lower:
    print(shoes.Nike_brands[0])
    print(shoes.Nike_brands[1])
    print(shoes.Nike_brands[1])

  elif brandid2 == 'under armour'.lower:
    print(shoes.Under_Armour_brands[0])
    print(shoes.Under_Armour_brands[1])
    print(shoes.Under_Armour_brands[2])

  elif brandid2 == 'vans'.lower:
    print(shoes.Vans_brands[0])
    print(shoes.Vans_brands[1])
    print(shoes.Vans_brands[2])
    
  #used to get cost of the item
  priceid2 = int(input(f' please enter the price of your {clothingid} here --> $'))
  time.sleep(0.5)
  
  print('we are looking for products that match your current selections' 
  f'{clothingid2},from {brandid2}, that cost {priceid2}.')
  time.sleep(1)
  
  if priceid == priceid2:
    print(' we are prepared to reimburse you as soon as you come in')
    counter += 2
  
  #if the item being return is worth less than what they want to exchange it for 
  #the user will be asked to try again
  elif priceid <= priceid2:
    print('it seems like you are not able to afford the item you want to exchange for.')
    time.sleep(0.5)
    print('please try again and select a different item.')
  
  else:
    print(' we are prepared to reimburse you with your item and change when you come in')
    counter += 2

exit()