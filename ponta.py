
import random
s = ['「おなかすいた」','「ねむたいよ」','「さんぽ行きたい」','「you一緒に遊んで！」','「お小遣いちょうだい！」']

u = random.choice(s)

monney = 10000

print('ぽんた',u)

if u == '「おなかすいた」' :
        t = input('お菓子をあげる？(yes or no)')
        if(t == 'yes'):
            print("ぽんた「ありがとう！！」")
            v = input('何をあげる？(くり or かき氷)')
            if(v == 'くり'):
                print("ぽんた「それ大好物なんだ！」")
        else:
            print("ぽんた「ご飯の時間まで我慢するね」")

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

if u == '「you一緒に遊んで！」' :
        t = input('遊んであげる？(yes or no)')
        if(t == 'yes'):
            print("ぽんた「やったー！！」")
        else:
            print("ぽんた「youは冷たいな...」")

if u == '「お小遣いちょうだい！」' :
        t = input('いくらあげる？(0 or 100 or 1000 or 10000)')
        if(t == '0'):
            print("ぽんた「ケチ」")
            print("所持金：10000円")
        elif(t == '100'):
            print("ぽんた「ありがとう。お菓子買ってくるね」")
            print("所持金：9900円")
        elif(t == '1000'):
            print("ぽんた「そんなにいいの！」")
            print("所持金：9000円")
        else:
            print("ぽんた「...シッシッシ、儲かった」")
            print("所持金：0円")



p = input('ぽんたに話しかける？(yes or no)')
if(p == 'yes'):
    a=input()
    
    if a == '大好き':
        print('ぽんた「ぼくも大好きだよ！」') 
    elif a == 'ぽんた':
        print('ぽんた「ぼく、ぽんた！」')
    else:
        print('ぽんた「日本語難しいな」')

            




