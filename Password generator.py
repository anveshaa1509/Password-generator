lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_chars = "!@#$%^&*()"

# Combine all characters into one string
all_chars = lowercase + uppercase + digits + special_chars

# Input desired password length
length = int(input("Enter desired password length: "))

password = ""

# Simple pseudo-random generator using basic concepts (linear congruential generator)
seed = 42  # Starting seed value, can be any number

def simple_rand(seed):
    # Linear congruential generator parameters
    a = 1103515245
    c = 12345
    m = 2**31
    return (a * seed + c) % m

for i in range(length):
    seed = simple_rand(seed)
    # Use the seed to pick an index in the character string
    index = seed % len(all_chars)
    password += all_chars[index]

print("Generated password:",password)