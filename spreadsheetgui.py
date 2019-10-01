#Need to figure out how to change "Very good" to "VG" etc.....

#create function, takes full string eg. Like New, switch statement/ifelse, or a dictionary

from tkinter import *
from tkinter import messagebox
from datetime import *
import csv

csvFile = 'amazongui_' + str(datetime.now().strftime('%Y_%m_%d')) + '.csv'
try:
    with open (csvFile, 'r') as amazon_gui:
        print("File exists")
except FileNotFoundError:
    with open(csvFile, mode='w', newline="") as amazon_gui:
        amazon_gui = csv.writer(amazon_gui)
        amazon_gui.writerow(['Product Name', 'trtrte'])


HEIGHT = 700
WIDTH = 1000

root = Tk()
root.config(background='light grey')
root.geometry('650x500')


def create_sku():
    shopPurchased = shop_purchased.get()
    condition2 = condition.get()

    if shopPurchased == "":
        messagebox.showerror("Create SKU", "Please enter Shop Purchased")
    elif condition2== "":
        messagebox.showerror("Create SKU", "Please enter Condition")
    else:
        entrysku.delete(0, END)
        createdSku = (shop_purchased.get()[0:2].upper() + "-" + now.strftime("%Y") + "-" + now.strftime("%b") + "-" + now.strftime("%d") + "-" + condition.get())
        entrysku.insert(0, createdSku)




def onReturn():
   submit_info()

def submit_info():
    productName = product_name.get()
    rankNumber = rank_number.get()
    purchasePrice = purchase_price.get()
    salesRank = sales_rank.get()
    sellPrice = sell_price.get()
    sellerFees = seller_fees.get()
    unitsPurchased = units_purchased.get()
    profitLoss  = profit_loss.get()
    aRoi = roi.get()
    aCategory = category.get()

    generatedSku = entrysku.get()


#on start run a function that will try and open the file or check if exists if it does do nothing, if it doesnt, create files with headers
    if productName == "":
        print("Error")
        messagebox.showerror("Error", "Please enter Product Name")
    elif aCategory == "":
        print("Error")
        messagebox.showerror("Error", "Please enter a Category")
    elif salesRank == "":
        print("Error")
        messagebox.showerror("Error", "Please enter Sales Rank")
    elif generatedSku == "":
        print("Error")
        messagebox.showerror("Error", "Please generate a SKU")
    elif purchasePrice == "":
        print("Error")
        messagebox.showerror("Error", "Please enter Purchase Price")
    elif rankNumber == "":
        print("Error")
        messagebox.showerror("Error", "Please enter Sales Ranks %")
    elif sellerFees == "":
        print("Error")
        messagebox.showerror("Error", "Please enter Seller Fees")
    elif sellPrice == "" :
        print("Error")
        messagebox.showerror("Error", "Please enter Sell Price")
    elif aRoi == "":
        print("Error")
        messagebox.showerror("Error", "Please enter ROI%")
    elif profitLoss == "":
        print("Error")
        messagebox.showerror("Error", "Please enter Profit/Loss")
    elif unitsPurchased == "":
        print("Error")
        messagebox.showerror("Error", "Please enter Units Purchased")

    else:
        with open(csvFile, mode = 'a') as amazon_gui:
            amazon_gui = csv.writer(amazon_gui)
            amazon_gui.writerow([product_name.get(), sales_rank.get(), purchase_price.get(), sales_rank.get(), category.get(), sell_price.get(), seller_fees.get(), units_purchased.get(), entrysku.get()])


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
category = StringVar()
roi = StringVar()
notes = StringVar()
date = StringVar(value=todaysDate)

root.bind("<Return>", onReturn)

lblHeading = Label(root, text='Add New Product', font=('Arial', 24, "bold")).grid(row=0, column=0, columnspan=7,
                                                                                  padx=20, pady=10)

# Row 1 labels and entries
lblProductName = Label(root, text='Product Name:', font=('Arial', 14, "bold")).grid(row=1, column=0, pady=3, sticky=W)
lblCategory = Label(root, text='Category:', font=('Arial', 14, "bold")).grid(row=1, column=2, pady=3)
entryProductName = Entry(root, width=30, textvariable=product_name).grid(row=1, column=1)
list1 = ['Baby', 'Books', 'Sports & Outdoors', 'Toys & Games']
categorylist = OptionMenu(root, category, *list1)
categorylist.config(width=7)
category.set('')
categorylist.grid(row=1, column=3, sticky=W)

# Row 2 labels and entries
lblShopPurchased = Label(root, text='Shop Purchased:', font=('Arial', 14, "bold")).grid(row=2, column=0)
lblSalesRankNumber = Label(root, text='Sales Rank Number:', font=('Arial', 14, "bold")).grid(row=2, column=2, pady=3,
                                                                                             padx=5)

entryRankNumber = Entry(root, width=8, textvariable=rank_number).grid(row=2, column=3, sticky=W)
list2 = ['Asda', 'Charity', 'Morrisons', 'Tesco', 'Tk Maxx']
shoplist = OptionMenu(root, shop_purchased, *list2)
shoplist.config(width=15)
shop_purchased.set('')
shoplist.grid(row=2, column=1, sticky=W, padx=3)
# Row 3 labels and entries\
lblPurchasePrice = Label(root, text='Purchase Price:', font=('Arial', 14, "bold")).grid(row=3, column=0)
lblSalesRank = Label(root, text='Sales Rank %:', font=('Arial', 14, "bold")).grid(row=3, column=2, pady=3, padx=5)
entryPurchasePrice = Entry(root, width=8, textvariable=purchase_price).grid(row=3, column=1, sticky=W)
entrySalesRank = Entry(root, width=8, textvariable=sales_rank).grid(row=3, column=3, sticky=W)

# Row 4 labels and entries
lblSellPrice = Label(root, text='Sell Price:', font=('Arial', 14, "bold")).grid(row=4, column=0)
lblCondition = Label(root, text='Condition:', font=('Arial', 14, "bold")).grid(row=4, column=2, pady=3, padx=5)
entrySellPrice = Entry(root, width=8, textvariable=sell_price).grid(row=4, column=1, sticky=W)
list1 = ['New', 'Like New', 'Very Good', 'G']
conditionlist = OptionMenu(root, condition, *list1)
conditionlist.config(width=7)
condition.set('')
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

#Row 7 notes and dates
lblNotes = Label(root, text='Notes:', font=('Arial', 14, "bold")).grid(row=7, column=0, pady=3, padx=5)
entryNotes = Entry(root, textvariable=notes).grid(row=7, column=1, sticky=W)
lblDate = Label(root, text='Date', font=('Arial', 14, "bold")).grid(row=7, column=2, pady=3, padx=5)
entryDate = Entry(root, textvariable=date, width=8).grid(row=7, column=3, sticky=W)



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


#TO CREATE .EXE FILE  IN CMD  (PYINSTALLER --ONEFILE -W SPREADSHEETGUI.PY)   https://www.youtube.com/watch?v=UZX5kH72Yx4
