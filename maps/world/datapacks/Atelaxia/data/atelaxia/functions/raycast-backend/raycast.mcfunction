#summon in an area effect cloud and make sure its individualized to the sender of this command each time it is sent ## one area effect cloud per person for efficiency, 
#continued... --> summon a more permenant fix if you need it memory past the initial function
function ctm:castcalc
#repeadly move the area effect cloud until a non air block is found ## the tag current is used when deciding which area effect cloud to move as well
execute positioned ~ ~1.55 ~ run function ctm:casting
#commands to be run after ray cast has reached its spot
##
#execute at @e[tag=raycast,tag=current] run setblock ~ ~ ~ stone


##
tellraw @a [{"color":"gold","selector":"@e[tag=raycast,tag=current]"},{"color":"red","text":" found something"}]
function ctm:framecalc
#remove the raycast sender's tag to allow for a new sender
tag @s remove raycastsender
# allow for the next caster to have a current raycast ## the tag is used for commands involving it in this function as well as in casting
tag @e[tag=raycast,tag=current] remove current