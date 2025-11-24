import datetime

class CouponValidator:
    def __init__(self):
        self.coupons = {
            "WELCOME10": {"discount": 10, "min_amount": 50, "expiry": "2025-12-31"},
            "SAVE15": {"discount": 15, "min_amount": 75, "expiry": "2026-08-31"},
            "FREESHIP": {"discount": 0, "min_amount": 40, "expiry": "2028-12-31", "free_shipping": True},
            "SUMMER25": {"discount": 25, "min_amount": 100, "expiry": "2022-06-30"},
            "FIRST5": {"discount": 5, "min_amount": 20, "expiry": "2024-12-31"},
        }
        self.used_coupons = set()

    def validate(self, coupon_code, cart_amount=0):
        """Validate a coupon code with friendly messages"""
        coupon_code = coupon_code.strip().upper()
        
        print(f"\n🔍 Checking: {coupon_code}")
        print("-" * 30)
        
        # Check if coupon exists
        if coupon_code not in self.coupons:
            return {"valid": False, "message": "❌ Oops! This coupon code doesn't exist. Please check for typos."}
        
        coupon = self.coupons[coupon_code]
        
        # Check if already used
        if coupon_code in self.used_coupons:
            return {"valid": False, "message": "❌ Sorry! This coupon has already been used."}
        
        # Check expiry date
        expiry_check = self._check_expiry(coupon["expiry"])
        if not expiry_check["valid"]:
            return {"valid": False, "message": f"❌ {expiry_check['message']}"}
        
        # Check minimum amount
        if cart_amount < coupon["min_amount"]:
            needed = coupon["min_amount"] - cart_amount
            return {
                "valid": False, 
                "message": f"❌ Add ${needed:.2f} more to use this coupon! (Minimum: ${coupon['min_amount']})"
            }
        
        # All checks passed - coupon is valid!
        self.used_coupons.add(coupon_code)
        
        if coupon.get("free_shipping"):
            message = "🎉 Perfect! You get FREE shipping on your order!"
        else:
            message = f"🎉 Excellent! You save {coupon['discount']}% on your order!"
        
        return {
            "valid": True,
            "message": message,
            "discount": coupon['discount'],
            "free_shipping": coupon.get('free_shipping', False)
        }

    def _check_expiry(self, expiry_date):
        """Check if coupon has expired"""
        try:
            expiry = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
            today = datetime.date.today()
            
            if today > expiry:
                days_past = (today - expiry).days
                return {"valid": False, "message": f"This coupon expired {days_past} day(s) ago."}
            
            days_left = (expiry - today).days
            if days_left == 0:
                return {"valid": True, "message": "Hurry! This coupon expires today!"}
            else:
                return {"valid": True, "message": f"Valid! Expires in {days_left} day(s)."}
                
        except ValueError:
            return {"valid": False, "message": "Invalid expiry date format."}

    def show_available(self, cart_amount):
        """Show available coupons for the given cart amount"""
        print(f"\n💡 Available coupons for ${cart_amount} cart:")
        print("-" * 40)
        
        available_found = False
        
        for code, details in self.coupons.items():
            if code in self.used_coupons:
                continue
                
            expiry_check = self._check_expiry(details["expiry"])
            if not expiry_check["valid"]:
                continue
                
            if cart_amount >= details["min_amount"]:
                if details.get("free_shipping"):
                    offer = "FREE shipping"
                else:
                    offer = f"{details['discount']}% off"
                
                print(f"   ✅ {code}: {offer}")
                available_found = True
        
        if not available_found:
            print("   No coupons available right now.")
            self._show_whats_needed(cart_amount)

    def _show_whats_needed(self, cart_amount):
        """Show what's needed to qualify for coupons"""
        min_required = None
        
        for details in self.coupons.values():
            if details["min_amount"] > cart_amount:
                if min_required is None or details["min_amount"] < min_required:
                    min_required = details["min_amount"]
        
        if min_required:
            needed = min_required - cart_amount
            print(f"   💡 Add ${needed:.2f} more to unlock coupon savings!")

    def list_all_coupons(self):
        """Show all coupons in the system"""
        print("\n📋 All Available Coupons:")
        print("-" * 25)
        
        for code, details in self.coupons.items():
            status = "❌ Used" if code in self.used_coupons else "✅ Available"
            
            if details.get("free_shipping"):
                offer = "FREE shipping"
            else:
                offer = f"{details['discount']}% off"
            
            print(f"   {code}: {offer} (min: ${details['min_amount']}) - {status}")

def main():
    """Main interactive program"""
    validator = CouponValidator()
    
    print("🛍️  Welcome to the Coupon Validator!")
    print("=" * 40)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Check a coupon code")
        print("2. See coupons for my cart amount")
        print("3. View all coupons")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            code = input("Enter coupon code: ").strip()
            if not code:
                print("❌ Please enter a coupon code.")
                continue
            
            try:
                amount = float(input("Enter your cart total: $"))
            except ValueError:
                print("❌ Please enter a valid amount like 50 or 75.50")
                continue
            
            result = validator.validate(code, amount)
            print(f"\n{result['message']}")
            
            if result['valid']:
                if result['free_shipping']:
                    print("🚚 Your shipping will be free!")
                else:
                    print(f"💰 You'll save {result['discount']}% on your order!")
        
        elif choice == "2":
            try:
                amount = float(input("Enter your cart total: $"))
                validator.show_available(amount)
            except ValueError:
                print("❌ Please enter a valid amount.")
        
        elif choice == "3":
            validator.list_all_coupons()
        
        elif choice == "4":
            print("\n👋 Thank you for using Coupon Validator! Happy shopping! 🎉")
            break
        
        else:
            print("❌ Please enter a number between 1 and 4.")

def run_demo():
    """Run a demo to show how it works"""
    print("🚀 Running Coupon Validator Demo!")
    print("=" * 35)
    
    validator = CouponValidator()
    
    # Test cases
    test_cases = [
        ("WELCOME10", 60),   # Should work
        ("SAVE15", 50),      # Too low amount
        ("INVALID", 100),    # Wrong code
        ("FREESHIP", 45),    # Free shipping
        ("WELCOME10", 60),   # Already used
    ]
    
    for code, amount in test_cases:
        print(f"\nTesting: '{code}' with ${amount} cart")
        result = validator.validate(code, amount)
        print(f"Result: {result['message']}")
    
    print(f"\n💡 Now showing available coupons for $30 cart:")
    validator.show_available(30)

if __name__ == "__main__":
    # Uncomment the next line to run demo instead of interactive mode
    # run_demo()
    
    main()
