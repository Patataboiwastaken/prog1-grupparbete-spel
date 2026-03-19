def battling(monster, player,player_inventory):
    print(f"you have encountered an {monster.name}")
    while True:
        print(f"your have: {player.hp} health")
        print(f"the monster has: {monster.hp} health")
        player_action=input("what do you do?\n1:attack \n2:defend \n3:item \n4:flee")
        if player_action=="attack" or player_action=="1":
            monster.hp-=monster.defen*player.atk    
        
        if player_action=="defend" or player_action=="2":
            dmg_mod=0.5
        
        if player_action=="item" or player_action=="3":
            used_item=input(f"input item you wish to use:\n{player_inventory}")
            
            try: 
                used_item=int(used_item)
                item(player_inventory[used_item]) 
            
            except:
                for x in player_inventory:
                    if x==used_item:
                        item(used_item)

        if player_action=="flee" or player_action=="4":
            player.hp-=monster.atk
            if player.hp>=0:
                death()
            break
        player.hp-=player.defen*monster.hp
        if player.hp>=0:
            death()
        if monster.hp>=0:
            print("you win!")
            loot(monster.loot)
            break