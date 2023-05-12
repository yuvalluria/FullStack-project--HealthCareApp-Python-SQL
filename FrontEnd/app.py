from FrontEnd.views import *
from Communication.model_input import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Apointment Manager')
        self.geometry('1200x800')
        self.resizable(True,True)
        #self.inputs = Insert2DB(self)
        #self.queries = DataQueries(self,"emr")
        # layout on the root window
        self.columnconfigure([1], weight=1, minsize=10)
        self.rowconfigure([1,2,3,4], weight=1, minsize=120)
        self.__create_frames()

    def __create_frames(self):
        # create the top frame
        self.frame1 = Frame1(self)
        self.frame1.grid(column=1, row=1, padx=5, pady=1)
        self.frame2= Frame2(self)
        self.frame2.grid(column=1, row=2, padx=5, pady=1)
        self.frame3= Frame3(self)
        self.frame3.grid(column=1, row=3, padx=5, pady=1)
        self.frame4= Frame4(self)
        self.frame4.grid(column=1, row=4, padx=5, pady=1)
        return

if __name__ == "__main__":
    app = App()
    app.mainloop()
