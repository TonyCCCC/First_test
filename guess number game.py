from random import randint

f = open('data.txt')
scores = {}
lines = f.readlines()
for l in lines:
     s = l.split()
     scores[s[0]] = s[1:]
print(scores)
f.close()
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
    if ans > num:
        print("Big!")
    elif ans < num:
        print("Small!")
    else:
        print("Bingo!")
        bingo = True
        break
    ans = int(input("Try again!\n"))
    times += 1

total_game += 1
if min_times == 0 or times < min_times:
    min_times = times
total_times += times
scores[name] = [total_game,min_times,total_times]
print(scores)
result = ""
for n in scores:
    line = ("%s %s %s %s\n"%(n,scores[n][0],scores[n][1],scores[n][2]))
    result += line
print(result)

f = open('data.txt','w')
f.write(result)
f.close()