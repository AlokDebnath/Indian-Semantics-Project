import os

g = open('README.txt', 'w+')
cnt = 0
tot = len(os.listdir('./txt/'))
for file in os.listdir('./txt/'):
    cnt += 1
    if cnt % 10 == 0:
        print(str(cnt/tot) + "\t" + str(cnt/tot * 100) + "% done \r", end = "")
    if cnt == tot:
        print(str(cnt/tot) + "\t" + str(cnt/tot * 100) + "% done \r")
    with open('./txt/' + file) as f:
        try:
            line = f.readlines()[2]
        except Exception as e:
            line = "-> does not have the first definition apparently\n"
        g.write(file + " :" + line + "\n")
g.close()
