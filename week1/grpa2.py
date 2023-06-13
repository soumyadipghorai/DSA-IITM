def isPrime(num) : 
    for i in range(2, int(pow(num, 0.5))+1) : 
        if num%i == 0 :
            return False 
    return True 
    
    
def Goldbach(num) : 
    output = []
    for i in range(2, num//2 + 1) : 
        if isPrime(i) : 
            if isPrime(num - i) : 
                output.append((i, num - i))
                
    return output
n=int(input())
print(sorted(Goldbach(n)))