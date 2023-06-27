def DishPrepareOrder(nums) : 
    orderCount = {}
        
    for id in nums : 
        if id not in orderCount.keys() : 
            orderCount[id] = 1 
        else : 
            orderCount[id] += 1 
            
    IDCount = []
    for key in orderCount.keys() : 
        IDCount.append([key, orderCount[key]])
        
    sortedID = sorted(IDCount, key = lambda x: (-x[1], x[0]))
    
    output = []
    for ID in sortedID : 
        output.append(ID[0])
        
    return output
    
nums = eval(input())
print(DishPrepareOrder(nums))