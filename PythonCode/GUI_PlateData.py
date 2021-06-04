import tkinter as tk
from Graph_Code import alldata_func, averagedata_func, ave_alldata
from tkinter import messagebox
# completeavg_func



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.submit = tk.Button(self)
        self.submit["text"] = "Retrieve All Data"
        self.submit["command"] = self.alldata_onclick
        self.submit.pack(side="top")

        self.submit = tk.Button(self)
        self.submit["text"] = "Retrieve Average Data"
        self.submit["command"] = self.averagedata_onclick
        self.submit.pack(side="top")

        self.submit = tk.Button(self)
        self.submit["text"] = "Retreive Average and Raw Data"
        self.submit["command"] = self.avealldata_onclick
        self.submit.pack(side="top")

        # self.submit= tk.Button(self)
        # self.submit["text"] = "Get complete average graphs"
        # self.submit["command"] = self.completeavg_onclick
        # self.submit.pack(side="top")

        self.composition=tk.StringVar()
        self.composition.set("Composition")
        self.comp_select = tk.OptionMenu(self, self.composition, "HE700", "HE700 + Mg", "HE700 + MgSi", "Aural 5", "Aural 2")
        self.comp_select.pack(side="left")
        
        self.heattreatment=tk.StringVar()
        self.heattreatment.set("Heat Treatment")
        self.heat_select = tk.OptionMenu(self, self.heattreatment, "F", "T4", "T5", "T7", "T7N")
        self.heat_select.pack(side="left")

        self.paintbake=tk.StringVar()
        self.paintbake.set("Paint Bake")
        self.paint_select = tk.OptionMenu(self, self.paintbake, "PB0", "PB1", "PB1A", "PB2")
        self.paint_select.pack(side="left")

        self.thickness=tk.StringVar()
        self.thickness.set("Thickness")
        self.thickness_select = tk.OptionMenu(self, self.thickness, "30", "25", "23")
        self.thickness_select.pack(side="left")

        self.xaxis=tk.StringVar()
        self.xaxis.set("X-Axis")
        self.xaxis_select = tk.OptionMenu(self, self.xaxis, "Ultimate Tensile Strength", "Yield Strength", "Percent Elongation", "Date")
        self.xaxis_select.pack(side="top")

        self.yaxis=tk.StringVar()
        self.yaxis.set("Y-Axis")
        self.yaxis_select = tk.OptionMenu(self, self.yaxis, "Ultimate Tensile Strength", "Yield Strength", "Percent Elongation", "Date")
        self.yaxis_select.pack(side="top")


    
    def alldata_onclick(self):
        if self.xaxis.get() == self.yaxis.get():
            messagebox.showerror("Error", "X-Axis and Y-Axis inputs must be different")
        alldata_func(self.composition.get(), self.heattreatment.get(), self.paintbake.get(), self.thickness.get(), self.xaxis.get(), self.yaxis.get())


    def averagedata_onclick(self):
        if self.xaxis.get() == self.yaxis.get():
            messagebox.showerror("Error", "X-Axis and Y-Axis inputs must be different")
        averagedata_func(self.composition.get(), self.heattreatment.get(), self.paintbake.get(), self.thickness.get(), self.xaxis.get(), self.yaxis.get())

    def avealldata_onclick(self):
        ave_alldata(self.composition.get(), self.heattreatment.get(), self.paintbake.get(), self.thickness.get(), self.xaxis.get(), self.yaxis.get())
    
    
    # def completeavg_onclick(self):
    #     completeavg_func(self.composition.get(),self.heattreatment.get(), self.paintbake.get(), self.thickness.get(), self.xaxis.get(), self.yaxis.get())

if __name__ == "__main__": 
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("Material Properties Graphing Program")
    app.mainloop()
