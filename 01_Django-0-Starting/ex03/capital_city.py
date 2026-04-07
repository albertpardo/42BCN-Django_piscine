import sys

def get_capital_city(state_tolookfor):

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

    if state_tolookfor in states:
        state = states[state_tolookfor]
        return capital_cities[state]
    return "Unkown state"

def capital_city(state):
    capital = get_capital_city(state)
    print(capital)

def main():
    args = sys.argv
    if len(args) == 2:
        capital_city(args[1])

if __name__ == '__main__':
    main()
