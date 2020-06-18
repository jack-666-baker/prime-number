# Python program which displays all prime numbers between two numbers chosen by
# the individual.


def inputNumber(message):
            goodinput = False
            while not goodinput:
                try:
                    userInput = int(input(message))
                    if userInput > 0:
                        goodinput = True
                        return userInput 
                        break
                    else:
                        print("That is not a positive number. Please try again")
                except ValueError:
                    print("That's not an number. Please try again")

            


def main():
    print("Welcome to the prime number generator!")
    print(" ")
    print("A prime number is whole number greater than one, and only has two factors - 1 and the number itself")
    print(" ")

    lower = inputNumber("Please enter the first number: ") #gets the input from a user and assigns it to a variable 'lower'
    upper = inputNumber("Please enter a second number, larger than the first one: ") #gets the input from a user and assigns it to a variable 'upper'
    print("The prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):

       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num)
    
    
    again = input("Would you like to play again? Yes or no\n")
    again = again.lower()

    if again=="yes" or again=="y":
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        main()
    else:
        print("\n")
        print("\n")
        print("Thank you for running my programme")
        print("You may now close my programme")



main() 
        
