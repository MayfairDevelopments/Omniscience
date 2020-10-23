#~ Basic 1 hidden layer Neural Network created by Mayfair#2022 
import Vector as vec;
import math;
class NeuralNetwork():
    def __init__(self, input_size, hidden_size, output_size):
        #For this iteration assume there is only 1 hidden layer
        self.input_size = input_size;
        self.hidden_size = hidden_size;
        self.output_size = output_size;
        #self.inputs = self.CreateInputs(input_size);
        #Weights:
        self.input_to_hidden = self.InstantiateWeights(self.input_size * self.hidden_size)
    def CreateInputs(self):
        pass;
    def TanH(self, input): #Returns the hyberbolic tangent function
        return math.tanh(input)
    def Sigmoid(self, input): #Returns the sigmoid function 1/(1+e^(-x))
        return(1/(1+math.exp(-1 * input)))
    def InstantiateWeights(self, size, randomise = True):
        weight_vec = vec.vec(size);
        if not randomise:
            return
        weight_vec.randomise()
        return weight_vec;
    def FeedForward(self, inp, expected, method = "Sigmoid"):
        if method == "Sigmoid":
            return self.Error(self.Sigmoid(inp.dot(self.input_to_hidden)), expected)
        elif method == "TanH":
            return self.Error(self.TanH(inp.dot(self.input_to_hidden)), expected)
        
    def Error(self, actual,expected):
        #Assume Binary Output
        return math.pow((actual-expected),2)

        
#>>[Usage]
# a = NeuralNetwork(2,1,1);
# b = vec.vec(2)
# b.set(0,2);
# b.set(1,3);
# print(a.FeedForward(b,1))




        

    
        
