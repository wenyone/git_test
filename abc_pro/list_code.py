
class IterTest:
    def __init__(self,step=1):
        self.start = 0
        self.step = step
    
    def __iter__(self):
        return self
        
    def __next__(self):
        self.start = self.start + self.step
        if self.start>10:
            raise StopIteration
        return self.start
        

if __name__=='__main__':
    for i in IterTest():
        print(i)
    