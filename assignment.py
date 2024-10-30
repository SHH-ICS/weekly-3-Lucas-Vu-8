def calculate_pizza_cost():
    # Pizza costs and constants
    LARGE_COST = 6.00
    EXTRA_LARGE_COST = 10.00
    
    # Topping costs
    TOPPING_COSTS = {
        1: 1.00,
        2: 1.75,
        3: 2.50,
        4: 3.35
    }
    
    # HST tax rate
    HST_RATE = 0.13
    
    # Prompt user for pizza size
    print("Pizza Size Options:")
    print("1. Large ($6.00)")
    print("2. Extra Large ($10.00)")
    
    size_choice = input("Enter your choice (1 for Large, 2 for Extra Large): ")
    
    if size_choice == '1':
        pizza_cost = LARGE_COST
        pizza_size = "Large"
    elif size_choice == '2':
        pizza_cost = EXTRA_LARGE_COST
        pizza_size = "Extra Large"
    else:
        print("Invalid choice. Please restart the program and select a valid option.")
        return
    
    # Prompt user for number of toppings
    print("\nTopping Options:")
    print("1. 1 Topping ($1.00)")
    print("2. 2 Toppings ($1.75)")
    print("3. 3 Toppings ($2.50)")
    print("4. 4 Toppings ($3.35)")
    
    topping_choice = input("Enter the number of toppings (1-4): ")
    
    if topping_choice.isdigit() and int(topping_choice) in TOPPING_COSTS:
        topping_cost = TOPPING_COSTS[int(topping_choice)]
        topping_count = int(topping_choice)
    else:
        print("Invalid choice. Please restart the program and select a valid option.")
        return
    
    # Calculate subtotal, tax, and final total
    subtotal = pizza_cost + topping_cost
    tax = subtotal * HST_RATE
    final_total = subtotal + tax
    
    # Display results
    print("\n--- Order Summary ---")
    print(f"Pizza Size: {pizza_size}")
    print(f"Number of Toppings: {topping_count}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"HST (13%): ${tax:.2f}")
    print(f"Total Cost: ${final_total:.2f}")
    
# Run the program
calculate_pizza_cost()
