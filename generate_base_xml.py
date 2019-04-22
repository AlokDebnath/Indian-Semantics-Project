import os

f = open('raw_meanings.txt', 'r')
g = open('ontology/base.xml', 'w+')

lines = f.readlines()
cnt = 0
tot = len(lines)

for line in lines:
    cnt += 1
    if cnt % 10 == 0:
        print(str(cnt/tot * 100) + "% done \r", end = " ")
    if cnt == tot:
        print(str(cnt/tot * 100) + "% done")

    word = line.split(':->')[0].strip()
    meaning = line.split(':->')[1].strip()
    g.write('<word>\n\t<form> ' + word + ' </form>\n' + '\t<meaning> ' + meaning + ' </meaning>\n</word>\n')

g.close()
