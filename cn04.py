import sys
#creating a dictionary with items and corresponding colours
mydata={"banana":["green","yellow"],"ink":["red","black"],"salt":["white"],"frog":["blue","yellow"],"blood":["red"],"sky":["blue","black"],"apple":["red","green"]}
#all the colors usable
color=["green","yellow","red","white","black","blue"]
#list of subscribed items
myitems=[]

#game is designed based on subscriber-publisher design pattern
def subscribe(st):
    if st in mydata.keys():
        myitems.append(st)
        print("subscribed "+st)
    else:
        print("Can't be subscribed")
def unsubscribe(st):
    if st in myitems:
        myitems.remove(st)
        print("unsubscribed "+st)
    else:
        print("can't unsubscribe")

#displaying items for entered color
def show(st):
    if st in color:
        for i in myitems:
            if len(mydata[i])>1 and st in mydata[i]:
                if i!="frog":
                    print("I'm "+i+" and i am sometimes "+st)
                else:
                    print("I'm frog and i am "+st+" today")
            elif st in mydata[i]:
                print("I'm "+i+" and i am always "+st)
    else:
        print("invalid input")

#taking user's choice
def main():
    print("--Welcome to color game--Type 'exit' to stop..")
    while(True):
        n=str(input())
        if n[0]=="+":
            subscribe(n[1:])
        elif n[0]=="-":
            unsubscribe(n[1:])
        elif n=="list":
            print(myitems)
        elif n=="exit":
            break
        else:
            show(n)
if __name__ == "__main__":
    main()       
 