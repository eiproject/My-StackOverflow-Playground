#Option 2 Binary to Decimal function
def Binary_to_Decimal(binary_number):
    while binary_number == '0':
        print("Please enter a number greater than 0.")
        binary_number = input("Input a binary number: ")
    decimal_input = 0
    for digit in str(binary_number):
        decimal_input = decimal_input*2 + int(digit)
    print("The decimal value of the number is", decimal_input)

User_Choice = str(input('What would you like to do [1,2,3,4]? '))

play_again = True

while play_again == True:
    if User_Choice == "2":
        print('In command 2 – convert to decimal')
        while True:
            # Only use one input on a loop
            binary_number = input("Input a binary number: ")
            
            # It must be an integer
            try:
                input_val = int(binary_number)
            except ValueError:
                print("Input was not a binary number")
                continue
            
            # It must only contain 1's or 0's - it can contain any combination of 0s and 1s 
            # but it cannot contain any number except 0s or 1s
            if len(binary_number.replace('0', '').replace('1', '')) > 0:
                print("Please make sure your number contains digits 0-1 only.")
                continue
            
            # It cannot be 0 (i.e. it must be > 0)
            if not int(binary_number) > 0:
                print("Please enter a number greater than 0.")
                continue
            
            # if all condition is passed, do the main method
            Binary_to_Decimal(binary_number)
            break
        
        User_Choice = str(input('What would you like to do [1,2,3,4]? '))