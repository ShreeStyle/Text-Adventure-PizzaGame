gameStart = "yes"
while gameStart == "yes":
    print("Welcome to La Mia Pizzaria Preferita!")
    print("What would you like for your toppings? Potatoes or Champignon Mushrooms")
    pizza_choice = input("Please choose one of them: ")
    
    if pizza_choice == "Potatoes":
        print("You chose " + pizza_choice + "! That's delicious! Here you are! Just wait for a minute mam/sir.")
        print("Would you like more toppings or ketchup?")
        want_toppings = input("yes or no? ")
        
        while want_toppings.lower() == "yes":
            print("This special pizza needs at least two toppings. Would you like to add something, or should we carry on with the current choice?")
            want_toppings = input("yes or no? ")
        
        print("Great! What would you like?")
        more_toppings = input("We have hot sauce, tomatoes, onions, extra cheese, black olives, and green peppers. --> ")
        
        print("Yay! " + more_toppings + " are my favourite!")
        print("Here's your pizza! Enjoy your food!")
        
        gameStart = input("Would you like to restart? (yes or no): ").lower()
       
    elif pizza_choice == "Champignon Mushrooms":
        print("You chose " + pizza_choice + "! That's delicious! Here you are! Just wait for a minute mam/sir.")
        print("Would you like more toppings?")
        want_toppings = input("yes or no? ")
        
        while want_toppings.lower() == "yes":
            print("This special pizza needs at least two toppings. Would you like to add something?")
            want_toppings = input("yes or no? ")
        
        print("Okay! What would you like?")
        more_toppings = input("We have herbs, breadcrumbs, balsamic glaze, and bacon bits. What would you prefer? --> ")
        
        print("Yay! " + more_toppings + " are my favourite!")
        print("Here's your pizza! Enjoy your food!")
        
        gameStart = input("Would you like to restart? (yes or no): ").lower()

    else:
        print("Sorry, we do not have that item.")
        gameStart = input("Would you like to restart? (yes or no): ").lower()
