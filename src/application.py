from utils import *
from tkinter import *
from tkinter import ttk


def main():
    # Setting the app
    root = Tk()
    root.geometry("300x300")
    root.title("Marc Video Converter")
    root.configure(bg="gray75")
    root.resizable(height=False, width=False)
    icon = PhotoImage(file="../app/icon.png")
    root.iconphoto(False, icon)

    # Select a file from your browser
    select_video_button = ttk.Button(root, text='Select a video to convert', width=20,
                                     command=lambda: select_file(root))
    select_video_button.pack(expand=True)
    select_video_button.place(x=50, y=25)

    # Label of the filepath
    root.filelocation = Entry(root, width=15, font="Arial")  # print path once selected
    root.filelocation.insert(0, 'Path to the video')
    root.filelocation.configure(state='disabled', borderwidth=0)
    root.filelocation.place(x=95, y=50)

    # BUTTONS
    vp8_button = Button(root, text="VP8 format", fg='black', bg='white', width=10,
                        command=lambda: convert_vp8(root.filename))
    vp8_button.place(x=110, y=105)

    vp9_button = Button(root, text="VP9 format", fg='black', bg='white', width=10,
                        command=lambda: convert_vp9(root.filename))
    vp9_button.place(x=110, y=145)

    h265_button = Button(root, text="h265 format", fg='black', bg='white', width=10,
                         command=lambda: convert_h265(root.filename))
    h265_button.place(x=110, y=185)

    av1_button = Button(root, text="AV1 format", fg='black', bg='white', width=10,
                        command=lambda: convert_av1(root.filename))
    av1_button.place(x=110, y=225)

    # QUIT
    quit_button = Button(root, text="Quit", width=5, command=root.destroy)
    quit_button.place(x=20, y=265)

    root.mainloop()

    return


main()
