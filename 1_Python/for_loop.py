data = [11, 22, 3, 33, 44, 55, 66, 77, 88, 99]

total_data = 0
for i in data:
    total_data += i
print(total_data)

# 
my_n = 88
for i in data:
    if my_n == i:
        print(f"Congratulation {i}! you ar lucky.")

# 
mounthly_cost = [11000, 22000, 23000, 33000, 44000, 55000, 66000, 77000, 88000]

total_cost = 0
for cost in range(len(mounthly_cost)):
    print(f"Month {cost + 1} Expense: {mounthly_cost[cost]}")
    total_cost += mounthly_cost[cost]
print(f"My Total Month is: {len(mounthly_cost)}, and Total Cost is: {total_cost}")


# 
building = ['a', 'b', 'c', 'd', 'e', 'f']

my_baby = 'd'
for baby in building:
    if my_baby == baby:
        print(f"Your baby location is: {baby}")
        
    elif my_baby != baby:
            continue
    


# 
building = ['a', 'b', 'c', 'd', 'e', 'f']

my_baby = 'd'
for baby in building:
    if my_baby == baby:
        print(f"Your baby location; bulding number, and bulding name {baby}")
    elif my_baby != baby:
        continue
    else:
        print("Sorry! apnar baby pai nai.")



