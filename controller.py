'''

Controller is aware of model and view. thereforeOBJECTS of both Model and View class are present in controller.
Model is not aware of view or model. view knows about controller


'''
from model import Model
from view import View
from view import genTool
class Controller:
    def __init__(self):
        self.model= Model()
        self.view= View(self)
	
        
        
    def main(self):
        self.view.main()
        

    def on_button_click(self,  caption):
        print(self.view.gen_Tool)
        if self.view.gen_Tool is   None:
           
           self.model.value1=self.view.value_var1  
        #self.model.value2= self.view.value_var2  # **Donot get the value #here**
           print(f'value received form entry on main screen is {self.model.value1.get()}')
           result= self.model.recogniseButton(caption)
        else:
           self.model.value2= self.view.about.value_var2 
           print(f'value received form entry on second screen is {self.model.value2.get()}')
           self.view.gen_Tool=None
        
        
if __name__ == "__main__":
    app = Controller()
    app.main()
