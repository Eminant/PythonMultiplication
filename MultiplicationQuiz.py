#Emily Campa; Student ID #0463272
#COSC-1302-NT1-20/FA; Prof. Inetha Sheffield
#Final Exam Program
#December 7, 2020

import random

#function to check answers and add up correct ones and return appropriate count
def check_answer(answer, solution, count):
    if answer == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count

#generate questions using * and 3-12
def get_quiz(index, count):
    firstNum = random.randrange(3, 12)
    secondNum = random.randrange(3, 12)
    generatedQuestion = str(firstNum) + " * " + str(secondNum)
    #produce correct answer
    solution = firstNum * secondNum
    #get answer from user
    print("\nEnter your answer >>")
    print(generatedQuestion, end="")
    answer = int(input(" = "))
    #call function to compare given answer with solution to count questions appropriate
    count = check_answer(answer, solution, count)
    x = 0
    if answer != solution:
        #when an incorrect answer is given, store the solution in a list
        wrongAnswers = []
        wrongAnswers.append(solution)
        #store the question in a list when the answer is incorrect
        missedProblems = []
        missedProblems.append(generatedQuestion)
        #give the user the solution to any questions answered incorrectly
        print("Solution for", missedProblems[x], "is", wrongAnswers[x])
        x = x + 1
    return count

#calculate scores and store them as needed
def show_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("\nYou answered", correct, "questions correctly out of", total)
    print("Your score is ", percentage, "%")
    score = []
    score.append(percentage)
    x = 0
    #automatically generate another quiz if score is <80%
    if percentage < 80:
        print("\nYou scored less than an 80, so you must take the quiz again.")
        correct = 0
        total = 0
        while correct < 10:
            total = total + 1
            correct = get_quiz(total, correct)
        print("\nYou answered", correct, "questions correctly out of", total)
        result = correct / total
        percentage = round((result * 100), 2)
        score.append(percentage)
        avgScore = (float(score[0]) + float(score[1])) / 2
        x = x + 1
    #if score is > 80% & if 2 quizzes have not been taken, ask if the user wants to quiz again
    if percentage > 80 and x < 1:
        print("\nWould you like to take the quiz again? Enter Y/N: ")
        quizAgain = input()

        if quizAgain == 'N' or quizAgain == 'n':
            score.append("NA")
            avgScore = (float(score[0]))

        if quizAgain == 'Y' or quizAgain == 'y':
            print("\nBecause you selected another take, here is another quiz.")
            correct = 0
            total = 0
            while correct < 10:
                total = total + 1
                correct = get_quiz(total, correct)
            print("\nYou answered", correct, "questions correctly out of", total)
            result = correct / total
            percentage = round((result * 100), 2)
            print("Your score is ", percentage, "%")
            # add percentage score made on quiz to list
            score.append(percentage)
            avgScore = (float(score[0]) + float(score[1]))/2
    #get users name and produce the appropriate scores for each quiz
    print("\nEnter your name to view your scores: ")
    name = input()
    print("\n{:<10} {:<10} {:<10} {:<10}".format('Name', 'Score 1', 'Score 2', 'Avg Score'))
    print("{:<10} {:<10} {:<10} {:<10}".format(name, str(score[0]), str(score[1]), str(round(avgScore, 2))))


def main():
    print("Multiplication Quiz\n~~~~~~~~~~~~~~~~~~~") #pretty title
    total = 0
    correct = 0
    while correct < 10:
        total = total + 1
        #send value to get_quiz to generate another question until 10 are answered correctly
        correct = get_quiz(total, correct)

    #call results function after 10 answered correctly
    show_result(total, correct)


main()
