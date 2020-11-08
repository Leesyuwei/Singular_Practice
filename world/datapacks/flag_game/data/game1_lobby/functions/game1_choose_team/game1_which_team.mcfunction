execute as @a[tag=game1lob,scores={g1teambluechose=1..}] run function game1_lobby:game1_choose_team/game1_joining_blue
execute as @a[tag=game1lob,scores={g1teamredchose=1..}] run function game1_lobby:game1_choose_team/game1_joining_red
execute as @a[tag=game1lob,scores={g1teamspectchose=1..}] run function game1_lobby:game1_choose_team/game1_joining_spect
