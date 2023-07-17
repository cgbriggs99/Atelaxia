#white_Wool_Slab - generations function
#tags the temp placed wool item frame (white bottom)
execute at @s as @e[type=minecraft:item_frame,distance=..10,nbt={ItemRotation:0b,Item:{id:"minecraft:white_wool",Count:1b}}] run data modify entity @s Tags set value ["white_wool_slab_temp","white_wool_slab_bottom_temp"]
#summons a white_Wool_Slab_Bottom (item_frame with custom model data 4 from atelaxia resource pack) at the location of a item_frame with white wool((rotated in the 2 or 3 position) in it. limited to 10 blocks from the player.
execute at @e[tag=white_wool_slab_bottom_temp] run summon minecraft:item_frame ~ ~ ~ {Tags:["wool_slab","white_wool_slab"],Facing:1b,Invulnerable:0b,Invisible:1b,Fixed:1b,Item:{id:"minecraft:item_frame",Count:1b,tag:{CustomModelData:1}}}
#kills the item_frame with white wool used as a placer.
execute at @e[tag=white_wool_slab_bottom_temp] run setblock ~ ~ ~ minecraft:bamboo_mosaic_slab[type=bottom]
#--#
#--#
#tags the temp placed wool item frame (white top)
execute at @s as @e[type=minecraft:item_frame,distance=..10,nbt={ItemRotation:1b,Item:{id:"minecraft:white_wool",Count:1b}}] run data modify entity @s Tags set value ["white_wool_slab_temp","white_wool_slab_top_temp"]
#summons a white_Wool_Slab_Top (item_frame with custom model data 3 from atelaxia resource pack) at the location of a item_frame with white wool(rotated in the 0 or 1 position) in it. limited to 10 blocks from the player.
execute at @e[tag=white_wool_slab_top_temp] run summon minecraft:item_frame ~ ~ ~ {Tags:["wool_slab","white_wool_slab"],Facing:1b,Invulnerable:0b,Invisible:1b,Fixed:1b,Item:{id:"minecraft:item_frame",Count:1b,tag:{CustomModelData:2}}}
#places solid block
execute at @e[tag=white_wool_slab_top_temp] run setblock ~ ~ ~ minecraft:smooth_quartz_slab[type=top]
#--#
kill @e[tag=white_wool_slab_temp]
