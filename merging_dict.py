my_list = [{'old_price': None, 'price': '5,75'}, {'old_price': None, 'price': '5,90'}, {'old_price': None, 'price': '5,95'}, {'old_price': None, 'price': '10,15'}, {'old_price': None, 'price': '19,90'}, {'old_price': None, 'price': '34,90'}, {'old_price': None, 'price': '46,50'}, {'old_price': None, 'price': '24,90'}]
result = {}
for each_dict in my_list:
    for k in each_dict:
        if (k in result): 
            result[k].append(each_dict[k])
        else:
            result[k] = [each_dict[k]]

print(result)