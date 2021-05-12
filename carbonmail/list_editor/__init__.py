import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.list_editor import view 

class List_Editor():
    def __init__(self,email_sender):
        self.window = None
        self.ems = email_sender
        
    def instantiate(self):
        if self.window == None:
            self.window = view.get_window()
    
    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()
            
            if event in (WIN_CLOSED,"-Back"):
                self.window.close()
                self.ems.unhide_window()
                break
                
            if event == "-Send-":
                title = values ["-Title-"]
                content = values ["-Content-"]
            
                sg.Popup(
                f"O título é:{title}\nO conteúdo é:{content}",
                title="E-mail",
                )
    
    def close_window(self):
        if self.window != None:
            self.window.close()
        self.window = None
    
    def hide_window(self):
        if self.window != None:
            self.window.hide()
    
    def unhide_window(self):
        if self.window != None:
            self.window.UnHide()
    