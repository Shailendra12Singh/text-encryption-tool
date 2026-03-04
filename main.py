from cipher import encrypt, decrypt
from attack import brute_force
from analysis import frequency_analysis


def main():
    while True:
        print("\n=== Text Encryption & Cryptanalysis Tool ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Attack")
        print("4. Frequency Analysis")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            print("Encrypted:", encrypt(text, shift))

        elif choice == "2":
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            print("Decrypted:", decrypt(text, shift))

        elif choice == "3":
            text = input("Enter cipher text: ")
            brute_force(text)

        elif choice == "4":
            text = input("Enter cipher text: ")
            frequency_analysis(text)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid Option")


if __name__ == "__main__":
    main()