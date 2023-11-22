
# 1.
# def is_palindrome(s):
#     return s == s[::-1]
#
# # Example
# input_string = "radar"
# print(f"Is '{input_string}' a palindrome? {is_palindrome(input_string)}")

# 2.
# string1 = "Hello"
# string2 = "World"
# concatenated_string = string1 + " " + string2
# print("Concatenated String:", concatenated_string)

# 3.
# numbers = [1, 2, 3, 4, 5]
# sum_of_numbers = sum(numbers)
# print("Sum of Numbers:", sum_of_numbers)

# 4.
# original_list = [1, 2, 3, 4, 5]
# reversed_list = original_list[::-1]
# print("Reversed List:", reversed_list)

# 5.
# string_list = ["apple", "banana", "orange", "kiwi"]
# sorted_list = sorted(string_list)
# print("Sorted List:", sorted_list)

# 6.
# def remove_duplicates(input_list):
#     unique_list = []
#     for item in input_list:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list
#
# # Example
# duplicate_list = [1, 2, 2, 3, 4, 4, 5]
# result_list = remove_duplicates(duplicate_list)
# print("List with Duplicates:", duplicate_list)
# print("List without Duplicates:", result_list)

# 7.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2
#
# print(f"Addition: {addition}")
# print(f"Subtraction: {subtraction}")
# print(f"Multiplication: {multiplication}")
# print(f"Division: {division}")

# 8.
# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# # Example
# input_number = 7
# result = check_even_odd(input_number)
# print(f"{input_number} is {result}")

# 9.
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
# # Example
# input_year = 2024
# print(f"{input_year} is a leap year? {is_leap_year(input_year)}")

# 10.
# a = True
# b = False
#
# print("AND:", a and b)
# print("OR:", a or b)
# print("NOT a:", not a)
# print("NOT b:", not b)

# 11.
# numbers = [4, 7, 1, 9, 3]
# max_value = max(numbers)
# min_value = min(numbers)
# print("Max Value:", max_value)
# print("Min Value:", min_value)

# 12.
# import string
#
# def is_pangram(s):
#     alphabet_set = set(string.ascii_lowercase)
#     return set(s.lower()) >= alphabet_set
#
# # Example
# input_sentence = "The quick brown fox jumps over the lazy dog"
# print(f"Is '{input_sentence}' a pangram? {is_pangram(input_sentence)}")

# 13.
# sentence = "This is a sample sentence. This sentence has some words."
# word_list = sentence.split()
# word_count = {word: word_list.count(word) for word in set(word_list)}
# print("Word Count:", word_count)

# 14.
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# intersection = list(set(list1) & set(list2))
# print("Intersection of Lists:", intersection)

# 15.
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]
# result_dict = dict(zip(keys, values))
# print("Resulting Dictionary:", result_dict)

# 16.
# def are_elements_unique(input_list):
#     return len(input_list) == len(set(input_list))
#
# # Example
# unique_list = [1, 2, 3, 4, 5]
# non_unique_list = [1, 2, 2, 3, 4]
# print("Are elements in 'unique_list' unique?", are_elements_unique(unique_list))
# print("Are elements in 'non_unique_list' unique?", are_elements_unique(non_unique_list))

# 17.
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# merged_list = sorted(list1 + list2)
# print("Merged and Sorted List:", merged_list)

# 18.
# def rotate_list(input_list, positions):
#     return input_list[positions:] + input_list[:positions]
#
# # Example
# original_list = [1, 2, 3, 4, 5]
# rotated_list = rotate_list(original_list, 2)
# print("Original List:", original_list)
# print("Rotated List:", rotated_list)

# 19.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# # Example
# input_number = 5
# print(f"The factorial of {input_number} is: {factorial(input_number)}")

# 20.
# numbers = [5, 8, 2, 10, 7]
# sorted_numbers = sorted(numbers)
# second_largest = sorted_numbers[-2]
# print("Second Largest Element:", second_largest)



