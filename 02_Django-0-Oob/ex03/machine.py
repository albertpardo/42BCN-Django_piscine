import random
from beverage import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine():
    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(price = 0.90, name = "empty cup")

        def description(self):
            return ("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        self.limit_drinks = 10
        self.count_drinks = 0

    def repair(self):
        print("..... Fixing machine .....")
        self.count_drinks = 0
        print("Machine fixed!!!!")


    def serve(self, beverage = EmptyCup()):
        if self.count_drinks < self.limit_drinks:
            self.count_drinks += 1
            if (random.choice([True, False])):
                return beverage
            return self.EmptyCup()
        else:
            raise self.BrokenMachineException()


if __name__ == '__main__':

    def random_beverage():
        beverage_list = [HotBeverage, Coffee, Tea, Chocolate, Cappuccino]
        selected_beverage = random.choice(beverage_list)
        return selected_beverage()


    def test_ask_beverage(n):
        try:
            for i in range(1,12):
                selected = random_beverage()
                print(f"- Beverage number : {i} -> Selected: {selected.name}")
                print("-- Served Beverage info :")
                print(machine.serve(selected))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)

    machine = CoffeeMachine()
    test_ask_beverage(12)
    print("\n---------------------------")
    machine.repair()
    print("---------------------------\n")
    test_ask_beverage(12)
