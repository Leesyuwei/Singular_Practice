playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.5 1
tp @s -76.0 51 223
execute as @s[tag=g1canstart] run scoreboard players remove A g1canstartplyc 1
tag @s remove game1lob
tag @s remove g1canstart
team leave @s
tellraw @a[tag=game1lob] [{"selector":"@s","color":"green","bold":"true"},{"text":" 離開了","color":"yellow","bold":"false","italic":"true"},{"text":"~奪旗大戰大廳~","color":"aqua","bold":"true","itlaic":"false"}]
tellraw @s {"text":"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"}
tellraw @s [{"text":"您已離開","color":"yellow","italic":"true"},{"text":" ~奪旗大戰大廳~","color":"aqua","bold":"true","italic":"false"}]
spawnpoint @s -83 37 221
effect give @s minecraft:slowness 2 3 true
clear @s stone_bricks
clear @s cod_bucket
clear @s jungle_leaves
clear @s blue_concrete
clear @s red_concrete
clear @s ender_eye
clear @s spectral_arrow
scoreboard players set @s g1teambluechose 0
scoreboard players set @s g1teamredchose 0
scoreboard players set @s g1teamspectchose 0
scoreboard players set @s game1ifstart 0