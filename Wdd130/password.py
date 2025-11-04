import os

def create_sample_files():
    """Create sample dictionary and password files if they don't exist"""
    # Sample dictionary words (70,000 words would be too long for example)
    dictionary_words = [
        "password", "secret", "admin", "welcome", "login", "user", "guest",
        "qwerty", "letmein", "access", "master", "hello", "monkey", "dragon",
        "baseball", "football", "superman", "letmein", "trustno1", "whatever"
    ]
    
    # Sample top passwords (1 million would be too long for example)
    top_passwords = [
        "123456", "password", "12345678", "qwerty", "123456789",
        "12345", "1234", "111111", "1234567", "dragon",
        "123123", "baseball", "abc123", "football", "monkey",
        "letmein", "shadow", "master", "666666", "qwertyuiop",
        "123321", "mustang", "1234567890", "michael", "654321",
        "superman", "1qaz2wsx", "7777777", "121212", "000000",
        "qazwsx", "123qwe", "killer", "trustno1", "jordan",
        "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster"
    ]
    
    # Create dictionary file
    with open("dictionary.txt", "w") as f:
        for word in dictionary_words:
            f.write(f"{word}\n")
    
    # Create top passwords file
    with open("top_passwords.txt", "w") as f:
        for pwd in top_passwords:
            f.write(f"{pwd}\n")

def load_dictionary(filename):
    """Load dictionary words into a set for case-insensitive matching"""
    dictionary_set = set()
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().lower()
            dictionary_set.add(word)
    return dictionary_set

def load_top_passwords(filename):
    """Load top passwords into a set for case-sensitive matching"""
    top_passwords_set = set()
    with open(filename, 'r') as file:
        for line in file:
            password = line.strip()
            top_passwords_set.add(password)
    return top_passwords_set

def calculate_password_strength(password, dictionary_set, top_passwords_set):
    """Calculate password strength based on multiple criteria"""
    # Check against dictionary (case-insensitive)
    if password.lower() in dictionary_set:
        print("Password is a dictionary word and is not secure.")
        return 0
    
    # Check against top passwords (case-sensitive)
    if password in top_passwords_set:
        print("Password is a commonly used password and is not secure.")
        return 0
    
    # Check length
    if len(password) < 10:
        print("Password is too short and is not secure.")
        return 1
    if len(password) > 15:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    # Analyze character complexity
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    
    complexity_score = sum([has_upper, has_lower, has_digit, has_special])
    strength = 1 + complexity_score
    
    # Provide feedback based on complexity
    if complexity_score == 1:
        print("Password has only one type of character - very weak.")
    elif complexity_score == 2:
        print("Password has two types of characters - weak.")
    elif complexity_score == 3:
        print("Password has three types of characters - moderate.")
    else:
        print("Password has all four types of characters - strong.")
    
    return strength

def main():
    # Create sample files if they don't exist
    if not os.path.exists("dictionary.txt") or not os.path.exists("top_passwords.txt"):
        print("Creating sample dictionary and password files...")
        create_sample_files()
    
    # Load data files
    dictionary_set = load_dictionary("dictionary.txt")
    top_passwords_set = load_top_passwords("top_passwords.txt")
    
    print("\nPassword Strength Checker")
    print("Enter a password to check its strength. Type 'quit' to exit.")
    print("--------------------------------------------------------")
    
    while True:
        password = input("\nEnter password: ").strip()
        if password.lower() == 'quit':
            print("Exiting password checker...")
            break
        
        print(f"\nAnalyzing password: '{password}'")
        strength = calculate_password_strength(password, dictionary_set, top_passwords_set)
        
        # Additional strength feedback
        if strength == 0:
            print("Strength: 0/5 - Extremely weak")
        elif strength == 1:
            print("Strength: 1/5 - Very weak")
        elif strength == 2:
            print("Strength: 2/5 - Weak")
        elif strength == 3:
            print("Strength: 3/5 - Moderate")
        elif strength == 4:
            print("Strength: 4/5 - Strong")
        elif strength == 5:
            print("Strength: 5/5 - Very strong")
        
        print("--------------------------------------------------------")

if __name__ == "__main__":
    main()