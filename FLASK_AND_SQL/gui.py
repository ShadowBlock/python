"""
Kasutab app.py poolt loodud Web API flaskis. Kasutab sealt GET, POST, PUT, DELETE meetodeid.
Tabeli loomiseks kasutasin Treeviewd.
Lisamise, uuendamise ja kustutamiseks tulevad andmelahtrid eraldi aknana.
Aja otsimiseks on lahter kohe olemas.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import requests


# Kasutab GET meetodit, et saada databaasi andmed tabelisse
def get_canteens(url='http://localhost:5000/'):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()


# Loome klassi CanteenGUI tkinteri GUI loomiseks
class CanteenGUI:
    def __init__(self, rootgui):
        # Kõikidele esialgu paneme Null, et PyCharm ei hakkaks karjuma.
        self.delete_button = None
        self.update_button = None
        self.id_entry = None
        self.id_label = None
        self.cancel_button = None
        self.add_button = None
        self.time_closed_entry = None
        self.time_closed_label = None
        self.time_open_entry = None
        self.time_open_label = None
        self.location_entry = None
        self.location_label = None
        self.name_entry = None
        self.name_label = None

        self.root = rootgui
        self.root.title("Canteens")
        self.root.geometry("700x650")

        # Tabeli pealkirjad
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("ID", "Name", "Location", "Open", "Closed")
        self.tree.heading("#0", text="", anchor="w")
        self.tree.column("#0", anchor="w", width=1)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Location", text="Location")
        self.tree.heading("Open", text="Opens")
        self.tree.heading("Closed", text="Closes")

        # Mõned veerud väiksemaks
        self.tree.column("ID", width=30)
        self.tree.column("Open", width=80)
        self.tree.column("Closed", width=80)

        self.tree.pack(expand=True, fill="both")

        # Kõik nupud
        self.data_button = tk.Button(self.root,
                                     text="Get All Canteen Data", command=self.canteen_table)
        self.data_button.pack(pady=5)
        self.time_label = tk.Label(self.root, text="Enter Time Range (HH:MM-HH:MM):")
        self.time_label.pack(pady=5)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack(pady=5)
        self.time_button = tk.Button(self.root, text="Get Canteens by Time Range", command=self.canteens_by_time)
        self.time_button.pack(pady=5)
        self.add_canteen_button = tk.Button(self.root, text="Add Canteen", command=self.add_canteen_window)
        self.add_canteen_button.pack(pady=5)
        self.update_canteen_button = tk.Button(self.root, text="Update Canteen", command=self.update_canteen_window)
        self.update_canteen_button.pack(pady=5)
        self.delete_canteen_button = tk.Button(self.root, text="Delete Canteen", command=self.delete_canteen_window)
        self.delete_canteen_button.pack(pady=5)
        self.close_button = tk.Button(self.root, text="Close Window", command=self.root.quit)
        self.close_button.pack(pady=5)

    # Võtab sööklate info Web APIst ja näitab Treeview tabelina
    def canteen_table(self):
        self.clear_table()
        canteens = get_canteens()
        for canteen in canteens:
            self.tree.insert("", "end",
                             text="", values=(canteen['ID'], canteen['NAME'],
                                              canteen['LOCATION'], canteen['TIME_OPEN'], canteen['TIME_CLOSED']))

    # Võtab vastavalt useri sisestatud kellaaegadele õiged sööklad ja näitab tabelis
    def canteens_by_time(self):
        time_range = self.time_entry.get()
        url = f"http://127.0.0.1:5000/canteens_by_time?time_range={time_range}"
        canteens = get_canteens(url)
        self.clear_table()
        for canteen in canteens:
            self.tree.insert("", "end",
                             text="", values=(canteen['ID'], canteen['NAME'], canteen['LOCATION'],
                                              canteen['TIME_OPEN'], canteen['TIME_CLOSED']))

    # Aken söökla lisamiseks andmetele
    def add_canteen_window(self):
        self.add_canteen_window = tk.Toplevel(self.root)
        self.add_canteen_window.title("Add Canteen")

        self.name_label = tk.Label(self.add_canteen_window, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.add_canteen_window)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.location_label = tk.Label(self.add_canteen_window, text="Location:")
        self.location_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.location_entry = tk.Entry(self.add_canteen_window)
        self.location_entry.grid(row=1, column=1, padx=5, pady=5)

        self.time_open_label = tk.Label(self.add_canteen_window, text="Opening Time (HH:MM):")
        self.time_open_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.time_open_entry = tk.Entry(self.add_canteen_window)
        self.time_open_entry.grid(row=2, column=1, padx=5, pady=5)

        self.time_closed_label = tk.Label(self.add_canteen_window, text="Closing Time (HH:MM):")
        self.time_closed_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.time_closed_entry = tk.Entry(self.add_canteen_window)
        self.time_closed_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.add_canteen_window, text="Add", command=self.add_canteen)
        self.add_button.grid(row=4, column=1, padx=5, pady=5)

        self.cancel_button = tk.Button(self.add_canteen_window, text="Cancel",
                                       command=self.add_canteen_window.destroy)
        self.cancel_button.grid(row=5, column=1, padx=5, pady=5)

    # Aken sööklate uuendamise andmetele
    def update_canteen_window(self):
        self.update_canteen_window = tk.Toplevel(self.root)
        self.update_canteen_window.title("Update Canteen")

        self.id_label = tk.Label(self.update_canteen_window, text="Canteen ID:")
        self.id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.id_entry = tk.Entry(self.update_canteen_window)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.name_label = tk.Label(self.update_canteen_window, text="Name:")
        self.name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.update_canteen_window)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.location_label = tk.Label(self.update_canteen_window, text="Location:")
        self.location_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.location_entry = tk.Entry(self.update_canteen_window)
        self.location_entry.grid(row=2, column=1, padx=5, pady=5)

        self.time_open_label = tk.Label(self.update_canteen_window, text="Opening Time (HH:MM):")
        self.time_open_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.time_open_entry = tk.Entry(self.update_canteen_window)
        self.time_open_entry.grid(row=3, column=1, padx=5, pady=5)

        self.time_closed_label = tk.Label(self.update_canteen_window, text="Closing Time (HH:MM):")
        self.time_closed_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.time_closed_entry = tk.Entry(self.update_canteen_window)
        self.time_closed_entry.grid(row=4, column=1, padx=5, pady=5)

        self.update_button = tk.Button(self.update_canteen_window, text="Update", command=self.update_canteen)
        self.update_button.grid(row=5, column=1, padx=5, pady=5)

        self.cancel_button = tk.Button(self.update_canteen_window, text="Cancel",
                                       command=self.update_canteen_window.destroy)
        self.cancel_button.grid(row=6, column=1, padx=5, pady=5)

    # Aken kustutamiseks, küsib ainult ID-d
    def delete_canteen_window(self):
        self.delete_canteen_window = tk.Toplevel(self.root)
        self.delete_canteen_window.title("Delete Canteen")

        self.id_label = tk.Label(self.delete_canteen_window, text="Canteen ID:")
        self.id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.id_entry = tk.Entry(self.delete_canteen_window)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(self.delete_canteen_window, text="Delete", command=self.delete_canteen)
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)

        self.cancel_button = tk.Button(self.delete_canteen_window, text="Cancel",
                                       command=self.delete_canteen_window.destroy)
        self.cancel_button.grid(row=2, column=1, padx=5, pady=5)

    # Saadab JSONiga POST requesti Web APIle, et teha uus söökla, uuendab tabelit ka
    def add_canteen(self):
        name = self.name_entry.get()
        location = self.location_entry.get()
        time_open = self.time_open_entry.get()
        time_closed = self.time_closed_entry.get()

        if name and location and time_open and time_closed:
            payload = {
                "NAME": name,
                "LOCATION": location,
                "TIME_OPEN": time_open,
                "TIME_CLOSED": time_closed
            }
            response = requests.post("http://127.0.0.1:5000/canteens", json=payload)
            if response.status_code == 201:
                self.add_canteen_window.destroy()
                self.canteen_table()
            else:
                messagebox.showerror("Error", "Canteen was not added.")
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

    # Saadab JSONiga PUT requesti söökla andmete uuendamiseks
    def update_canteen(self):
        canteen_id = self.id_entry.get()
        name = self.name_entry.get()
        location = self.location_entry.get()
        time_open = self.time_open_entry.get()
        time_closed = self.time_closed_entry.get()

        if canteen_id and name and location and time_open and time_closed:
            payload = {
                "NAME": name,
                "LOCATION": location,
                "TIME_OPEN": time_open,
                "TIME_CLOSED": time_closed
            }
            url = f"http://127.0.0.1:5000/canteens/{canteen_id}"
            response = requests.put(url, json=payload)
            if response.status_code == 200:
                self.update_canteen_window.destroy()
                self.canteen_table()
            else:
                messagebox.showerror("Error", "Failed to update canteen.")
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

    # Saadab DELETE requesti söökla kustutamiseks databaasist
    def delete_canteen(self):
        canteen_id = self.id_entry.get()

        if canteen_id:
            url = f"http://127.0.0.1:5000/canteens/{canteen_id}"
            response = requests.delete(url)
            if response.status_code == 200:
                self.delete_canteen_window.destroy()
                self.canteen_table()
            else:
                messagebox.showerror("Error", "Canteen not deleted.")
        else:
            messagebox.showerror("Error", "Please enter correct ID.")

    # Kustutab tabeli, et uuesti lisada sinna
    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = CanteenGUI(root)
    root.mainloop()
