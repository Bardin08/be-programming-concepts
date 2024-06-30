fruit_shop = {"apple": {"amount": 3, "price": 13},
              "orange": {"amount": 4, "price": 23},
              "banana": {"amount": 5, "price": 37},
              "pear": {"amount": 7, "price": 48}}

rules = ("What would you like to do"
         " 1 add product"
         " 2. delete product "
         " 3. update price "
         " 4. show available products "
         " 5. buy product "
         " 6. exit")

print(fruit_shop)
print(rules)

while True:
    action = int(input("What would you like to do: "))
    if action not in range(1, 7):
        print("Invalid option. Please try again.")

    elif action == 1:
        f_name = str(input("entre a product name plz "))
        if f_name in fruit_shop.keys():
            print("we have this product")

        else:
            f_price = int(input("entre a product price plz "))
            f_amount = int(input("entre a product amount plz "))
            fruit_shop[f_name] = {"amount": f_amount, "price": f_price}
            print(fruit_shop)

    elif action == 2:
        del_f_name = str(input("entre a product name plz "))
        if del_f_name not in fruit_shop.keys():
            print("we have already had this product")
        else:
            del fruit_shop[del_f_name]
            print(fruit_shop)

    elif action == 3:
        update_f_name = str(input("entre a product name plz "))
        update_f_price = int(input("entre a new product price plz "))
        if update_f_name not in fruit_shop.keys():
            print("choose correct product name")
        else:
            fruit_shop[update_f_name]["price"] = update_f_price
            print(fruit_shop)

    elif action == 4:
        available_products = str(input("entre a product name plz "))
        if available_products in fruit_shop.keys():
            print(available_products, fruit_shop[available_products]["amount"])
        else:
            print("choose correct product name")

    elif action == 5:
        p_for_buy = str(input("entre a product name plz "))
        if p_for_buy not in fruit_shop.keys():
            print("choose correct product name")
        else:
            product_which_is_buy = fruit_shop[p_for_buy]
            amount_of_buy = int(input("entre a product amount plz "))
        fruit_shop[p_for_buy]["amount"] = fruit_shop[p_for_buy]["amount"] - amount_of_buy
        cost = fruit_shop[p_for_buy]["price"] * amount_of_buy
        print(f"the cost is {cost} ")
        print(fruit_shop)

    else:
        action == 6
        print("Thank you for using this program")
        exit(0)
