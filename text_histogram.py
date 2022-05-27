def charHistogram(filename: str):
    filename = filename.lower()
    g = list(filename)
    f = []
    for x in g:
        f.append([x, (g.count(x)*'+')])
    return f

def printlines(lines):
    for line in lines:
        print(line)
    
printlines(charHistogram(
    filename='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
            Praesent ac sem lorem. Integer elementum \
            ultrices purus, sit amet malesuada tortor \
            pharetra ac. Vestibulum sapien nibh, dapibus \
            nec bibendum sit amet, sodales id justo.'))