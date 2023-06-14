def odd_one(arr) : 
    mapping = [0 for i in range(4)]
    for item in arr : 
        if type(item) == int :
            mapping[0] += 1 
        elif type(item) == float :
            mapping[1] += 1 
        elif type(item) == str :
            mapping[2] += 1 
        elif type(item) == bool :
            mapping[3] += 1 
            
    if mapping[0] == 1 : 
        return 'int' 
    if mapping[1] == 1 : 
        return 'float' 
    if mapping[2] == 1 : 
        return 'str' 
    if mapping[3] == 1 : 
        return 'bool' 
print(odd_one(eval(input().strip())))