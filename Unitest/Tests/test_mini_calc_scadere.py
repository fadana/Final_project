from Unitest.App.Mini_calc import Mini_calc


class TestMiniCalcinmultire():
    def setup_method (self):
        print ("Instructiuni executate la inceput")
        self.calc = Mini_calc(8,4)
    def teardown_method(self):
        print("instructiuni executate la final")
    def inmultire(self):
        self.calc.inmultire();