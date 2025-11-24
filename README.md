🧾 **Coupon Code Validator**

📌 Project Title
Coupon Code Validator – Python CLI Application

📘 **Overview**

This project is a command-line application that helps users validate coupon codes instantly. It checks whether a coupon exists, is expired, already used, or meets the minimum cart amount. It also displays all available coupons and shows which coupons can be applied based on a user’s cart total.
Perfect for learning Python classes, date handling, and interactive CLI applications.

⭐ **Features**

✔ Validate coupon codes with friendly messages
✔ Check expiry dates automatically
✔ Prevent reusing coupons
✔ Supports free-shipping coupons
✔ Show available coupons based on cart total
✔ List all coupons (Used / Unused)
✔ Fully interactive menu-driven interface
✔ Includes demo mode for quick testing

🛠️ **Technologies / Tools Used**

Python 3.x
datetime module (for expiry checks)
Object-Oriented Programming (OOP)
Command-Line Interface (CLI)

📥 Installation & Running Steps
1️⃣ Clone or Download the Project
git clone https://github.com/your-repo/coupon-validator.git

Or simply download the .py file.

2️⃣ Navigate to the directory
cd coupon-validator

3️⃣ Run the Program
python coupon_validator.py


This launches the interactive menu in your terminal.
**
🧪 Instructions for Testing**
✔ Test via Interactive Mode

When you run the file, choose options like:

Validate a coupon

See coupons for cart amount

View all coupons

Exit

Example test values:

Coupon: WELCOME10, Cart: 60

Coupon: SAVE15, Cart: 50

Coupon: FREESHIP, Cart: 45

Coupon: INVALID, Cart: 80

✔ Run Built-In Demo Mode

Inside the file, find this line at the bottom:

# run_demo()


Just uncomment it:

run_demo()


Then run:

python coupon_validator.py


You’ll see automatic test cases like:

Valid coupon

Wrong coupon

Expired coupon

Already used coupon

Free shipping coupon
