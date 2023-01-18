from originator import Originator
from caretaker import Caretaker

if __name__ == "__main__":
    originator = Originator("Whoop!")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more with feeling!\n")
    caretaker.undo()
