scoreboard players reset @s atelaxia_key
scoreboard players add key atelaxia_backend 1
execute if block ^ ^ ^0.5 air positioned ^ ^ ^0.5 run function atelaxia:key/key_raycast
execute if block ^ ^ ^0.5 water positioned ^ ^ ^0.5 run function atelaxia:key/key_raycast
execute if block ^ ^ ^0.6 chiseled_stone_bricks positioned ^ ^ ^0.5 run function atelaxia:key/fountainkey
execute if block ^ ^ ^0.6 #bed positioned ^ ^ ^0.5 run say Hu