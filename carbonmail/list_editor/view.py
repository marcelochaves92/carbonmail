from carbonmail.email_sender.view import get_window
import PySimpleGUI as sg
from carbonmail.utils import inner_element_space
lista = ['Administradores','Alunos']

def get_layout():
    
    frame_list = [
        inner_element_space(600),
        [
            sg.Text("Selecione a lista:"),
            sg.Combo(lista,default_value=lista[1],key="-List-"),
        ],
        [
            sg.Text("Cria uma lista:"),
            sg.In(key="-ListName-"),
            sg.Button("Criar",key="-Create-",size=(10,1) ),
        ],
        [
            sg.Button(
                "Deletar a lista",
                key="-Delete-",
                size=(15,1),
                pad=(5,(7,7)),
            ),
            sg.Button(
                "Mostrar contatos",
                key="-Delete-",
                size=(15,1),
                pad=(5,(7,7)),
            ),
        ],
        inner_element_space(600),
    ]
    
    frame_import = [
        inner_element_space(600),
        [
                sg.Text(
                    "Selecione o arquivo (CSV):",
                    tooltip="Cabeçalhos: name e email"
                ),
                sg.In(key="-CSV-"),
                sg.FileBrowse(
                    "Selecionar",
                    file_types=(("CSV","*.csv"),),
                    tooltip="Cabeçalhos: name e email",
                ),
        ],
        [
          sg.Button(
              "Importar contatos",
              key="-Import-",
              size=(15,1),
              pad=(0,(7,7)),
          )  
        ],
        inner_element_space(600),
    ]
    
    frame_add = [
        inner_element_space(600),
        [
            sg.Text("Insira o nome:"),
            sg.In(key="-Name-")
        ],
        [
            sg.Text("Insira o e-mail:"),
            sg.In(key="-Email-")
        ],
        [
            sg.Button(
            "Adicionar contato:",
            sg.In(key="-Add-"),
            size=(15,1),
            pad=(0,(7,7)),
            ),
        ],
        inner_element_space(600),
    ]
    
    layout = [
        [
            sg.Frame(
                "Configurações da lista",
                frame_list,
                element_justification ="c",
                )
        ],
        [
            sg.Frame(
                "Importar contatos",
                frame_import,
                element_justification ="c",
            )
        ],
        [
            sg.Frame(
                "Adicionar contato",
                frame_add,
                element_justification ="c",
            )
        ],
        [
            sg.Button(
                "Voltar",
                key="-Back",
                size=(15,1),
                pad=(0,(7,7))
            )
        ],
        inner_element_space(600),
    ]
    return layout

def get_window():
    sg.theme("DarkBlue14")
    
    return sg.Window(
        "Editor de listas",
        get_layout(),
        element_justification ="c",
        )