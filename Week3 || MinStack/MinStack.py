class Node:

    def __init__(self, val, nextNode=None):
        """
        initialize your data structure here.
        """
        self.val = val #val是一個值
        self.temp_min = val #暫時最小值
        self.next = nextNode #下一個值
        
        class MinStack:
    
    def __init__(self):
        
        self.topNode = None #容器中沒有數值的存在

    def push(self, x: int) -> None:
        
        if self.topNode is None:
            self.topNode = Node(x, None) #如果沒有第一個值的話，加進一個Node
        else:
            temp = self.topNode.temp_min  #最上面的最小值成為temp
            self.topNode = Node(x, self.topNode) #加進一個Node成為最上面的數值
            if temp < self.topNode.val:
                self.topNode.temp_min = temp    #如果加進來的數值沒有比原來的最小值小，那麼最小值依舊是temp

            
    def pop(self) -> None:
        
        if top.Node is None:
            return None
        data = self.topNode
        self.topNode = self.topNode.next
        
        return data

    def top(self) -> int:
        
        return self.topNode.val
        

    def getMin(self) -> int:
        
        return self.topNode.temp_min
