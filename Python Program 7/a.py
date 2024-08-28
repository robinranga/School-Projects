Stack=[]
def Push(stk,elt):
    stk.append(elt)
    print('Element inserted')
    print(stk)
def Pop(stk):
    if isempty(stk):
        print('Stack is empty')
    else:
        pos=int(input('Enter index of element which you want to remove : '))
        print('Deleted element is : ',stk.pop(pos))
def Peek(stk):
    if isempty(stk):
        print('Stack is empty')
    else:
         print('Element at top of Stack  : ',stk[-1])       
def isempty(stk):
    if stk==[]:
        return True
    else:
        return False
def Display(stk):
    if isempty(stk):
        print('Stack is Empty')
    else:
        a=stk[::1]
        print(a)
while True:
    print('.......Stack Operations......')
    print('1.Push')
    print('2.Pop')
    print('3.Peek')
    print('4.Display')
    print('5.Exit')
    ch=int(input('Enter your choice : '))
    if ch==1:
        element=int(input('Enter the element which you want to Push  : '))
        Push(Stack,element)
    if ch==2:
        Pop(Stack)
    if ch==3:
        Peek(Stack)
    if ch==4:
        Display(Stack)
    elif ch==5:
        print('Exited')
        break
        

