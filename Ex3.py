# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

# your code here
if __name__ == '__main__':  
    for i in l:
        fac = ""
        for j in range(i+1):
            if(not j==0 and i%j==0):
                fac+=str(j)+" "
        print(str(i)+"'s factor: "+fac+"\n")
