# Find the all factors of x using a loop and the operator % 
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
if __name__ == '__main__':
    x = 52633
    for i in range(x+1):
        # your code here
        if( not i==0 and x%i==0): print(i)