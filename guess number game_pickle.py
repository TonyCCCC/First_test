from random import randint
import pickle

with open('data_pkl.txt','rb') as file:
    scores = pickle.load(file)
file.close()

name = input("输入帐号名：")
if scores.get(name) == None:
    scores[name] = [0,0,0]
score = scores.get(name)
print(scores)
total_game = int(score[0])
min_times = int(score[1])
total_times = float(score[2])
if total_times == 0:
    avg_times = 0
else:
    avg_times = float(total_times)/total_game
print("你已经玩了%d次，最好成绩是%d次猜中，平均每轮猜%.2f次。"%(total_game,min_times,avg_times))
num = randint(1,10)
ans = int(input("Guess the num:\n"))
times = 0
bingo = False
while bingo == False:
    times += 1
    if ans > num:
        print("Big!")
    elif ans < num:
        print("Small!")
    else:
        print("Bingo!")
        bingo = True
        break
    ans = int(input("Try again!\n"))

total_game += 1
if min_times == 0 or times < min_times:
    min_times = times
total_times += times
scores[name] = [total_game,min_times,total_times]
print(scores)


with open('data_pkl.txt','wb') as file2:
    pickle.dump(scores,file2)
file2.close()