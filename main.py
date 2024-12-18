def calculate_love(name1, name2):
    combined_name = name1.lower() + name2.lower()

    score = 0
    for char in combined_name:
        score += ord(char)

    love_percentage = score % 101

    return love_percentage


name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

love_percentage = calculate_love(name1, name2)
print(f"The love percentage between {name1} and {name2} is: {love_percentage}%")