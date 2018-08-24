poem = "\
静夜思 李白\n\
床前明月光，\n\
疑似地上霜。\n\
举头望明月，\n\
低头思故乡。".split('\n')

poem = poem[::-1]

gun = "|"
poem_1 = []
for i in range(len(poem)):
    for j in list(poem[i]):
        print(j)
print(poem[0][1])

for word in range(6):
    for sentence in range(len(poem)):
        print(poem[sentence][word],end="")
        if sentence != 4:
            print('|',end="")
        else:
            print('\n',end="")