def bubble(collection):
    for endnum in range(len(collection)-1, 0, -1): 
        print(collection)
        for i in range(endnum):
            if str(collection[i]) > str(collection[i+1]):
                collection[i], collection[i+1] = collection[i+1], collection[i]
                
                
bubble([19, 5, 'cat', 2, 'rabbit', 32, 'mice', 'dog', 7])