# Rule_Based_Inference_Python

The idea is the following: given the path to some input python file, return a list of function-info of functions in the file. 
Each function-info will be a list of function name and a sublist with the arguments of the function and their inferred types. 
The inferred types would be based on some rules that look at the operations performed on these arguments in the function body. 
If you could not infer the type, return the unknown type. This inference cannot be done by running the code. 
You can use any python library you deem useful. Let me give you an example. If a file ‘mycode.py’ contains these two functions:

def f1 (x, y):
  z = x[:y]
  return z

def f2 (x, y):
  z = x[y].unique().tolist()
  return z

def f3 (x, y):
  z = x[y]
  return z

your code should return when you call it: 

your_code(‘my_code.py’)
[[f1, [[x, list], [y, int]]], [f2, [[x, pd.DataFrame], [y, str]]], [f3, [[x, unkown], [y, unkown]]]]


Instructions to run the code:-

python djtype_inference.py sample_demo.py.txt

