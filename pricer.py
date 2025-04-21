import tkinter as tk
from tkinter import ttk, messagebox

def estimate_price(property_type, area, location, condition=None, details=None):
    base_price = {
        "urban": 5000,
        "suburban": 3000,
        "rural": 1500
    }.get(location.lower(), 3000)

    multiplier = 1

    if property_type == "House":
        if condition == "New":
            multiplier += 0.2
        elif condition == "Old":
            multiplier -= 0.2

        if details:
            rooms = int(details.get("rooms", 0))
            bathrooms = int(details.get("bathrooms", 0))
            parking = details.get("parking") == "Yes"
            garden = details.get("garden") == "Yes"
            pool = details.get("pool") == "Yes"

            multiplier += 0.02 * rooms
            multiplier += 0.03 * bathrooms
            multiplier += 0.05 if parking else 0
            multiplier += 0.04 if garden else 0
            multiplier += 0.06 if pool else 0

    return base_price * area * multiplier


class PropertyEstimatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("House/Land Price Estimator")
        self.create_main_screen()

    def create_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Select Property Type", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="House", width=20, height=2, command=self.house_form).pack(pady=10)
        tk.Button(self.root, text="Land", width=20, height=2, command=self.land_form).pack(pady=10)

    def land_form(self):
        self.property_form("Land")

    def house_form(self):
        self.property_form("House", allow_details=True)

    def property_form(self, prop_type, allow_details=False):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"{prop_type} Details", font=("Arial", 14)).pack(pady=10)

        # Area input
        tk.Label(self.root, text="Enter Area (sq ft):").pack()
        area_entry = tk.Entry(self.root)
        area_entry.pack()
        area_entry.focus()

        # Location
        tk.Label(self.root, text="Select Location Type:").pack()
        location_var = tk.StringVar(value="Urban")
        location_menu = ttk.Combobox(self.root, textvariable=location_var, values=["Urban", "Suburban", "Rural"], state="readonly")
        location_menu.pack()

        # Condition
        condition_var = tk.StringVar(value="New")
        if prop_type == "House":
            tk.Label(self.root, text="Select Condition:").pack()
            condition_menu = ttk.Combobox(self.root, textvariable=condition_var, values=["New", "Old", "Average"], state="readonly")
            condition_menu.pack()

        # More details toggle
        show_extra = tk.BooleanVar(value=False)
        extra_fields = {}

        def toggle_details():
            if show_extra.get():
                tk.Label(self.root, text="No. of Rooms:").pack()
                extra_fields["rooms"] = tk.Entry(self.root)
                extra_fields["rooms"].pack()

                tk.Label(self.root, text="No. of Bathrooms:").pack()
                extra_fields["bathrooms"] = tk.Entry(self.root)
                extra_fields["bathrooms"].pack()

                tk.Label(self.root, text="Parking (Yes/No):").pack()
                extra_fields["parking"] = ttk.Combobox(self.root, values=["Yes", "No"], state="readonly")
                extra_fields["parking"].pack()

                tk.Label(self.root, text="Garden (Yes/No):").pack()
                extra_fields["garden"] = ttk.Combobox(self.root, values=["Yes", "No"], state="readonly")
                extra_fields["garden"].pack()

                tk.Label(self.root, text="Pool (Yes/No):").pack()
                extra_fields["pool"] = ttk.Combobox(self.root, values=["Yes", "No"], state="readonly")
                extra_fields["pool"].pack()
            else:
                for widget in extra_fields.values():
                    widget.pack_forget()
                extra_fields.clear()

        if allow_details:
            tk.Checkbutton(self.root, text="Add More Details", variable=show_extra, command=toggle_details).pack(pady=5)

        # Submit function
        def submit(event=None):
            try:
                area = float(area_entry.get())
                location = location_var.get()
                condition = condition_var.get() if prop_type == "House" else None
                details = {}

                if show_extra.get():
                    for key, field in extra_fields.items():
                        details[key] = field.get()

                price = estimate_price(prop_type, area, location, condition, details)
                messagebox.showinfo("Estimated Price", f"Estimated Price: ₹{int(price):,}")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid inputs!")

        # Add Enter key focus change for input flow
        def bind_enter_jump(entries, final_action=None):
            for i in range(len(entries) - 1):
                entries[i].bind("<Return>", lambda e, nxt=entries[i + 1]: nxt.focus())
            if final_action:
                entries[-1].bind("<Return>", final_action)

        # Collect all fields to enable enter-key navigation
        entry_fields = [area_entry]
        if prop_type == "House":
            entry_fields.append(condition_menu)
        if allow_details:
            entry_fields.append(location_menu)

        # Submit button
        submit_btn = tk.Button(self.root, text="Estimate Price", command=submit)
        submit_btn.pack(pady=20)
        tk.Button(self.root, text="Back", command=self.create_main_screen).pack()

        self.root.bind("<Return>", submit)
        bind_enter_jump(entry_fields, final_action=lambda e: submit())

def start_app():
    root = tk.Tk()
    root.geometry("400x700")
    app = PropertyEstimatorApp(root)
    root.mainloop()

start_app()
