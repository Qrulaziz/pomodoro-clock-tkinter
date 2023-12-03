from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
MINT = "#C5FFF8"
PURPLE = "#7B66FF"
BLUE = "#5FBDFF"
YELLOW = "#F4F27E"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", font=(FONT_NAME, 32, "bold"))
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=MINT)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=MINT)
    else:
        count_down(work_sec)
        title_label.config(text="Working",fg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}", font=(FONT_NAME, 33, "bold"))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
    
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro Clock")
window.config(padx=52, pady=52, bg=BLUE)


canvas = Canvas(width=342, height=284, bg=BLUE, highlightthickness=0)
owl_img = PhotoImage(file="clock.png")
canvas.create_image(171, 142, image=owl_img)
timer_text = canvas.create_text(171, 164, text="00:00", font=(FONT_NAME, 32, "bold"), fill="white")
canvas.grid(column=1, row=1)


# Label
title_label = Label(text="Timer", font=(FONT_NAME, 52))
title_label.config(fg=YELLOW, bg=BLUE)
title_label.grid(column=1, row=0)

# Button
start_button = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 16, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 16, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=MINT, bg=BLUE, font=(FONT_NAME, 24))
check_marks.grid(column=1, row=3)

window.mainloop()