print("===================================")
print("      SPAM EMAIL CLASSIFIER")
print("===================================\n")

spam_words = ["win", "free", "offer", "money", "prize"]

while True:

    print("1. Check Email")
    print("2. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":

        sender = input("\nEnter sender name: ")

        email = input("Enter email message: ").lower()

        print("\nChecking email...")
        print("Please wait...\n")

        spam_count = 0

        for word in spam_words:

            if word in email:
                spam_count = spam_count + 1

        print("===================================")
        print("            RESULT")
        print("===================================")

        print("Sender:", sender)

        if spam_count > 0:
            print("Email Type: Spam Email")
            print("Spam Words Found:", spam_count)
        else:
            print("Email Type: Safe Email")
            print("No Spam Words Found")

        print("===================================\n")

        again = input("Do you want to check another email? (yes/no): ").lower()

        if again == "no":
            print("\nProgram Closed Successfully.")
            break

        elif again != "yes":
            print("\nInvalid Input. Program Closed.")
            break

    elif choice == "2":

        print("\nThank you for using Spam Email Classifier.")
        break

    else:

        print("\nInvalid Choice! Please try again.\n")
