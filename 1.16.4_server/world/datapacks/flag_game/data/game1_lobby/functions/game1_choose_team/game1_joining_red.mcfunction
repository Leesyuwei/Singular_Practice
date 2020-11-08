team join g1red @s
function game1_lobby:game1_choose_team/game1_teaming_item
playsound minecraft:block.note_block.harp master @s ~ ~ ~ 1 2 1
tellraw @s {"text":"您已加入紅隊","color":"red","bold":"true","italic":"true"}
tellraw @a[tag=game1lob] [{"selector":"@s","bold":"true","color":"red"},{"text":" 已加入紅隊","bold":"false"}]
execute at @a[tag=game1lob] run kill @e[type=item,distance=0..2,nbt={Item:{id:"minecraft:red_concrete",Count:1b}}]
scoreboard players set @s g1teambluechose 0
scoreboard players set @s g1teamredchose 0
scoreboard players set @s g1teamspectchose 0