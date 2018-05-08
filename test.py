import mobula

@mobula.register_op('FirstOP')
class FirstOP(mobula.operator.CustomOp):
    def __init__(self, par):
        print (type(par))
        self.par = par
        print ('self.par = {}'.format(self.par))
    def forward(self, x, y):
        return x + y
    def backward(self, dy): 
        return [dy, dy]
    def infer_shape(self, in_shape):
        assert in_shape[0] == in_shape[1]
        return in_shape, [in_shape[0]]

if __name__ == '__main__':
    import mxnet as mx
    import numpy as np
    a = mx.nd.array([1,2,3]) 
    b = mx.nd.array([4,5,6])
    c = FirstOP(a, b, dict(a = 3))
    # c = FirstOP(a, b, par = dict(a = 3))
    assert ((a + b).asnumpy() == c.asnumpy()).all()
    print ("Okay")
