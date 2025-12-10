# ============================
# Part 1 — Basic Function Arguments
# ============================

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} and its name is {pet_name}.")

# Calling the function three times
describe_pet("dog", "Buddy")
describe_pet("cat", "Milo")
describe_pet("hamster", "Peanut")


# ============================
# Part 2 — Positional vs Keyword Arguments
# ============================

# Positional arguments
describe_pet("dog", "Buddy")

# Keyword arguments (reversed order)
describe_pet(pet_name="Milo", animal_type="cat")


# ============================
# Part 3 — Default Arguments
# ============================

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} and its name is {pet_name}.")

# Calls
describe_pet("Brownie")                 # uses default animal_type
describe_pet("Nugget", "chicken")       # overrides default


# ============================
# Part 4 — Create Your Own Function
# ============================

def order_drink(drink, size="medium", iced=False):
    # iced = True → "iced", else "hot"
    ice_state = "iced" if iced else "hot"
    return f"Your order: {size} {ice_state} {drink}"

# Orders
print(order_drink("coffee"))                        # default drink
print(order_drink("chocolate", size="large"))       # large hot chocolate
print(order_drink("milk tea", size="small", iced=True))  # small iced milk tea


# ============================
# Part 5 — Mini Challenge (Calculator)
# ============================

def compute(operation, num1, num2=1):
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"

# Tasks
print(compute("add", 5, 10))
print(compute("multiply", num1=3, num2=4))
print(compute("subtract", 20))       # uses default num2 = 1
print(compute("divide", 10, 2))      # invalid operation
