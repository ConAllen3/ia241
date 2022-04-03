class car:
    
    maker = 'toyota'
    
    def __init__(self,input_model):
    
        self.model = input_model
    
    def report(self):
        
        return self.maker, self.model
        
#my_corolla = car('corolla')

#my_highlander = car('highlander')

#print(my_corolla.report())
#print(my_highlander.report())

#my_corolla.model = 'venza'

#print(my_corolla.model)
