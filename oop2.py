from tkinter import *
from analise import *
from tkinter import ttk
import xml.dom.minidom
import webbrowser


class App(object):
    root = Tk()


class TextWidget(App):
    def __init__(self):
        # create a Frame for the Text and Scrollbar
        txt_frm = Frame(App.root)
        txt_frm.grid(row=2, column=0, columnspan=3, rowspan=10, sticky=W + E + N + S, padx=10, pady=50)

        # create a Text widget
        self.txt = Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        # create a Scrollbar and associate it with txt
        scrollb = Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

        self.cname3 = StringVar()
        self.lbox_3 = ttk.Combobox(textvariable=self.cname3, width=40, state='disabled')
        self.lbox_3.bind('<<ComboboxSelected>>', lambda _: name_callback(self.cname3))

        #self.label_name.grid(column=3, row=6, sticky=W+N)
        self.lbox_3.grid(column=4, row=6, rowspan=2, sticky=N)



    def get_txt(self):
        return self.txt

    def delete(self):
        self.txt.grid_forget()

    def remember(self):
        self.__init__()


class Buttons(App):
    def __init__(self):
        # create a Frame for buttons (search and html)
        buttons_frm = Frame(App.root)

        # buttons_frm.config(bg="black")
        buttons_frm.grid(row=13, column=0, columnspan=3, sticky=W + E + N + S, padx=10, pady=10)

        # create buttons search and html in a button_frm
        self.search_b = Button(buttons_frm, text="Search", width=20, height=5, command=search_callback)
        self.html_b = Button(buttons_frm, text="Get HTML", width=20, height=5, command=html_callback)
        self.clean_b = Button(buttons_frm, text="Clean", width=20, height=5, command=clean_callback)

        self.search_b.config(bg="grey")
        self.html_b.config(bg="grey")
        self.clean_b.config(bg="red")

        self.search_b.grid(row=0, column=0, padx=45, pady=10)
        self.html_b.grid(row=0, column=1, padx=50, pady=10)
        self.clean_b.grid(row=0, column=2, padx=50, pady=10)


class ChooseMethod(App):
    def __init__(self):
        self.radio_choice = IntVar()
        self.value = -1

        label_choose_method = Label(text="Choose search method: ")
        self.sax_radio_b = Radiobutton(text="SAX", variable=self.radio_choice, value=1,
                                       command=lambda: radio_buttons_callback(self.sax_radio_b))
        self.dom_radio_b = Radiobutton(text="DOM", variable=self.radio_choice, value=2,
                                       command=lambda: radio_buttons_callback(self.dom_radio_b))

        label_choose_method.grid(row=2, column=3, padx=50, sticky=W + E + N + S)
        self.sax_radio_b.grid(row=2, column=4, padx=50, sticky=W + E + N + S)
        self.dom_radio_b.grid(row=2, column=5, padx=50, pady=0, sticky=W + E + N + S)

    def get_sax_radio(self):
        return self.sax_radio_b

    def get_dom_radio(self):
        return self.dom_radio_b


class CityList(App):
    def __init__(self):
        self.label_city = Label(text="City: ")

        self.cnames1 = StringVar()
        self.lbox_1 = ttk.Combobox(textvariable=self.cnames1, width=40, state='disabled')
        self.lbox_1.bind('<<ComboboxSelected>>', lambda _: city_callback(self.cnames1))

        self.lbox_1['values'] = ('Вінниця', 'Київ', '')
        self.label_city.grid(column=3, row=4, sticky=W + N)
        self.lbox_1.grid(column=4, row=4, rowspan=2, sticky=N)

    def get_city_list(self):
        return self.lbox_1


def city_callback(event):
    global city
    city = event.get()
    if not city:
        city = None


class AddressList(App):
    def __init__(self):
        self.label_address = Label(text="Address: ")

        self.cnames2 = StringVar()
        self.lbox_2 = ttk.Combobox(textvariable=self.cnames2, width=40, state='disabled')
        self.lbox_2.bind('<<ComboboxSelected>>', lambda _: address_callback(self.cnames2))

        self.lbox_2['values'] = ('Майдан ТЦ "Глобус"', 'Майдан "Арома кава"', 'Соборна ТЦ "Sky Park"',
                                 'Коцюбинського ТЦ "Петроцентр"', 'Сорокоріччя перемоги ТЦ "Магігранд"', '')
        self.label_address.grid(column=3, row=5, sticky=W + N)
        self.lbox_2.grid(column=4, row=5, rowspan=2, sticky=N)

    def get_address_list(self):
        return self.lbox_2


