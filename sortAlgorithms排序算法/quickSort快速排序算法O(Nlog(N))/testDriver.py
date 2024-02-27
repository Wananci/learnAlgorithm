import random

class testDriver():
    def __init__(self, maxSize, maxValue, onlyPositiveNum=False):
        self.maxSize = maxSize
        self.maxValue = maxValue
        size = int(self.maxSize * random.random())
        if not onlyPositiveNum:
            self.generatedArray = [int((self.maxValue + 1) * random.random()) - 
                               int(self.maxValue * random.random()) for _ in range(size)]
        else:
            self.generatedArray = [abs(int((self.maxValue + 1) * random.random()) - 
                               int(self.maxValue * random.random())) for _ in range(size)]
        
    def __len__(self):
        return len(self.generatedArray)
    
    def naiveSort(self):
        return sorted(self.generatedArray)
    
    def getArray(self):
        return self.generatedArray
    



