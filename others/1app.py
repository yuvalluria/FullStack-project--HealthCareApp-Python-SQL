from FrontEnd.views import *
from Communication.model_input import *
from Communication.queries import *



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('lung_cancer_system')
        self.geometry('1200x800')
        self.resizable(True,True)
        self.inputs = Insert2DB(self)
        self.queries = DataQueries(self, "lung_cancer")
        # layout on the root window



if __name__ == "__main__":
    app = App()
    app.mainloop()
