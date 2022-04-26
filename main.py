import requests
from bs4 import BeautifulSoup
import requests
from datetime import date
import sys
from tkinter import *
from  tkinter import ttk

def gui():
    window = Tk()
    window.title('Please kill me!')
    window.geometry('250x300')
    window.resizable(width=False, height=False)

    def click_price():
        ws = Tk()
        ws.title('PythonGuides')
        ws.geometry('500x500')
        ws['bg'] = '#AC99F2'

        price_frame = Frame(ws)
        price_frame.pack()

        price_for_time = ttk.Treeview(price_frame)

        price_for_time['columns'] = ('id_collum', 'usd_collum', 'eur_collum', 'date_collum')

        price_for_time.column("#0", width=0, stretch=NO)
        price_for_time.column("id_collum", anchor=CENTER, width=80)
        price_for_time.column("usd_collum", anchor=CENTER, width=80)
        price_for_time.column("eur_collum", anchor=CENTER, width=80)
        price_for_time.column("date_collum", anchor=CENTER, width=80)

        price_for_time.heading("#0", text="", anchor=CENTER)
        price_for_time.heading("id_collum", text="ID", anchor=CENTER)
        price_for_time.heading("usd_collum", text="USD", anchor=CENTER)
        price_for_time.heading("eur_collum", text="EUR", anchor=CENTER)
        price_for_time.heading("date_collum", text="DATE", anchor=CENTER)


        price_for_time.insert(parent='', index='end', iid=0, text='',
                       values=('1', 'Ninja', '101', 'Oklahoma'))

        price_for_time.pack()

        ws.mainloop()

    def post():
        current_date = date.today()

        s = requests.Session()

        response = s.post(f"http://217.71.129.139:4915/users.get.php",
                          data={'usd': usd_rub, 'eur': eur_rub, 'date': current_date})
        print(response.text)

    def click_calc():
        window_calc = Tk()
        window_calc.title('calc')
        window_calc.geometry('400x400')
        window_calc.resizable(width=False, height=False)
        frame = Frame(window_calc, bg='white')
        frame.place(relheight=1, relwidth=1)
        have_input = Entry(frame)
        have_input.pack()
        def calculation():
            have = have_input.get()
            have_str = Label(frame, text=float(have) * float(usd_rub), bg='red')
            have_str.pack()
        btn_calculation = Button(frame, text='Calculation', padx='100', pady='20', command=calculation)
        btn_calculation.pack()

        window_calc.mainloop()

    usd_label = Label(window, text='$: '+usd_rub, font='Arial 25')
    usd_label.pack()

    eur_label = Label(window, text='€: ' + eur_rub, font='Arial 25')
    eur_label.pack()

    btn_price = Button(window, text='Price for time', padx='72', pady='20', command=click_price)
    btn_price.pack()

    btn_calc = Button(window, text='Calc', padx='100', pady='20', command=click_calc)
    btn_calc.pack()

    btn_post = Button(window, text='Post', padx='100', pady='20', command=post)
    btn_post.pack()

    window.mainloop()

def get_data_usd(url):
    headers = {
        'accept': '*/*'
    }

    response = requests.get(url=url, headers=headers)

    with open('usd.html', 'w', encoding="utf-8") as file:
        file.write(response.text)

    with open(file='usd.html', encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    table = soup.find('div', class_="col-md-2 col-xs-9 _right mono-num")

    global usd_rub

    for usd_rub in table:
        usd_rub = usd_rub.text.replace(" ₽", "").strip()
        usd_rub = usd_rub.replace(",", ".")

def get_data_eur(url):
    headers = {
        'accept': '*/*'
    }

    response = requests.get(url=url, headers=headers)

    with open('eur.html', 'w', encoding="utf-8") as file:
        file.write(response.text)

    with open(file='eur.html', encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    table = soup.find('div', class_="main-indicator_rate").find_next_sibling().find_next().find_next()

    global eur_rub

    for eur_rub in table:
        eur_rub = eur_rub.text.replace(" ₽", "").strip()

def get_price_for_time(url):
    headers = {
        'accept': '*/*'
    }

    response = requests.get(url=url, headers=headers)

    with open('eur.html', 'w', encoding="utf-8") as file:
        file.write(response.text)

    with open(file='eur.html', encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    table = soup.find('body')



    for price in table:
        price = price.text.replace(" ₽", "").strip()
        print(price)
        type(price)

def main():
    get_data_usd(url='https://cbr.ru/')
    get_data_eur(url='https://cbr.ru/')
    get_price_for_time(url='http://217.71.129.139:4915/take_inf_2.get.php')
    gui()

if __name__ == '__main__':
    main()

