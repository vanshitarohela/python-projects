  # Coffee Maker Machine
  This project aims at replicating the mechanisms of a Coffee Maker Machine.
  Its MENU contains of Espresso, Latte and Cappuccino consisting of different requirements of milk, coffee and water and also priced differently.
  The user can input their order and the maintainers of the Machine can get a report about the profit made and the resources left in the Machine.
  
  ## Functions defined
  ### 1. check_requirements
  This function checks the requirements to make the user specified coffee and returns True if the requirements are met, else it will return a string specifying which resource the machine has run out of.
  It takes MENU, resources and user_input as parameters.
  
  ### 2. user_money
  This function calculates the user's money and returns the sum of all the coins given by the user.
  It asks user to input number of quarters, dimes, nickels, and pennies.
  
  ### 3. check_money
  This function checks if the user has given enough money to make the coffee they are asking for.
  It returns True if condition is met, else it returns a string stating that money is insufficient and returns the money to the user which means that money is not added to the profit variable.
  It take MENU, user_input and money as parameters.
  
  ### 4. resources_and_profit
  This function handles the resources in the machine, subtracts the resources every time a successful purchase of coffee is made and adds the money to the profit.
  It takes MENU, user_input and resources as parameters.
  
  ### 5. return_change
  This function returns the change to the user if they have submitted more money than needed. It is called when a successful purchase is being made.
  It takes MENU, user_input and money as parameters.
  
  ### 6. give_report
  It gives report of the resources left in the Coffee Maker Machine. This is triggered by a command called "report" when asked for input.
  This is for the maintainers of the machine.
  It takes resources and profit as parameters.
  
  
