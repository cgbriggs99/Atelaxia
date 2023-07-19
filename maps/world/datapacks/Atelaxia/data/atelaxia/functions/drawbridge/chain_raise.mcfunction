# chain_raise
# Raises the chain on a drawbridge.

execute as @e[tag=chain] at @s run tp @s ~ ~ ~ ~ ~-1
execute if score counter drawbridge < ninety drawbridge run schedule function atelaxia:drawbridge/chain_raise 2t