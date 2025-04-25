#1:Quiz 
quiz = {
    1: {
        "question": "What is the capital of India?",
        "options": ("A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"),
        "answer": "B"
    },
    2: {
        "question": "Which planet is known as the Red Planet?",
        "options": ("A. Earth", "B. Venus", "C. Mars", "D. Jupiter"),
        "answer": "C"
    },
    3: {
        "question": "What is 9 + 3?",
        "options": ("A. 7", "B. 8", "C. 9", "D. 10"),
        "answer": "B"
    }
}

#2:Lambda function to check answer
check_answer = lambda correct, user: correct.upper() == user.upper()

#3:run the quiz
def start_quiz():
    score = 0
    print("")
    print("Starting the Quiz...")
    print("")
    for q_no in quiz:
        print("Question", q_no, ":", quiz[q_no]["question"])
        for opt in quiz[q_no]["options"]:
            print(opt)
        user_ans = input("Your answer (A/B/C/D): ")
        if check_answer(quiz[q_no]["answer"], user_ans):
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer is:", quiz[q_no]["answer"])
        print("")
    print("Quiz Completed!")
    print("Your score is", score, "out of", len(quiz))
    print("")

#4:add your own question
def add_question():
    print("")
    print("Add your own question")
    question = input("Enter the question: ")
    option_a = input("Enter option A: ")
    option_b = input("Enter option B: ")
    option_c = input("Enter option C: ")
    option_d = input("Enter option D: ")
    answer = input("Enter the correct answer (A/B/C/D): ").upper()
    
    new_id = len(quiz) + 1
    options_tuple = ("A. " + option_a, "B. " + option_b, "C. " + option_c, "D. " + option_d)
    quiz[new_id] = {
        "question": question,
        "options": options_tuple,
        "answer": answer
    }
    print("Your question has been added!\n")

#5:menu
def main():
    while True:
        print("=== Quiz App Menu ===")
        print("1. Start Quiz")
        print("2. View Total Questions")
        print("3. Exit")
        print("4. Add Your Own Question")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            start_quiz()
        elif choice == "2":
            print("Total questions in the quiz:", len(quiz))
            print("")
        elif choice == "3":
            print("Exiting the Quiz App. Goodbye!")
            break
        elif choice == "4":
            add_question()
        else:
            print("Invalid choice. Please try again.\n")

main()
