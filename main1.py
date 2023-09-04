'''Assalamualaikum'''
def swg1():
  import random
  a=["Snake","Water","Gun"]
  computer = random.choice(a)
  c = input("\nWhat do you want to select ?\nInput 'S' for snake\nInput 'W' for water\nInput 'G' for gun\n:")
  user =(c.capitalize())
  d = "\nHehe! match drawn"
  e ="\nOops! You lost\ncomputeretter luck next time"
  f ="\nHurray! You won"
  pointswon =1000 
  pointslost = 0
  pointsdrawn=500
#   print(f'\ncomputer input : {computer}')
  # print(f'Your input     : {}')
  if (user =="S" or user =="W" or user =="G"):
    if (computer=="Snake"):
        if(user == "S"):
            print(f'\ncomputer input : {computer}')
            print(f'Your input     : Snake')
            print(d)
            print(f'\n Your score :{pointsdrawn}')
            from exit import exit 
            exit()
            
        if(user== "W"):
            print(f'\ncomputer input : {computer}')
            print(f'Your input     : Water')
            print(e)
            print(f'\n Your score :{pointslost}')
            print("\n\n")
            from exit import exit 
            exit()
        if (user =="G"):
            print(f'\ncomputer input : {computer}')
            print(f'Your input     : Gun')
            print(f)
            print(f'\n Your score :{pointswon}')
            from exit import exit
            exit()
            
    if (computer=="Water"):
        if(user == "S"):
            print(f'\ncomputer input : {computer}')
            print(f'Your input     : Snake')
            print(f)
            print(f'\n Your score :{pointswon}')
            from exit import exit 
            exit()
        if(user == "W"):
            print(f'\ncomputer input : {computer}')
            print(f'Your input     : Water')
            print(d)
            print(f'\n Your score :{pointsdrawn}')
            from exit import exit 
            exit()
        if (user =="G"):
            print(f'\ncomputer input : {computer}')
            print(f'Your input     : Gun')
            print(e)
            print(f'\n Your score :{pointslost}')
            from exit import exit 
            exit()
    if (computer=="Gun"):
        if(user == "S"):
            print(f'\ncomputer input : {computer}')
            print(f'Your input     : Snake')
            print(e)
            print(f'\n Your score :{pointslost}')
            from exit import exit
            exit()

        if(user == "W"):
            print(f'\ncomputer input : {computer}')
            print(f'Your input     : Water')
            print(f)
            print(f'\n Your score :{pointswon}')
            from exit import exit
            exit()
        if (user =="G"):
            print(f'\ncomputer input : {computer}')
            print(f'Your input     : Gun')
            print(d)
            print(f'\n Your score :{pointsdrawn}')
            from exit import exit
            exit()
  else :
        print("Please input properly")
        from main1 import swg1
        swg1()

