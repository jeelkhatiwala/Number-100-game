from random import randint

def my_custom_random_eve():
  exclude=[1,3,5,7,9]
  randInt = randint(1,9)
  return my_custom_random_eve() if randInt in exclude else randInt 
print(my_custom_random_eve())
