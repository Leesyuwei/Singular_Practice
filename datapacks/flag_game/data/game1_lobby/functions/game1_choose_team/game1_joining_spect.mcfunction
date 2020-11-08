team join g1spect @s
function game1_lobby:game1_choose_team/game1_teaming_item
playsound minecraft:block.note_block.harp master @s ~ ~ ~ 1 2 1
tellraw @s {"text":"您將旁觀此遊戲","color":"gray","bold":"true","italic":"true"}
tellraw @a[tag=game1lob] [{"selector":"@s","bold":"true","color":"gray"},{"text":" 將旁觀此遊戲","bold":"false"}]
execute at @a[tag=game1lob] run kill @e[type=item,distance=0..2,nbt={Item:{id:"minecraft:ender_eye",Count:1b}}]
scoreboard players set @s g1teambluechose 0
scoreboard players set @s g1teamredchose 0
scoreboard players set @s g1teamspectchose 0