from tkinter import *
import webbrowser
import datetime
import time

try:
    open("BLACKSHARK_Logs.txt")
except Exception:
    demo_log_create = open("BLACKSHARK_Logs.txt", "w")
    demo_log_headers = demo_log_create.write("Date,Time,Search Term,Search Engine,Link" + "\n")
    demo_log_create.close()

def search_function():
    entry_value = main_window_entry.get()
    entry_value_replaced = entry_value.replace(" ", "+")
    intvalue_1 = search_int_1.get()
    intvalue_2 = search_int_2.get()
    intvalue_3 = search_int_3.get()
    intvalue_4 = search_int_4.get()
    intvalue_5 = search_int_5.get()
    intvalue_6 = search_int_6.get()
    datetime_create = datetime.datetime.now()
    datetime_log = datetime_create.strftime("%y/%m/%d,%H:%M:%S,")
    if intvalue_1 == 1:
        webbrowser.open("https://www.google.com/search?q="+entry_value_replaced)
        intvalue_1_log = open("BLACKSHARK_Logs.txt", "a")
        intvalue_1_write = intvalue_1_log.write(datetime_log + entry_value + "," + "Google" + ",https://www.google.com/search?q="+entry_value_replaced + "\n")
        intvalue_1_log.close()
        time.sleep(1)
    if intvalue_2 == 1:
        webbrowser.open("https://duckduckgo.com/?t=ffab&q="+entry_value_replaced+"&ia=web")
        intvalue_2_log = open("BLACKSHARK_Logs.txt", "a")
        intvalue_2_write = intvalue_2_log.write(datetime_log + entry_value + "," + "DuckDuckGo" + ",https://duckduckgo.com/?t=ffab&q"+entry_value_replaced+"&ia=web" + "\n")
        intvalue_2_log.close()
        time.sleep(1)
    if intvalue_3 == 1:
        webbrowser.open("https://www.youtube.com/results?search_query="+entry_value_replaced+"&ia=web")
        intvalue_3_log = open("BLACKSHARK_Logs.txt", "a")
        intvalue_3_write = intvalue_3_log.write(datetime_log + entry_value + "," + "YouTube" + ",https://www.youtube.com/results?search_query="+entry_value_replaced+"&ia=web" + "\n")
        intvalue_3_log.close()
        time.sleep(1)
    if intvalue_4 == 1:
        webbrowser.open("https://ca.search.yahoo.com/search?p="+entry_value_replaced+"&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8")
        intvalue_4_log = open("BLACKSHARK_Logs.txt", "a")
        intvalue_4_write = intvalue_4_log.write(datetime_log + entry_value + "," + "Yahoo" + ",https://ca.search.yahoo.com/search?p="+entry_value_replaced + "&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8" + "\n")
        intvalue_4_log.close()
        time.sleep(1)
    if intvalue_5 == 1:
        webbrowser.open("https://www.bing.com/search?q="+entry_value_replaced)
        intvalue_5_log = open("BLACKSHARK_Logs.txt", "a")
        intvalue_5_write = intvalue_5_log.write(datetime_log + entry_value + "," + "Bing" + ",https://www.bing.com/search?q="+entry_value_replaced + "\n")
        intvalue_5_log.close()
        time.sleep(1)
    if intvalue_6 == 1:
        webbrowser.open("https://yandex.com/search/?text="+entry_value_replaced+"&lr=10115")
        intvalue_6_log = open("BLACKSHARK_Logs.txt", "a")
        intvalue_6_write = intvalue_6_log.write(datetime_log + entry_value + "," + "Yandex" + ",https://yandex.com/search/?text="+entry_value_replaced + "&lr=10115" + "\n")
        intvalue_6_log.close()
        time.sleep(1)
            
main_window = Tk()
main_window.geometry("500x500")
main_window.title("BLACKSHARK")
main_window.configure(bg="White")
main_window.resizable(False, False)

search_int_1 = IntVar()
search_int_2 = IntVar()
search_int_3 = IntVar()
search_int_4 = IntVar()
search_int_5 = IntVar()
search_int_6 = IntVar()

main_window_title = Label(main_window, text="BLACKSHARK", bg="White", fg="Black", font=("Arial", 20))
main_window_title.pack(pady=5)

main_window_description = Label(main_window, text="Enter a search term into the entry bar, then select which search engines you would like to search with", bg="White", fg="Black", font=("Arial", 12), wraplength=500)
main_window_description.pack(pady=5)

main_window_search_1 = Checkbutton(main_window, text="Google", bg="White", fg="Black", variable=search_int_1, onvalue=1, offvalue=0)
main_window_search_1.pack(pady=5)

main_window_search_2 = Checkbutton(main_window, text="DuckDuckGo", bg="White", fg="Black", variable=search_int_2, onvalue=1, offvalue=0)
main_window_search_2.pack(pady=5)

main_window_search_3 = Checkbutton(main_window, text="YouTube", bg="White", fg="Black", variable=search_int_3, onvalue=1, offvalue=0)
main_window_search_3.pack(pady=5)

main_window_search_4 = Checkbutton(main_window, text="Yahoo", bg="White", fg="Black", variable=search_int_4, onvalue=1, offvalue=0)
main_window_search_4.pack(pady=5)

main_window_search_5 = Checkbutton(main_window, text="Bing", bg="White", fg="Black", variable=search_int_5, onvalue=1, offvalue=0)
main_window_search_5.pack(pady=5)

main_window_search_6 = Checkbutton(main_window, text="Yandex", bg="White", fg="Black", variable=search_int_6, onvalue=1, offvalue=0)
main_window_search_6.pack(pady=5)

global main_window_entry
main_window_entry = Entry(main_window, width=75, borderwidth=5)
main_window_entry.pack(pady=5)

main_window_search_button = Button(main_window, text="SEARCH", relief="flat", borderwidth=0, font=("Arial", 12), command=search_function)
main_window_search_button.pack(pady=5)

main_window_close_button = Button(main_window, text="CLOSE", relief="flat", borderwidth=0, font=("Arial", 12), command=main_window.destroy)
main_window_close_button.pack(pady=5)

main_window.mainloop()
