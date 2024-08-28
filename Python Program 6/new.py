import random
while True:
   print('='*67)
   print('*'*24,'Rolling The Dice','*'*25
         )
   print('='*67)
   n=random.randint(1,6)
   if n==6:
       print('****Congratulations**** you got a', n)
   elif n==1:
       print('Well tried but you got',n)
   else:
       print('You got ',n)
   ch=input('Roll Again ? (Y/N)')
   if ch in ('nN'):
      break
print('Thanks for Playing!!!!!!!!!!!!!!!!!!')