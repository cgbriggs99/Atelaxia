# castcalc
# Calculate raycasting.

#note the sender of this raycast instance
tag @s add raycastsender
#reset score board once it gets high
execute if score count ctm_api matches 10000 run scoreboard players set count ctm_api 1
#kill old cloud
execute as @e[tag=raycast] if score @s ctm_raycast = @a[tag=raycastsender,limit=1] ctm_raycast run kill @s
#summon the ray cast cloud
summon area_effect_cloud ~ ~ ~ {Particle:"block air",Glowing:1b,Age:-1000,Duration:1000,CustomName:'{"text":"I"}',Tags:["raycast","noscore","current"]}
#set the player to a score
execute unless score @a[tag=raycastsender,limit=1] ctm_raycast matches 0.. run scoreboard players operation @a[tag=raycastsender] ctm_raycast = count ctm_raycast
#set the raycast cloud to the player
execute as @e[tag=raycast,tag=noscore] run scoreboard players operation @s ctm_raycast = @a[tag=raycastsender,limit=1] ctm_raycast
#add one to the count score no players have the same score
execute if score @a[tag=raycastsender,limit=1] ctm_raycast = count ctm_raycast run scoreboard players add count ctm_raycast 1



