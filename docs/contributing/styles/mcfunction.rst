Minecraft Functions
===================

.. highlight:: MCFunction

Due to how Minecraft functions are designed, it is often difficult to read them. Therefore, in order for code to be accepted, it must obey certain rules. To start, your code must begin with a preamble that includes the name of the function, as well as a short description of what it does. If your function uses any arguments or parameters, these should also be specified and documented. Optionally, the author of the function may be given, but it is not required. After the preamble, your code should contain comments that describe what each section of your code is doing. As an example, take a look at one version of ``atelaxia:key/castcalc`` written by Randall.

.. code-block:: MCFunction

   # castcalc
   # Calculates raycasting for the key.

   # note the sender of this raycast instance
   tag @s add raycastsender_key
   # kill old cloud
   execute as @e[tag=raycast] if score @s ctm_raycast = @a[tag=raycastsender,limit=1] ctm_raycast run kill @s
   # summon the ray cast cloud
   summon area_effect_cloud ~ ~ ~ {Particle:"block air",Glowing:1b,Age:-1000,Duration:1000,CustomName:'{"text":"I"}',Tags:["raycast","noscore","current"]}
   # set the player to a score
   execute unless score @a[tag=raycastsender,limit=1] ctm_raycast matches 0.. run scoreboard players operation @a[tag=raycastsender] ctm_raycast = count ctm_raycast
   # set the raycast cloud to the player
   execute as @e[tag=raycast,tag=noscore] run scoreboard players operation @s ctm_raycast = @a[tag=raycastsender,limit=1] ctm_raycast
   # add one to the count score no players have the same score
   execute if score @a[tag=raycastsender,limit=1] ctm_raycast = count ctm_raycast run scoreboard players add count ctm_raycast 1

Observe that the function file begins with the preamble.

.. code-block:: MCFunction

   # castcalc
   # Calculates raycasting for the key.

This starts with the name of the function, which may be one of ``castcalc``, ``key/castcalc``, or ``atelaxia:key/castcalc``. This is to help navigation of the functions, and is just standard practice in general. After that, a description of the function is given. These can be as long as needed, but they should get across what the function is trying to do. Optionally, an author line can be given.

.. code-block:: MCFunction
   
   # Author: Randy Golden

In this case, the author is not given. After that, note that most lines are documented.

.. code-block:: MCFunction

   # note the sender of this raycast instance
   tag @s add raycastsender_key
   # kill old cloud
   execute as @e[tag=raycast] if score @s ctm_raycast = @a[tag=raycastsender,limit=1] ctm_raycast run kill @s
   # summon the ray cast cloud
   summon area_effect_cloud ~ ~ ~ {Particle:"block air",Glowing:1b,Age:-1000,Duration:1000,CustomName:'{"text":"I"}',Tags:["raycast","noscore","current"]}
   ...

This helps readers to follow the flow of the program. In some instances, it will not be necessary to document every line. Here is a short section of code from one version of ``atelaxia:drawbridge/chain_extend_1`` written by Joe Wanger that exhibits this idea.

.. code-block:: MCFunction
   
   execute if score counter drawbridge matches 90 run data modify entity @e[tag=chain1,limit=1] transformation.scale set value [1.0f,1.0f,7.00f]
   execute if score counter drawbridge matches 89 run data modify entity @e[tag=chain1,limit=1] transformation.scale set value [1.0f,1.0f,6.92f]
   execute if score counter drawbridge matches 88 run data modify entity @e[tag=chain1,limit=1] transformation.scale set value [1.0f,1.0f,6.84f]
   execute if score counter drawbridge matches 87 run data modify entity @e[tag=chain1,limit=1] transformation.scale set value [1.0f,1.0f,6.77f]
   execute if score counter drawbridge matches 86 run data modify entity @e[tag=chain1,limit=1] transformation.scale set value [1.0f,1.0f,6.69f]
   ...

This function continues on in a similar manner for 90 lines of code. For this, it would make sense to simply add a comment to the beginning of the file and not 90 individual comments for each line.

Sphinx Documentation
--------------------

At some point, it will be possible to include Sphinx directives in your code. This will be denoted by beginning a line with ``#@`` followed by properly formatted ReStructured Text. The Sphinx lines will then be directly imported into a file that contains references to all the functions in a given namespace and directory. Here is an example for what that will look like.

.. code-block:: MCFunction
   
   # foobar
   #@ Here is a brief description.
   #@ It contains some *markup codes* and other **stuff**.

This will produce output that looks like this.

.. code-block:: rest

   namespace:foobar
   """"""""""""""""

      Here is a brief description.
      It contains some *markup codes* and other **stuff**.

File Template
-------------

Here is a simple preamble template to get you started.

.. code-block:: MCFunction

   # {function name}
   # Brief description goes here.
   # Author: You or Authors: You and Others (Optional)

   # First line goes here. Document it well
