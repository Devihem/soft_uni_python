starting_letter = int(input())

for first_letter in range(97, 97 + starting_letter):
    for second_letter in range(97, 97 + starting_letter):
        for third_letter in range(97, 97 + starting_letter):
            print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}")
