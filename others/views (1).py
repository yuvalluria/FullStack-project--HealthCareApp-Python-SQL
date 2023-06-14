import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkcalendar import DateEntry


class Views():
    def __init__(self,app):
        # ttk.Frame.__init__(self, master=app, borderwidth=5, width=200, height=10)
        self.window = tk.Tk()
        self.window.title("Organ Donation App")
        self.screen0(app)

    def run(self):
        self.window.mainloop()
    def screen0(self,app):
        # Get screen dimensions
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate window dimensions
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.6)

        # Calculate window position
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        # Set window size and position
        self.window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Load the background image
        image_path = "Background.jpg"
        self.background_image = ImageTk.PhotoImage(Image.open(image_path))

        # Create a background label and place it in the window
        background_label = ttk.Label(self.window, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a title label
        title_label = ttk.Label(self.window, text="Organ Donation App", font=('Times New Roman', 36, "bold"),
                                foreground="#1E6FBA", background="SystemButtonFace")
        title_label.pack(pady=20)

        button_frame = ttk.Frame(self.window, width=int(self.window.winfo_screenwidth() * 0.7),
                                 height=int(self.window.winfo_screenheight() * 0.7))
        button_frame.pack()

        button_style = ttk.Style()
        button_style.configure("TButton", font=('Times New Roman', 26), width=20, background="SystemButtonFace",
                               focuscolor="systemTransparent", lightcolor="systemTransparent",
                               darkcolor="systemTransparent", troughcolor="systemTransparent")

        add_patient_button = ttk.Button(button_frame, text="Add New Patient", command=lambda : self.add_new_patient(app),
                                        style="TButton")
        add_patient_button.grid(row=0, column=1, padx=5, pady=15, sticky="e")

        add_donor_button = ttk.Button(button_frame, text="Add New Donor", command=lambda : self.add_new_donor(app), style="TButton")
        add_donor_button.grid(row=1, column=1, padx=5, pady=15, sticky="e")

        view_organs_button = ttk.Button(button_frame, text="View Available Organs", command=lambda : self.view_available_organs,
                                        style="TButton")
        view_organs_button.grid(row=2, column=1, padx=5, pady=15, sticky="e")

        view_matching_button = ttk.Button(button_frame, text="View Matching Organs", command=lambda : self.view_matching_organs,
                                          style="TButton")
        view_matching_button.grid(row=3, column=1, padx=5, pady=15, sticky="e")

        # Configure grid weights for button frame to fill the window
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.rowconfigure((0, 1, 2, 3), weight=1)

    def view_available_organs(self):
        print("View Available Organs button clicked")

    def view_matching_organs(self):
        print("View Matching Organs button clicked")

        # Create an instance of the Main_Screen class and run the application
    def add_new_patient(self, app):
        self.window = tk.Toplevel()
        self.window.title("Add New Patient")

        # Create labels and entry fields
        id_Patient_label = ttk.Label(self.window, text="ID Patient:")
        id_Patient_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.id_entry = ttk.Entry(self.window)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)

        first_name_label = ttk.Label(self.window, text="First Name:")
        first_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.first_name_entry = ttk.Entry(self.window)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=10)

        last_name_label = ttk.Label(self.window, text="Last Name:")
        last_name_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.last_name_entry = ttk.Entry(self.window)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create dropdown list for gender
        gender_label = ttk.Label(self.window, text="Select Your Gender:")
        gender_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.gender_var = tk.StringVar()
        self.gender_dropdown = ttk.Combobox(self.window, textvariable=self.gender_var, values=["Male", "Female"])
        self.gender_dropdown.grid(row=3, column=1, padx=10, pady=10)

        # Create dropdown list for blood type
        blood_type_label = ttk.Label(self.window, text="Select Your Blood Type:")
        blood_type_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.blood_type_var = tk.StringVar()
        self.blood_type_dropdown = ttk.Combobox(self.window, textvariable=self.blood_type_var,
                                                values=["A", "B", "AB", "O"])
        self.blood_type_dropdown.grid(row=4, column=1, padx=10, pady=10)

        # Create date of birth (calendar widget)
        dob_label = ttk.Label(self.window, text="Date of Birth:")
        dob_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.dob_calendar = DateEntry(self.window, date_pattern="yyyy-mm-dd")
        self.dob_calendar.grid(row=5, column=1, padx=10, pady=10)

        # Create checkboxes for needed organs
        needed_organs_label = ttk.Label(self.window, text="Needed organs:")
        needed_organs_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.heart_var = tk.IntVar()
        self.liver_var = tk.IntVar()
        self.kidney_var = tk.IntVar()
        heart_checkbox = ttk.Checkbutton(self.window, text="Heart", variable=self.heart_var)
        heart_checkbox.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        liver_checkbox = ttk.Checkbutton(self.window, text="Liver", variable=self.liver_var)
        liver_checkbox.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        kidney_checkbox = ttk.Checkbutton(self.window, text="Kidney", variable=self.kidney_var)
        kidney_checkbox.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        # Create submit button
        submit_button = ttk.Button(self.window, text="Submit", command=self.submit_patient(app))
        submit_button.grid(row=9, column=1, padx=10, pady=20, sticky="e")

    def submit_patient(self,app):
        # Get the values entered by the user
        patient_id = self.id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        gender = self.gender_var.get()
        blood_type = self.blood_type_var.get()
        dob = self.dob_calendar.get_date()
        needed_organs = []
        if self.heart_var.get():
            needed_organs.append("Heart")
        if self.liver_var.get():
            needed_organs.append("Liver")
        if self.kidney_var.get():
            needed_organs.append("Kidney")

        # Print the values (you can replace this with your desired functionality)
        print("Patient ID:", patient_id)
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Gender:", gender)
        print("Blood Type:", blood_type)
        print("Date of Birth:", dob)
        print("Needed Organs:", needed_organs)

    def add_new_donor(self,app):
        self.window = tk.Toplevel()
        self.window.title("Add New Donor")

        # Create a title label
        title_label = ttk.Label(self.window, text="Add your information and save lives!", font=('Times New Roman', 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=20)

        # Create the ID Donor label and entry
        id_Donor_label = ttk.Label(self.window, text="ID Donor:")
        id_Donor_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        id_entry = ttk.Entry(self.window)
        id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Create the First Name label and entry
        first_name_label = ttk.Label(self.window, text="First Name:")
        first_name_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        first_name_entry = ttk.Entry(self.window)
        first_name_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Create the Last Name label and entry
        last_name_label = ttk.Label(self.window, text="Last Name:")
        last_name_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        last_name_entry = ttk.Entry(self.window)
        last_name_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Create the Gender label and dropdown
        gender_label = ttk.Label(self.window, text="Select Your Gender:")
        gender_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        gender_combobox = ttk.Combobox(self.window, values=["Male", "Female", "Other"])
        gender_combobox.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Create the Blood Type label and dropdown
        blood_type_label = ttk.Label(self.window, text="Select Your Blood Type:")
        blood_type_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        blood_type_combobox = ttk.Combobox(self.window, values=["A", "B", "AB", "O"])
        blood_type_combobox.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        # Create the Date of Birth label and calendar
        dob_label = ttk.Label(self.window, text="Date of Birth:")
        dob_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        dob_calendar = DateEntry(self.window, date_pattern='yyyy-mm-dd')
        dob_calendar.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        # Create the Status label and radio buttons
        status_label = ttk.Label(self.window, text="Status:")
        status_label.grid(row=7, column=0, padx=10, pady=10, sticky="e")
        status_var = tk.StringVar()
        alive_radio = ttk.Radiobutton(self.window, text="Alive", variable=status_var, value="Alive")
        alive_radio.grid(row=7, column=1, padx=10, pady=10, sticky="w")
        deceased_radio = ttk.Radiobutton(self.window, text="Deceased", variable=status_var, value="Deceased")
        deceased_radio.grid(row=7, column=2, padx=10, pady=10, sticky="w")

        # Create the Organs Donation label and checkboxes
        organs_label = ttk.Label(self.window, text="Organ Donation:")
        organs_label.grid(row=8, column=0, padx=10, pady=10, sticky="e")
        heart_checkbox = ttk.Checkbutton(self.window, text="Heart")
        heart_checkbox.grid(row=8, column=1, padx=10, pady=5, sticky="w")
        liver_checkbox = ttk.Checkbutton(self.window, text="Liver")
        liver_checkbox.grid(row=9, column=1, padx=10, pady=5, sticky="w")
        kidney_checkbox = ttk.Checkbutton(self.window, text="Kidney")
        kidney_checkbox.grid(row=10, column=1, padx=10, pady=5, sticky="w")

        # Create the Submit button
        submit_button = ttk.Button(self.window, text="Submit", command=self.submit(app))
        submit_button.grid(row=11, column=2, padx=10, pady=20, sticky="e")

    def submit(self,app):
        # Perform submission logic here
        print("Submit button clicked")
