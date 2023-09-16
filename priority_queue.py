class PriorityQueue : 
    def __init__(self) : 
        self.queue = []

    def insert(self, val) :
        self.queue.append(val)

    def isEmpty(self) : 
        return self.queue == []

    def __str__(self) : 
        return str(self.queue)
    
    def delete_max(self) : 
        if not self.isEmpty() : 
            max_val_index = 0 
            for i in range(len(self.queue)) : 
                if self.queue[i] > self.queue[max_val_index] : 
                    max_val_index = i 

            item = self.queue[max_val_index]
            self.queue = self.queue[:max_val_index] + self.queue[max_val_index+1:]
            return item 
        else : 
            return -1 

    def delete_min(self) : 
        if not self.isEmpty() : 
            max_val_index = 0 
            for i in range(len(self.queue)) : 
                if self.queue[i] < self.queue[max_val_index] : 
                    max_val_index = i 

            item = self.queue[max_val_index]
            self.queue = self.queue[:max_val_index] + self.queue[max_val_index+1:]
            return item 
        else : 
            return -1 

if __name__ == '__main__' : 
    q = PriorityQueue()
    q.insert(10)
    q.insert(2)
    q.insert(14)
    q.insert(1)
    q.insert(19)
    print(q)
    # max_queue 
    # print(q.delete_max())
    # print(q.delete_max())
    # print(q.delete_max())
    # print(q.delete_max())
    # print(q.delete_max())
    # print(q.delete_max())
    # min_queue 
    print(q.delete_min())
    print(q.delete_min())
    print(q.delete_min())
    print(q.delete_min())
    print(q.delete_min())
    print(q.delete_min())