from tkinter import *

class Paint(Frame):
    def __init__(self, parent):
            Frame.__init__(self,parent)
            self.parent = parent
            self.setUI()
            self.brush_size = 10
            self.color = "black"

    def draw(self,event):
        # self.canv.create_oval(event.x - self.brush_size,
        #                       event.y - self.brush_size,
        #                       event.x + self.brush_size,
        #                       event.y + self.brush_size,
        #                       fill=self.color, outline=self.color)
        self.canv.create_rectangle(event.x - self.brush_size,
                                   event.y - self.brush_size,
                                   event.x + self.brush_size,
                                   event.y + self.brush_size,
                                   fill=self.color, outline=self.color)
    def setUI(self):
        self.parent.title("R.U.S.Y.A")  # Setting up window name
        self.pack(fill=BOTH, expand=1)  # Placing items on the panel

        self.columnconfigure(6,
                             weight=1)  # Giving the seven column resize option
        self.rowconfigure(2, weight=1)  # The same for the third row

        self.canv = Canvas(self, bg="white")  # Creating canvas with white background
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5,
                       sticky=E + W + S + N)  # Attaching the canvas by grid method. It will be placed on a 3rd row, 1st column, and will occupy 7 columns, making 5px paddings, and giving resize option
        self.canv.bind("<B1-Motion>",
                       self.draw)  # Bind handler to canvas. <B1-Motion> means "when you move the left mouse button ", call the function draw

        color_lab = Label(self, text="Color: ")  # Creating a label for the brush color change buttons.
        color_lab.grid(row=0, column=0,
                       padx=6)  # Setting created label in the first row and the first column, set the horizontal indent of 6 pixels

        red_btn = Button(self, text="Red", width=10,
                         command=lambda: self.set_color(
                             "red"))  # Button creation: Setting the button text, setting the button width (10 characters), the function calling when the button is pressed.
        red_btn.grid(row=0, column=1)  # Setting up the button

        # The creation of the remaining buttons follows the same logic
        # as the creation of the red button, only the arguments differ.

        green_btn = Button(self, text="Green", width=10,
                           command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Blue", width=10,
                          command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Black", width=10,
                           command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="White", width=10,
                           command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)

        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="Two", width=10,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="Five", width=10,
                         command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="Seven", width=10,
                          command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="Ten", width=10,
                           command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="Twenty", width=10,
                         command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="Fifty", width=10,
                            command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)

        clear_btn = Button(self, text="Clear all", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

def main():
    root = Tk()
    root.geometry("1920x1080+300+300")
    app = Paint(root)
    root.mainloop()

if __name__ == "__main__":
    main()

