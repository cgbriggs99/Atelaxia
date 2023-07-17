execute as @e[tag=chain] at @s run tp @s ~ ~ ~ ~ ~1
execute if score counter drawbridge < ninety drawbridge run schedule function atelaxia:drawbridge/chain_lower 2t