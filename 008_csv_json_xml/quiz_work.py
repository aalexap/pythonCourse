import json

# answer_questions() - function to take one question as an argument
# returns user picket answer
def answer_queston(question):
    while True:
        print(f'1. {question[0]}\n2. {question[1]}\n'
              f'3. {question[2]}\n4. {question[3]}')
        user_choice = input('What is your answer? -> ')
        if user_choice.lower() == 'exit':
            print('Good bye')
            quit()
        if user_choice in '1234':
            return question[int(user_choice) - 1]
        else:
            print('Choice is out of range. Try again or type "exit" to quit.')

# check_answer() - function that takes right answer and user answer
# Compares them returns True of False
def check_answer(answer, user_answer):
    if user_answer == answer:
        return True
    return False


# start_quiez() - function to start quiz
def start_quiz(topic, data):
    quiz = data[topic]
    score = 0
    for question in quiz.values():
        print(question.get('question'))
        user_answer = answer_queston(question.get('options'))
        if check_answer(question.get('answer'), user_answer):
            score += 1
    print(f'You answered {score} questions right.')



# main() - function to controll quiz process
def main(data):
    print('Hello. Welcome to our quiz.')
    print(f'You can choose from {len(data.keys())} topics')

    for topic in data.keys():
        print('*', topic)
    while True:
        quiz_topic = input('Type topic name to continue or "exit" to quit - >')
        if quiz_topic.lower() == 'exit':
            print('Good bye!')
            quit()
        if quiz_topic.lower() in data.keys():
            start_quiz(quiz_topic.lower(), data)
            if input('Another quiz? y/n').lower() == 'y':
                main(data)
            else:
                print('Good bye')

        else:
            print(f'There is no {quiz_topic}')

with open('csv_files/quiz.json', 'r', encoding='utf-8') as file:
    quiz_data = json.load(file).get('quiz')

main(quiz_data)
