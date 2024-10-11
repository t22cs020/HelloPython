import random

def hands(choice):
    if(choice == '0'):
        return "グー"
    elif(choice == '1'):
        return "チョキ"
    elif(choice == '2'):
        return "パー"
    
def janken():
    A_win = 0
    B_win = 0
    
    choices = ['0', '1', '2']
    
    print("３回勝負のじゃんけんを始めます！")
    
    while(A_win < 3 and B_win < 3):
        print("0:グー、1:チョキ、2:パー")

        user_choice = input("あなたの選択を入力してください: ")
    
        if user_choice not in choices:
            print("無効な選択です。もう一度試してください。")
            return
    
        user_hand = hands(user_choice)
        print("Aの手:", user_hand)
        print("v.s.")
        computer_choice = random.choice(choices)
        computer_hand = hands(computer_choice)
        print("Bの手:", computer_hand)
    
        if user_choice == computer_choice:
            print("引き分け")
        elif (user_choice == 0 and computer_choice == 1) or \
             (user_choice == 1 and computer_choice == 2) or \
             (user_choice == 2 and computer_choice == 0):
            print("Aの勝ち")
            A_win += 1
        else:
            print("Bの勝ち")
            B_win += 1
            
        print("A:",A_win,"  B:",B_win)
    

if __name__ == "__main__":
    A_win = 0
    B_win = 0
    
    janken()