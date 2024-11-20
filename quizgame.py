questions = [
    ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "Php", 4],
    ["Which language is used for AI?", "Python", "Java", "C++", "Ruby", 1],
    ["Which framework is used for web development?", "Django", "React", "Vue", "Laravel", 1],
    ["Which company developed Windows?", "Apple", "Microsoft", "IBM", "Google", 2],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3]
]

levels = [1000, 2000, 3000, 5000, 10000]
money = 0

# Loop through all the questions
for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]}")
    
    try:
        # Get user input
        reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
        
        # Check if the user chose to quit
        if reply == 0:
            money = levels[i - 1] if i > 0 else 0
            print(f"You chose to quit. You take home Rs. {money}")
            break
        
        # Check if the answer is correct
        if reply == question[-1]:
            print(f"Correct answer! You have won Rs. {levels[i]}")
            money = levels[i]
        else:
            print("Wrong answer!")
            money = levels[i - 1] if i > 0 else 0
            break

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")

print(f"\nYour take-home money is Rs. {money}")