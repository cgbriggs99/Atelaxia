# summon_drawbridge
# Summons the drawbridge to a specific coordinate.

function atelaxia:drawbridge/fill_air
function atelaxia:drawbridge/fill_bridge
summon block_display -16.001 72.001 867.001 {Tags:["rotate"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[5.002f,1.002f,6.002f]},brightness:{sky:15,block:15},block_state:{Name:"minecraft:oak_wood",Properties:{axis:"z"}}}
summon block_display -16.50 77.00 866.50 {Tags:["chain","chain1"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.00f,1.00f,7.00f]},Rotation:[0.0f,45.0f],brightness:{sky:15,block:15},block_state:{Name:"minecraft:chain",Properties:{axis:"z"}}}
summon block_display -11.50 77.00 866.50 {Tags:["chain","chain2"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.00f,1.00f,7.00f]},Rotation:[0.0f,45.0f],brightness:{sky:15,block:15},block_state:{Name:"minecraft:chain",Properties:{axis:"z"}}}