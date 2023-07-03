def EvaluateExpression(arr) : 
    op, num = [], []
    exp = ['+', '-', '*', '/', '**']
    arr = arr.split(' ')
    for val in arr : 
        if val in exp : 
            a, b = num[-2], num[-1]
            num = num[:-2]
            if val == '+' : 
                num.append(a+b)
            elif val == '-' : 
                num.append(a-b)
            elif val == '*' : 
                num.append(a*b)
            elif val == '/' : 
                num.append(a/b)
            elif val == '**' : 
                num.append(a**b)
        else : 
            num.append(int(val))
            
    return float(num[0])
    
print(float(EvaluateExpression(input())))