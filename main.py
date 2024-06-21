import random
from rich import print

# Initialize price list with original values
price = [
    "Q1= 1000", "Q2= 5000", "Q3= 10000", "Q4= 20000", "Q5= 50000",
    "Q6= 100000", "Q7= 1000000", "Q8= 2000000", "Q9= (7cr)"
]

que = [
    "What is the largest state in India by area?",  # [0]
    "Which river is known as the 'Ganga of the South'?",  # [1]
    "Which state is known as the 'Land of Five Rivers'?",  # [2]
    "Which Indian state is known for its famous backwaters?",  # [3]
    "Which state is home to the famous Valley of Flowers National Park?",  # [4]
    "Which Indian state is known for its famous hill station, Shimla?",  # [5]
    "Where does printing come first in India?",  # [6]
    "What is the capital of Maharashtra?",  # [7]
    "Which state is known for the Silent Valley National Park?",  # [8]
    "In which state the famous Sanchi Stupa is located?",  # [9]
    "Which state is known for the Hazaribagh Wildlife Sanctuary?",  # [10]
    "What is India’s largest city by population?",  # [11]
    "Which state is known for the Dudhwa National Park?",  # [12]
    "In which state are the famous Elephanta Caves located?"  # [13]
]

ans = [
    "Rajasthan",  # [0]
    "Godavari",  # [1]
    "Punjab",  # [2]
    "Kerala",  # [3]
    "Uttarakhand",  # [4]
    "Himachal Pradesh",  # [5]
    "Goa",  # [6]
    "Mumbai",  # [7]
    "Kerala",  #[8]
    "Madhya Pradesh",  #[9]
    "Jharkhand",  #[10]
    "Mumbai",  #[11]
    "Uttar Pradesh",  #[12]
    "Maharashtra"  #[13]
]

rules = [
    "1. There are total 9 questions in this game.",
    "2. Each question has a different price value.",
    "3. If you answer a question correctly, you will win the corresponding prize money.",
    "4. If you answer a question incorrectly, you will lose the game."
]

print("[bold]Kon Banega Crorepati (KBC) Me apka swagat hai![/]\n")
print("The prize money of the questions is according to:\n\n", price, "\n")
print("RULES ", rules)
print("\nTo apke question aapke computer screen par ye rahe:\n")

def select_question(asked_indices):
    """
    Selects a random question from the list and prints it to the user.

    Args:
        asked_indices (set): The set of already asked question indices.

    Returns:
        tuple: The correct answer and the index of the question.
    """
    a = random.choice([i for i in range(len(que)) if i not in asked_indices])  
    # Random question index not in asked_indices

    print("•", que[a],"\n")  # Print the question

    correct_answer = ans[a]  # Store the correct answer

    # Display options with shuffled order
    options = [ans[a]]  # Add the correct answer first
    while len(options) < 4:  # Ensure we have four options
        option = ans[random.randint(0, len(ans) - 1)]
        if option not in options:
            options.append(option)
 
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"{chr(65 + i)}. {option}\n")

    return correct_answer, a

def price_update(price, correct_answer, price_index=0):
    """
    Updates the price based on the user's answer.

    Args:
        price (list): The list of price values.
        correct_answer (str): The correct answer to the question.
        price_index (int, optional): The current price index. Defaults to 0.
    """
    user_answer = input("Enter the correct answer: ").strip()
    
    if user_answer=="quit" or user_answer=="Quit":
        print("You quit the game and you are out with",{price[price_index]},"money")
        exit()
    
    elif user_answer.lower() == correct_answer.lower():  # Case-insensitive comparison
        print(f"\nSahi jawab! Aap jeet chuke hai {price[price_index]}\n")
        price_index += 1
    else:
        print(f"\nGalat jawab! Aap apne {price[price_index]} har chuke hai.\n")
        print(f"Iska sahi jawab tha {correct_answer}.\n")
        price_index = 0  # Reset the price index if the answer is incorrect

    return price_index

# Main loop to simulate the game
price_index = 0
asked_indices = set()  # Set to keep track of asked questions

for _ in range(9):
    correct_answer, question_index = select_question(asked_indices)
    asked_indices.add(question_index)
    price_index = price_update(price, correct_answer, price_index)
    if price_index == 9 or price_index == 0:
        break  # End the game if an incorrect answer is given

print("To hamara safar yahi katam hota hai.\n")
print(f"Apne hatho ko takleef dekar please aap apne {price_index} rupee samet le")
