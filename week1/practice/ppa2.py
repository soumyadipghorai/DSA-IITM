class Triangle : 
    def __init__(self, a, b, c) : 
        self.a = a 
        self.b = b 
        self.c = c
    
    def Is_valid(self) : 
        if self.a + self.b > self.c and self.a+self.c > self.b and self.b+self.c > self.a : 
            return 'Valid'
        return 'Invalid'
        
    def Side_Classification(self) : 
        if self.Is_valid() == 'Valid' :
            if (self.a == self.b) and (self.b == self.c) : 
                return 'Equilateral'
            
            if ((self.a == self.b) and (self.b != self.c)) or ((self.a == self.c) and (self.c != self.b)) or ((self.b == self.c) and (self.c != self.a)) : 
                return 'Isosceles'
                
            if (self.a != self.b) and (self.b != self.c) and (self.a != self.c) : 
                return 'Scalene'
        
        return self.Is_valid()
            
    def Angle_Classification(self) : 
        if self.Is_valid() == 'Valid' : 
            arr = [self.a, self.b, self.c]
            arr.sort()
            min_side, mid_side, max_side = arr[0], arr[1], arr[2]
            
            if pow(min_side, 2) + pow(mid_side, 2) > pow(max_side, 2) : 
                return 'Acute'
            if pow(min_side, 2) + pow(mid_side, 2) == pow(max_side, 2) : 
                return 'Right'
            if pow(min_side, 2) + pow(mid_side, 2) < pow(max_side, 2) : 
                return 'Obtuse'
                
        return self.Is_valid()
        
    def Area(self) : 
        if self.Is_valid() == 'Valid' : 
            s = (self.a + self.b + self.c)/2 
            return pow(s*(s-a)*(s-b)*(s-c), 0.5)
            
        return self.Is_valid()

a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())