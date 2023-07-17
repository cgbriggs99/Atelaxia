# raise_increment
# Increments the raising animation timer.

execute as @e[tag=rotate] at @s run tp @s ~ ~ ~ ~ ~-1
scoreboard players add counter drawbridge 1
execute if score counter drawbridge < ninety drawbridge run schedule function atelaxia:drawbridge/raise_increment 1t
execute if score counter drawbridge = ninety drawbridge run schedule clear atelaxia:drawbridge/chain_raise
execute if score counter drawbridge = ninety drawbridge run schedule clear atelaxia:drawbridge/chain_shrink_1
execute if score counter drawbridge = ninety drawbridge run schedule clear atelaxia:drawbridge/chain_shrink_2
execute if score counter drawbridge = ninety drawbridge run scoreboard players set counter drawbridge 0
