#Import libreries
import os
import random
import readchar

POS_X = 0
POS_Y = 1

#Number of trainers
trainers = 3

#Create maze
obstacle_definition = """\
############################
      #####      ##         
                      ##### 
######  ############  ##### 
####          ######  ##### 
###     ###                 
             #######  ##### 
##  ###########             
###   #            ##   ### 
##       #####              
##   #  ###############    #
##        ########         #
###   ###                 ##
####   #  ####  ##       ###
#####     #####    ##   ####
############################\
"""
#Initial position
my_position = [0, 1]

map_objects = []
tail = []

#Win, lose or finish?
end_game = False
died = False
win = False

#Create maze lists
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Generate random objects
while len(map_objects) < trainers:
  new_position = [
    random.randint(0, MAP_WIDTH - 1),
    random.randint(0, MAP_HEIGHT - 1)
    ]

  if new_position not in map_objects and new_position != my_position\
            and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":

    map_objects.append(new_position)
# Main Loop
while not end_game:
  if trainers == 0:
    win = True
  if win == True:
    print ("Has ganado!!!")
    end_game = True

  if end_game:
    print("Fin del juego!")
    exit()
  os.system("clear")

  #Start drawing map
  print("+" + "-" * MAP_WIDTH * 2 + "+")

  for coordinate_y in range(MAP_HEIGHT):

    print("|", end="")

    for coordinate_x in range(MAP_WIDTH):

      char_to_draw = "  "
      object_in_cell = None

      for map_object in map_objects:
        if map_object[POS_X] == coordinate_x and map_object[
            POS_Y] == coordinate_y:
          char_to_draw = ":("
          object_in_cell = map_object


      if my_position[POS_X] == coordinate_x and my_position[
          POS_Y] == coordinate_y:
        char_to_draw = " @"

        # Check if the main trainter is in a another trainer    
        if object_in_cell:
          #Select a random pokemon to struggle
          pokemon_list = ["Squirtle", "Charizard", "Butterfree"]
          rival_pokemon = random.choice(pokemon_list)
          win_combat = False
          os.system ("clear")
          
          
          if win_combat:
            pokemon_list.remove(rival_pokemon)
            win_combat = False
            trainers -= 1
            map_objects.remove(object_in_cell)
            break
          

      if obstacle_definition[coordinate_y][coordinate_x] == "#":
        char_to_draw = "##"

      print("{}".format(char_to_draw), end="")

    print("|")

  print("+" + "-" * MAP_WIDTH * 2 + "+")
  # Movement of the player

  direction = readchar.readchar() #Save key pressed
  new_position = None
  #Define action knowing key presed
  if direction == "w":
    new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

  elif direction == "s":
    new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

  elif direction == "a":
    new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

  elif direction == "d":
    new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

  elif direction == "q":
    end_game = True

  if new_position:
    if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
      tail.insert(0, my_position.copy())
      my_position = new_position

  os.system("clear")
