'''
There are 3 persons in a trading game
Player ---- Middle Man ----- Account Holder 
 70%          20%                10%
Account Holder = He will give his coc account to the middle man for making some profit. So, that he can upgrade his account  (The profit of only of coc resourses --> GOLD, ELIXER, DARK. He must have 80% of the account holder capacity

account holder capacity                         : 10,00,000
Amount to be paid by the account holder (80%)   : 8,00,000


So if the account holder has this much of virtual money in his account then his account is capable of REGISTERING 


Middle man  = He will provide the coc account of the Account Holder to the player. So that the player can play on the Account Holder base (by investing the {20% of the Account holder capacity})   and can make some profit out of it 

all the money are virtual


'''
# ACCOUNT HOLDER SIDE WORK
print('TRADEMILL.COM')
ahname=input('Enter the name of the Account Holder:- ')
ahcapacity=float(input('Enter the capacity of your Account:- '))
ahminamount=round((0.8*ahcapacity),2)
print(F'Min amount to have in your account is:- {ahminamount}')
ah_amount_have=float(input('Enter the amount you have right now in your account:- '))
if(ah_amount_have<ahminamount):
    diff=ahminamount-ah_amount_have
    print(f'You have to pay an amount of:- {diff}')
    print('''If you want to register your account. 
    So, that other people can play on your account. 
    And you make profit sitting in your home''')
else:
    print('Your accout fuilfill all the requirement to get REGISTERED ')
    print('''So, that other people can play on your account. 
And you make profit sitting in your home''')
    print('Do you want to register now')
    decision=input('Press Y for Yes and N for No:- ')
    if(decision=='Y' or decision=='y'):
        print('Oh thats Great!')
        print('***DISCLAMER:- You will get only (10% proft not loss on per attack) only if you agree with this statement then only you take decision for further legal works and official produre of registering your account  ')
    else:
        print('Ok Thank You. Visit Again')
        
i=input()
