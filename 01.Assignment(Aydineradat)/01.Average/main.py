print("We calculate average of yuor 3 scores and give our opnion")

a = int(input("Plz enter your first grade:"))
b = int(input("Plz enter your seconed grade"))
c = int(input("Plz enter your third score"))

avg = ( a + b + c) / 3 

if avg >= 17:
    print (avg , "Great")
elif 17 > avg >= 12:
    print (avg , not bad)
elif 12 > avg :
    print(avg , "Body you should reconsider your education")
