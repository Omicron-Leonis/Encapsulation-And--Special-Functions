class RomanConverter:
    def __init__(self):
        # Mapping of integers to Roman numerals
        self.value_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

    def int_to_roman(self, num):
        roman = ""
        for value, numeral in self.value_map:
            while num >= value:
                roman += numeral
                num -= value
        return roman


# Input from the user
try:
    number = int(input("Enter an integer to convert to Roman numeral: "))
    if number <= 0 or number > 3999:
        print("Please enter a number between 1 and 3999.")
    else:
        converter = RomanConverter()
        roman_numeral = converter.int_to_roman(number)
        print(f"The Roman numeral for {number} is: {roman_numeral}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
