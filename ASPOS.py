# Author: Vassey Konneh and Leocalis Quezada
# Date: 04/10/2026
# Description: Main file for starting the ASPOS program.

import tkinter as tk
from GUI import ASPOSGUI


def main():
    """Start the ASPOS GUI application."""
    root = tk.Tk()
    app = ASPOSGUI(root, 'student_learning_trajectory.csv')
    root.mainloop()


if __name__ == "__main__":
    main()
