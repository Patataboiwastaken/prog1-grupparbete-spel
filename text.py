def welcome_func():
    print("""
|-\\                      ____     ___     _______                                ____     ___  
|   \\       |         |  !   \\    ! !    / _____  \\    _________       ______    !   \\    ! !  
|     \\     |         |  ! !\\ \\   ! !   ! !     !__!   | _______!     /      \\   ! !\\ \\   ! !
|     |     |         |  ! ! \\ \\  ! !   ! !     ____   ! |______     |   _    |  ! ! \\ \\  ! !
|     /      \\       /   ! !  \\ \\ ! !   ! !    !_  !   | _______|    |  |_|   |  ! !  \\ \\ ! !
|   /         \\     /    ! !   \\ \\! !    \\ \\_____! !   ! |______     |        |  ! !   \\ \\! !
|-/            \\___/     !_!    \\___!     \\________!   |________|     \\______/   !_!    \\___!  
   ______    _______                                       ___                       _______  
  /  ____!  |   _   \\         /\\     _                 _   | |                      |   _   \\
 / /        |  |_|   |       /  \\    \\ \\              / /  | |          _________   |  |_|   |
/ /         | _ ____/       / /\\ \\    \\ \\     /\\     / /   | |          | _______!  | _ ____/  
! !         | |\\ \\         / /__\\ \\    \\ \\   /  \\   / /    | |          ! |______   | |\\ \\      _______  ___    ___
\\ \\         | | \\ \\       / _____\\ \\    \\ \\_/ /\\ \\_/ /     | |          | _______|  | | \\ \\    |__   __| |  \\  /  |
 \\ \\_____   | |  \\ \\     / /      \\ \\    \\   /  \\   /      | |________  ! |______   | |  \\ \\      | |    |   \\/   |
  \\_____!   |_|   \\_\\   /_/        \\_\\    \\_/    \\_/       |__________| |________|  |_|   \\_\\     |_|    |_|\\__/|_|
""")
    print("Welcome ro DUNGEON CRAWLER TM.\nGo forth, battle monsters and find treasure!\nAre you brave enough to get to the bottom?")
    input("press enter to continue")
    controls()

def controls():
    print("""
controls:
help = show controls
w = move up
a = move left
d = move right
s = move down
l = legend(explains the symbols on the map)
i = inventory
c = view character stats
""")
    input("press enter to continue")

def death():
    print("Tyvärr verkar du ha dött, bättre lycka nästa gång ('v')")
    exit()

def legend():
    print("""
# = wall
P = player
T = trapdoor to next floor
r = rat
g = goblin
o = orc
z = zombie
s = skeleton
S = chest
l = lich
""")