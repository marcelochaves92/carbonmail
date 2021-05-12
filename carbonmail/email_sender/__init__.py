import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.email_sender import view 
from carbonmail.list_editor.manager import initialize as init_list_editor

class Email_Sender():
    def __init__(self):
        self.window = None
        
    def instantiate(self):
        if self.window == None:
            self.window = view.get_window()
    
    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()
            
            if event == WIN_CLOSED:
                self.close_window()
                break
                
            if event == "-Send-":
                title = values ["-Title-"]
                content = values ["-Content-"]
            
                sg.Popup(
                f"O título é:{title}\nO conteúdo é:{content}",
                title="E-mail",
                )

            if event == '-ListEditor-':
                    self.hide_window()
                    init_list_editor(self)
    def close_window(self):
        if self.window != None:
            self.window.close()
    
    def hide_window(self):
        if self.window != None:
            self.window.hide()
    
    def unhide_window(self):
        if self.window != None:
            self.window.UnHide()
    
    