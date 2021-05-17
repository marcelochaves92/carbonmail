#É onde fica o código para a interface gráfica
#Tudo que for VISUAL estará aqui
#É principalmente aqui que usaremos o PySimpleGUI

import PySimpleGUI as sg

lista=['Administradores','Aluno']

def get_layout():
    layout = [
        [
            sg.Text("Selecione o seu código:"),
            sg.In(),
            sg.FileBrowse("Selecione",file_types=(("Códigos Python","*.py"),) )
        ],
        [
            sg.Text("Selecione a lista de destinatários"),
            sg.Combo(lista, default_value = lista[1] )
        ],
        [
            sg.Text("Insira o título:"),
            sg.In(key="-Title-")
        ],
        [
            sg.Text("Insira o conteúdo do email"),
            sg.MLine(key="-Content-")
        ],
        [
            sg.Button("Enviar",key="-Send-"),
            sg.Button("Gerenciar listas",key="-ListEditor-"),
        ],
    ]
    
    return layout

def get_window():
    
    return sg.Window("Teste de Janela",get_layout())