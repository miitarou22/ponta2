
import random
s = ['「おなかすいた」','「ねむたいよ」','「さんぽ行きたい」' ]

u = random.choice(s)


print('ぽんた',u)

if u == '「おなかすいた」' :
        t = input('お菓子をあげる？(yes or no)')
        if(t == 'yes'):
            print("ぽんた「ありがとう！！」")
        else:
            print("ぽんた「そっか...」")
