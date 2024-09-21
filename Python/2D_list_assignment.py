data=[["January",6,3],["February",7,3],["March",10,4],["April",13,6],["May",17,9],["June",20,12],["July",22,14],["August",21,14],["September",19,12],["October",14,9],["November",10,6],["December",7,3]]
#key=lambda x: x[1]: This specifies the sorting should be based on the second element (index 1, which is the maximum temperature) in each sublist.
sorted_data= sorted(data, key=lambda x: x[1], reverse=True)
print("Six month with highest Temperatur: ")
for i in range(6):
    #The formatting (:<10, :<5) ensures the output is aligned by setting the width for each column (10 characters for the month and 5 characters for the temperatures).
    print(f"{sorted_data[i][0]:<10} { sorted_data[i][1]:<5} {sorted_data[i][2]:<5}")
print("\nMonths with minimum temperature below 9:")
for month in data:
    #if month[2] < 9: This checks if the minimum temperature (index 2) is below 9
    if month[2] < 9:
        print(f"{month[0]:<10} {month[1]:<5} {month[2]:<5}")
print("\nMonths with maximum temperature 20 or above:")
#if month[1] >= 20: This checks if the maximum temperature (index 1) is greater than or equal to 20.
for month in data:
    if month[1] >= 20:
        print(f"{month[0]}{month[1]:<5} {month[2]:<5}")        