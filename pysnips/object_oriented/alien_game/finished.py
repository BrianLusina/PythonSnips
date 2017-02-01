from ObjectOriented.AlienGame import Scene


class Finished(Scene):

    @staticmethod
    def enter():
        print("You won! Good job.")
        return 'finished'
