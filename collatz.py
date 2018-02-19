def collatz(number):
  if number % 2 == 0:
    mod = number//2
    print(mod)
    return mod
  else:
    mod = (3*number + 1)
    print(mod)
    return(mod)
    
num = int(input("Input Starting Number: "))
while num != 1:
  num = collatz(num)
