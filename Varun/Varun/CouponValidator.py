import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class CouponValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coupon Code Validator - Professional Edition")
        
        # Set to fullscreen
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='white')
        
        # Configure colors with meaningful names
        self.colors = {
            "background": "white",
            "success_green": "green",
            "error_red": "red",
            "dark_blue": "dark blue",
            "white": "white",
            "light_green": "light green",
            "light_red": "light coral",
            "header_blue": "steel blue",
            "border_gray": "light gray"
        }
        
        # Create main container with scrollbar
        self.create_scrollable_interface()
        
        # Valid coupons database with clear descriptions - FIXED EXPIRY DATES
        self.valid_coupons = {
            "WELCOME10": {
                "discount": "10% OFF",
                "description": "Perfect for your first order - enjoy 10% off everything!",
                "expiry": "2026-12-31",  # Future date
                "min_purchase": 0,
                "category": "Welcome Offer"
            },
            "SUMMER25": {
                "discount": "25% OFF", 
                "description": "Summer special! Get 25% off on orders over $100",
                "expiry": "2026-12-31",  # Future date
                "min_purchase": 100,
                "category": "Seasonal"
            },
            "FREESHIP": {
                "discount": "FREE SHIPPING",
                "description": "We'll cover the shipping costs for your order",
                "expiry": "2026-12-31",  # Future date
                "min_purchase": 0,
                "category": "Shipping"
            },
            "SAVE15": {
                "discount": "15% OFF",
                "description": "Enjoy 15% off your entire purchase",
                "expiry": "2026-12-31",  # Future date
                "min_purchase": 50,
                "category": "General"
            },
            "NEWUSER": {
                "discount": "20% OFF",
                "description": "Welcome to our store! 20% off for new customers",
                "expiry": "2026-12-31",  # Future date
                "min_purchase": 0,
                "category": "Welcome Offer"
            },
            "FLASH50": {
                "discount": "50% OFF",
                "description": "Flash sale! Limited time 50% off selected items",
                "expiry": "2026-12-31",  # Future date
                "min_purchase": 200,
                "category": "Flash Sale"
            },
            "LOYALTY10": {
                "discount": "10% OFF",
                "description": "Thank you for being a loyal customer",
                "expiry": "2026-12-31",  # Future date
                "min_purchase": 0,
                "category": "Loyalty"
            },
            "BULK20": {
                "discount": "20% OFF",
                "description": "Special discount for bulk orders",
                "expiry": "2026-12-31",  # Future date
                "min_purchase": 300,
                "category": "Bulk Order"
            },
            "STUDENT15": {
                "discount": "15% OFF",
                "description": "Exclusive discount for students",
                "expiry": "2026-12-31",  # Future date
                "min_purchase": 25,
                "category": "Student"
            },
            "FIRST5": {
                "discount": "5% OFF",
                "description": "Small discount to get you started",
                "expiry": "2026-12-31",  # Future date
                "min_purchase": 0,
                "category": "Welcome Offer"
            }
        }
        
        self.create_widgets()
        
        # Bind Escape key to exit fullscreen
        self.root.bind('<Escape>', self.toggle_fullscreen)
        
    def create_scrollable_interface(self):
        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create a canvas for scrolling
        self.canvas = tk.Canvas(self.main_frame, background=self.colors["background"])
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel to canvas
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.scrollable_frame.bind("<MouseWheel>", self.on_mousewheel)
        
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
    def toggle_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))
    
    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit the Coupon Validator?"):
            self.root.quit()
    
    def create_widgets(self):
        # Header section
        header_frame = ttk.Frame(self.scrollable_frame, padding="30")
        header_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Title with exit button
        title_frame = ttk.Frame(header_frame)
        title_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        title_label = tk.Label(title_frame, text="🎉 Professional Coupon Code Validator", 
                               font=('Arial', 24, 'bold'), foreground=self.colors["header_blue"],
                               background=self.colors["background"])
        title_label.grid(row=0, column=0, sticky=tk.W)
        
        # Exit fullscreen button
        exit_fullscreen_btn = ttk.Button(title_frame, text="Exit Fullscreen (ESC)", 
                                        command=self.toggle_fullscreen)
        exit_fullscreen_btn.grid(row=0, column=1, sticky=tk.E, padx=(20, 0))
        
        # Exit app button
        exit_app_btn = ttk.Button(title_frame, text="Exit App", command=self.exit_app)
        exit_app_btn.grid(row=0, column=2, sticky=tk.E, padx=(10, 0))
        
        # Welcome message
        welcome_text = "Welcome to our advanced coupon validation system! Enter your coupon code below to discover your savings. Scroll down to see all available coupons and their details."
        welcome_label = tk.Label(header_frame, text=welcome_text, font=('Arial', 12), 
                                 wraplength=1000, justify=tk.CENTER, foreground=self.colors["dark_blue"],
                                 background=self.colors["background"])
        welcome_label.grid(row=1, column=0, columnspan=2, pady=(20, 0))
        
        # Coupon validation section
        validation_container = ttk.Frame(self.scrollable_frame)
        validation_container.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=50, pady=20)
        
        # Section title
        section_title = tk.Label(validation_container, text="🔍 Validate Your Coupon", 
                                font=('Arial', 14, 'bold'), foreground=self.colors["header_blue"],
                                background=self.colors["background"])
        section_title.grid(row=0, column=0, sticky=tk.W, pady=(0, 15))
        
        validation_frame = ttk.Frame(validation_container, padding="25", relief="solid", borderwidth=1)
        validation_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Coupon entry
        tk.Label(validation_frame, text="Enter your coupon code:", font=('Arial', 12),
                background=self.colors["background"]).grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        self.coupon_var = tk.StringVar()
        self.coupon_entry = ttk.Entry(validation_frame, textvariable=self.coupon_var, 
                                     font=('Arial', 14), width=30)
        self.coupon_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        self.coupon_entry.focus()
        
        # Bind Enter key
        self.coupon_entry.bind('<Return>', lambda e: self.check_coupon_validity())
        
        # Action buttons
        button_frame = ttk.Frame(validation_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        validate_btn = ttk.Button(button_frame, text="Check This Coupon", 
                                 command=self.check_coupon_validity, width=20)
        validate_btn.grid(row=0, column=0, padx=(0, 10))
        
        clear_btn = ttk.Button(button_frame, text="Clear", command=self.reset_form, width=15)
        clear_btn.grid(row=0, column=1, padx=10)
        
        # Results display
        results_container = ttk.Frame(validation_frame)
        results_container.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(20, 0))
        
        results_title = tk.Label(results_container, text="Validation Results", 
                                font=('Arial', 12, 'bold'), background=self.colors["background"])
        results_title.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        self.results_display = ttk.Frame(results_container, padding="20", relief="solid", borderwidth=1)
        self.results_display.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.results_display.grid_remove()
        
        self.result_status = tk.Label(self.results_display, text="", font=('Arial', 16, 'bold'),
                                     background=self.colors["background"])
        self.result_status.grid(row=0, column=0, columnspan=2, pady=(0, 15))
        
        self.result_details = tk.Label(self.results_display, text="", font=('Arial', 11),
                                       wraplength=800, justify=tk.LEFT, background=self.colors["background"])
        self.result_details.grid(row=1, column=0, columnspan=2, sticky=tk.W)
        
        # Available coupons section
        coupons_container = ttk.Frame(self.scrollable_frame)
        coupons_container.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=50, pady=20)
        
        coupons_title = tk.Label(coupons_container, text="📋 All Available Coupon Codes", 
                                font=('Arial', 14, 'bold'), foreground=self.colors["header_blue"],
                                background=self.colors["background"])
        coupons_title.grid(row=0, column=0, sticky=tk.W, pady=(0, 15))
        
        coupons_section = ttk.Frame(coupons_container, padding="25", relief="solid", borderwidth=1)
        coupons_section.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Create a grid of coupons
        row_num = 0
        col_num = 0
        
        for code, details in self.valid_coupons.items():
            coupon_card = ttk.Frame(coupons_section, relief="solid", borderwidth=1, padding="15")
            coupon_card.grid(row=row_num, column=col_num, padx=10, pady=10, sticky=(tk.W, tk.E))
            
            # Coupon code
            code_label = tk.Label(coupon_card, text=code, font=('Arial', 16, 'bold'), 
                                  foreground=self.colors["header_blue"], background=self.colors["background"])
            code_label.grid(row=0, column=0, sticky=tk.W)
            
            # Discount
            discount_label = tk.Label(coupon_card, text=details["discount"], 
                                      font=('Arial', 14, 'bold'), foreground=self.colors["success_green"],
                                      background=self.colors["background"])
            discount_label.grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
            
            # Category
            category_label = tk.Label(coupon_card, text=f"Category: {details['category']}", 
                                      font=('Arial', 9), foreground="gray", background=self.colors["background"])
            category_label.grid(row=2, column=0, sticky=tk.W, pady=(5, 0))
            
            # Description
            desc_label = tk.Label(coupon_card, text=details["description"], font=('Arial', 10),
                                  wraplength=300, justify=tk.LEFT, background=self.colors["background"])
            desc_label.grid(row=3, column=0, sticky=tk.W, pady=(10, 0))
            
            # Requirements
            req_text = f"• Min. purchase: ${details['min_purchase']}\n• Valid until: {details['expiry']}"
            req_label = tk.Label(coupon_card, text=req_text, font=('Arial', 9),
                                 foreground="dark gray", background=self.colors["background"])
            req_label.grid(row=4, column=0, sticky=tk.W, pady=(10, 0))
            
            # Alternate columns
            col_num += 1
            if col_num > 2:  # 3 coupons per row
                col_num = 0
                row_num += 1
        
        # Footer
        footer_frame = ttk.Frame(self.scrollable_frame, padding="20")
        footer_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=20)
        
        footer_text = "Thank you for using our Coupon Validator! 💝\nFor customer support, please contact: support@ourstore.com"
        footer_label = tk.Label(footer_frame, text=footer_text, font=('Arial', 10), 
                                foreground="gray", justify=tk.CENTER, background=self.colors["background"])
        footer_label.grid(row=0, column=0, columnspan=2)
        
        # Configure column weights for responsiveness
        self.scrollable_frame.columnconfigure(0, weight=1)
        validation_frame.columnconfigure(0, weight=1)
        coupons_section.columnconfigure(0, weight=1)
        coupons_section.columnconfigure(1, weight=1)
        coupons_section.columnconfigure(2, weight=1)
    
    def check_coupon_validity(self):
        user_coupon = self.coupon_var.get().strip().upper()
        
        if not user_coupon:
            messagebox.showinfo("Missing Code", "Please enter your coupon code first.")
            return
        
        self.results_display.grid()
        
        if user_coupon in self.valid_coupons:
            coupon_info = self.valid_coupons[user_coupon]
            expiry_date = datetime.strptime(coupon_info['expiry'], "%Y-%m-%d")
            
            # FIXED: Compare dates correctly (check if current date is BEFORE expiry)
            if datetime.now().date() > expiry_date.date():
                self.display_result("expired", "This coupon has expired")
            else:
                self.display_result("valid", user_coupon, coupon_info)
        else:
            self.display_result("invalid", "We couldn't find this coupon")
    
    def display_result(self, result_type, coupon_code, coupon_info=None):
        if result_type == "valid":
            self.result_status.configure(text="🎊 Congratulations! Valid Coupon!", 
                                       foreground=self.colors["success_green"])
            
            details_message = f"""
✨ Coupon Code: {coupon_code}
💰 Your Discount: {coupon_info['discount']}
🏷️ Category: {coupon_info['category']}
📝 What you get: {coupon_info['description']}
💳 Minimum order: ${coupon_info['min_purchase']}
📅 Valid until: {coupon_info['expiry']}

Happy shopping! Your discount will be automatically applied at checkout.
            """
            self.result_details.configure(text=details_message.strip())
            
        elif result_type == "expired":
            self.result_status.configure(text="⏰ Coupon Expired", 
                                       foreground=self.colors["error_red"])
            self.result_details.configure(text="Sorry, this coupon is no longer valid. Please check our current offers above!")
        else:
            self.result_status.configure(text="❌ Invalid Coupon Code", 
                                       foreground=self.colors["error_red"])
            self.result_details.configure(text="Please double-check the code and try again. Browse our available coupons above!")
    
    def reset_form(self):
        self.coupon_var.set("")
        self.results_display.grid_remove()
        self.coupon_entry.focus()

def main():
    root = tk.Tk()
    app = CouponValidatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()