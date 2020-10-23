#Vectors naturally have dimensions N x 1
import random;
class vec:
    #Construct vector with n rows
    def __init__(self,n):
        self.rows = n;
        self.content = [];
        self.initialise()
    #Populate the primative data structure with 0, 
    def initialise(self):
        for i in range(0, self.rows):
            self.content.append(0)
    #Scale each element/row in the vector by a fixed constant x
    def scale(self, x):
        for i in range(0,self.rows):
            self.content[i] *= x;
    #Perform the scalar / dot product with another matrix m.
    def dot(self, m):
        #Rows must be equal.
        if self.rows != m.rows:
            print("Error, rows must be equal")
            return 
        buffer = 0;
        for i in range(0, self.rows):
            buffer += self.content[i] * m.content[i]
        return buffer;
    
    def index(self, x):
        if x > len(self.content):
            print("Error, index out of range")
            return
        else:
            return self.content[x]
    def set(self, x, val):
        if x > len(self.content):
            print("Error, index out of range")
            return
        self.content[x] = val;
    
    def randomise(self, start = 0, end = 1, float_ = True):
        for i in range(0, len(self.content)):
            if float_:
                self.content[i] = random.uniform(start, end)
            else:
                self.content[i] = random.randint(start, end)
            
 

        

        

    
    

    

