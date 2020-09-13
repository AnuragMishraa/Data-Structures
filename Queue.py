
#this function deals with inserting an element into the Queue
def enqueue(que,ele):

    if isempty(que):
        front=0 #declares front and rear to be zero in the first time of enqueue
        rear=0

    else:
        rear=len(que)-1

    que.append(ele)
    rear+=1
    print(ele,"is inserted sucessfully!!!")


#this function deals with removing an element from the Queue
def dequeue(que):

    if isempty(que):
        print("Queue is empty--> Underflow")

    else:
        front=0

        item=que.pop(front)
        print("the item dequeued is:",item)


#this function displays the queue in LIFO format.
def display(que):

    if isempty(que):
        print("Queue is empty--> Underflow")

    else:
        front=0
        rear=len(que)-1

        print(que[front],"<--FRONT")

        for i in range(front+1,rear,1):
            print(que[i])

        print(que[rear],"<--REAR")


#this function checks the is empty or not.
def isempty(que):

    if len(que)==0:
        return 1

    else:
        return 0





#___main__
que=[]

front=rear=None

while 1:

    print("---------------------------------------------------WELCOME TO QUEUE IMPLEMENTATION------------------------------------------------------")
    print("Please enter your choice:")
    print("1) ENQUEUE")
    print("2) DEQUEUE")
    print("3) DISPLAY")
    print("4) EXIT")


    ch=int(input()) #accepts user input choice

    #checks for the correct choice and implement user demand for the choice.
    if ch==1:

        ele=input("Please enter an element to be inserted:") #takes input for the element to be inserted in the queue.
        enqueue(que,ele)
        
    elif ch==2:
        dequeue(que)

    elif ch==3:
        display(que)

    elif ch==4:

        print("--------------------------THANKYOU FOR USING MY QUEUE IMPLEMENTATION-------------------------------")
        break #breaks the loop for choice.

    else:

        print("Please enter a valid choice (1-4)")



