import tkinter as tk
from tkinter import messagebox
import time
import random

print("ENJOY YOUR TYPING PRACTICE !!!")

class WpmCalculator:
    def __init__(self, root):
        self.root = root

        self.root.title("WPM Calculator")

        self.root.geometry("800x400")

        custom_font = ("Comic Sans MS", 14, "bold")

        self.text_label = tk.Label(root, text="Type the following text:", font=custom_font)

        self.text_label.pack()

        self.sentences = [
            "The quick brown fox jumps over the lazy dog",
            "She sells seashells by the seashore",
            "How much wood would a woodchuck chuck if a woodchuck could chuck wood",
            "A quick brown dog jumps over a lazy cat",
        ]

        self.text_to_type = random.choice(self.sentences)

        self.text_display = tk.Label(root, text=self.text_to_type, font=custom_font)

        self.text_display.pack()

        self.entry_label = tk.Label(root, text="Type here:", font=custom_font)

        self.entry_label.pack()

        self.text_entry = tk.Entry(root, font=custom_font)

        self.text_entry.pack()

        self.start_button = tk.Button(root, text="Start Typing", command=self.toggle_typing, font=custom_font)

        self.start_button.pack()

        self.button_color = "green"

        self.calculate_button = tk.Button(root, text="Calculate WPM", state=tk.DISABLED, command=self.calculate_wpm, font=custom_font)

        self.calculate_button.pack()

        self.calculate_button.configure(bg="#5294f7", font=custom_font)

        self.timer_label = tk.Label(root, text="Timer: 0s", font=custom_font)

        self.timer_label.pack()

        self.result_label = tk.Label(root, text="WPM: 0", font=custom_font)

        self.result_label.pack()

        self.started = False

        self.start_time = 0

    def toggle_typing(self):
        if not self.started:
            self.started = True

            self.start_time = time.time()

            self.start_button.config(text="Stop Typing")

            self.button_color = "red"

            self.calculate_button.config(state=tk.DISABLED)

            self.text_entry.bind('<KeyRelease>', self.check_text)

        else:
            self.started = False

            self.start_button.config(text="Start Typing")

            self.button_color = "green"

            self.calculate_button.config(state=tk.NORMAL)

            self.text_entry.unbind('<KeyRelease>')

        self.start_button.configure(bg=self.button_color)

    def check_text(self, event):
        typed_text = self.text_entry.get()
        if typed_text == self.text_to_type:
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            self.timer_label.config(text=f"Timer: {int(elapsed_time)}s")

    def calculate_wpm(self):
        typed_text = self.text_entry.get()

        end_time = time.time()

        elapsed_time = end_time - self.start_time

        wpm = (len(typed_text) / 5) / (elapsed_time / 60)

        self.result_label.config(text=f"WPM: {wpm:.2f}")

        messagebox.showinfo("Typing Test", f"Your WPM: {wpm:.2f}")

        self.text_to_type = random.choice(self.sentences)

        self.text_display.config(text=self.text_to_type)

        self.text_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = WpmCalculator(root)
    root.mainloop()
