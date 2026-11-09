"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data
import math

# Part 1: vowel_count
def vowel_count(text: str) -> int:
    #Input: String, word in which vowels are counted
    #Output: Int, num of vowels in the string
    count = 0
    new_string = text.lower()
    for char in new_string:
        if ((char == "a") or (char == "e") or (char == "i") or (char == "o") or (char =="u")):
            count = count + 1
    return count


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    new_list = []
    for row in items:
        if len(row) == 2:
            new_list.append(row)
    return new_list

# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    new_list = []
    for row in items:
        if len(row) == 2:
            if row[1] < row[0]:
                new_list.append([row[1],row[0]])
            else:
                new_list.append(row)
        else:
            new_list.append(row)
    return new_list
               
   


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    dollars_1 = first.dollars
    cents_1 = first.cents
    dollars_2 = second.dollars
    cents_2 = second.cents
    new_dollars = dollars_1 + dollars_2
    new_cent = cents_1 + cents_2
    if (cents_1 + cents_2) <= 100:
        add_dollars = (cents_1 + cents_2)//100
        new_cent = (cents_1 + cents_2)%100
        new_dollars = new_dollars + add_dollars
    return(data.Price(new_dollars,new_cent))

# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    distance = abs(rectangle.top_left.x - rectangle.bottom_right.x)
    length = abs(rectangle.top_left.y - rectangle.bottom_right.y)
    area = distance * length
    return area

# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    result = []
    for book in books:
        if author in book.authors:
            result.append(book)
    return result

# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    half_width = (abs(rectangle.top_left.x - rectangle.bottom_right.x))/2
    half_height = (abs(rectangle.top_left.y - rectangle.bottom_right.y))/2
    center_x = half_width + rectangle.top_left.x
    center_y = half_height + rectangle.bottom_right.y
    distance_from_center = math.sqrt(((half_height)**2) + ((half_width)**2))
    new_circle = data.Circle(data.Point(center_x, center_y),distance_from_center)
    return new_circle

# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    if employees == []:
        return []
    total = 0
    num = 0
    for employee in employees:
        total = total + employee.pay_rate
        num = num + 1
    average= total/num
    list_names = []
    for employee in employees:
        if employee.pay_rate < average:
            list_names.append(employee.name)
    return list_names 