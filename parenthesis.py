def paren(equation):
    equation = equation.replace(' ', '')
    for i in range(len(equation)):
        if equation[i] == "(":
            for j in range(i + 1, len(equation)):
                if equation[j] == ')':
                    print(equation[i + 1:j])
                    return equation[i + 1:j]
                
                elif equation[j] == '(':
                    for x in range(len(equation) - 1, -1, -1):
                        if equation[x] == ')':
                            return equation[i + 1:x]
                
                else:
                    continue
                
                
def paren2(equation):
    equation = equation.replace(' ', '')
    open_parentheses_index_ = -1
    open_parentheses_count_ = 0
    close_parentheses_count_ = 0
    for i in range(len(equation)):
        if equation[i] == "(":
            if open_parentheses_index_ == -1:
                open_parentheses_index_ = i 
            open_parentheses_count_ += 1
        elif equation[i] == ")":
            close_parentheses_count_ += 1
            if open_parentheses_count_ == close_parentheses_count_:
                return equation[open_parentheses_index_+1 : i] 
            



a = '(1+(1+1))'
b = '(1+1) + (2+2)'
c = '(1+(1+1)) + (1+1)'

print(paren2(a))
print(paren2(b))
print('res: ', paren2(c))