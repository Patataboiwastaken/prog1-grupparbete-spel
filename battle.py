from equipment import inventory
from equipment import equipped
from text import death

def start_battle(monster, player):
    #sparar i variabel så att det inte förs över mellan strider
    enemy_hp = monster.hp

    player = equipped(player)
    print(f"\nyou have encountered a {monster.name}")
    while True:
        #välj vad du ska göra
        print(f"your have: {player.hp} health")
        print(f"the monster has: {enemy_hp} health")
        player_action=input("what do you do?\n1:attack \n2:defend \n3:item(WIP) \n4:flee\n")

        if player_action=="attack" or player_action=="1":
            enemy_hp -= monster.dmg*player.atk    

        if player_action=="defend" or player_action=="2":
            player.dmg *= 0.5
        
        if player_action=="item" or player_action=="3":
            used_item=input(f"input item you wish to use:\n{player.inventory}")
            
            try: 
                used_item=int(used_item)
                inventory(player)
            
            except:
                for x in player.inventory:
                    if x == used_item:
                        item(used_item)
        
        #fiende anfaller
        player.hp -= player.dmg*monster.atk
        if player.hp <= 0:
            death()

        if player_action == "flee" or player_action == "4":
            return(False, player)
    
        if enemy_hp <= 0:
            print("you win!")
            for item in monster.loot:
                player.inventory.append(item)
           
            return(True, player)