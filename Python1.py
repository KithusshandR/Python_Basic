''''
#Q1)

print("Kithusshand")
'''

'''
#Q2)

sum=0

for i in range (0,11,1):
    sum=sum+i
    print(sum)
'''

'''
#Q3)

x = int(input('Enter The Result: '))

if x<100 and x>74:
    print ("A")
elif x<75 and x>64:
    print ("B")
elif x<65 and x>49:
    print ("C")
elif x<50 and x>34:
    print ("S")
elif x<35:
    print ("F")
else:
    x<0
    print("Invalid Input")
'''

'''
#Q4)

for x in range (0,101,1):
    if x<101 and x>74:
        print ("A")
    elif x<75 and x>64:
        print ("B")
    elif x<65 and x>49:
        print ("C")
    elif x<50 and x>34:
        print ("S")
    elif x<35 and x>0:
        print ("F")
    else:
        print("Invalid Input")
'''

'''
#Q5)

for i in range (1,16,1):
    print("15*" + str(i) + "="+ str(15*i))
'''
'''
a=[]
sum=0
average=0;
for i in range (1,4,1):
    x =(int(input("Enter  Integer Number"+str(i)+":")))
    a.append(x)
    sum=sum+x
average=sum/len(a);
print(a)
print(average)
 '''   


'''
a=[]
for i in range (1,4,1):
    x = int(input("Enter Integer Number"+ " "+str(i)+":"))
    a.append(x)
print(a)
'''

'''
from array import array
a=array("H",[4000,20,700,22222])
sum (a) 
print (sum)
a[1:3]
'''

'''
#Q7)

x = int(input('Enter Week No: '))
y = int(input('Enter Day No: '))

if x>0 and y>0:
    for i in range (0,x,1):
        print("Week" + " " + str(i))
        for j in range (0,y,1):
            print(" " +"Day" + " " + str(j))
else:
    print("Invalid Input ")
'''




'''
#Q8)

x = int(input('Enter Week No: '))
if x>0:
    y = int(input('Enter Day No: '))

    if y>0:
            z = int(input('Enter Not Print Day No: '))
            if z<y:
                for i in range (1,x+1,1):
                    print("Week" + " " + str(i))
                    for j in range (1,y+1,1):
                        if j != z:
                            print(" " +"Day" + " " + str(j))
            else:
                print("Invalid Not Print Day No: ")
    else:
        print("Invalid Day ")
        
else:
    print("Invalid Week ")
'''    

