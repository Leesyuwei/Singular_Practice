execute as @a[tag=game1lob,scores={game1ifstart=3..}] at @s run function game1_lobby:game1_choose_start/game1_cancel_start
execute as @a[tag=game1lob,team=!g1red,team=!g1blue,team=!g1spect,scores={game1ifstart=1..}] at @s run function game1_lobby:game1_choose_start/game1_noteam_start
execute as @a[tag=game1lob,team=g1spect,scores={game1ifstart=1..}] at @s run function game1_lobby:game1_choose_start/game1_spect_starts
execute as @a[tag=game1lob,scores={game1ifstart=1..1}] at @s run function game1_lobby:game1_choose_start/game1_prepare_start
execute unless entity @a[tag=game1lob,team=!g1red,team=!g1blue,team=!g1spect] if entity @a[tag=game1lob,team=g1blue] if entity @a[tag=game1lob,team=g1red] run say start 