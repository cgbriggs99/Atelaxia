execute unless block ^ ^ ^0.5 air run tp @e[type=area_effect_cloud,tag=raycastkey,tag=current] ~ ~ ~
execute if block ^ ^ ^0.6 chiseled_stone_bricks run say stone
scoreboard players add key atelaxia_backend 1
execute unless score key atelaxia_backend matches 100.. if block ^ ^ ^0.5 air positioned ^ ^ ^0.5 run function atelaxia:key/casting
