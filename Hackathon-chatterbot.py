import tkinter as tk
from tkinter import messagebox

# Function to simulate sending OTP (fixed OTP for testing)
def send_otp(pnr):
    otp = "111111"  # Fixed OTP for testing
    print(f"OTP for PNR {pnr}: {otp}")  # Display OTP on the console for testing
    return otp

# Function to simulate backend for ticket booking
def book_ticket(from_location, to_location, depart_date, return_date, ticket_type):
    return f"Booking successful! Ticket from {from_location} to {to_location} (Depart: {depart_date}, Return: {return_date}) ({ticket_type})."

# Function to simulate backend for ticket cancellation
def cancel_ticket(ticket_id):
    return f"Ticket {ticket_id} cancelled. Refund status: Processing."

# Function to display Frequently Asked Questions
def show_faqs():
    faqs = """
    1. How to book a ticket? - Go to the booking section and provide travel details.
    2. How to cancel a ticket? - Enter your ticket ID in the cancel section.
    3. When will I get my refund? - Refunds are processed within 5-7 business days.
    """
    messagebox.showinfo("FAQs", faqs)

# Function to collect feedback
def submit_feedback(feedback):
    print(f"Feedback received: {feedback}")
    messagebox.showinfo("Thank you!", "Thank you for your feedback!")

# Function to handle ticket booking form
def create_booking_form(parent):
    booking_frame = tk.Frame(parent)
    booking_frame.pack(pady=10)

    tk.Label(booking_frame, text="From").grid(row=0, column=0, pady=5)
    tk.Label(booking_frame, text="To").grid(row=1, column=0, pady=5)
    tk.Label(booking_frame, text="Depart Date").grid(row=2, column=0, pady=5)
    tk.Label(booking_frame, text="Return Date").grid(row=3, column=0, pady=5)
    tk.Label(booking_frame, text="Ticket Type").grid(row=4, column=0, pady=5)

    from_entry = tk.Entry(booking_frame)
    to_entry = tk.Entry(booking_frame)
    depart_entry = tk.Entry(booking_frame)
    return_entry = tk.Entry(booking_frame)
    
    ticket_type = tk.StringVar(value="Economy")
    tk.Radiobutton(booking_frame, text="Economy", variable=ticket_type, value="Economy").grid(row=4, column=1)
    tk.Radiobutton(booking_frame, text="Business", variable=ticket_type, value="Business").grid(row=4, column=2)

    from_entry.grid(row=0, column=1)
    to_entry.grid(row=1, column=1)
    depart_entry.grid(row=2, column=1)
    return_entry.grid(row=3, column=1)

    # Function to confirm booking
    def confirm_booking():
        from_location = from_entry.get()
        to_location = to_entry.get()
        depart_date = depart_entry.get()
        return_date = return_entry.get()
        ticket = ticket_type.get()
        if not from_location or not to_location or not depart_date or not return_date:
            messagebox.showerror("Error", "Please fill all details.")
            return
        booking_msg = book_ticket(from_location, to_location, depart_date, return_date, ticket)
        messagebox.showinfo("Booking Confirmation", booking_msg)

    confirm_btn = tk.Button(booking_frame, text="Confirm Booking", command=confirm_booking, bg="blue", fg="white")
    confirm_btn.grid(row=5, column=1, pady=10)

# Function to handle ticket cancellation form
def ticket_cancellation():
    cancel_window = tk.Toplevel()
    cancel_window.title("Ticket Cancellation")

    tk.Label(cancel_window, text="Enter Ticket ID").grid(row=0, column=0, pady=5)
    ticket_id_entry = tk.Entry(cancel_window)
    ticket_id_entry.grid(row=0, column=1)

    # Function to cancel the ticket
    def cancel_ticket_func():
        ticket_id = ticket_id_entry.get()
        if not ticket_id:
            messagebox.showerror("Error", "Please enter a ticket ID.")
            return
        cancel_msg = cancel_ticket(ticket_id)
        messagebox.showinfo("Cancellation Status", cancel_msg)
        cancel_window.destroy()

    tk.Button(cancel_window, text="Cancel Ticket", command=cancel_ticket_func).grid(row=1, column=1, pady=10)

