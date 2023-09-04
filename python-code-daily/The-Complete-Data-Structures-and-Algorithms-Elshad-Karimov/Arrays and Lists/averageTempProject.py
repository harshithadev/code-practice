# this program gets a user input for number of days and then gets their respective high temperatures.
# After which it calculates the average and also gives out a count of the number of days it has been over the average temperature.

days = int(input("Enter the number of days you wanna track : "))
temps = []
for i in range(days):
    temps.append(int(
        # input("Enter the highest temperature of day "+str(i+1)+" : ")))
        input("Enter the temp of the {} day ".format(i+1))))
avg = sum(temps)/len(temps)
print("Average of the temperatures observed is :", avg)
print("The number of days with temperature over avgerage temperature is :", len(
    [t for t in temps if t > avg]))
