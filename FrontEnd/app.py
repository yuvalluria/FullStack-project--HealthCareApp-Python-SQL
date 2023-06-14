
from FrontEnd.views import HomePage
from Communication.model_input import Insert2DB
from Communication.queries import DataQueries

class App():
    def __init__(self):

        self.dbName = "lung_cancer"
        self.model_input = Insert2DB(self)
        self.queries = DataQueries(self.dbName)
        self.views = HomePage(self)

if __name__ == "__main__":
    app = App()
    app.views.run()

