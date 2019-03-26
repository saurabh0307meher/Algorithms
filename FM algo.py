x = [1,3,2,1,2,3,4,3,1,2,3,1]
a = []
maxx = 0
for i in x:
    h = (6*i + 1) % 5   #Hash Function
    a.append(h)         #Appending the Values to Empty list a[]
            
print("The Original list",x)    #[1, 3, 2, 1, 2, 3, 4, 3, 1, 2, 3, 1]
print("The Hash Fnc list",a)    #[2, 4, 3, 2, 3, 4, 0, 4, 2, 3, 4, 2]
print(len(a))

#Function to convert the elemnts of a[] to Binary digits
for x in a:
    count = 0
    z = []
    num = x
    while(x>0):
        rem = x%2
        x = x // 2
        z.append(rem)
        
    print("\n The binary value of ",num, "is", z)
    for m in z:
        if(m==0):
            count = count + 1
            print("The count is ", count)
        if(maxx < count):
            maxx = count
            print("The max is", maxx)
            

print(" The FM is ", 2**maxx)
    

    



