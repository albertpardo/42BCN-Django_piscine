import sys

def get_key_dict_from_value(dict_var, value_tolookfor):
    for key, value in dict_var.items():
        if value == value_tolookfor:
            return key
    return ""

def get_state(capital_tolookfor):

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

    state_value = get_key_dict_from_value(capital_cities, capital_tolookfor)
    if state_value == "":
        return "Unkown capital city"
    return get_key_dict_from_value(states, state_value) 

def state(capital):
    state_found = get_state(capital)
    print(state_found)

def main():
    args = sys.argv
    if len(args) == 2:
        state(args[1])

if __name__ == '__main__':
    main()
