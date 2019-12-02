class Model:

    def __init__(self):
        self.value1 =''
        self.value2 =''
    def recogniseButton(self, caption):
        
        if caption == 'Button1':
            print('Inside the Model Button1  registered. ')
            self.value= ''
            return self.value
        if caption == 'Button2':
            print("Inside the Model Button2  registered. This button is  toplevel")
            self.value= ''
            return self.value
            
        
        
