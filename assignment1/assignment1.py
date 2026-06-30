# Task 1
def hello():
    return "Hello!"


# Task 2
def greet(name):
    return f"Hello, {name}!"


# Task 3
def calc(a, b, op="multiply"):
    try:
        if op == "add":
            return a + b
        elif op == "subtract":
            return a - b
        elif op == "multiply":
            return a * b
        elif op == "divide":
            return a / b
        elif op == "modulo":
            return a % b
        elif op == "int_divide":
            return a // b
        elif op == "power":
            return a ** b
        else:
            return a * b

    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


# Task 4
def data_type_conversion(value, type_name):
    try:
        if type_name == "int":
            return int(value)
        elif type_name == "float":
            return float(value)
        elif type_name == "str":
            return str(value)

    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type_name}."
    

    # Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    except:
        return "Invalid data was provided."
    

    # Task 6
def repeat(text, count):
    result = ""
    for _ in range(count):
        result += text
    return result


# Task 7
def student_scores(mode, **kwargs):
    try:
        if mode == "mean":
            return sum(kwargs.values()) / len(kwargs)

        elif mode == "best":
            best_student = max(kwargs, key=kwargs.get)
            return best_student

    except:
        return "Invalid data was provided."
    

    # Task 8
def titleize(sentence):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}

    words = sentence.split()

    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in little_words:
            result.append(word)
        else:
            result.append(word.capitalize())

    return " ".join(result)


# Task 9
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result


# Task 10
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")

        elif word[:2] == "qu":
            result.append(word[2:] + "quay")

        else:
            # move leading consonants
            i = 0
            while i < len(word) and word[i] not in vowels:
                # handle "qu" inside consonants
                if word[i:i+2] == "qu":
                    i += 2
                    break
                i += 1

            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)