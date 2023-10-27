import customtkinter as ctk
import darkdetect
import resources.calculator_settings as setting
from buttons import Button, ImageButton, NumButton, MathButton, MathImageButton
from PIL import Image
 
class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        super().__init__(fg_color= (setting.WHITE, setting.BLACK))
        #1.set appearance to dark or light depeding on is_dark
        ctk.set_appearance_mode(f'{"dark" if is_dark else "right"}')
        #2. fg_color= WHITE OR BLACK 
        #3. get start app size form the settings and disable widow resizing
        self.geometry(f"{setting.APP_SIZE[0]}x{setting.APP_SIZE[1]}")
        self.resizable(False, False)
        #4. hide the title and the icon
        self.title("")
        self.iconbitmap(r"C:\test\PythonWorkspace\Udemy_tkinter\resources\empty.ico")
        
        #layout
        self.columnconfigure(list(range(setting.MAIN_COLUMNS)), weight=1, uniform="a")
        self.rowconfigure(list(range(setting.MAIN_ROWS)), weight=1, uniform="a")
        
        #data
        self.result_string = ctk.StringVar(value="0")
        self.formula_string = ctk.StringVar(value="")
        self.display_nums = []
        self.full_operation=[]
        
        #widgets
        self.create_widgets()

        
        
        
        
        
        
        self.mainloop()
        
    def create_widgets(self):
        main_font = ctk.CTkFont(family= setting.FONT, size= setting.NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family= setting.FONT, size= setting.OUTPUT_FONT_SIZE)
        #output labes
        OutputLabel(self,0, "SE", main_font, self.formula_string) # formula
        OutputLabel(self,1, "E", result_font, self.result_string) # result
        
        #clear (AC) button
        Button(parent= self, 
               func = self.clear,
               text= setting.OPERATORS["clear"]["text"], 
               col=setting.OPERATORS["clear"]["col"],
               row=setting.OPERATORS["clear"]["row"],
               font = main_font)
        #percentage button
        Button(parent= self, 
               func = self.percent,
               text= setting.OPERATORS["percent"]["text"], 
               col=setting.OPERATORS["percent"]["col"],
               row=setting.OPERATORS["percent"]["row"],
               font = main_font)
        
        #invert button
        invert_image = ctk.CTkImage(
            light_image= Image.open(setting.OPERATORS["invert"]["image path"]["dark"]),
            dark_image= Image.open(setting.OPERATORS["invert"]["image path"]["light"])
        )
        ImageButton( parent= self,
                    func= self.invert, 
                    col = setting.OPERATORS["invert"]["col"], 
                    row =setting.OPERATORS["invert"]["row"], 
                    image = invert_image)
        
        #num button
        for num, data in setting.NUM_POSITIONS.items():
            NumButton(
                parent=self,
                text= num,
                func= self.num_press,
                col=data["col"],
                row=data["row"],
                font= main_font,
                span = data["span"]
            )
            
        #math button
        for operator, data in setting.MATH_POSITIONS.items():
            if data["image path"]:
                divide_image = ctk.CTkImage(
                    light_image= Image.open(data["image path"]["dark"]),
                    dark_image= Image.open(data["image path"]["light"])
                )
                MathImageButton(parent= self ,
                                operator = operator,
                                func = self.math_press,
                                col= data["col"],
                                row= data["row"],
                                image = divide_image)
            else:
                MathButton(
                parent=self,
                text= data["character"],
                operator=operator,
                func= self.math_press,
                col=data["col"],
                row=data["row"],
                font= main_font
                )
            
    def num_press(self,value):
        self.display_nums.append(str(value))
        full_number = "".join(self.display_nums)
        self.result_string.set(full_number)
        
    def math_press(self,value):
        current_number = "".join(self.display_nums)
        if current_number:
            self.full_operation.append(current_number)
            if value != "=":
                #update data
                self.full_operation.append(value)
                self.display_nums.clear()
                #update output
                self.result_string.set("")
                self.formula_string.set(" ".join(self.full_operation))
            else:
                formula = " ".join(self.full_operation)
                result = eval(formula)
                #format the result
                if isinstance(result, float):
                    #an integer isformatted lie a float 4.0
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 3)
                #update data
                self.full_operation.clear()
                self.display_nums = [str(result)]
                #update my output
                self.result_string.set(result)
                self.formula_string.set(formula)
   
    def clear(self):
        #clear the output
        self.result_string.set(0)
        self.formula_string.set("")
        #clear the data
        self.display_nums.clear()
        self.full_operation.clear()
        
    def percent(self):
        #devide the current value by 100
        if self.display_nums:
            #get the percentage number
            current_number = float("".join(self.display_nums))
            percent_number = current_number /100
            #update the data and output
            self.display_nums = list(str(percent_number))
            self.result_string.set("".join(self.display_nums))
            
    def invert(self):
        current_number = "".join(self.display_nums)
        if current_number:
            #positive/negative
            if float(current_number)>0:
                self.display_nums.insert(0, "-")
            else:
                del self.display_nums[0]
            self.result_string.set("".join(self.display_nums))
            
class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent,row,anchor,font,string_var):
        super().__init__(master=parent, text="123",font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row=row, sticky= anchor, padx=10)
        
if __name__ == "__main__":
    Calculator(darkdetect.isDark())
    # Calculator(False)