def address_callback(event):
    global address
    address = event.get()
    if not address:
        address = None


class NameList(App):
    def __init__(self):
        self.label_name = Label(text="Name: ")

        self.cnames3 = StringVar()
        self.lbox_3 = ttk.Combobox(textvariable=self.cnames3, width=40, state='disabled')
        self.lbox_3.bind('<<ComboboxSelected>>', lambda _: name_callback(self.cnames3))

        self.lbox_3['values'] = ('Американо', 'Еспрессо', 'Капучіно', 'Мокачіно', 'Лате', 'Кава з молоком', '')
        self.label_name.grid(column=3, row=6, sticky=W + N)
        self.lbox_3.grid(column=4, row=6, rowspan=2, sticky=N)

    def get_name_list(self):
        return self.lbox_3


def name_callback(event):
    global name
    name = event.get()
    if not name:
        name = None


class PriceList(App):
    def __init__(self):
        self.label_price = Label(text="Price: ")

        self.cnames4 = StringVar()
        self.lbox_4 = ttk.Combobox(textvariable=self.cnames4, width=40, state='disabled')
        self.lbox_4.bind('<<ComboboxSelected>>', lambda _: price_callback(self.cnames4))

        self.lbox_4['values'] = ('4.0', '4.5', '5.0', '5.5', '6.0', '6.5', '7.0', '7.5', '8.0', '8.5', '9.0', '9.5',
                                 '10.0', '10.5', '11.0', '11.5', '12.0', '12.5', '13.0', '13.5', '14.0', '')
        self.label_price.grid(column=3, row=7, sticky=W + N)
        self.lbox_4.grid(column=4, row=7, rowspan=2, sticky=N)

    def get_price_list(self):
        return self.lbox_4


def price_callback(event):
    global price
    price = event.get()
    if not price:
        price = None


class Ratelist(App):
    def __init__(self):
        self.label_rate = Label(text="Rate: ")

        self.cnames5 = StringVar()
        self.lbox_5 = ttk.Combobox(textvariable=self.cnames5, width=40, state='disabled')
        self.lbox_5.bind('<<ComboboxSelected>>', lambda _: rate_callback(self.cnames5))

        self.lbox_5['values'] = ('0.1', '', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8',
                                 '1.9', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3.0',
                                 '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '4.0',
                                 '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8', '4.9', '5.0', '')
        self.label_rate.grid(column=3, row=8, sticky=W + N)
        self.lbox_5.grid(column=4, row=8, rowspan=3, sticky=N)

    def get_rate_list(self):
        return self.lbox_5


def rate_callback(event):
    global rate
    rate = event.get()
    if not rate:
        rate = None


class KindList(App):
    def __init__(self):
        self.label_kind = Label(text="Kind: ")

        self.cnames6 = StringVar()
        self.lbox_6 = ttk.Combobox(textvariable=self.cnames6, width=40, state='disabled')
        self.lbox_6.bind('<<ComboboxSelected>>', lambda _: kind_callback(self.cnames6))

        self.lbox_6['values'] = ('Зерновий', 'Розчинний', 'Невідомо', '')
        self.label_kind.grid(column=3, row=9, sticky=W + N)
        self.lbox_6.grid(column=4, row=9, rowspan=2, sticky=N)

    def get_kind_list(self):
        return self.lbox_6


def kind_callback(event):
    global kind
    kind = event.get()
    if not kind:
        kind = None


class BagsList(App):
    def __init__(self):
        self.label_bag = Label(text="Bags: ")

        self.cnames7 = StringVar()
        self.lbox_7 = ttk.Combobox(textvariable=self.cnames7, width=40, state='disabled')
        self.lbox_7.bind('<<ComboboxSelected>>', lambda _: bags_callback(self.lbox_7))

        self.lbox_7['values'] = ('Так', 'Ні', '')
        self.label_bag.grid(column=3, row=10, sticky=W + N)
        self.lbox_7.grid(column=4, row=10, rowspan=2, sticky=N)

    def get_bags_list(self):
        return self.lbox_7


