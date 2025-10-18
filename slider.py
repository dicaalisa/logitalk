from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Logik")
        self.geometry("800x600")
        self.configure(fg_color="#1e1e1e")
        self.resizable(True,False)
        
        self.menu_frame = CTkFrame(self,width=30,height=600, fg_color="#1a1a1a")
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0,y=0)
        self.is_showMenu = False
        self.speed_animateMenu = -5
        self.menu_btn = CTkButton(self,text="※", font=('aria',24), width=30, fg_color="#2b0202",command=self.toggle_menu)
        self.menu_btn.place(x=0,y=0)

        self.chat_field = CTkScrollableFrame(self)
        self.chat_field.place(x=0,y=0)

        self.message_entry = CTkEntry(self, placeholder_text='Введіть повідомлення...',height=40)
        self.message_entry.place(x=0,y=0)

        self.send_btn = CTkButton(self,text="→",width=50,height=40,command = self.send_massage)
        self.send_btn.place(x=0,y=0)


    def toggle_menu(self):
        if self.is_showMenu:
            self.is_showMenu = False
            self.speed_animateMenu *= -1
            self.menu_btn.configure(text="※ MENU")
            self.show_menu()
        else:
            self.is_showMenu = True
            self.speed_animateMenu *= -1
            self.menu_btn.configure(text="※")
            self.show_menu()
            self.label = CTkLabel(self.menu_frame, text="Name", font=('aria', 24), fg_color="#ffffff")
            self.label.pack(pady=20)
            self.entry = CTkEntry(self.menu_frame, fg_color="#1a1a1a")
            self.entry.pack(pady=10)

    def show_menu(self):
        self.menu_frame.configure(width=self.menu_frame.winfo_width()+self.speed_animateMenu)
        if not self.menu_frame.winfo_width() >= 200 and self.is_showMenu:
            self.after(5,self.show_menu)
            self.menu_btn.configure(width=200)
        elif self.menu_frame.winfo_width() <= 30 and not self.is_showMenu:
            self.after(5,self.show_menu)
            self.menu_btn.configure(width=30)
            if self.label and self.entry:
                self.label.destroy()
                self.entry.destroy()




window = MainWindow()
window.mainloop()