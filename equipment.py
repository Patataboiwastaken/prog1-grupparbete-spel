
def equipped(player):
    equipment = [player.head, player.body, player.legs, player.right_hand, player.left_hand]
    
    total = 0
    for i in equipment:
        total += i.atk
    player.equipment_atk = total

    total = 0
    for i in equipment:
        total += i.hp
    player.equipment_hp = total

    total = 1
    for i in equipment:
        total *= i.dmg
    player.equipment_dmg = total

    player.atk = player.base_atk + player.equipment_atk
    player.hp  = player.base_hp + player.equipment_hp
    player.dmg = player.base_dmg * player.equipment_dmg
    return player

def inventory(player):
    while True:
        counter = 0
        print("--------------------------")
        print("Your items:")
        for x in player.inventory:
            print(f"{counter}. {x.name}")
            counter += 1

        print("\nto equip items, enter their number")
        print("to view equipped items, enter e")
        print("to exit inventory, press enter")
        inp=input()

        if inp=="":
            return player
        
        if inp == "e":
            print(f"Head: {player.head.name}")
            print(f"Body: {player.body.name}")
            print(f"Legs: {player.legs.name}")
            print(f"Right hand: {player.right_hand.name}")
            print(f"Left hand: {player.left_hand.name}")
            input("Press enter to continue")
        else:
            try:
                inp=int(inp)
            except:
                inp = ""

        if inp=="":
            print("invalid input, try again")
            
        elif not inp == "e":
            equipment = player.inventory.pop(inp)
            slot = equipment.slot
            if slot == "head":
                unequipped_item = player.head
                player.head = equipment
            if slot == "body":
                unequipped_item = player.body
                player.body = equipment
            if slot == "legs":
                unequipped_item = player.legs
                player.legs = equipment

            if slot == "hand":
                inp = ""
                while not (inp == "r" or "l"):
                    print("Enter r to equip in right hand or l to equip in left hand:")
                    inp = input()
                    if inp == "l":
                        unequipped_item = player.left_hand
                        player.left_hand = equipment
                    if inp == "r":
                        unequipped_item = player.right_hand
                        player.right_hand = equipment

            if not unequipped_item.name == "nothing":
                player.inventory.append(unequipped_item)