class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You drive the {self.color} {self.model}, year {self.year}.")
        
    
    def stop(self):
        print(f"You stopped driving the {self.color} {self.model}, year {self.year}.")

    def sale(self):
        if self.for_sale:
            print(f"I see that your {self.model} is for sale.")
        else:
            print(f"I see that your {self.model} is not for sale.")

