import tkinter as tk
from tkinter import ttk, messagebox
import pymysql #sql connected 


class Movies:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Ticket Reservation")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(
            self.root,
            text="Movie Ticket Reservation",
            bd=4,
            relief="raised",
            fg="white",
            bg="gray",
            font=("Arial", 35, "bold")
        )
        title.pack(side="top", fill="x")

        self.frame = tk.Frame(
            self.root,
            bd=5,
            relief="ridge",
            bg=self.clr(250, 150, 150)
        )
        self.frame.place(
            width=self.width - 300,
            height=self.height - 180,
            x=150,
            y=100
        )

        tk.Label(
            self.frame,
            text="Select Show:",
            bg=self.clr(250, 150, 150),
            fg="white",
            font=("Arial", 15, "bold")
        ).grid(row=0, column=0, padx=20, pady=30)

        self.opt = ttk.Combobox(
            self.frame,
            values=("first", "second", "third"),
            width=18,
            state="readonly",
            font=("Arial", 15, "bold")
        )
        self.opt.set("Select One")
        self.opt.grid(row=0, column=1, padx=10)

        tk.Label(
            self.frame,
            text="Your Name:",
            bg=self.clr(250, 150, 150),
            fg="white",
            font=("Arial", 15, "bold")
        ).grid(row=0, column=2, padx=20)

        self.name = tk.Entry(
            self.frame,
            width=20,
            font=("Arial", 15, "bold")
        )
        self.name.grid(row=0, column=3, padx=10)

        tk.Button(
            self.frame,
            text="Reserve",
            width=10,
            font=("Arial", 15, "bold"),
            command=self.reserveFun
        ).grid(row=0, column=4, padx=20)

        self.tabFun()
        self.showFun()

    def tabFun(self):
        table_frame = tk.Frame(
            self.frame,
            bd=5,
            relief="sunken"
        )
        table_frame.place(
            x=50,
            y=90,
            width=self.width - 400,
            height=self.height - 300
        )

        x_scroll = tk.Scrollbar(
            table_frame,
            orient="horizontal"
        )
        x_scroll.pack(side="bottom", fill="x")

        y_scroll = tk.Scrollbar(
            table_frame,
            orient="vertical"
        )
        y_scroll.pack(side="right", fill="y")

        self.table = ttk.Treeview(
            table_frame,
            columns=(
                "show_no",
                "show_time",
                "movie_name",
                "price",
                "seats"
            ),
            xscrollcommand=x_scroll.set,
            yscrollcommand=y_scroll.set
        )

        x_scroll.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)

        self.table.heading("show_no", text="Show No")
        self.table.heading("show_time", text="Show Time")
        self.table.heading("movie_name", text="Movie Name")
        self.table.heading("price", text="Price")
        self.table.heading("seats", text="Seats")

        self.table["show"] = "headings"

        self.table.pack(fill="both", expand=True)

    def showFun(self):
        try:
            self.dbFun()

            self.cur.execute("SELECT * FROM movie")
            rows = self.cur.fetchall()

            self.table.delete(*self.table.get_children())

            for row in rows:
                self.table.insert("", tk.END, values=row)

            self.con.close()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    def reserveFun(self):
        show_no = self.opt.get()
        name = self.name.get().strip()

        if show_no == "Select One" or name == "":
            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )
            return

        try:
            self.dbFun()

            self.cur.execute(
                """
                SELECT show_time,
                       movie_name,
                       price,
                       seats
                FROM movie
                WHERE show_no=%s
                """,
                (show_no,)
            )

            row = self.cur.fetchone()

            if row is None:
                messagebox.showerror(
                    "Error",
                    "Show not found."
                )
                self.con.close()
                return

            if row[3] <= 0:
                messagebox.showerror(
                    "Error",
                    "No seats available."
                )
                self.con.close()
                return

            seats_left = row[3] - 1

            self.cur.execute(
                """
                UPDATE movie
                SET seats=%s
                WHERE show_no=%s
                """,
                (seats_left, show_no)
            )

            self.con.commit()
            self.con.close()

            messagebox.showinfo(
                "Success",
                f"Seat Reserved For: {name}\n\n"
                f"Movie: {row[1]}\n"
                f"Time: {row[0]}\n"
                f"Price: ₹{row[2]}"
            )

            self.showFun()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def dbFun(self):
        self.con = pymysql.connect(
            host="localhost",
            user="root",          # change if needed
            password="jit@12345",  # put actual password
            database="startersql"
        )

        self.cur = self.con.cursor()

    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"


root = tk.Tk()
obj = Movies(root)
root.mainloop()