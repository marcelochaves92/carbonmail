import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.list_editor import view 
from carbonmail.list_editor.manager import create_list, create_contact, update_lists

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
            
            if values is not None:
                self.lists = values["-Lists-"]
            
            if event in (WIN_CLOSED,"-Back-"):
                self.window.close()
                self.ems.unhide_window()
                break
                
            elif event == "-Create-":
                list_name=values["-ListName-"]
                
                if create_list(list_name):
                    sg.Popup("Sua lista foi criada", title="Sucesso")
                    update_lists(self.window,self.lists)
                else:
                    sg.Popup("Digite um nome válido", title="Erro!")
                    
    def close_window(self):
        if self.window is not None:
            self.window.Close()
        self.window = None
    
    def hide_window(self):
        if self.window is not None:
            self.window.Hide()
    
    def unhide_window(self):
        if self.window is not None:
            self.window.UnHide()
    