for link in ['a', 'b', 'c']:
    src = link
    print(src)
    with open('links.txt', 'a') as file:
        file.write(str(src + '\n'))