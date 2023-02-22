import tkinter as tk
from tkinter import NW, W

import block_generator, constants


class Model:
    def __init__(self):
        self.current_player = constants.Player.red #choose who is the starting player
        self.selected_block = "-1"
        self.selected_block_segment = "-1"
        self.tiles = [[None for _ in range(constants.BOARD_SIZE_CELLS)]
                      for _ in range(constants.BOARD_SIZE_CELLS)]
        self.picker_tiles = [[None for _ in range(constants.PICKER_COLS)]
                             for _ in range(constants.PICKER_ROWS)]
        self.picker_blocks = {constants.Player.red: block_generator.generate_blocks(),
                              constants.Player.green: block_generator.generate_blocks(),
                              constants.Player.yellow: block_generator.generate_blocks(),
                              constants.Player.blue: block_generator.generate_blocks()}
        self.move_flag = False
        self.mouse_xpos = -1
        self.mouse_ypos = -1
        self.white_flag = {0: False, 1: False, 2:False, 3: False}
        self.score = {0: -89, 1: -89, 2:-89, 3:-89}

        self.canvas = tk.Canvas(None, width=constants.CANVAS_WIDTH_PX - 4, height=constants.CANVAS_HEIGHT_PX - 4)
        self.canvas.pack()

        self.red_score_label = self.canvas.create_text(
            1200, 100, font="Times 16", text="Red Score: " + str(self.score[0]))
        self.green_score_label = self.canvas.create_text(
            1200, 300, font="Times 16", text="Green Score: " + str(self.score[1]))
        self.yellow_score_label = self.canvas.create_text(
            1200, 500, font="Times 16", text="Yellow Score: " + str(self.score[2]))
        self.blue_score_label = self.canvas.create_text(
            1200, 700, font="Times 16", text="Blue Score: " + str(self.score[3]))

        self.end_game_label = self.canvas.create_text(950, 20, font="Times 16", text="")

        self.resign_button = tk.Button(self.canvas, text='Resign')
        self.resign_button.configure(width=8, activebackground="#33B5E5", font="Times 12")
        self.canvas.create_window(750, 5, anchor=NW, window=self.resign_button)

        self.save_button = tk.Button(self.canvas, text="Save game")
        self.save_button.configure(width=8, activebackground="#33B5E5", font="Times 12")
        self.canvas.create_window(900, 5, anchor=NW, window=self.save_button)

    def get_selected_block_segment(self):
        return int(self.selected_block_segment.split("_")[2])

    def get_selected_block(self):
        return int(self.selected_block.split("_")[2])
