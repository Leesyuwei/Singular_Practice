playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.5 1
tp @s -90.0 49 494
tag @s add game1lob
tellraw @a[tag=game1lob,distance=0.1..] [{"selector":"@s","color":"green","bold":"true"},{"text":" 加入了","color":"yellow","bold":"false","italic":"true"},{"text":"~奪旗大戰大廳~","color":"aqua","bold":"true","itlaic":"false"}]
tellraw @s {"text":"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"}
tellraw @s [{"text":"您已加入","color":"yellow","italic":"true"},{"text":" ~奪旗大戰大廳~","color":"aqua","bold":"true","italic":"false"}]
spawnpoint @s -90 49 494
effect give @s minecraft:slowness 2 3 true
function game1_lobby:game1_choose_map/game1_choose_map1
function game1_lobby:game1_choose_map/game1_choose_map2
function game1_lobby:game1_choose_map/game1_choose_map3
function game1_lobby:game1_choose_team/game1_teaming_item
replaceitem entity @s container.0 minecraft:spectral_arrow{display:{Name:'[{"text":"開始遊戲","color":"aqua","bold":"true","italic":"false"},{"text":" -按Q以操作","color":"yellow","italic":"true","bold":"false","italic":"true"}]',Lore:['[{"text":""}]','[{"text":"遊戲將會於全部玩家準備完成後開始","color":"light_purple"}]']}}
team leave @s
execute if score A g1canstartplyc matches ..-1 run scoreboard players set A g1canstartplyc 0
scoreboard players set @s g1teambluechose 0
scoreboard players set @s g1teamredchose 0
scoreboard players set @s g1teamspectchose 0
scoreboard players set @s game1ifstart 0