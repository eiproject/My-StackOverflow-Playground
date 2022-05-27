import re

def tokenize_for_bleu_eval(code):
    tokens_list = []
    codes = code.split(' ')
    for i in range(len(codes)):
        code = codes[i]
        code = re.sub(r'([^A-Za-z0-9_])', r' \1 ', code)
        code = re.sub(r'([a-z])([A-Z])', r'\1 \2', code)
        code = re.sub(r'\s+', ' ', code)
        code = code.replace('"', '`')
        code = code.replace('\'', '`')
        tokens = [t for t in code.split(' ') if t]
        tokens_list.append(tokens)
        if i != len(codes) -1:
            tokens_list.append([' '])
    
    flatten_list = []

    for tokens in tokens_list:
        for token in tokens:
            flatten_list.append(token)

    return flatten_list

def merge_tokens(flatten_list):
    code = ''.join(flatten_list)
    code = code.replace('`', "'")

    return code

test1 ="struct.unpack('h', pS[0:2])"
test2 = "items = [item for item in container if item.attribute == value]"
tokenize = tokenize_for_bleu_eval(test1)
print(tokenize)
merge_result = merge_tokens(tokenize)
print(merge_result) # struct.unpack('h', pS[0:2])

tokenize = tokenize_for_bleu_eval(test2)
print(tokenize)
merge_result = merge_tokens(tokenize)
print(merge_result)