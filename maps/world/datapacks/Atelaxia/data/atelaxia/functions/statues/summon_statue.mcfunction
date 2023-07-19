# summon_statue
# Summons a statue.

execute at @s run summon block_display ~ ~ ~ {Tags:["head","statue","gold_statue"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.25f,0f,-0.25f],scale:[0.5f,0.5f,0.5f]},brightness:{sky:15,block:15},billboard:"center",block_state:{Name:"minecraft:jack_o_lantern",Properties:{facing:"south"}}}
execute at @s run summon block_display ~ ~ ~ {Tags:["torso","statue","gold_statue"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.25f,0f,-0.125f],scale:[0.5f,0.75f,0.25f]},brightness:{sky:15,block:15},block_state:{Name:"minecraft:gold_block"}}
execute at @s run summon block_display ~ ~ ~ {Tags:["rleg","statue","gold_statue"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.25f,0f,-0.125f],scale:[0.25f,0.75f,0.25f]},brightness:{sky:15,block:15},block_state:{Name:"minecraft:gold_block"}}
execute at @s run summon block_display ~ ~ ~ {Tags:["lleg","statue","gold_statue"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,-0.125f],scale:[0.25f,0.75f,0.25f]},brightness:{sky:15,block:15},block_state:{Name:"minecraft:gold_block"}}
execute at @s run summon block_display ~ ~ ~ {Tags:["rarm","statue","gold_statue"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.5f,0f,-0.125f],scale:[0.25f,0.75f,0.25f]},brightness:{sky:15,block:15},block_state:{Name:"minecraft:gold_block"}}
execute at @s run summon block_display ~ ~ ~ {Tags:["larm","statue","gold_statue"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0.25f,0f,-0.125f],scale:[0.25f,0.75f,0.25f]},brightness:{sky:15,block:15},block_state:{Name:"minecraft:gold_block"}}

execute at @s run tp @e[tag=head,limit=1,sort=nearest] ~ ~1.4 ~ ~ ~
execute at @s run tp @e[tag=torso,limit=1,sort=nearest] ~ ~0.7 ~ ~ 0
execute at @s run tp @e[tag=rleg,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute at @s run tp @e[tag=lleg,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute at @s run tp @e[tag=rarm,limit=1,sort=nearest] ~ ~0.7 ~ ~ 0
execute at @s run tp @e[tag=larm,limit=1,sort=nearest] ~ ~0.7 ~ ~ 0