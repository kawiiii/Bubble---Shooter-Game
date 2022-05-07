import tkinter as tk

from tkinter import ttk

from game_popupwindow import AboutPopupWindow



#------BUTTONS ON THE RIGHT FRAME----------
class ControlButtons:
    color_background = '#047E97'

    def __init__(self, frame, window):
        # width of buttons must be together equal to right_toolbar_width from Window
        self.frame = frame
        self.window = window

        # restart button
        self.restart_btn_image = tk.PhotoImage(file="../images/marble_green_restart.png")
        self.restart_btn_image = self.restart_btn_image.subsample(4, 4)

        restart_btn = tk.Button(self.frame, width=85,
                                image=self.restart_btn_image,
                                bg=self.color_background,
                                relief='flat',
                                command=self.click_restart,
                                borderwidth=0,
                                activebackground=self.color_background)
        restart_btn.grid(row=0, column=0, padx=(10, 0))

        # about button
        self.about_btn_image = tk.PhotoImage(file="../images/marble_purple_about.png")
        self.about_btn_image = self.about_btn_image.subsample(5, 5)

        about_btn = tk.Button(self.frame, width=65,
                              image=self.about_btn_image,
                              bg=self.color_background,
                              relief='flat',
                              command=self.click_about,
                              borderwidth=0,
                              activebackground=self.color_background)
        about_btn.grid(row=1, column=1, padx=(0, 10))

        # high-score button
        self.highscore_btn_image = tk.PhotoImage(file="marble_red_highscore.png")
        self.highscore_btn_image = self.highscore_btn_image.subsample(4, 4)

        highscore_btn = tk.Button(self.frame, width=100,
                                  image=self.highscore_btn_image,
                                  bg=self.color_background,
                                  relief='flat',
                                  command=self.click_highscore,
                                  borderwidth=0,
                                  activebackground=self.color_background)
        highscore_btn.grid(row=2, column=0, padx=(10, 0))


    def click_restart(self):
        """
        when restart button is pressed, score is not saved
            playground is restored to starting point
        """
        # print("Restart Button was pressed")
        self.window.playground.delete('all')
        self.window.marbles = self.window.init_marbles()
        self.window.show_marbles()
        # self.window.show_grid()
        self.window.score.restart_score()
        self.window.next_marble_counter.set_number_of_marbles(MarbleCounter.default_counter)

    def click_about(self):
        """
        when help is pressed, it displays about window
        """
        AboutPopupWindow(self.frame)

    @staticmethod
    def click_highscore():
        """
        when highscore button is pressed, a popup windows shows up with table of highscore
        """
        HighscoreTable()

    @staticmethod
    def save_highscore(username, achieved_score):
        with open('../docs/highscore.txt', 'a') as file:
            file.write("\n{} {}".format(username, achieved_score))


class HighscoreTable(object):
    width = 600
    height = 300
    color_background = '#04AACE'

    def __init__(self):
        data = self.load_data('../docs/highscore.txt')

        # create root Tk object and set its properties
        self.root = tk.Tk()
        self.root.title("")
        self.root.geometry("{}x{}".format(self.width, self.height))
        self.root.configure(background=self.color_background)
        self.root.resizable(False, False)

        tk.Label(self.root,
                 text="High Scores",
                 font=("Helvetica", 22),
                 bg=self.color_background).grid(row=0, columnspan=3)

        # create tree-view with 3 columns
        cols = ('Position', 'Name', 'Score')
        self.listBox = ttk.Treeview(self.root, columns=cols, show='headings')

        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)

        self.listBox.grid(row=1, column=0, columnspan=2)

        self.show_score(data)

        # at the end of __init__
        self.root.mainloop()

    def show_score(self, data):

        temp_list = data
        temp_list.sort(key=lambda e: e[1], reverse=True)

        for i, (name, score) in enumerate(temp_list, start=1):
            self.listBox.insert("", "end", values=(i, name, score))

    @staticmethod
    def load_data(filename):
        """
        loads data from json file self.filename
        """
        data = []
        with open(filename) as file:
            for line in file:
                try:
                    name = line.strip().split()[0]
                    score = int(line.strip().split()[1])
                    data.append([name, score])
                except IndexError:
                    pass
        return data


