import string, random, argparse
combined = [x for x in string.ascii_lowercase[:26]]
upper_case = [x for x in string.ascii_uppercase[:26]]
numbers = [str(x) for x in range(0,10)]
symbols = [x for x in string.punctuation]
combined.extend(upper_case)
combined.extend(numbers)
combined.extend(symbols)
def find_consecutive_values(lst):
    indices = []
    for i in range(len(lst) - 2):
        if (ord('a') <= ord(lst[i].lower()) <= ord('z') and
            ord(lst[i].lower()) + 1 == ord(lst[i+1].lower()) == ord(lst[i+2].lower()) - 1) or \
           (ord('0') <= ord(lst[i]) <= ord('9') and
            ord(lst[i]) + 1 == ord(lst[i+1]) == ord(lst[i+2]) - 1):
            indices.append(i+1)
    return indices
def ensure_elements(lst, combined):
    def categorize_characters(char_set):
        lower_case = set()
        upper_case = set()
        numbers = set()
        symbols = set()

        for char in char_set:
            if char.islower():
                lower_case.add(char)
            elif char.isupper():
                upper_case.add(char)
            elif char.isdigit():
                numbers.add(char)
            else:
                symbols.add(char)

        return lower_case, upper_case, numbers, symbols
    lower_case, upper_case, numbers, symbols = categorize_characters(combined)
    sets = {
        'lower': lower_case,
        'upper': upper_case,
        'digit': numbers,
        'symbol': symbols
    }
    def check_categories(char_list):
        missing_sets = []

        has_integer = False
        has_lowercase = False
        has_uppercase = False
        has_symbol = False

        for char in char_list:
            if char.isdigit():
                has_integer = True
            elif char.islower():
                has_lowercase = True
            elif char.isupper():
                has_uppercase = True
            else:
                has_symbol = True

        if not has_integer:
            missing_sets.append("digit")
        if not has_lowercase:
            missing_sets.append("lower")
        if not has_uppercase:
            missing_sets.append("upper")
        if not has_symbol:
            missing_sets.append("symbol")

        return missing_sets

    while True:
        missing_sets = check_categories(lst)
        print(missing_sets)
        if not missing_sets:
            break

        # Randomly select a set from which to add a character
        set_name = missing_sets[0]
        char = random.choice(list(sets[set_name]))

        # Randomly insert the character and record the index
        index = random.randint(0, len(lst))
        lst.insert(index, char)

        # Randomly delete a character not at the recorded index
        del_index = random.choice([i for i in range(len(lst)) if i != index])
        del lst[del_index]
        missing_sets.pop(0)
    return lst
def generate_password(pass_length,combined):
    temp_set = set()
    current = 0
    _try = 1
    password = []
    previous_rando = ""
    place_holding = []
    while current != pass_length:
        some_rando = random.choice(combined)
        temp_set.add(some_rando)
        place_holding.append(some_rando)
        combined.remove(some_rando)
        if len(place_holding) == 5:
            combined.append(place_holding.pop(0))
        if some_rando == previous_rando:
            _try += 1
            if _try == 3:
                continue
        else:
            _try = 1
        password.append(some_rando)
        current+=1
        previous_rando = some_rando
    return password, temp_set
parser = argparse.ArgumentParser(description='Process pass_length input')

# Add the arguments
parser.add_argument('pass_length', type=int, help='The length of the password')

# Parse the arguments
args = parser.parse_args()
pass_length = args.pass_length
if pass_length < 8:
    raise argparse.ArgumentTypeError("An invalid pass_length! It must be equal to or more than 8.")
elif pass_length > 50:
    raise argparse.ArgumentTypeError("An invalid pass_length! It cannot be more than 50.")
password, temp_set = generate_password(pass_length,combined)
for x in temp_set:
    try:
        combined.remove(x)
    except:
        pass
for x in password:
    print(x,end="")
print()
password = ensure_elements(password, combined)
consec_values = find_consecutive_values(password)
if consec_values != []:
    for x in consec_values:
        combined.remove(password[x])
for x in consec_values:
    password[x] = random.choice(combined)
for x in password:
    print(x,end="")
print()
