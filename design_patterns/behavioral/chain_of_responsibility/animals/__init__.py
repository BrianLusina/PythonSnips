from handler import Handler
from monkey_handler import MonkeyHandler
from squirrel_handler import SquirrelHandler
from dog_handler import DogHandler


def client(hdlr: Handler) -> None:
    """
    The client is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    @param hdlr: Handler
    """

    foods = ["Nut", "MeatBall", "Cup of Coffee", "Banana"]

    for food in foods:
        print(f"\nClient: Who wants {food}?")
        result = hdlr.handle(food)
        if result:
            print(f"\t{result}", end="")
        else:
            print(f"\t{food} was left untouched", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog\n")
    client(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client(squirrel)
