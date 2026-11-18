
import tkinter as tk
from tkinter import messagebox
from checker import check_password
from storage import save_record, load_records, search_records

class PasswordApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("650x550")
        self.root.configure(bg="#101827")

        tk.Label(
            root,
            text="PASSWORD STRENGTH CHECKER",
            font=("Arial", 20, "bold"),
            bg="#101827",
            fg="white"
        ).pack(pady=25)

        tk.Label(
            root,
            text="Enter your password",
            bg="#101827",
            fg="white",
            font=("Arial", 12)
        ).pack()

        self.password = tk.Entry(
            root, width=35, show="*",
            font=("Arial", 14)
        )
        self.password.pack(pady=15)

        self.show_var = tk.BooleanVar(value=False)

        tk.Checkbutton(
            root,
            text="Show password",
            variable=self.show_var,
            command=self.toggle_password,
            bg="#101827",
            fg="white",
            selectcolor="#101827"
        ).pack()

        tk.Button(
            root,
            text="CHECK PASSWORD",
            command=self.check,
            bg="#2563eb",
            fg="white",
            font=("Arial", 12, "bold"),
            width=22
        ).pack(pady=20)

        self.result = tk.Label(
            root, text="Your result will appear here",
            bg="#101827", fg="#38bdf8",
            font=("Arial", 16, "bold")
        )
        self.result.pack(pady=10)

        self.suggestions = tk.Label(
            root, text="", bg="#101827",
            fg="white", font=("Arial", 11),
            justify="left"
        )
        self.suggestions.pack(pady=10)

        tk.Button(
            root, text="VIEW SUMMARY",
            command=self.summary,
            bg="#059669", fg="white",
            width=20
        ).pack(pady=10)

        tk.Button(
            root, text="SEARCH RECORDS",
            command=self.search,
            bg="#7c3aed", fg="white",
            width=20
        ).pack(pady=5)

    def toggle_password(self):
        self.password.config(
            show="" if self.show_var.get() else "*"
        )

    def check(self):
        value = self.password.get()

        if not value:
            messagebox.showwarning(
                "Warning", "Please enter a password"
            )
            return

        if len(value) > 128:
            messagebox.showwarning(
                "Warning", "Password is too long"
            )
            return

        strength, tips = check_password(value)

        self.result.config(text="Strength: " + strength)

        self.suggestions.config(
            text="\n".join(tips) if tips
            else "Excellent! All basic rules passed."
        )

        save_record(strength)

        # Clear password from the input after checking
        self.password.delete(0, tk.END)

    def summary(self):
        records = load_records()

        total = len(records)
        weak = sum(r["strength"] == "Weak" for r in records)
        medium = sum(r["strength"] == "Medium" for r in records)
        strong = sum(r["strength"] == "Strong" for r in records)

        messagebox.showinfo(
            "Summary",
            f"Total checks: {total}\n"
            f"Weak: {weak}\n"
            f"Medium: {medium}\n"
            f"Strong: {strong}"
        )

    def search(self):
        from tkinter import simpledialog

        keyword = simpledialog.askstring(
            "Search", "Enter Weak, Medium or Strong:"
        )

        if keyword:
            results = search_records(keyword)

            messagebox.showinfo(
                "Search Results",
                "\n".join(
                    r["date"] + " - " + r["strength"]
                    for r in results
                ) if results else "No records found"
            )
