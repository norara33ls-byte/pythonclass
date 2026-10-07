# Grocery Shopping Assistant

while True:

    print("\n==============================")
    print("   GROCERY SHOPPING ASSISTANT")
    print("==============================")

    # Step 1: Input Budget
    budget = float(input("Enter your shopping budget: M "))

    # Create an empty cart
    cart = []

    # Step 2: Add Items to the Cart
    while True:
        print("\n--- Add Item ---")

        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: M "))

        # Step 3: Calculate cost for the item
        item_cost = quantity * price

        # Add item to the cart
        cart.append({
            "name": item_name,
            "quantity": quantity,
            "price": price,
            "cost": item_cost
        })

        print(f"{item_name} added to your cart.")
        print(f"Item cost: M {item_cost:.2f}")

        # Ask if user wants to add another item
        another = input("\nDo you want to add another item? (yes/no): ")

        if another.lower() != "yes":
            break

    # Calculate total cart cost
    total_cost = sum(item["cost"] for item in cart)

    # Step 4: Check Budget
    print("\n==============================")
    print("       BUDGET CHECK")
    print("==============================")

    print(f"Your budget: M {budget:.2f}")
    print(f"Total cost:  M {total_cost:.2f}")

    if total_cost > budget:
        overage = total_cost - budget
        print(f"WARNING: You are over your budget by M {overage:.2f}")
    else:
        remaining = budget - total_cost
        print(f"SUCCESS: Your shopping is within budget.")
        print(f"Money remaining: M {remaining:.2f}")

    # Step 5: Display Cart Summary
    print("\n==============================")
    print("        CART SUMMARY")
    print("==============================")

    print(f"{'Item':<15}{'Quantity':<10}{'Price':<12}{'Total':<12}")
    print("-" * 49)

    for item in cart:
        print(
            f"{item['name']:<15}"
            f"{item['quantity']:<10}"
            f"M {item['price']:<10.2f}"
            f"M {item['cost']:<10.2f}"
        )

    print("-" * 49)
    print(f"{'TOTAL':<37}M {total_cost:.2f}")

    # Step 6: Allow Multiple Sessions
    print("\n==============================")

    new_session = input(
        "Do you want to start a new shopping session? (yes/no): "
    )

    if new_session.lower() != "yes":
        print("\nThank you for using the Grocery Shopping Assistant!")
        print("Goodbye!")
        break