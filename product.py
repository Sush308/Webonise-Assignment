import json
import hashlib


class Product:

    def add(self, name="", price=0, stock_item=0, company_name=""):
        product = dict()

        product["name"] = name
        product["price"] = price
        product["stock_item"] = stock_item
        product["company_name"] = company_name
        try:
            with open("inventory.json", "r+") as json_file:
                product_data = json.load(json_file)
                if len(product_data["products"]) > 0:
                    id = product_data["products"][-1]["id"]
                    product["id"] = id + 1
                else:
                    product["id"] = 0

                product_data["products"].append(product)
                product_data["products"] = sorted(product_data["products"], key=lambda i: i['id'])
                json_file.seek(0)
                json.dump(product_data, json_file, indent=4)
                print("\nProduct added successfully\n\n")
        except Exception:
            print(Exception)

    def remove(self, id):
        with open("inventory.json", "r") as json_file:
            product_data = json.load(json_file)
            products = product_data["products"]
            index = -1

            for i in range(len(products)):
                if products[i]["id"] == id:
                    index = i
                    break

            if index != -1:
                del products[index]
                product_data["products"] = products
                with open('inventory.json', 'w') as json_file:
                    product_data["products"] = sorted(product_data["products"], key=lambda i: i['id'])
                    json.dump(product_data, json_file, indent=4)
                print("\nProduct Deleted Successfully...\n\n")
            else:
                print("ID not found")

    def update(self, id):
        with open("inventory.json", "r+") as json_file:
            product_data = json.load(json_file)
            for product in product_data["products"]:
                if product["id"] == id :
                    try:
                        name = input("Enter product name: ")
                    except ValueError:
                        name = ""
                        print("Error: You entered something wrong")
                        break

                    try:
                        price = float(input("Enter price of Product: "))
                    except ValueError:
                        price = 0.0
                        print("Error: You entered something wrong")
                        break

                    try:
                        stock_item = int(input("Enter total stock of Prouct: "))
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

                    product["name"] = name
                    product["price"] = price
                    product["stock_item"] = stock_item
                    product["company_name"] = company_name
                    print("Product updated Successfully")
                    break

            json_file.seek(0)
            json.dump(product_data, json_file,indent=4)


    def buy_product(self, product_id):
        order_successful = 0
        with open("inventory.json", "r") as json_file:
            product_data = json.load(json_file)
            for product in product_data["products"]:
                if product_id == product['id']:
                    if product["stock_item"] > 0:
                        try:
                            customer_name = input("Enter customer name: ")
                        except ValueError:
                            customer_name = ""
                            print("Error: You entered something wrong")
                            break
                        try:
                            card_number = input("Enter Credit card number: ")
                        except ValueError:
                            card_number= ""
                            print("Error: You entered something wrong")
                            break
                        try:
                            cvv = input("Enter CVV: ")
                            cvv = hashlib.md5(cvv.encode()).hexdigest()
                        except ValueError:
                            cvv = ""
                            print("Error: You entered something wrong")
                            break

                        try:
                            confirmation = input("Are you sure to buy product (y / n): ")
                        except ValueError:
                            confirmation = ""
                            print("Error: You entered something wrong")
                            break

                        if confirmation != "y":
                            print("Your transaction cancled successfully...")
                            return

                        order = dict()
                        if customer_name !="" and card_number != 0 and cvv != "":
                            order["product_id"] = product["id"]
                            order["customer_name"] = customer_name
                            order["card_number"] = card_number
                            order["cvv"] = cvv

                            with open("order.json", "r+") as order_file:
                                order_data = json.load(order_file)
                                order["id"] = len(order_data["orders"]) + 1
                                order_data["orders"].append(order)
                                order_file.seek(0)
                                json.dump(order_data, order_file,indent=4)

                            order_successful = 1
                            product["stock_item"] -= 1
                            with open("inventory.json", "w") as file:
                                json.dump(product_data, file, indent=4)
                                break

                        else:
                            print("Please enter all details...")
                    else:
                        print("Product out of stock")
        print("-"*50)
        print("\nProduct successfully placed...\n")
        print("-" * 50)
        if not order_successful:
            print("Product ID not found")



    def search(self, name):
        with open("inventory.json", "r") as json_file:
            product_data = json.load(json_file)
            for product in product_data["products"]:
                if name.lower() == product['name'].lower():
                    print("- " * 40)
                    print("Product ID:", product["id"])
                    print("Product Name:", product["name"])
                    print("Price:", product["price"])
                    print("Stock Item:", product["stock_item"])
                    print("Company Name:", product["company_name"])
                    print("- " * 40)
                    print("\nProduct search successfully...\n")
                    print("- " * 40)



    def list_product(self):
        with open("inventory.json", "r") as json_file:
            product_data = json.load(json_file)
            if len(product_data["products"]):
                print("\t\t -------------- Products List -------------------")
                for product in product_data["products"]:
                    print("- " * 40)
                    print("Product ID:", product["id"])
                    print("Product Name:", product["name"])
                    print("Price:", product["price"])
                    print("Stock Item:", product["stock_item"])
                    print("Company Name:", product["company_name"])
                    print("- " * 40)

