# lower_increment
# Increments the lowering animation counter.

execute as @e[tag=rotate] at @s run tp @s ~ ~ ~ ~ ~1
scoreboard players add counter drawbridge 1
execute if score counter drawbridge < ninety drawbridge run schedule function atelaxia:drawbridge/lower_increment 1t
execute if score counter drawbridge = ninety drawbridge run schedule clear atelaxia:drawbridge/chain_lower
execute if score counter drawbridge = ninety drawbridge run schedule clear atelaxia:drawbridge/chain_extend_1
execute if score counter drawbridge = ninety drawbridge run schedule clear atelaxia:drawbridge/chain_extend_2
execute if score counter drawbridge = ninety drawbridge run scoreboard players set counter drawbridge 0