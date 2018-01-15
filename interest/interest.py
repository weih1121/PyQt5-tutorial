# -*- coding: utf-8 -*-


import random
peace=""
iscontinue='y'
while iscontinue=='y'or iscontinue=="Y":#注意这里的是判断所以应该是==
    words=("english","happy","sad","cry","welcome","supervised","yes")
    word=random.choice(words)
    correty=word
    while word!='':
        position=random.randrange(len(word))
        peace+=word[position]
        word=word[:position]+word[(position+1):]
    print("please speak word %s"%peace)
    answer=input("please answer word：")
    if correty==answer:
        print("right")
    while correty != answer:
        print("wrong")
        answer = input("please answer word again ：")
    iscontinue=input("是否继续Y/N：")
