from random import randint

def my_custom_random_odd():
  exclude=[2,4,6,8]
  randInt = randint(1,9)
  return my_custom_random_odd() if randInt in exclude else randInt 
print(my_custom_random_odd())
