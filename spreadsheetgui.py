from tkinter import *
from tkinter import messagebox
from datetime import *
import tkinter.simpledialog
import csv

HEIGHT = 700
WIDTH = 1000

root = Tk()
root.config(background='light grey')
root.geometry('650x500')



#NEED TO ADD THE LAST DIGIT (X + 1) from the csv file
def create_sku():
    shopPurchased2 = shop_purchased.get()
    if shopPurchased2 == "":
        messagebox.showerror("Create SKU", "Please enter shop purchased from")
    else:
        Ans = (shop_purchased.get() + "-" + now.strftime("%Y") + "-" + now.strftime("%b") + "-" + now.strftime("%d") + "-" + condition.get() + "-" )
    entrysku.insert(0, Ans)






# productname is new, product_name.get is a text variable that needs to be entered into the () where i put the root

def submit_info():
    productName = product_name.get()
    shopPurchased = shop_purchased.get()
    rankNumber = rank_number.get()
    purchasePrice = purchase_price.get()
    salesRank = sales_rank.get()
    sellPrice = sell_price.get()
    aCondition = condition.get()
    sellerFees = seller_fees.get()
    unitsPurchased = units_purchased.get()
    profitLoss  = profit_loss.get()
    aRoi = roi.get()
    aNotes = notes.get()



    if (productName == "", shopPurchased == "", rankNumber == "", purchasePrice == "", salesRank == "", sellPrice == "",
        aCondition == "", sellerFees == "", unitsPurchased == "", profitLoss == "", aRoi == "", aNotes == ""):
       print("Error")
       messagebox.showerror("Error", "You have made an error")


    #print(testing)

now = datetime.now()
todaysDate = now.strftime("%x")
product_name = StringVar()
shop_purchased = StringVar()
rank_number = StringVar()
purchase_price = StringVar()
sales_rank = StringVar()
sell_price = StringVar()
condition = StringVar()
seller_fees = StringVar()
units_purchased = StringVar()
profit_loss = StringVar()
roi = StringVar()
notes = StringVar()
date = StringVar(value=todaysDate)


lblHeading = Label(root, text='Add New Product', font=('Arial', 24, "bold")).grid(row=0, column=0, columnspan=7,
                                                                                  padx=20, pady=10)

# Row 1 labels and entries
lblProductName = Label(root, text='Product Name:', font=('Arial', 14, "bold")).grid(row=1, column=1, pady=3, sticky=W)
entryProductName = Entry(root, width=30, textvariable=product_name).grid(row=1, column=2)

# Row 2 labels and entries
lblShopPurchased = Label(root, text='Shop Purchased:', font=('Arial', 14, "bold")).grid(row=2, column=0)
lblSalesRankNumber = Label(root, text='Sales Rank Number:', font=('Arial', 14, "bold")).grid(row=2, column=2, pady=3,
                                                                                             padx=5)
entryShopPurchased = Entry(root, width=8, textvariable=shop_purchased).grid(row=2, column=1, sticky=W)
entryRankNumber = Entry(root, width=8, textvariable=rank_number).grid(row=2, column=3, sticky=W)

# Row 3 labels and entries
lblPurchasePrice = Label(root, text='Purchase Price:', font=('Arial', 14, "bold")).grid(row=3, column=0)
lblSalesRank = Label(root, text='Sales Rank:', font=('Arial', 14, "bold")).grid(row=3, column=2, pady=3, padx=5)
entryPurchasePrice = Entry(root, width=8, textvariable=purchase_price).grid(row=3, column=1, sticky=W)
entrySalesRank = Entry(root, width=8, textvariable=sales_rank).grid(row=3, column=3, sticky=W)

# Row 4 labels and entries
lblSellPrice = Label(root, text='Sell Price:', font=('Arial', 14, "bold")).grid(row=4, column=0)
lblCondition = Label(root, text='Condition:', font=('Arial', 14, "bold")).grid(row=4, column=2, pady=3, padx=5)
entrySellPrice = Entry(root, width=8, textvariable=sell_price).grid(row=4, column=1, sticky=W)
list1 = ['N', 'VG', 'G']
conditionlist = OptionMenu(root, condition, *list1)
conditionlist.config(width=15)
condition.set('Condition')
conditionlist.grid(row=4, column=3)

# Row 5 labels and entries
lblSellerFees = Label(root, text='Seller Fees:', font=('Arial', 14, "bold")).grid(row=5, column=0)
lblUnitsPurchased = Label(root, text='Units Purchased:', font=('Arial', 14, "bold")).grid(row=5, column=2, pady=3,
                                                                                          padx=5)
entrySellerFees = Entry(root, width=8, textvariable=seller_fees).grid(row=5, column=1, sticky=W)
entryUnitsPurchased = Entry(root, width=8, textvariable=units_purchased).grid(row=5, column=3, sticky=W)

# Row 6 labels and entries
lblProfitLoss = Label(root, text='Profit/Loss:', font=('Arial', 14, "bold")).grid(row=6, column=0)
lblRoi = Label(root, text='ROI%:', font=('Arial', 14, "bold")).grid(row=6, column=2, pady=3, padx=5)
entryProfitLoss = Entry(root, width=8, textvariable=profit_loss).grid(row=6, column=1, sticky=W)
entryRoi = Entry(root, width=8, textvariable=roi).grid(row=6, column=3, sticky=W)

lblNotes = Label(root, text='Notes:', font=('Arial', 14, "bold")).grid(row=7, column=0, pady=3, padx=5)
entryNotes = Entry(root, textvariable=notes).grid(row=7, column=1, sticky=W)
lblDate = Label(root, text='Date', font=('Arial', 14, "bold")).grid(row=7, column=2, pady=3, padx=5)
entryDate = Entry(root, textvariable=date).grid(row=7, column=3, sticky=W)



lowerframe = Frame(root, bg='#80c1ff', bd=5)
lowerframe.place(relx=0.5, anchor='s', rely=1, relwidth=1, relheight=0.2,)



upperframe = Frame(root, bg='gray', bd=5)
upperframe.place(relx=0.5, anchor='s', rely=0.7, relwidth=1, relheight=0.1)

middleframe = Frame(root, bg='gray', bd=5)
middleframe.place(relx=0.5, anchor='s', rely=0.8, relwidth=1, relheight=0.1)

submit = Button(lowerframe, text='Submit', command=submit_info).grid(row=9, column=0)

createsku = Button(upperframe, text='Create SKU', command=create_sku).grid(row=10, column=0)

entrysku = Entry(middleframe, command=createsku)
entrysku.grid()

root.mainloop()


#TO CREATE .EXE FILE  IN CMD  (PYINSTALLER --ONEFILE -W SPREADSHEETGUI.PY)