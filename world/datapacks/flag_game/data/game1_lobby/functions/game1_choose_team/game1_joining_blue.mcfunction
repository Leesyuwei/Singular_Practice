team join g1blue @s
function game1_lobby:game1_choose_team/game1_teaming_item
playsound minecraft:block.note_block.harp master @s ~ ~ ~ 1 2 1
tellraw @s {"text":"您已加入藍隊","color":"aqua","bold":"true","italic":"true"}
tellraw @a[tag=game1lob] [{"selector":"@s","bold":"true","color":"aqua"},{"text":" 已加入藍隊","bold":"false"}]
execute at @a[tag=game1lob] run kill @e[type=item,distance=0..2,nbt={Item:{id:"minecraft:blue_concrete",Count:1b}}]
scoreboard players set @s g1teambluechose 0
scoreboard players set @s g1teamredchose 0
scoreboard players set @s g1teamspectchose 0