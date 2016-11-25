from ObjectOriented.AlienGame import Map
from ObjectOriented.AlienGame.central_corridor import CentralCorridor
from ObjectOriented.AlienGame.laser_weapon_armory import LaserWeaponArmory
from ObjectOriented.AlienGame.thebridge import TheBridge
from ObjectOriented.AlienGame.escape_pod import EscapePod
from ObjectOriented.AlienGame.death import Death
from ObjectOriented.AlienGame.finished import Finished
from ObjectOriented.AlienGame.engine import EngineX


class StartGame(Map):

    __scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def next_scene(self, scene_name):
        val = self.__scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = EngineX(a_map)
a_game.play()
