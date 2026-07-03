def organize_contacts(contact_list):
    # Your solution here
    clean_lst = []
    
    email_set = set()
    phone_set = set()

    # 1. Create helper functions for validation
    # - Function to validate email format
    # - Function to clean and validate phone numbers
    def email_fun(element):
            element["email"] = element["email"].lower()
            email = element["email"]
            if " " in email:
                return False
            if ("@" in email) and ("." in email) and email.count("@") == 1 and email.count(".") == 1:
                return True
            return False
    def phone_fun(element):
            element["phone"] = element["phone"].replace("-", "").replace(".", "").replace("(", "").replace(")", "")
            phone = element["phone"]
            if phone.isdigit():   
                if len(phone) == 10:
                    return True
            return False
    # 2. Process each contact
    # - Clean email (lowercase) and phone (digits only)
    # - Check if email and phone are valid
    # - Check for duplicates
    for element in contact_list:
        if email_fun(element) and phone_fun(element):
            email = element["email"]
            phone = element["phone"]
            if email not in email_set and phone not in phone_set:
                clean_lst.append(element)
                email_set.add(email)
                phone_set.add(phone)
    # 3. Return the clean contact list
    return clean_lst
    


# TESTS!

# TEST 1
contacts1 = [
    {"name": "John Doe", "email": "john@email.com", "phone": "123-456-7890"}
]
print("TEST 1: ", organize_contacts(contacts1))

# TEST 2
contacts2 = [
    {"name": "John Doe", "email": "john@email.com", "phone": "123-456-7890"},
    {"name": "Jane Smith", "email": "jane@email.com", "phone": "987-654-3210"}
]
print("\nTEST 2: ", organize_contacts(contacts2))

# TEST 3
contacts3 = [
    {"name": "Alice Brown", "email": "alice brown@email.com", "phone": "111-222-3333"},
    {"name": "Bob Smith", "email": "bobemail.com", "phone": "444-555-6666"}
]
print("\nTEST 3: ", organize_contacts(contacts3))

# TEST 4
contacts4 = [
    {"name": "Charlie", "email": "charlie@email.com", "phone": "12345"},
    {"name": "David", "email": "david@email.com", "phone": "abc-def-ghij"},
    {"name": "Eve", "email": "eve@email.com", "phone": "123-456-789"}
]
print("\nTEST 4: ", organize_contacts(contacts4))

# TEST 6
contacts6 = [
    {"name": "Anna", "email": "ANNA@EMAIL.COM", "phone": "123-456-7890"},
    {"name": "Brian", "email": "brian@ email.com", "phone": "987-654-3210"},
    {"name": "Cara", "email": "cara@email.com", "phone": "123.456.7890"},
    {"name": "Dan", "email": "dan@email.com", "phone": "1112223333"},
    {"name": "Eli", "email": "dan@email.com", "phone": "000-000-0000"}
]
print("\nTEST 6: ", organize_contacts(contacts6))

# TEST 7
contacts7 = [
    {"name": "Person A", "email": "a@email.com", "phone": "111-111-1111"},
    {"name": "Person B", "email": "b@email.com", "phone": "222-222-2222"},
    {"name": "Person C", "email": "c@email.com", "phone": "333-333-3333"}
]
print("\nTEST 7: ", organize_contacts(contacts7))