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
        self.genTool=None
        
    def main(self):
        self.view.main()
        
    def on_button_click(self,  caption):
        #print(f' Inside controller  data for {caption} recieved')
        if self.view.gen_tool is not None:
            print("Buttonf fuction access From  view class")
#             self.about= genTool(self,self.controller)
#             self.model.value2=self.about.value_var2
#             print(self.model.value2.get())
        
        else:
            print("Buttonf fuction access From  genTool class")
#             self.model.value1=self.view.value_var1
#             print(self.model.value1.get())
#             result= self.model.recogniseButton(caption)
#             self.view.value_var1.set(result)
        # old varient
    #def on_button_click(self,  caption):
        #print(f' Inside controller  data for {caption} recieved')
        #self.model.value1=self.view.value_var1  
        #self.model.value2= self.view.value_var2  # **Donot get the value #here**
        #print(self.model.value1.get())
        #result= self.model.recogniseButton(caption)
        #self.view.value_var1.set(result)
if __name__ == "__main__":
    app = Controller()
    app.main()
