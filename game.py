import random

user_score = 0
computer_score = 0
ties = 0

choices = ['rock', 'paper', 'scissors']

print("Osh xonaga kirish uchun ro'yhatdan o'ting.")
print("Bo'limni tanlang !")

cart = []

menu = [
    "Osh",
    "Mastava",
    "Shovla",
    "Manti",
    "Lag'mon",
    "Shashlik",
    "Chuchvara",
    "Dimlama",
    "Norin",
    "Kabob",
    "Samsa",
    "Somsa",
    "Choy",
    "Non",
]
royhat = []

while True:
    print("1.SignUp")
    print("2.Login")
    print("3.Exit()")

    txt1 = input("Bo'limni tanlang: ")

    if txt1 == '1':
        fullname = input("Ismingizni kiriting: ")
        Username = input("Usernameni kirting: ")
        password = input("Parolni kiriting: ").isalnum()
        royhat.append((Username, password))
        print("Registratsiyadan o'tingiz !")
    elif txt1 == '2':
        Username = input("Usernameni kirting: ")
        password = input("Parolni kiriting: ").isalnum()
        logged_in = False
        for user in royhat:
            if user[0] == Username and user[1] == password:
                logged_in = True
                print(f"{fullname}! login mavaffaqiyatli tekshirildi.")
                break
        if not logged_in:
            print("Username yoki parol xato. Tekshirib boshqattan urining !")
        else:
            while True:
                print("1.Play a game")
                print("2.access to the kitchen")
                print("3.Exit()")

                tx = input("Bo'limni tanlang: ")
                if tx == '1':
                    while True:

                        user_choice = input('Tanlovingizni kiriting: ').lower()  # kichik harflashtirmoq

                        while user_choice not in choices:
                            user_choice = input("Xato! Tanlovingizni yana kiriting: ").lower()

                        computer_choice = random.choice(choices)  # computerdan randomli tanlov olinyapti
                        print(f'Computer tanlovi: {computer_choice}')

                        if user_choice == computer_choice:
                            print("Durrang")
                            ties += 1

                        elif user_choice == 'rock' and computer_choice == 'scissors' or \
                                user_choice == 'paper' and computer_choice == 'rock' or \
                                user_choice == 'scissors' or computer_choice == 'paper':
                            print("Foydalanuvchi yutdi!")
                            user_score += 1
                        else:
                            print("Computer yutdi!")
                            computer_score += 1

                        davom_etish = input("Davom etasizmi? (yes/no)").lower()

                        if davom_etish != 'yes':  # Yes
                            break

                    print(f"Natijalar\n\nFoydalanuvchi: {user_score}\nComputer: {computer_score}\nDurrang: {ties}")
                    print("Thanks for playing and staying with us!")
                elif tx == '2':
                    while True:
                        print()
                        print("1.Buyurtma qilish.")
                        print("2.Menuni ko'rish.")
                        print("3.Savatni ko'rish.")
                        print("4.Exit()")
                        print()
                        # Bu yerda esa user tanlovi !
                        son = input("Tanlovingizni kiriting: ")  # Userdan tanlovini olish.
                        print()  # bu print esa \n vazifasini bajaradi.
                        if son == '1':
                            txt = input("Nima buyurtma qilmoqchisiz: ").title()  # User buyurtma qilishi uchun.
                            if txt in menu:
                                print(f"{txt} - buyurtma qabul qilindi. ")
                                cart.append(txt)  # savatga qo'shish.
                            else:
                                print(f"{txt} bu nomli taom bizda yo'q.")
                        elif son == '2':
                            print("Menu:")
                            for item in menu:  # men menuni itemga tengladim.
                                print(f"- {item}")  # va bu yerda chiqardim.
                        elif son == '3':
                            print("Savatingizda: ")
                            for mb in cart:
                                print(f"- {mb}")
                        elif son == '4':
                            break  # bu esa funksiyani tugatish.
                        else:
                            print(
                                "Noto'g'ri tanlov, iltimos qaytadan urinib ko'ring.")
                if tx == '3':
                    print("xayr")
                    break
    elif txt1 == '3':
        print("Xayr sog' bo'ling.")
        break
    else:
        print("Xato bunday bo'lim yo'q !")
