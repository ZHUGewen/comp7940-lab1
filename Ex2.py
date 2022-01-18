# Write a function that prints all factors of the given parameter x
def print_factor(x):
  # your code here
  for i in range(x+1):
      if(not i==0 and x%i==0): print(i)

if __name__ == '__main__':
    print_factor(52633)