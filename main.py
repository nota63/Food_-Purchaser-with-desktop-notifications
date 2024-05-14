# PROJECT - VIRTUAL FOOD PURCHASE

import datetime
import time
from plyer import notification
import pandas as pd


# CREATING CLASS AND INITIALIZE IT
class Food:
    def __init__(self):
        self.balance = 5000
        self.healthy_food = []
        self.junk_food = []
        self.chicken = []

    # CREATING FUNCTION TO PURCHASE HEALTHY FOOD

    def h_food(self):
        try:
            data = {'Healthy_Food': ['Pane', 'gulagAmon', 'Rasgulla'],
                    'Price': [450, 700, 430]}
            ui = pd.DataFrame(data)
            print(ui)

            user = int(input('Enter Price To Purchase:'))
            if self.balance >= user:
                self.balance -= user
                self.healthy_food.append(user)
                print(f" Healthy_Food: Of Rupees'{user}'  Purchased")
                notification.notify(
                    title="Healthy_Food-{}".format(datetime.date.today()),
                    message=f"Healthy_Food Purchased!\n And Your account ha been debited for rupees: {user}\n And Your Available Balance is {self.balance}",
                    timeout=7
                )
            else:
                print('Insufficient_Funds!')
                notification.notify(
                    title="FoodFetcher-{}".format(datetime.date.today()),
                    message='Insufficient Funds!!',
                    timeout=5
                )

        except ValueError:
            print('ValueError!!')

        except IndexError:
            print('IndexError!!1')
        finally:
            print('THANKS FOR PURCHASING FOOD FROM US.')

    # CREATING A FUNCTION TO PURCHASE JUNK_FOOD

    def junk(self):
        try:
            data2 = {'Junk_Food': ['Pizza', 'Burger', 'Lolipop', 'chineese', 'chilly_chicken'],
                     'Price': [230, 450, 211, 422, 450]}

            ux = pd.DataFrame(data2)
            print(ux)

            user2 = int(input('Enter Item price To Purchase:'))

            if self.balance >= user2:
                self.balance -= user2
                self.junk_food.append(user2)
                print(f"Junk_Food Of Rupees: '{user2}' Purchased!")
                notification.notify(
                    title="FoodFetcher-{}".format(datetime.date.today()),
                    message=f"Junk_Food Purchased! And Your\n Account is Debited For Rupees {user2}\n And Your Available Balance is {self.balance}",
                    timeout=6
                )

            else:
                print("INSUFFICIENT FUNDS!")
                notification.notify(
                    title='FoodFetcher-{}'.format(datetime.date.today()),
                    message="INSUFFICIENT FUNDS!\n COULD NOT PURCHASE!!",
                    timeout=3
                )

        except ValueError:
            print('ValueError!')
        except IndexError:
            print('INDEX ERROR')
        finally:
            print('thanks for using our virtual foodFetcher')

            # CREATING A FUNCTION TO PURCHASE CHICKEN

    def chicken2(self):
        try:
            data3 = {'Chicken': ['Chicken Masala', 'chicken_tikka', 'chicken kadhai'],
                     'Price': [788, 1200, 2111]}
            um = pd.DataFrame(data3)
            print(um)

            user4 = int(input('Enter Price To Purchase:'))

            if self.balance >= user4:
                self.balance -= user4
                self.chicken.append(user4)
                print(f" Chicken : Of rupees '{user4}' Purchased")
                notification.notify(
                    title="FoodFetcher-{}".format(datetime.date.today()),
                    message=f"Chicken Purchased!! Yur Account debited for rupees {user4} \n and your current balance is {self.balance}",
                    timeout=6
                )
            else:
                print('Insufficient Funds!')
                notification.notify(
                    title='FoodFetcher-{}'.format(datetime.date.today()),
                    message='Insufficient_funds!!!\n could not purchase food',
                    timeout=4
                )
        except ValueError:
            print('ValueError!')
        except IndexError:
            print('IndexError!')
        finally:
            print('Thanks For using our virtual food fetcher')

    # CREATING A FUNC TO ADD_MONEY

    def add_money(self):
        money = int(input('How Much To Add:'))
        self.balance += money
        print("Done")
        notification.notify(
            title='Food_Fetcher-{}'.format(datetime.date.today()),
            message=f"RUPEES {money} Deposited To Your Account\n Available balance is {self.balance}",
            timeout=5
        )

    # creating a func to withdraw money

    def withdraw(self):
        money1 = int(input("How Much to withdraw:"))
        self.balance -= money1
        print('Done')
        notification.notify(
            title='FoodFetcher-{}'.format(datetime.date.today()),
            message=f"RUPEES {money1} Debited From Your Account\n Available Balance IS {self.balance}",
            timeout=4
        )

    #     CREATING A FUNCTION TO VIEW WHAT YOU PURCHASED

    def view_total(self):
        if self.healthy_food:
            for food1 in self.healthy_food:
                print('HealthyFood:', food1)
        else:
            print('Healthy_ Food Is Empty!')

        if self.junk_food:
            for food2 in self.junk_food:
                print('Junk_Food:', food2)
        else:
            print('Junk_Food Is Empty!')

        if self.chicken:
            for food3 in self.chicken:
                print('Chicken:', food3)
        else:
            print('Chicken Is Empty!')

            # FUNC TO VIEW BALANCE

    def view_balance(self):
        print('Done\n View notification')
        notification.notify(
            title='FoodFetcher-{}'.format(datetime.date.today()),
            message=f"✅ Balance Fetched Successfully\n Available Balance In Your Account Is 💲{self.balance}",
            timeout=5
        )

        # CREATE MAIN FUNCTION


def main():
    food = Food()

    intro = 'welcome to food fetcher\n a digital virtual machine'
    print(intro.upper())

    email = input('Enter A Valid Email  To Login:')
    if len(email) <= 32:
        if email.count("@") == 1:
            if email[-3] == "." or email[-4] == ".":
                if 'gmail' in email:
                    if 'com' in email:
                        print('Email verified!')
                        notification.notify(
                            title='Google-{}'.format(datetime.date.today()),
                            message=f'Email Verified Successes "{email}" 🥰🙃\n Now You Can Purchase Food from us',
                            timeout=4
                        )

                        while True:
                            try:
                                menu = ('....menu....\n 1.purchase_healthy_food\n 2. purchase junk_food\n 3.purchase '
                                        'chicken\n 4.add_funds to your foodfetcher account\n 5.withdraw funds\n '
                                        '6.view_your purchased foods\n 7.view_balance\n 8.QuiteApp')
                                print(menu.upper())

                                foodie = int(input('Enter An index from Menu!:'))

                                if foodie == 1:
                                    food.h_food()

                                elif foodie == 2:
                                    food.junk()

                                elif foodie == 3:
                                    food.chicken2()

                                elif foodie == 4:
                                    food.add_money()

                                elif foodie == 5:
                                    food.withdraw()

                                elif foodie == 6:
                                    food.view_total()

                                elif foodie == 7:
                                    food.view_balance()

                                elif foodie == 8:
                                    print("Quiting FoodFetcher...Done")
                                    break

                            except ValueError:
                                print('ValueError!')

                            except IndexError:
                                print('IndexError!')

                    else:
                        print('email should be have "com" ')
                else:
                    print('Email should be have "Gmail" ')
            else:
                print(' "." should be have over -3 or -4 indexes')
        else:
            print(' email should contain only one "@"')
    else:
        print('Email length should be les than 32')


if __name__ == "__main__":
    main()
