import itertools
import string
import time
from colorama import init, Fore, Style

# Initialize colorama
init()

def brute_force(charset, password):
    start_time = time.time()
    attempts = 0

    # Generate combinations of the charset with increasing length
    for length in range(1, len(password) + 1):
        for guess in itertools.product(charset, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            print(Fore.YELLOW + f"Trying: {guess}" + Style.RESET_ALL)
            if guess == password:
                end_time = time.time()
                print(Fore.GREEN + f"Password found: {guess}" + Style.RESET_ALL)
                print(Fore.BLUE + f"Total attempts: {attempts}" + Style.RESET_ALL)
                print(Fore.BLUE + f"Time taken: {end_time - start_time} seconds" + Style.RESET_ALL)
                return guess

    print(Fore.RED + "Password not found" + Style.RESET_ALL)
    return None

def main():
    print(Fore.CYAN + "Welcome to the Brute Force Attack Tool" + Style.RESET_ALL)
    charset = string.ascii_letters + string.digits
    password = input(Fore.CYAN + "Enter the password to brute force: " + Style.RESET_ALL)
    brute_force(charset, password)

if __name__ == "__main__":
    main()