# Function to handle PNR authentication after selecting an issue
def pnr_authentication(selected_issue):
    auth_window = tk.Toplevel()
    auth_window.title(f"PNR Authentication for {selected_issue}")

    tk.Label(auth_window, text="Enter your PNR number for verification:").grid(row=0, column=0, pady=5)
    pnr_entry = tk.Entry(auth_window)
    pnr_entry.grid(row=0, column=1)

    def verify_pnr():
        user_pnr = pnr_entry.get()
        if not user_pnr:
            messagebox.showerror("Error", "Please enter your PNR number.")
            return
        otp = send_otp(user_pnr)

        # OTP Verification Window
        otp_window = tk.Toplevel()
        otp_window.title("OTP Verification")
        tk.Label(otp_window, text="Enter OTP sent to your email:").grid(row=0, column=0, pady=5)
        otp_entry = tk.Entry(otp_window)
        otp_entry.grid(row=0, column=1)

        # Function to verify OTP
        def check_otp():
            entered_otp = otp_entry.get()
            if entered_otp == otp:
                messagebox.showinfo("Success", f"OTP Verified! You selected '{selected_issue}'.")
                otp_window.destroy()
                auth_window.destroy()
                # Continue to the specific service (e.g., cancel ticket or show FAQs)
                if selected_issue == 'Voluntary Cancel':
                    ticket_cancellation()
                elif selected_issue == 'FAQs':
                    show_faqs()
                elif selected_issue == 'Submit Feedback':
                    submit_feedback("Good Service")
            else:
                messagebox.showerror("Error", "Incorrect OTP. Try again.")

        tk.Button(otp_window, text="Verify OTP", command=check_otp).grid(row=1, column=1, pady=10)

    tk.Button(auth_window, text="Send OTP", command=verify_pnr).grid(row=1, column=1, pady=10)

# Function to display post-authentication options with icons
def show_main_options():
    main_window = tk.Tk()
    main_window.title("Customer Support - Issue Selection")

    # "Welcome" text
    tk.Label(main_window, text="Welcome, how may I help you today?", font=("Arial", 14)).pack(pady=10)

    # Create the booking form at the top
    create_booking_form(main_window)

    tk.Label(main_window, text="Looking for something else?", font=("Arial", 12)).pack(pady=5)

    # Create buttons for each option
    def handle_selection(choice):
        pnr_authentication(choice)

    # List of issues
    issues = [
        "Digital Support",
        "MileagePlus",
        "Post Flight",
        "Products and Services",
        "Schedule Change",
        "Seating",
        "Traveler Updates",
        "Upgrade",
        "Voluntary Cancel",
        "Voluntary Change",
        "FAQs",
        "Submit Feedback",
    ]

    # Create a frame for the buttons
    button_frame = tk.Frame(main_window)
    button_frame.pack(pady=10)

    # Create a grid of buttons for each issue in two columns
    for idx, issue in enumerate(issues):
        btn = tk.Button(button_frame, text=issue, width=20, height=2, command=lambda c=issue: handle_selection(c))
        # Place each button in a 2-column layout
        row = idx // 2  # Row number based on index
        column = idx % 2  # Column number based on index
        btn.grid(row=row, column=column, padx=5, pady=5)

    # "Other" section that redirects to customer care phone number
    def other_issue():
        messagebox.showinfo("Redirect", "For other issues, please call customer care at +44 1025606")

    # Button for "Other" section
    other_button = tk.Button(button_frame, text="Other Issues", width=20, height=2, command=other_issue)
    other_button.grid(row=len(issues) // 2, columnspan=2, pady=10)  # Place it below the issues

    main_window.mainloop()

# Run the chatbot
show_main_options()
