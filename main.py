# Food list example
foodlist = {
    "Turkey": 1,
    "Cranberry sauce": 2,
    "Gravy": 3,
    "Pumpkin Pie": 2,
    "Sweet potato marshmallow": 3,
    "Apple pie": 5,
    "Cornbread dressing": 4,
    "Stuffing": 2,
    "Bread roll": 4,
}

print("Food Items:")
for item, quantity in foodlist.items():
    print(f"We need {quantity} of {item}.")

# Hanukkah gifts example
hklist = {
    "day 1": ["Playstation 5"],
    "day 2": ["Watch", "Toy"],
    "day 3": ["Necklace", "Money", "Jacket"],
    "day 4": ["TV", "Car", "Clothes", "Gift card"],
    "day 5": ["Headphones", "Bracelet", "Ring", "Candy", "Flowers"],
    "day 6": ["Xbox", "Nintendo Switch", "Computer", "Mouse", "Keyboard", "PC"],
    "day 7": ["Mac", "Surface"],
    "day 8": ["Surprise Gift"]
}

print("\nHanukkah Gifts:")
for day, gifts in hklist.items():
    print(f"{day}:")
    for gift in gifts:
        print(f"  - {gift}")


# 12 Days of Christmas gifts example
christmas_gifts = {
    "1st": ["A Partridge in a Pear Tree"],
    "2nd": ["Two Turtle Doves", "And a Partridge in a Pear Tree"],
    "3rd": ["Three French Hens", "Two Turtle Doves", "And a Partridge in a Pear Tree"],
    "4th": ["Four Calling Birds", "Three French Hens", "Two Turtle Doves", "And a Partridge in a Pear Tree"],
    "5th": ["Five Golden Rings", "Four Calling Birds", "Three French Hens", "Two Turtle Doves", "And a Partridge in a Pear Tree"],
    "6th": ["Six Geese a-Laying", "Five Golden Rings", "Four Calling Birds", "Three French Hens", "Two Turtle Doves", "And a Partridge in a Pear Tree"],
    "7th": ["Seven Swans a-Swimming", "Six Geese a-Laying", "Five Golden Rings", "Four Calling Birds", "Three French Hens", "Two Turtle Doves", "And a Partridge in a Pear Tree"],
    "8th": ["Eight Maids a-Milking", "Seven Swans a-Swimming", "Six Geese a-Laying", "Five Golden Rings", "Four Calling Birds", "Three French Hens", "Two Turtle Doves", "And a Partridge in a Pear Tree"],
    "9th": ["Nine Ladies Dancing", "Eight Maids a-Milking", "Seven Swans a-Swimming", "Six Geese a-Laying", "Five Golden Rings", "Four Calling Birds", "Three French Hens", "Two Turtle Doves", "And a Partridge in a Pear Tree"],
    "10th": ["Ten Lords a-Leaping", "Nine Ladies Dancing", "Eight Maids a-Milking", "Seven Swans a-Swimming", "Six Geese a-Laying", "Five Golden Rings", "Four Calling Birds", "Three French Hens", "Two Turtle Doves", "And a Partridge in a Pear Tree"],
    "11th": ["Eleven Pipers Piping", "Ten Lords a-Leaping", "Nine Ladies Dancing", "Eight Maids a-Milking", "Seven Swans a-Swimming", "Six Geese a-Laying", "Five Golden Rings", "Four Calling Birds", "Three French Hens", "Two Turtle Doves", "And a Partridge in a Pear Tree"],
    "12th": ["Twelve Drummers Drumming", "Eleven Pipers Piping", "Ten Lords a-Leaping", "Nine Ladies Dancing", "Eight Maids a-Milking", "Seven Swans a-Swimming", "Six Geese a-Laying", "Five Golden Rings", "Four Calling Birds", "Three French Hens", "Two Turtle Doves", "And a Partridge in a Pear Tree"]
}

# Print the song lyrics
for day, gifts in christmas_gifts.items():
    print(f"On the {day} day of Christmas my true love gave to me:")
    for gift in gifts:
        print(f"  - {gift}")
    print()  # Add a blank line between days
