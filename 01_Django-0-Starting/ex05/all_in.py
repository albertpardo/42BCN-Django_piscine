import sys

def get_capital_city(states, capital_cities, state_tolookfor):
    for key in states.keys():
        if key.lower() == state_tolookfor.lower():
            state = states[key]
            return capital_cities[state]
    return ""

def get_key_dict_from_value(dict_var, value_tolookfor):
    for key, value in dict_var.items():
        if value.lower() == value_tolookfor.lower():
            return key
    return ""

def get_state(states, capital_cities, capital_tolookfor):
    state_value = get_key_dict_from_value(capital_cities, capital_tolookfor)
    if state_value != "":
        return get_key_dict_from_value(states, state_value)
    return ""

def all_in(input_str):
    state = ""
    capital = ""
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    input_lst = input_str.split(",")
    for item in input_lst:
        item = item.strip()
        if item != "":
            state = get_state(states, capital_cities, item)
            capital = get_capital_city(states, capital_cities, item)
            if (state == "" and capital == "" ):
                print(item, "is neither a capital city nor a state")
            elif (state != "" and capital == "" ):
                capital = get_capital_city(states, capital_cities, state)
                print(capital , "is the capital of", state)
            elif (state == "" and capital != "" ):
                state = get_state(states, capital_cities, capital)
                print(capital , "is the capital of", state)
            else:
                print(" ERROR : No posible state!")

def main():
    args = sys.argv
    if len(args) == 2:
        all_in(args[1])

if __name__ == '__main__':
    main()
