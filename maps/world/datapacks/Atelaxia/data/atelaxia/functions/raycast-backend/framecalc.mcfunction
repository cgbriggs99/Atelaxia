# framecalc
# Compute raycasting for a frame.

##getting the precise numbers and putting them into a scoreboard
# get precise numbers from entitys
execute as @e[tag=raycast] at @s run data modify storage ctm:itemframecalc frameX set from entity @e[type=minecraft:glow_item_frame,sort=nearest,limit=1] Pos[0]
execute as @e[tag=raycast] at @s run data modify storage ctm:itemframecalc frameY set from entity @e[type=minecraft:glow_item_frame,sort=nearest,limit=1] Pos[1]
execute as @e[tag=raycast] at @s run data modify storage ctm:itemframecalc frameZ set from entity @e[type=minecraft:glow_item_frame,sort=nearest,limit=1] Pos[2]
execute as @e[tag=raycast] run data modify storage ctm:itemframecalc raycastX set from entity @s Pos[0]
execute as @e[tag=raycast] run data modify storage ctm:itemframecalc raycastY set from entity @s Pos[1]
execute as @e[tag=raycast] run data modify storage ctm:itemframecalc raycastZ set from entity @s Pos[2]
#move the numbers from storage to the same storage except scaled
execute store result storage ctm:itemframecalc frameX long 1 run data get storage ctm:itemframecalc frameX 100000
execute store result storage ctm:itemframecalc frameY long 1 run data get storage ctm:itemframecalc frameY 100000
execute store result storage ctm:itemframecalc frameZ long 1 run data get storage ctm:itemframecalc frameZ 100000
execute store result storage ctm:itemframecalc raycastX long 1 run data get storage ctm:itemframecalc raycastX 100000
execute store result storage ctm:itemframecalc raycastY long 1 run data get storage ctm:itemframecalc raycastY 100000
execute store result storage ctm:itemframecalc raycastZ long 1 run data get storage ctm:itemframecalc raycastZ 100000
#move the precise numbers from storage to scoreboard for calculations
execute store result score frameX ctm_itemframecalc run data get storage ctm:itemframecalc frameX
execute store result score frameY ctm_itemframecalc run data get storage ctm:itemframecalc frameY
execute store result score frameZ ctm_itemframecalc run data get storage ctm:itemframecalc frameZ
execute store result score raycastX ctm_itemframecalc run data get storage ctm:itemframecalc raycastX
execute store result score raycastY ctm_itemframecalc run data get storage ctm:itemframecalc raycastY
execute store result score raycastZ ctm_itemframecalc run data get storage ctm:itemframecalc raycastZ
##
#####Manipulatiing the numbers
##
