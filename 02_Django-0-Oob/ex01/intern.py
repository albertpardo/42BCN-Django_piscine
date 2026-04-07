class Intern():
    def __init__(self, name = "My name? I’m nobody, an intern, I have no name."):
        self.name = name 

    def __str__(self):
        return self.name

    def work(self):
       raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()

    class Coffee():
        def __str__(self):
            return "This is the worst coffee you ever tasted."

if __name__ == '__main__':
    # Test "Intern" whithout name
    intern_one = Intern()
    print(f"What is your name \"intern_one\"?\n  - {intern_one}")
    print()

    # Test "Intern" whit name = "Mark"
    intern_two = Intern("Mark")
    print(f"What is your name \"intern_two\"?\n  - {intern_two}")
    print()

    # Test "Intern" with name "Mark" to make a coffee
    print(f"You say : {intern_two}, can you get me a coffee, please?")
    print(f"{intern_two} says : {intern_two.make_coffee()}")
    print()
    
    # Test "Intern" without name to work
    try:
        print("You say : Hey, do you have a moment to help with this task?")
        print(f"intern_one says : ")
        print(f"{intern_one.work()}")
    except Exception as e :
        print(e)

    # Test "Mark" to work
    try:
        print(f"\nYou say : Hey {intern_two} , do you have a moment to help with this task?")
        print(f"{intern_two} says:")
        print(f"{intern_two.work()}")
    except Exception as e :
        print(e)

