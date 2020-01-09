class Node:

    def __init__(self, val, nextNode=None):
        """
        initialize your data structure here.
        """
        self.val = val #val是一個值
        self.temp_min = val #最小值=val
        self.next = nextNode #下一個值
        
class MinStack:
    
    def __init__(self):
        
        self.topNode = None #初始值的第一個值不存在

    def push(self, x: int) -> None:
        
        if self.topNode is None:
            self.topNode = Node(x, None) #如果沒有第一個值的話，加進一個Node
        else:
            temp = self.topNode.temp_min
            self.topNode = Node(x, self.topNode)
            if temp < self.topNode.val:
                self.topNode.temp_min = temp 
            
    def pop(self) -> None:
        
        self.topNode = self.topNode.next
        

    def top(self) -> int:
        
        return self.topNode.val
        

    def getMin(self) -> int:
        
        return self.topNode.temp_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
