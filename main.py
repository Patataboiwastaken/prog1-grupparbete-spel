import items
import game_map
import equipment
import text
class player:
    map_icon = "P"
    name = "player"
    entity_type = "player"
    x = 1
    y = 1
    base_atk =1.0
    base_hp = 10.0
    base_dmg = 1.0
    equipment_atk = 0
    equipment_hp = 0
    equipment_dmg = 0
    atk = 0
    hp = 10
    dmg = 1
    inventory = []
    consumeables =[]
    head = items.nothing
    body = items.nothing
    legs = items.nothing
    right_hand = items.short_sword
    left_hand = items.nothing

if __name__ == "__main__":
    text.welcome_func()
    karta = game_map.map_list[0]
    while True:
        game_map.print_map(karta)

        action = input("input: ").lower()
        if action == "w" or action == "a" or action == "s" or action == "d":
            karta, player = game_map.move(karta, action, player)
        if action == "help":
            text.controls()
        if action == "e":
            equipment.inventory(player)
        if action == "c":
            equipment.consumeables(player)
        if action == "l":
            text.legend()
   