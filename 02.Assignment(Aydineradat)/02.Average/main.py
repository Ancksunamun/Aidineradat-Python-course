print("average counter plz enter your numbers and (exit) for result ")
counter = 0
sum = 0
while True:
    number = input("Number: ")
    if number == "exit":
        break
    counter += 1 
    sum += int(number)
print (sum)
avg = sum / counter

print("The Average is : " , avg)