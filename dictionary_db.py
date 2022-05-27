def Program():
    Storage = {}
    while True:
        print('1 - Query parts\n2 - Add part\n3 - Delete part\n4 - Exit\n')
        choice = int(input())
        if choice == 1:
            while True:
                print(
                    '1 - Consult All Parts\n2 - Consult Parts by Code\n3 - Consult Parts by Manufacturer\n4 - Return')
                choice2 = int(input())
                if choice2 == 1:
                    for items in Storage.keys():
                        print(f'Code: {items} \n{Storage[items]}')
                elif choice2 == 2:
                    search = input('Enter search: ')
                    print(Storage[search])
                elif choice2 == 3:
                    search = str(input('Enter the search: '))
                    print(Storage[search])
                elif choice2 == 4:
                    break
        elif choice == 2:
            Storage[input('Code: ')] = {'Name': input('Enter item name: '), 'brand': input('Enter item brand: '), 'value(R$) ': input('Enter the value of the item: ')}
        elif choice == 3:
            Storage.remove[input('Choose a part to remove: ')]
        elif choice == 4:
            break
        
Program()