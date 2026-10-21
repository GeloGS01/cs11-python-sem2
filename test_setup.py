"""
CS11 Python - Setup Check
Run this once at the start of the semester:  python test_setup.py
Each check prints PASS or FAIL.
"""
import os
import sys

GREEN = "\033[32m"
RED = "\033[31m"
BOLD = "\033[1m"
RESET = "\033[0m"


def result(name, ok, detail=""):
    tag = f"{GREEN}PASS{RESET}" if ok else f"{RED}FAIL{RESET}"
    print(f"[{tag}] {name}" + (f"  ->  {detail}" if detail else ""))


print(f"{BOLD}CS11 Python - Setup Check{RESET}\n")

# 0. Python version
result("Python version", sys.version_info >= (3, 9), sys.version.split()[0])

# 1. File handling (Lesson 1)
try:
    with open("test_output.txt", "w") as f:
        f.write("If you can read this, file handling works.\n")
    with open("test_output.txt") as f:
        text = f.read().strip()
    result("File handling", text.startswith("If you can"), "created test_output.txt")
except Exception as e:
    result("File handling", False, e)

# 2. Time zones (Lesson 2)
try:
    from datetime import datetime
    from zoneinfo import ZoneInfo
    fmt = "%H:%M"
    bkk = datetime.now(ZoneInfo("Asia/Bangkok")).strftime(fmt)
    lon = datetime.now(ZoneInfo("Europe/London")).strftime(fmt)
    nyc = datetime.now(ZoneInfo("America/New_York")).strftime(fmt)
    result("Time zones", True, f"Bangkok {bkk} | London {lon} | New York {nyc}")
except Exception as e:
    result("Time zones", False, e)

# 3. Custom module (Lesson 5)
try:
    import setup_helper
    result("Custom module", True, setup_helper.greet("CS11"))
except Exception as e:
    result("Custom module", False, e)

# 4. Console codes (Lesson 6)
print(f"[{GREEN}PASS{RESET}] Console codes  ->  "
      f"{RED}red{RESET} {GREEN}green{RESET} \033[34mblue{RESET} {BOLD}bold{RESET}"
      "   (if you see colours, not strange symbols, it works)")

# 5. GUI (Lessons 3-4) - run last because the window waits until it is closed
try:
    import tkinter as tk
    root = tk.Tk()
    root.title("Setup Check")
    root.geometry("360x160")
    tk.Label(root, text="tkinter works!", font=("Arial", 20)).pack(pady=20)
    tk.Button(root, text="Close", command=root.destroy).pack()
    result("GUI (tkinter)", True, "window opened - view it on the GUI Desktop tab (port 6080), then click Close")
    root.mainloop()
except Exception as e:
    result("GUI (tkinter)", False, e)
    if not os.environ.get("DISPLAY"):
        print("   Hint: no DISPLAY set - this check only works inside the Codespace or on a computer with a screen.")

print("\nDone.")
