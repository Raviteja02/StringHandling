fno = input("Enter First Number : ")
lno = input("Enter Last Number : ")

sum = fno + lno

print ("Sum Of values is : ", sum)  # The output is 100200 because input function reads data stream as string class objecs,
                                    # so that we have to convert string class object into required class object using Type Convervesion Methods.


print(type(fno))
print(type(lno))

b = int(fno)
print(type(b))

c = int(lno)
print(type(c))

d = b + c

print ("Sum Of values is : ", d)
                                    # In another way...
first=int(input("Enter First Number : "))
second=int(input("Enter seconf number : "))

total = first + second

print(total)



