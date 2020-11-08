execute at @a[tag=game1lob] run kill @e[type=item,distance=0..2,nbt={Item:{id:"minecraft:spectral_arrow",Count:1b}}]
clear @s spectral_arrow
replaceitem entity @s container.0 minecraft:spectral_arrow{display:{Name:'[{"text":"開始遊戲","color":"aqua","bold":"true","italic":"false"},{"text":" -按Q以操作","color":"yellow","italic":"true","bold":"false","italic":"true"}]',Lore:['[{"text":""}]','[{"text":"遊戲將會於全部玩家準備完成後開始","color":"light_purple"}]']}}
tellraw @s {"text":"您已取消開始遊戲","color":"gold","bold":"true"}
tag @s remove g1canstart
function game1_lobby:game1_choose_team/game1_teaming_item
scoreboard players set @s game1ifstart 0
scoreboard players remove A g1canstartplyc 1
playsound minecraft:block.note_block.harp master @s ~ ~ ~ 10 0.48 1