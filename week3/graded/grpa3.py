def reverse(root) :
    itr = root 
    prev = None 
    
    while itr : 
        nextNode = itr.next 
        itr.next = prev 
        prev = itr 
        itr = nextNode 
        
    root = prev 
    return root 