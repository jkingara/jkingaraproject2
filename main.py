import random

import arcade

#was not able to get the graphs plotted. 
def main():
     my_colors = [arcade.color.WHITE, arcade.color.BLUE, arcade.color.GREEN,
                   arcade.color.RED, arcade.color.ORANGE,
                   arcade.color.ALIZARIN_CRIMSON, arcade.color.ARSENIC,
                   arcade.color.YELLOW, arcade.color.LAVENDER, arcade.color.BRONZE_YELLOW]

     arcade.open_window(900, 700, " project 2")
     arcade.set_background_color(arcade.color.BLACK)

     sample1 = open("kingara.txt", 'r')
     sample2 = open("sample2.txt", 'r')
     all_lines = sample1.readlines()
     all_lines2 = sample2.readlines()

     filename = input("what file should we use")


     arcade.start_render()

     arcade.draw_text(all_lines[0], 300, 655, arcade.color.WHITE, 18)
     #arcade.draw_text(all_lines[0], 300, 655, arcade.color.WHITE, 18)

     arcade.draw_text(all_lines[1], 300, 30, arcade.color.RED, 18)
     #arcade.draw_text(all_lines2[1], 300, 30, arcade.color.GREEN, 18)

     arcade.draw_text(all_lines[2], 10, 330, arcade.color.BLUEBERRY, 15)
     #arcade.draw_text(all_lines[2], 10, 330, arcade.color.BLUEBERRY, 15)

     arcade.draw_text(all_lines[3:], 40, 330, arcade.color.ANTI_FLASH_WHITE, 15)


     x_loc = 50
     y_loc = 200

     therest = all_lines[1:]

     for line in therest:
         split_line = line.split(':')
         size = int(split_line[1])
         this_color = random.choice(my_colors)
         shape = arcade.create_rectangle(50, 200, 50, size * 2, this_color)
         shape.draw()
         x_loc = x_loc+55


     arcade.finish_render()
     arcade.run()

main()