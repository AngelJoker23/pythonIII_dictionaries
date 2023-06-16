from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
def shopping_cart():
    cart = []
    
    while True:
        print("Shopping Cart Menu:")
        print("1. Show Cart")
        print("2. Add Item")
        print("3. Delete Item")
        print("4. Quit")
        
        choice = input("Please enter your choice (1-4): ")
        
        if choice == "1":
            show_cart(cart)
        elif choice == "2":
            add_item(cart)
        elif choice == "3":
            delete_item(cart)
        elif choice == "4":
            print("Thank you for using the shopping cart. Here are the items in your cart:")
            show_cart(cart)
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
        
        print("\n")
        
def show_cart(cart):
    if not cart:
        print("Your shopping cart is empty.")
    else:
        print("Items in your shopping cart:")
        for item in cart:
            print("- " + item)
            
def add_item(cart):
    item = input("Enter the item to add: ")
    cart.append(item)
    print("Item added to the shopping cart.")
    
def delete_item(cart):
    item = input("Enter the item to delete: ")
    if item in cart:
        cart.remove(item)
        print("Item deleted from the shopping cart.")
    else:
        print("Item not found in the shopping cart.")
        

shopping_cart()