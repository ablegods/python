from tkinter import *
import urllib3
import certifi

def main(w):
    gui(w)
    w.mainloop()

def gui(w):
    w.title("收集資料")
    # w.geometry('500x300')
    topFrame = Frame(w,bd=1,relief=GROOVE)
    topFrame.config(bg="#dddddd")
    Button(topFrame, text="空氣品質指標",font=('Verdans',13,'bold'),command="aqi").pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    Button(topFrame, text="確定2",font=('Verdans',13,'bold')).pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    Button(topFrame, text="確定3",font=('Verdans',13,'bold')).pack(ipadx=25, ipady=10, side=LEFT, expand=YES)
    topFrame.pack(ipady=20,ipadx=20,pady=20,padx=20)
    bottomFrame = Frame(w,bd=1,relief=GROOVE)
    bottomFrame.pack(ipady=20,ipadx=20,pady=20,padx=20,expand=YES,fill=X)

def aqi():
    # 下載AQI
    CSV_URL = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=csv"



if __name__ == "__main__":
    window = Tk()
    main(window)