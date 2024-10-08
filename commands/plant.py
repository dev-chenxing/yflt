import re
import game
import commands.field as 田

name = "种"


def callback(args: list[str]):
    seed_plant_all = re.findall("^下全部(.+)", args[0])
    if seed_plant_all:
        item = game.get_object(name=seed_plant_all[0])
        for _ in range(game.get_item_count(item)):
            game.plant(seed=item, room=game.get_room(id="farm"))
    else:
        item = game.get_object(name=args[0])
        game.plant(seed=item, room=game.get_room(id="farm"))
    田.callback()
