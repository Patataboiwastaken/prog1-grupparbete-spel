#alla saker man ser på kartan (förutom spelaren) är klasser som defineras här
class wall:
    name = "wall"
    map_icon = "#"
    entity_type = "wall"

class empty_tile:
    name = "empty_tile"
    map_icon = " "
    entity_type = "empty_tile"

class trapdoor:
    name = "trapdoor"
    map_icon = "T"
    entity_type = "trapdoor"

class chest1:
    name = "1"
    map_icon = "S"
    entity_type = "chest"

class chest2:
    name = "2"
    map_icon = "S"
    entity_type = "chest"

class chest3:
    name = "3"
    map_icon = "S"
    entity_type = "chest"

class goblin:
    name = "goblin"
    map_icon = "g"
    entity_type = "enemy"
    hp = 10
    atk = 3
    dmg = 1
    loot = []

class orc:
    name = "orc"
    map_icon = "o"
    entity_type = "enemy"
    hp = 20
    atk = 1
    dmg = 0.85
    loot = []

class zombie:
    name = "zombie"
    map_icon = "z"
    entity_type = "enemy"
    hp = 15
    atk = 0.5
    dmg = 0.95
    loot = []

class skeleton:
    name = "skeleton"
    map_icon = "s"
    entity_type = "enemy"
    hp = 10
    atk = 1
    dmg = 1
    loot = []

class rat:
    name = "rat"
    map_icon = "r"
    entity_type = "enemy"
    hp = 5
    atk = 1
    dmg = 1
    loot = []

class troll:
    name = "troll"
    map_icon = "t"
    entity_type = "enemy"
    hp = 50
    atk = 5
    dmg = 0.75
    loot = []
class lich:
    name = "lich"
    map_icon = "l"
    entity_type = "enemy"
    hp = 40
    atk = 15
    dmg = 2
    loot = []

#denna klassen behövs eftersom att man inte kan importera player till game_map
class player_placeholder:
    name = "player_placeholder"
    map_icon = "P"
    entity_type = "misc"

#lista för att map_creator ska fungera
list_of_entity_types = [wall, empty_tile, goblin, orc, zombie, skeleton, rat, troll, player_placeholder, trapdoor, chest1, chest2, chest3, lich]