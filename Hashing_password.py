import bcrypt

# Password to hash
password = "userPassword123"

# Hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))

# Print the hashed password
print("Hashed Password:", hashed_password.decode('utf-8'))
