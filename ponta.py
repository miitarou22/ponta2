
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

if u == '「ねむたいよ」' :
        t = input('布団をかけてあげる？(yes or no)')
        if(t == 'yes'):
            print("ぽんた「おやすみなさい」")
        else:
            print("ぽんた「さ.さむいな...」")

if u == '「さんぽ行きたい」' :
        t = input('お出かけする？(yes or no)')
        if(t == 'yes'):
            print("ぽんた「今から準備してくるね！！」")
        else:
            print("ぽんた「そっか...」")


