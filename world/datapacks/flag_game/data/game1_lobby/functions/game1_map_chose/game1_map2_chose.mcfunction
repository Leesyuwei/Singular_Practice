clear @a[tag=game1lob] stone_bricks
clear @a[tag=game1lob] jungle_leaves
clear @a[tag=game1lob] cod_bucket
replaceitem entity @a[tag=game1lob] container.8 jungle_leaves{HideFlags:1,Enchantments:[{id:"minecraft:smite",lvl:0}],display:{Name:"[{\"text\":\"目前地圖 \",\"color\":\"dark_aqua\",\"italic\":\"true\",\"underlined\":\"false\"},{\"text\":\"地圖二\",\"color\":\"aqua\",\"bold\":\"true\",\"underlined\":\"true\",\"italic\":\"false\"},{\"text\":\" -按Q以選擇\",\"underlined\":\"false\",\"color\":\"yellow\",\"bold\":\"false\",\"italic\":\"true\"}]",Lore:["[{\"text\":\" - \",\"color\":\"gray\"},{\"text\":\"地圖一\",\"color\":\"gray\"}]","[{\"text\":\" - \",\"color\":\"gold\"},{\"text\":\"地圖二\",\"color\":\"gold\",\"bold\":\"true\",\"underlined\":\"true\"},{\"text\":\"   [已選擇]\",\"color\":\"green\",\"bold\":\"true\",\"italic\":\"false\"}]","[{\"text\":\" - \",\"color\":\"gray\"},{\"text\":\"地圖三\",\"color\":\"gray\"}]"]}}
tellraw @s {"text":"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"}
scoreboard players set A game1map 2
playsound minecraft:block.note_block.harp master @s ~ ~ ~ 1 2
tellraw @a[tag=game1lob] ["",{"text":"遊戲地圖已更改為 ","color":"yellow","italic":"true"},{"text":"地圖二","color":"aqua","bold":"true","underlined":"true","italic":"true"}]