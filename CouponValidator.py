from datetime import datetime

class CouponValidator:
    def __init__(self):
        self.coupons = {
            "WELCOME10": {"discount": 10, "min": 50, "expiry": "2025-12-31", "description": "Welcome discount for new customers"},
            "SAVE15": {"discount": 15, "min": 75, "expiry": "2026-08-31", "description": "Perfect for larger orders"},
            "FREESHIP": {"discount": 0, "min": 40, "expiry": "2028-12-31", "free_shipping": True, "description": "Free shipping on your order"},
            "SUMMER25": {"discount": 25, "min": 100, "expiry": "2022-06-30", "description": "Summer special (expired)"},
            "FIRST5": {"discount": 5, "min": 20, "expiry": "2024-12-31", "description": "Small discount for any order"},
        }
        self.used = set()

    def validate(self, code, cart_amount=0):
        code = code.strip().upper()
        
        print(f"\n Checking your coupon: '{code}'...")
        print("━" * 40)
        
        # Check if coupon exists
        if code not in self.coupons:
            return self._show_result(False, "❌ Oops! We couldn't find that coupon code.\n   Please check the spelling and try again.")
        
        coupon = self.coupons[code]
        
        # Check if already used
        if code in self.used:
            return self._show_result(False, "❌ This coupon has already been used.\n   Each coupon can only be used once!")
        
        # Check expiry
        if not self._is_valid_expiry(coupon["expiry"]):
            days_past = (datetime.now().date() - datetime.strptime(coupon["expiry"], "%Y-%m-%d").date()).days
            return self._show_result(False, f"❌ This coupon expired {days_past} days ago.\n   Check out our current offers below!")
        
        # Check minimum amount
        if cart_amount < coupon["min"]:
            needed = coupon["min"] - cart_amount
            return self._show_result(False, 
                f"❌ You're ${needed:.2f} away from using this coupon!\n"
                f"   Add a few more items to unlock your {coupon['discount']}% discount!")
        
        # Success!
        self.used.add(code)
        
        if coupon.get("free_shipping"):
            message = " Amazing! You've unlocked FREE shipping!\n   Your delivery charges are on us! "
            return self._show_result(True, message, 0, True)
        else:
            message = f" Fantastic! You save {coupon['discount']}% on your order!\n   That's great savings! "
            return self._show_result(True, message, coupon['discount'])

    def _is_valid_expiry(self, expiry_date):
        return datetime.now().date() <= datetime.strptime(expiry_date, "%Y-%m-%d").date()

    def _show_result(self, valid, message, discount=0, free_shipping=False):
        print(message)
        return {"valid": valid, "message": message, "discount": discount, "free_shipping": free_shipping}

    def show_available_coupons(self, cart_amount):
        print(f"\n Available Coupons for ${cart_amount} order:")
        print("━" * 45)
        
        available_coupons = []
        for code, details in self.coupons.items():
            if (code not in self.used and 
                self._is_valid_expiry(details["expiry"]) and 
                cart_amount >= details["min"]):
                
                if details.get("free_shipping"):
                    offer = " FREE Shipping"
                else:
                    offer = f" {details['discount']}% OFF"
                
                available_coupons.append({
                    'code': code,
                    'offer': offer,
                    'description': details['description']
                })
        
        if available_coupons:
            for i, coupon in enumerate(available_coupons, 1):
                print(f"{i}. {coupon['code']} - {coupon['offer']}")
                print(f"    {coupon['description']}")
                print()
        else:
            print(" No coupons available for your cart amount yet...")
            self._show_how_to_qualify(cart_amount)

    def _show_how_to_qualify(self, cart_amount):
        valid_coupons = [c for c in self.coupons.values() 
                        if self._is_valid_expiry(c["expiry"]) and c["min"] > cart_amount]
        
        if valid_coupons:
            min_needed = min(c["min"] for c in valid_coupons)
            amount_needed = min_needed - cart_amount
            
            print(f"\n Pro tip: Add ${amount_needed:.2f} more to your cart and you'll qualify for:")
            for coupon in valid_coupons:
                if coupon["min"] == min_needed:
                    offer = "free shipping" if coupon.get("free_shipping") else f"{coupon['discount']}% off"
                    print(f"    {offer}!")

    def show_all_coupons(self):
        print("\n All Coupon Codes:")
        print("━" * 25)
        
        for code, details in self.coupons.items():
            status = "🔴 Used" if code in self.used else "🟢 Available"
            expiry_status = " (Expired)" if not self._is_valid_expiry(details["expiry"]) else ""
            
            if details.get("free_shipping"):
                offer = "Free Shipping"
            else:
                offer = f"{details['discount']}% Off"
            
            print(f"   {code}: {offer} (min ${details['min']}) - {status}{expiry_status}")

def main():
    validator = CouponValidator()
    
    print("🛍️  Welcome to Your Coupon Helper!")
    print("✨ Find the best discounts for your shopping!")
    print("=" * 50)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. 🔍 Check a coupon code")
        print("2. 📋 See available coupons for my cart")
        print("3. 🏷️  View all coupon codes") 
        print("4. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\nLet's check your coupon!")
            code = input("Enter your coupon code: ").strip()
            
            if not code:
                print("❌ Please enter a coupon code to check")
                continue
                
            try:
                amount = float(input("Enter your cart total: $"))
                result = validator.validate(code, amount)
                
                if result['valid']:
                    print("\n" + "" * 20)
                    print("COUPON APPLIED SUCCESSFULLY!")
                    print("" * 20)
                    
            except ValueError:
                print("❌ Please enter a valid amount (like 50 or 75.50)")
        
        elif choice == "2":
            print("\nLet's find coupons for your cart!")
            try:
                amount = float(input("Enter your cart total: $"))
                validator.show_available_coupons(amount)
            except ValueError:
                print("❌ Please enter a valid amount")
        
        elif choice == "3":
            validator.show_all_coupons()
        
        elif choice == "4":
            print("\n" + "" * 20)
            print("Thank you for shopping with us!")
            print("Hope you found great savings! ")
            print("" * 20)
            break
        
        else:
            print("❌ Please choose 1, 2, 3, or 4")

if __name__ == "__main__":
    main()