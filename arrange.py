import os

f = open('./meaningSets/Alok.txt')
for line in f.readlines():
    word = line.split("\"")[1].strip()
    file = './words_project/'+ word + '.txt'
    os.system('python3 get.py '+ word + ' > ' + file)
