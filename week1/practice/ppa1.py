def isPrime(n) : 
    for i in range(2, int(pow(n, 0.5))+1) : 
        if n%i == 0 : 
            return False 
    return True 
    
def Twin_Primes(n, m) : 
    lastPrime, output = -1, []
    for i in range(n, m+1) : 
        if isPrime(i) : 
            if lastPrime != -1 and abs(lastPrime - i) == 2 : 
                output.append((lastPrime, i))
            lastPrime = i 
    return output
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))