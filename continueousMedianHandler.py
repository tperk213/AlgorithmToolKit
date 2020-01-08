

class ContinuousMedianHandler:

    def __init__(self):
            numbers = []
            self.median = None

    def insert(self, number):
        self.numbers.append(number)
        self.numbers.sort()
        #odd
        if len(numbers)%2 > 0:
            idx = len(numbers)//2
            self.median = numbers[idx]
        else:
            upper_num = self.numbers[len(numbers)//2] 
            lower_num = self.numbers[len(numbers)//2 - 1]
            self.median = (upper_num + lower_num)/2
            
    
    def getMedian(self):
        return self.median