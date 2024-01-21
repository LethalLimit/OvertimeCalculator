import tkinter as tk
from tkinter import messagebox

# Calculate the overtime bonus
def calculate_overtime_bonus():
    try:
        quota = float(quota_entry.get())
        sold_scrap_value = float(sold_scrap_value_entry.get())
        days_until_deadline = int(days_until_deadline_entry.get())
        if days_until_deadline == 0:
            days_until_deadline = -1
        overtime_bonus = max(0, (sold_scrap_value - quota) / 5 + 15 * (days_until_deadline))
        overtime_bonus_var.set(f"Overtime Bonus: {int(overtime_bonus)}")
    except ValueError as e:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Set up the main window
root = tk.Tk()
root.title("Overtime Bonus Calculator")
root.configure(bg="#8B0000")

# Set up the variable for overtime bonus display
overtime_bonus_var = tk.StringVar(root, "Overtime Bonus: 0")

# Instructions
instructions = tk.Label(root, text="Press Enter after typing to calculate Overtime Bonus", bg="#8B0000", fg="white")
instructions.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=(20, 0))

# Entry field configurations
entry_bg = "#000080"  # Darker blue background for entry fields
entry_fg = "#00FF00"  # Text color for entry fields (green)

# Quota
quota_label = tk.Label(root, text="Quota:", bg="#8B0000", fg="white")
quota_label.grid(row=1, column=0, sticky="e", padx=(20, 0), pady=(10, 0))
quota_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
quota_entry.grid(row=1, column=1, sticky="we", padx=(0, 20), pady=(10, 0))

# Sold Scrap Value
sold_scrap_value_label = tk.Label(root, text="Sold Scrap Value:", bg="#8B0000", fg="white")
sold_scrap_value_label.grid(row=2, column=0, sticky="e", padx=(20, 0), pady=(10, 0))
sold_scrap_value_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
sold_scrap_value_entry.grid(row=2, column=1, sticky="we", padx=(0, 20), pady=(10, 0))

# Days until Deadline
days_until_deadline_label = tk.Label(root, text="Days until Deadline:", bg="#8B0000", fg="white")
days_until_deadline_label.grid(row=3, column=0, sticky="e", padx=(20, 0), pady=(10, 0))
days_until_deadline_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
days_until_deadline_entry.insert(0, "0")  # Default value set to 0
days_until_deadline_entry.grid(row=3, column=1, sticky="we", padx=(0, 20), pady=(10, 0))

# Overtime Bonus
overtime_bonus_label = tk.Label(root, textvariable=overtime_bonus_var, bg="#8B0000", fg="white")
overtime_bonus_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=20, pady=(10, 20))

# Calculate button binding to the Enter key
root.bind('<Return>', lambda event: calculate_overtime_bonus())

# Set focus on the Quota entry
quota_entry.focus_set()

# Start the main loop
root.mainloop()
