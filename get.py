import requests
from bs4 import BeautifulSoup
import re
import sys

key = sys.argv[1]

r = requests.get('https://www.sanskrit-lexicon.uni-koeln.de/cgi-bin/monier/monierv1a.pl?key=' + key + '&filter=SktRomanUnicode&noLit=off&transLit=SLP2SLP&scandir=../..MWScan/MWScanpng&filterdir=../../docs/filter')

def get_head_word(head):
    word = ""
    for el in head.find_all('font'):
        if 'color="blue"' in str(el):
            word = el.contents[0]
    return word

doc = r.content
soup = BeautifulSoup(doc, 'html.parser')

table = soup.find_all('td')
heads = []
for td in table:
    for n in range(1, 100):
        s = 'H' + str(n)
        if s in str(td):
            heads.append(td)
            break

cur_head = ""
meanings = {}
for td in table:
    if td in heads:
        cur_head = td
        meanings[cur_head] = []
    else:
        meanings[cur_head].append(td)

#ptrn = re.compile("</*\s*a[^>]*>(.*?)")
ptrn1 = re.compile("</*\s*[^>]*>")
ptrn2 = re.compile("\&amp\;c")
ptrn3 = re.compile("\[L\=[0-9]+\]")

for head in heads:
    mngs = meanings[head]
    print(get_head_word(head))
    print("-----------------------------------------------------------------------")
    for m in mngs:
        m_ = re.sub(ptrn1, "", str(m))
        m_ = re.sub(ptrn2, "", m_)
        m_ = re.sub(ptrn3, "", m_)
        m_ = m_.rstrip().lstrip()
        if m_ != "":
            print("->  " + m_)
print("=======================================================================")
