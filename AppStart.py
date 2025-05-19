from tkinter import *
import InputError as e
import LayoutTest as LT


def startApp(root):
    root.title("Keyboard Layout Test")
    root.geometry("1000x500")
    root.resizable(width=False, height=False)

    # Padding from top
    label = Label(root, text="")
    label.pack(padx=(0, 50), pady=(50, 0))

    # Welcome Label
    header = Label(root, text="Welcome to our keyboard layout test!", font=("Cambria", 25, "bold"))
    header.place(y=10)
    header.pack()

    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 10), pady=(10, 0))

    # Please Select label
    selection = Label(root, text="Please select a keyboard layout to get started:", font=("Cambria", 15, "bold"))
    selection.place(y=30)
    selection.pack()

    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 10), pady=(10, 0))

    # Select Button
    selectedLayout = StringVar(root)
    selectedLayout.set("--Select a layout--")
    layoutMenu = OptionMenu(root, selectedLayout, "--Select a layout--", "QWERTY", "Dvorak", "Colemak", "Workman")
    layoutMenu.pack()
    layoutMenu.config(font=("Cambria", 15, "bold"))

    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 5), pady=(5, 0))

    # Start Button
    def startApp():
        layout = selectedLayout.get()
        if layout == "--Select a layout--":
            e.errorWindow(root)
        else:
            LT.createTest(root, layout)

    button = Button(root, text="Start Test", command=startApp, height=2, width=16, font=("Cambria", 15, "bold"))
    button.pack()

    root.mainloop()
