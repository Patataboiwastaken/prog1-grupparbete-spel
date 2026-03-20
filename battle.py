from equipment import inventory
from equipment import equipped
from text import death

def use_item(item, monster, player, enemy_hp):
    if item.name == "bomb":
        enemy_hp -= 10
    if item.name == "health potion":
        player.hp += 10
    if item.name == "strenght potion":
        player.atk += 10
    if item.name == "fortitude potion":
        player.dmg *= 0.5
    return(monster, player, enemy_hp)

def start_battle(monster, player):
    #sparar i variabel så att det inte förs över mellan strider
    enemy_hp = monster.hp

    player = equipped(player)
    print(f"\nyou have encountered a {monster.name}")
    while True:
        #välj vad du ska göra
        print(f"your have: {player.hp} health")
        print(f"the monster has: {int(enemy_hp)} health")
        player_action=input("what do you do?\n1:attack \n2:defend \n3:item \n4:flee\n")

        if player_action=="attack" or player_action=="1":
            enemy_hp -= monster.dmg*player.atk    

        if player_action=="defend" or player_action=="2":
            player.dmg *= 0.5
        
        if player_action=="item" or player_action=="3":
            done_with_items = False
            while not done_with_items:
                counter = 0
                print("Your items:")
                for x in player.consumeables:
                    print(f"{counter}. {x.name}")
                    print(f"    {x.description}")
                    counter += 1
                print("")
                print("To use item: enter their number")
                print("To continue the fight: click enter")
                used_item=input(f"input: ")
                
                try: 
                    used_item = int(used_item)
                    used_item = player.consumeables.pop(used_item)
                    #player.consumeables[used_item]
                    monster, player, enemy_hp = use_item(used_item, monster, player, enemy_hp)
                except ValueError:
                    if used_item == "":
                        done_with_items = True
                    else:
                        print("Error: You have no consumeable with that number")
                except TypeError:
                    print("Error: Not a number")
                
                print("--------------------------")
                if enemy_hp <= 0:
                    done_with_items = True
                    print("The monster dies")
                    input("Click enter to continue")
        
        #fiende anfaller ifall inte använde item
        if not(player_action=="item" or player_action=="3"):
            player.hp -= player.dmg*monster.atk
        if player.hp <= 0:
            death()

        if player_action == "flee" or player_action == "4":
            return(False, player)
    
        if enemy_hp <= 0:
            print("you win!")
            for item in monster.loot:
                if item.item_type == "equipment":
                    player.inventory.append(item)
                if item.item_type == "consumable":
                    player.consumeables.append(item)
           
            return(True, player)