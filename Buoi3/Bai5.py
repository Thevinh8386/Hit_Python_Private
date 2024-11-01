m = int(input())
animals = []
food = []

total_food = 0
top_eater = None
max_food = 0
lowest_eater_index = "Không có"
min_food = 5

for i in range(m):
    animals.append(input())
for i in range(m):
    food.append(int(input()))

daily_descriptions = []
for i in range(m):
    daily_descriptions.append((animals[i],food[i]))

for i in range(m):
    if food[i] >= 5:
        total_food += food[i]
        if food[i] > 100:
            break

for i in range(m):
    if food[i] < min_food:
        min_food = food[i]
        lowest_eater_index = i
    if food[i] > max_food:
        max_food = food[i]
        top_eater = animals[i]

print(daily_descriptions)
print(total_food)
print(top_eater)
print(lowest_eater_index)