def bags_callback(event):
    global bags
    bags = event.get()
    if not bags:
        bags = None


# call in class Buttons
def search_callback():
    global city, address, name, price, rate, kind, bags, dom_flag
    if dom_flag:
        print("dom")
        dom_parse()
    elif sax_flag:
        print('sax')
        sax_parse()

    txt = text.get_txt()
    txt.delete('1.0', END)

    with open('output5.txt', encoding='utf8') as file:  # Use file to refer to the file object
        data = file.read()
    txt.insert('1.0', data)

    delete_content('output5.txt')


# call in class Buttons
def clean_callback():
    txt = text.get_txt()
    txt.delete('1.0', END)

    city_list.get_city_list()['state'] = 'disabled'
    address_list.get_address_list()['state'] = 'disabled'
    name_list.get_name_list()['state'] = 'disabled'
    price_list.get_price_list()['state'] = 'disabled'
    rate_list.get_rate_list()['state'] = 'disabled'
    kind_list.get_kind_list()['state'] = 'disabled'
    bags_list.get_bags_list()['state'] = 'disabled'

    city_list.get_city_list().set('')
    address_list.get_address_list().set('')
    name_list.get_name_list().set('')
    price_list.get_price_list().set('')
    rate_list.get_rate_list().set('')
    kind_list.get_kind_list().set('')
    bags_list.get_bags_list().set('')

    choose_method.get_dom_radio().deselect()
    choose_method.get_sax_radio().deselect()

    global city, address, name, price, rate, kind, bags

    city = None
    address = None
    name = None
    price = None
    rate = None
    kind = None
    bags = None


# call in class Buttons
def html_callback():
    webbrowser.open('C:/Users/Bohdan/PycharmProjects/laboop2/1.html')


# call in class ChooseMethod
def radio_buttons_callback(event):
    city_list.get_city_list()['state'] = 'normal'
    address_list.get_address_list()['state'] = 'normal'
    name_list.get_name_list()['state'] = 'normal'
    price_list.get_price_list()['state'] = 'normal'
    rate_list.get_rate_list()['state'] = 'normal'
    kind_list.get_kind_list()['state'] = 'normal'
    bags_list.get_bags_list()['state'] = 'normal'

    global dom_flag, sax_flag
    if event['text'] == "SAX":
        sax_flag = True
        dom_flag = False
    elif event['text'] == "DOM":
        dom_flag = True
        sax_flag = False


# call in function search_callback
def dom_parse():
    doc = xml.dom.minidom.parse('1.xml')
    dom = DOM()
    output = open('output5.txt', 'w', encoding='utf8')

    global city, address, name, price, rate, kind, bags
    print(city, address, name, price, rate, kind, bags)

    document = Document(dom, doc, output, city=city, address=address, name=name, price=price,
                        rate=rate,
                        kind=kind, bags=bags)
    document.context_interface()
    output.close()


def sax_parse():
    sax = SAX()
    source = open('1.xml', encoding='utf-8')
    output = open("output5.txt", 'w', encoding='utf-8')


    global city, address, name, price, rate, kind, bags
    print(city, address, name, price, rate, kind, bags)

    document = Document(sax, source, output, city=city, address=address, name=name, price=price,
                        rate=rate,
                        kind=kind, bags=bags)
    document.context_interface()
    output.close()
    source.close()


def delete_content(file):
    with open(file, "w"):
        pass


if __name__ == '__main__':
    app = App()
    text = TextWidget()
    buttons = Buttons()
    choose_method = ChooseMethod()
    city_list = CityList()
    address_list = AddressList()
    name_list = NameList()
    price_list = PriceList()
    rate_list = Ratelist()
    kind_list = KindList()
    bags_list = BagsList()

    city = None
    address = None
    name = None
    price = None
    rate = None
    kind = None
    bags = None

    dom_flag = False
    sax_flag = False

    app.root.mainloop()




