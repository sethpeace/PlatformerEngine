from PlatformerEngine.sprites import Tile


class Grass(Tile):
    def __init__(self, *args, **kwargs):
        super().__init__("grass", *args, **kwargs)
