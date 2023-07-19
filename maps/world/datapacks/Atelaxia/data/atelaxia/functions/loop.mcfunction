# loop

##this file runs every tick of the server/world is located with
##fix biome sound upon death
execute as @a if score @s atelaxia_death matches 1.. as @s run function atelaxia:biome_ambient_death_fix
execute as @a[scores={atelaxia_key=1..},nbt={SelectedItem:{id:"minecraft:carrot_on_a_stick",tag:{CustomModelData:1}}}] at @s positioned ~ ~1.55 ~ run function atelaxia:key/key_raycast