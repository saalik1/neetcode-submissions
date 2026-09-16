class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = []
        operators.append("/")
        operators.append("*")
        operators.append("+")
        operators.append("-")
        stack = []
       
        for k in tokens:
            if k not in operators:
                stack.append(int(k))
    
            else:
                y = stack.pop()
                x = stack.pop()
                
                if k == "+":
                    res = x + y
    
                elif k == "-":
                    res = x - y
                    
                elif k == "*":
                    res = x * y
                    
                elif k == "/": 
                    res = int(x / y)
                stack.append(res)
                
        return stack.pop()