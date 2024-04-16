import tkinter as tk

class Root(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Palindrome detector")

        self.label_1 = tk.Label(self,text = "Welcome to the palindrome checker", fg = "#000000", bg = "#78c679", font = ("", 20), pady = 30)
        self.label_1.pack()

        self.label_2 = tk.Label(self,text = "Please type your word or phrase and press enter\n", fg = "#ddf3f5", bg = "#78c679", font = ("", 16))
        self.label_2.pack()       

        self.entry_0 = tk.Entry(self, bg = "#ddf3f5", font = ("", 14))
        self.entry_0.pack()

        self.label_3 = tk.Label(self, fg = "#ffffcc", bg = "#78c679", font = ("", 14))
        self.label_3.pack()

        self.btn_1 = tk.Button(self,text="Clear", font=("", 14), command = self.clear_text)
        self.btn_1.place(x = 400, y = 145)

        # Bind <Return> key to the entry widget
        self.entry_0.bind("<Return>", self.palindrome_detector)


    def palindrome_detector(self,event):

        input_word_lower = self.entry_0.get().replace(" ", "").lower()  
        input_word_lower_reversed = input_word_lower[::-1]

        if input_word_lower_reversed == input_word_lower:
                self.label_3["text"] = "\nThis is a palindrome\n"        
        else:            
                self.label_3["text"] = "\nThis is not a palindrome\n"


    #Resets app
    def clear_text(self):
        self.entry_0.delete(0, "end")
        self.label_3.config(text = " ")


if __name__ == "__main__":
    root = Root()
    root["bg"] = "#78c679"
    root.geometry("550x350")
    root.eval('tk::PlaceWindow . center')
    root.mainloop()

