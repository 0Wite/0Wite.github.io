import random
card_num=[]
all_card=[]
deck=[[],[],[],[]]
for num in range(52):
    card_num.append(num)

def check(ch=False):
    for num in range(52):
        card=""
        if card_num[num]%4==0:
            card+="♣"
        if card_num[num]%4==1:
            card+="♠"
        if card_num[num]%4==2:
            card+="♡"
        if card_num[num]%4==3:
            card+="♢"
        if num//4<8:
            card+=str(card_num[num]//4+3)
        if num//4==8:
            card+="J"
        if num//4==9:
            card+="Q"
        if num//4==10:
            card+="K"
        if num//4==11:
            card+="A"
        if num//4==12:
            card+="2"
        if ch==False:
            all_card.append(card)
check()
rand_num=[]

for num1 in range(4):
    card_num=set(card_num)-set(rand_num)
    rand_num=random.sample(card_num,13)
    rand_num.sort()
    for num2 in rand_num:
        deck[num1].append(all_card[num2])

for num in range(4):
    print(deck[num])

print("Player1 vs Player2")
i=0
current_card_num=0
current_card=""
while(True):
    i%=2
    while(True):
        print("\nあなたのデッキ: "+str(deck[i]))
        try:
            print("場のカード"+current_card)
            current_card_num=int(all_card.index(current_card))//4
        except:
            current_card_num=-1
            print("場のカードなし")
        a=input("Player"+str(i+1)+"は入力してください:")
        if a=="show":
            print(deck[i])
        if a=="pass":
            current_card=""
            current_card_num=-1
            break;
        try:
            if current_card_num<all_card.index(deck[i][int(a)-1])//4:
                print(deck[i][int(a)-1])
                current_card=deck[i][int(a)-1]
                deck[i].pop(int(a)-1)
                break;
            else:
                print("このカードは出せません")
        except:
            print("Error")
    if len(deck[i])==0:
        print("Player"+str(i+1)+"の勝利")
        break;
    i+=1