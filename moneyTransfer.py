menu = int(input("MENU\n 1.Transfer Money\n 2.MomoPay\n 3.Airtime\n 4.Allow Cashout\n 5.Financial Services\n 6.My Wallet\n 7.Momo Promo\n "))

if menu == 1 :
    opt_1 = int(input("TRANSFER MONEY\n 1.Momo User\n 2.Non Momo User\n 3.Send with Care\n 4.Favorite\n 5.Other Networks\n Bank Acc.\n 0.Back\n "))
    if opt_1 == 1 :
        opt_2 = input("Enter receipient's number:\n ")
        if len(opt_2) == 10:
            opt_3 = input("Re-enter receipient's number:\n ")
            if opt_2 != opt_3:
                print("Receipient number mismatch.\n Please try again.")
            else:
                opt_4 = int(input("Enter Amount To Transfer(GHc).\n ")) 
                if opt_4 <= 0:
                    print("Invalid Amount!!, Try again.\n") 
                else:
                    opt_5 = input("Enter Your Pin to complete transaction \n")
                    if len(opt_5) == 4 :
                        opt_6 = int(input("An amount of GHS " + str(opt_4)+" will be sent to " + opt_2 +"\n Enter 1 to complete transaction\n"))
                        if opt_6 == 1:
                            print("Transaction successful!!\n GenPay's got you!")
                    else:
                        print("Transaction has been terminated, Please start over.\n")
        else:
            print("Number is not up to standard, check number and try again.")
        

    
        
