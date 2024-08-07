from Art import logo
from Question import quiz
from replit import clear
import pprint

# greeting function
def greeting(p_question_num):
    print(f"There are a total of {p_question_num} question, you can skip a question anytime by typing 'skip' ")
    input("Press any key to get started...")
    print(logo)

# print correct answer
def print_correct_answer():
    for question_num,nested_dic in quiz.items():
        for key,value in nested_dic.items():
            print(key+":",value)

# For checking Answer
def check_answer(question_num,answer,attempt,player):
    clear()
    correct_answer=quiz[question_num]["answer"]
    if correct_answer.lower() == answer.lower():
        print(f"Correct Answer: \n {player}'s score is {player_score[player]+1} ")
        return True
    else:
        print(f"Wrong Answer :( \n You have {attempt -1} attempt left! \nTry Again...")
        return False
    
# for switching user 
def switch_users(p_user_index):
    if p_user_index == 0:
        return 1
    return 0
    
def find_winner(player1,player2):
    if player_score[player1] > player_score[player2]:
        print(f"{player1} WON! The score is {player_score[player1]}")
    elif player_score[player1] < player_score[player2]:
        print(f"{player2} WON! The score is {player_score[player2]}")
    else:
        print("It is DRAW!")

# Gretting
greeting(len(quiz))
players=input("Enter 2 players with space: ")
player_list=players.split(" ")
# print(player_list)
player_score=dict.fromkeys(player_list,0)
# print(player_score)
current_player=player_list[0]  #starting with first player

for questions in quiz:
    print("--------------------------------------")
    print(f"It is {current_player}'s turn. ")
    attempt=2
    while attempt > 0:
        print(quiz[questions]["question"])
        answer=input("Enter Answer (To move to the next Question type 'skip'): ").lower()
        if answer == "skip":
            break
        check=check_answer(questions,answer,attempt,current_player)
        if check:
            player_score[current_player]+=1
            break
        attempt-=1
    current_player_index=player_list.index(current_player)
    next_player_index=switch_users(current_player_index)
    current_player=player_list[next_player_index]
find_winner(player_list[0],player_list[1])

show_correct_answer=input("Do you want to see the correct answer?(Y/N): ").upper()
if show_correct_answer =="Y":
    print_correct_answer()
print("Thanks for playing!") 