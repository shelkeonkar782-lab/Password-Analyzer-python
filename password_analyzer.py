print("============================")
print("   PASSWORD SECURITY ANALYZER")
print("===============================")
password = input("Enter your password:")

print("You entered a password.")
print("Password length:",len(password))

has_uppercase = any(char.isupper() for char in password)
print("Contains uppercase:",has_uppercase)

has_lowercase = any(char.islower() for char in password)
print("Contains lowercase:", has_lowercase)

has_digit =any(char.isdigit() for char in password)
print("Contains number:",has_digit)

has_special = any(not char.isalnum() for char in password)
print("Contains special character:",has_special)

score = 0
if len(password) >= 8:
    score += 1

    if has_lowercase:
        score += 1

        if has_digit:
            score += 1

            if has_special:
                score += 1

                print("Password score:",score, "/5")

                if score <= 2:
                    print("Strength: Weak")
                elif score <= 4:
                    print("Strength: Medium")
                else:
                    print("Strength: Strong")
            