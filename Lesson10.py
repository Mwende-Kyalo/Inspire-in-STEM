#fav_food list
mary_fav_food = ['beef','chicken','vegetable']
jane_fav_food = ['rice','ugali','potato']

#dictionary containing the above
food={
    'Mary ': ['beef','chicken','vegetable'],
    'Jane ': ['rice','ugali','potato'],
}

for key, value in food.items():
    print(f"{key}:{ value}") 
