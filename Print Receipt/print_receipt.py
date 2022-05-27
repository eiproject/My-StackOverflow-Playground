def check_code(orders_list, code):
    codes = []
    for i in orders_list:
        codes.append(i["code"])
    if(code in codes):
        return True, codes.index(code)
    else:
        return False, 0

def main():
    products = {
        "americano":{"name":"Americano","price":150.00},
        "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
        "cappuccino":{"name":"Cappuccino","price":170.00},
        "dalgona":{"name":"Dalgona","price":170.00},
        "espresso":{"name":"Espresso","price":140.00},
        "frappuccino":{"name":"Frappuccino","price":170.00},
        }
    orders_list = []
    total = 0
    
    while(True):
        
        customer_order = input("Welcome to the CoffeePython POS Terminal.\nPlease enter the Product Code and the Quantity in this format - {Product Code},{Quantity}.\nEnter '/' to quit.\n")
        
        if customer_order == "/":
            break
             
        else:
            code_quantity_list = customer_order.split(",")
            code = code_quantity_list[0]
            quantity = code_quantity_list[1]
            quantity_int = int(quantity)
            
            if code in products:
                # subtotal = get_property(code,"price")*quantity_int
                subtotal = products[code]["price"] *quantity_int
                
                check = check_code(orders_list, code)
                if check[0]:
                    orders_list[check[1]]["subtotal"] += subtotal
                    orders_list[check[1]]["qty"] += quantity_int
                else:
                    ordered_item = dict([
                        ('code', code),                        
                        ('qty', quantity_int),                    
                        ('subtotal', subtotal)
                        ])
                    
                    orders_list.append(ordered_item)
                
                total += subtotal
                
            else:
                print("The Product Code that you entered is invalid. Please try again.")
                
    print("==")
    print("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL")
    orders_list = sorted(orders_list, key=lambda k: k['code']) 

    for order in orders_list:
        order_code = order['code']
        order_name = products[order_code]["name"]
        order_qty = order['qty']            
        order_subtotal = order['subtotal']
    
        print(f"{order_code}\t\t{order_name}\t\t{order_qty}\t\t\t\t{order_subtotal}\t\t")   
    
    print(f"\nTotal:\t\t\t\t\t\t\t\t\t\t{total}")
    print("==")
    print("Thank you for ordering. Goodbye.")

main()
