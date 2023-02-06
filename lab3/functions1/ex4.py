def is_prime(x):
    for i in range(2,x-1,1):
        if(x%i==0):
            return False;
    return True;


def filter_prime(*arg):
    a=[]
    for i in arg:
        if(is_prime(i)):
            a.append(i)
    return a

#print(filter_prime(1,5,8,7,9,11))