words = ["Apple", "Banana", "Avocado", "Cherry"]
new_li = [word for word in words if word.startswith("A")]
print(new_li)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO: Create a new list called 'even_numbers' that only contains the even numbers.
# Hint: A number is even if (number % 2 == 0)

even_numbers = [even_num for even_num in numbers if even_num%2 == 0]
print(even_numbers)

fruits = ["Apple", "Banana", "Cherry"]

# 'i' catches the index number, 'fruit' catches the actual item
for i, fruit in enumerate(fruits):
    print(f"Index {i} is {fruit}")


database = [
    {"roll_no": 101, "name": "Amit"},
    {"roll_no": 102, "name": "Priya"},
    {"roll_no": 103, "name": "Rahul"}
]

target_roll_no = 103

# TODO: Write a 'for' loop using enumerate() to loop through the database.
# Inside the loop, check IF the dictionary's "roll_no" matches the target_roll_no.
# If it does, print: "Found Rahul at index X!" (replace X with the actual index number).


for index , value in enumerate(database):
    if value["roll_no"] == target_roll_no:
        print(f"{value["name"] }found at index {index}")