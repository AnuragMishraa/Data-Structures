
#this function deals with adding an element to the stack in FIFO format.
def push(stk,ele):

    top=len(stk)-1 #index of last element in the stack.
    
    stk.append(ele)  #inserts the element at the end of the stack.
    print(ele,"is successfully pushed to the Stack!!!") 



#this function deals with removing an element from the stack in FIFO format.
def pop(stk):

    if isempty(stk):
        print("Stack is empty --> Underflow")
    
    else:
        top=len(stk)-1 #index of last element in the stack.

        item=stk.pop(top) #removes the last element of the stack.
        print("the poped item is:",item)



#this function deals with displaying the stack contents in FIFO format.
def display(stk):

    if isempty(stk):
        print("Stack is empty --> Underflow")

    else:
        top=len(stk)-1 #index of last element in the stack.

        print(stk[top],"<--TOP") #prints the last elemnent of the stack.

        for i in range(top-1,-1,-1):
            print(stk[i]) #prints the coresponding elememt of the stack.



#this function checks the stack is empty or not.
def isempty(stk):
    if len(stk)==0: #checks the length to be zero.
        return 1
    else:
        return 0



#___main___
stk=[] #Creates the stack for implementation


while 1:

    #prints the choice for the user.
    print("---------------------------------------------------WELCOME TO STACK IMPLEMENTATION------------------------------------------------------")
    print("Please enter your choice:")
    print("1) PUSH")
    print("2) POP")
    print("3) DISPLAY")
    print("4) EXIT")

    ch=int(input()) #accepts user input choice

    #checks for the correct choice and implement user demand for the choice.
    if ch==1:
        ele=input("Please enter an element to be inserted:") #takes input for the element to be pushed in the stack.
        push(stk,ele)
        
    elif ch==2:
        pop(stk)

    elif ch==3:
        display(stk)

    elif ch==4:
        print("--------------------------THANKYOU FOR USING MY STACK IMPLEMENTATION-------------------------------")
        break #breaks the loop for choice.

    else:
        print("Please enter a valid choice (1-4)")
