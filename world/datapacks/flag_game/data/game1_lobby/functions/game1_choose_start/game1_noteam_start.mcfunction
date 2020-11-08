playsound minecraft:entity.villager.no master @s ~ ~ ~ 2 1
clear @s spectral_arrow
execute at @a[tag=game1lob] run kill @e[type=item,distance=0..2,nbt={Item:{id:"minecraft:spectral_arrow",Count:1b}}]
scoreboard players set @s game1ifstart 0
replaceitem entity @s container.0 minecraft:spectral_arrow{display:{Name:'[{"text":"開始遊戲","color":"aqua","bold":"true","italic":"false"},{"text":" -按Q以操作","color":"yellow","italic":"true","bold":"false","italic":"true"}]',Lore:['[{"text":""}]','[{"text":"遊戲將會於全部玩家準備完成後開始","color":"light_purple"}]']}}
tellraw @s [{"text":"請先加入隊伍!!","color":"red","bold":"true"}]