class Score:
    color_background = '#047E97'

    def __init__(self, frame,score=0):
        self.score = score

        self.score_label = tk.Label(frame, text='Score', font='Arial 15', bg=self.color_background)
        self.score_label.grid(row=5, column=0, columnspan=2, pady=(100, 0))

        self.score_value = tk.Label(frame, text="{}".format(self.score), font='Arial 15', bg=self.color_background)
        self.score_value.grid(row=6, column=0, columnspan=2)

    def add_to_score(self, score):
        self.score += score
        # print("Score =", self.score)
        self.score_value.config(text="{}".format(self.score))

    def get_score(self):
        return self.score

    def restart_score(self):
        self.score = 0
        # print("Score =", self.score)
        self.score_value.config(text="{}".format(self.score))


class NextMarble:
    color_background = '#047E97'

    def __init__(self, frame, picture, color):
        self.frame = frame
        self.color = color

        # create image with random color
        self.next_marble = picture

        # create image in frame
        self.next_marble_icon = tk.Label(self.frame, height=100, width=77,
                                         image=self.next_marble,
                                         bg=self.color_background,
                                         relief='flat',
                                         borderwidth=0)
        self.next_marble_icon.grid(row=0, column=0)

    def update_color(self, picture, color):
        self.color = color
        self.next_marble = picture
        self.next_marble_icon.config(image=picture)

    def get_picture(self):
        return self.next_marble

    def get_color(self):
        return self.color


class MarbleCounter:
    default_counter = 5
    color_background = '#047E97'

    def __init__(self, frame, picture):
        self.frame = frame

        self.picture = picture
        self.marbles = []
        self.inner_frame = tk.Frame(self.frame,
                                    bg=self.color_background,
                                    width=231,
                                    height=100)
        self.inner_frame.grid(row=0, column=1)
        self.inner_frame.grid_propagate(False)

        # create correct number of marbles
        self.counter = self.default_counter

        for i in range(self.counter):
            self.marbles.append(tk.Label(self.inner_frame, height=100, width=37,
                                         image=self.picture,
                                         bg=self.color_background,
                                         relief='flat',
                                         borderwidth=0))
            self.marbles[i].grid(row=0, column=1 + i)

    def set_number_of_marbles(self, number):
        for i in range(self.counter):
            self.marbles[i].grid_forget()
        self.counter = number

        for i in range(self.counter):
            self.marbles[i].grid(row=0, column=1 + i)

    def get_counter(self):
        return self.counter


class ActMarble:
    color_background = '#047E97'

    def __init__(self, frame, picture, color):
        self.frame = frame
        self.color = color

        # create image with random color
        self.act_marble = picture

        # create image in frame
        self.act_marble_icon = tk.Label(self.frame, height=100, width=37,
                                        image=self.act_marble,
                                        bg=self.color_background,
                                        relief='flat',
                                        borderwidth=0)
        self.act_marble_icon.grid(row=0, column=2)

    def update_color(self, picture, color):
        self.color = color
        self.act_marble = picture
        self.act_marble_icon.config(image=self.act_marble)

    def get_picture(self):
        return self.act_marble

    def get_color(self):
        return self.color

class features:
    def pause(self):
        with open('../docs/settings.txt') as file:
            self.pause_key=file.read(0)
            print(self.pause_key)

        return self.pause_key

    def boss(self):
        with open('../docs/settings.txt') as file:
            if file.read(1)=="":
                self.boss_key=file.read(0)
            else:
                self.boss_key=file.read(1)
                print(self.boss_key)
        return self.boss_key
