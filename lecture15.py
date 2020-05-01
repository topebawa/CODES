trial =1
while trial >2:
    print('wish to see you again')
    break
    
    print('WELCOME TO WHO WANTS TO BE A BILLIONAIRE. YOU HAVE ONLY 2 TRIALS,USE ALL AND YOU ARE OUT\n')
    RESPONSE1=input('Who won the 2017 NBA Championship? \na) Boston Celtics \t\tb) Detrot Pistons \nc) Golden State Warriors \td) Cleveland Cavaliers:\n===> ')
    if(RESPONSE1!='c'):
        trial-=1
        print('Wrong answer! You have',trial,' trials left')
        
    else:
            print("Correct answer! You've just won 1 Billion Naira!!")
            trial+=1
            
    RESPONSE2=input('Who won the 2017 NBA MVP finals? \na) Michael Jordan \tb) Kevin Durant \nc) Stephen Curry \td) Russell Westbrook: \n===>')
    if(RESPONSE2!="b"):
        print('Wrong answer! You have',trial,' trials left')
    else:
        print("Correct answer! You've just won 5 Billion Naira!!")
    RESPONSE3=input('Whats your name? \na)jide \tb)stanley \nc)lola \td)code: \n===> ')
    if (RESPONSE3 !="b"):
        trial-=1
        if(trial<=0):
            print('Wrong answer! You have',trial,' trials left')
    else:
        print("Correct answer! You've just won 7 Billion Naira!!")
    RESPONSE4=input('Whats year is this? \na)2071 \tb)20 17 \nc)2016 \td)2017: \n===> ')
    if (RESPONSE3 !="d"):
        trial-=1
        if(trial<=0):
            print('Wrong answer! You have',trial,' trials left')
    else:
        print("Correct answer! You've just won 10 Billion Naira!!")
        print('wish to see you again')   
