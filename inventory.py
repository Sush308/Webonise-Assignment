import sys
from product import Product
from menus import user_menu, shopkeeper_menu, print_menu


def start_app():
    print("\t\t*********** Inventory Shop ***********")
    while True:
        # print("Who are you?")
        print_menu()

        try:
            choice = int(input("Please, Enter your choice: "))
        except ValueError:
            print("Error: You entered the wrong choice. Please try again")
            choice = 0

        if choice == 3:
            sys.exit(1)
        else:
            while choice > 0 and choice < 3:
                if choice == 1:
                    shopkeeper_menu()
                    try:
                        shopkeeper_choice = int(input("Hey Shopkeeper, Please Enter your choice: "))
                    except ValueError:
                        print("Error: You entered the wrong choice. Please try again")

                    if shopkeeper_choice == 6:
                        break

                    while shopkeeper_choice > 0 and shopkeeper_choice < 7:
                        if shopkeeper_choice == 1:
                            try:
                                name = input("Enter product name: ")
                            except ValueError:
                                name = ""
                                print("Error: You entered something wrong")
                                break

                            try:
                                price = float(input("Enter price of Product(per kg): "))
                            except ValueError:
                                price = 0.0
                                print("Error: You entered something wrong")
                                break

                            try:
                                stock_item = int(input("Enter total stock of Product(in kg): "))
                            except ValueError:
                                stock_item = 0
                                print("Error: You entered something wrong")
                                break

                            try:
                                company_name = input("Enter company name of Product: ")
                            except ValueError:
                                company_name = ""
                                print("Error: You entered something wrong")
                                break

                            product = Product()
                            product.add(name, price, stock_item, company_name)

                        elif shopkeeper_choice == 2:
                            id = int(input("Enter the product ID for Delete/Remove the product: "))
                            product = Product()
                            product.remove(id)


                        elif shopkeeper_choice == 3:
                            product = Product()
                            product.list_product()


                        elif shopkeeper_choice == 4:
                            name = input("Enter the name of the product for search: ")
                            product = Product()
                            product.search(name)

                        elif shopkeeper_choice == 5:
                            id = int(input("Enter Product ID: "))
                            product = Product()
                            product.update(id)

                        elif shopkeeper_choice == 6:
                            sys.exit(1)
                            print_menu()
                        else:
                            print("Please Enter number 1 to 6")

                        shopkeeper_menu()
                        try:
                            shopkeeper_choice = int(input("Hey Shopkeerper, Please Enter your choice: "))
                        except ValueError:
                            print("Error: You entered the wrong choice. Please try again")
                            shopkeeper_choice = 0

                else:
                    user_menu()
                    try:
                        user_choice = int(input("Please, Enter your choice: "))
                    except ValueError:
                        print("Error: You entered the wrong choice. Please try again")

                    if user_choice == 4:
                        break

                    while user_choice > 0 and user_choice < 4:
                        if user_choice == 1:
                            product = Product()
                            product.list_product()

                        elif user_choice == 2:
                            name = input("Enter the name of the product for Search:  ")
                            product = Product()
                            product.search(name)

                        elif user_choice == 3:
                            product_id = int(input("Enter Product ID: "))
                            product = Product()
                            product.buy_product(product_id)

                        elif user_choice == 4:
                            sys.exit(1)
                            print_menu()

                        else:
                            print("Enter number between 01 to 04")


                        user_menu()
                        try:
                            user_choice = int(input("Please, Enter your choice: "))
                        except ValueError:
                            print("Error: You entered the wrong choice. Please try again")
                            user_choice = 0

        print_menu()
        try:
            choice = int(input("Please, Enter your choice: "))
        except ValueError:
            print("Error: You entered the wrong choice. Please try again")
            choice = 0

if __name__ == "__main__":
    start_app()
