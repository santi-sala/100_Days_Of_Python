# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Julia", "Spain")

greet_with(location = "Catalunya", name = "Pipo")


def calculate_love_score(first_name, second_name):
    names = (first_name + second_name).lower()
    true_score = calculate_true(names, "true")
    love_score = calculate_true(names, "love")
    final_score = str(true_score) + str(love_score)
    print(final_score)


def calculate_true(name, word):
    score = 0
    for first_character in name:
        for second_character in word:
            if first_character == second_character:
                score += 1
    return score


calculate_love_score("santi", "pia")
