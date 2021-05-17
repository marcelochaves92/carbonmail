#É onde fica o código para a interface gráfica
#Tudo que for VISUAL estará aqui
#É principalmente aqui que usaremos o PySimpleGUI

from carbonmail.email_sender.view import get_window
import PySimpleGUI as sg
from carbonmail.utils import inner_element_space

lista = ["Administradores","Alunos"]

def get_layout():
    
    frame_list = [
        inner_element_space(600),
        [ 
            sg.Text("Selecione a lista"),
            sg.Combo(lista, default_value = lista[1], key="-List-" )
        ],
        [
            sg.Text("Criar uma lista"),
            sg.In(key="-ListName-"),
            sg.Button("Criar", key="-Create-", size=(10,1)),
            
        ],
        [
            sg.Button(
                "Deletar a lista",
                key="-Delete-",
                size=(15,1),
                pad = (5,(7,7)),
                ),
            sg.Button(
                "Mostrar contatos",
                key="-Delete-",
                size=(15,1),
                pad = (5,(7,7)),
                ),
        ],
        inner_element_space(600),
    ] 
    
    frame_import = [
        inner_element_space(600),
        [
            sg.Text(
                "Selecione o arquivo CSV:", 
                tooltip="Cabeçalhos: name e email",
            ),
            sg.In(key="-CSV-"),
            sg.FileBrowse(
                "Selecionar",
                file_types=(("CSV","*.csv"),),
                tooltip="Cabeçalhos: name e email",
            ),
        ],
        [sg.Button(
            "Importar contatos",
            key="-Import-",
            size = (15,1)
            )
         ],
        inner_element_space(600),
    ]
        
    frame_add = [
        inner_element_space(600),
        [
            sg.Text("Insira o nome"),
            sg.In(key="-Name-"),
        ],
        [
            sg.Text("Insira o email"),
            sg.In(key="-Email-"),
        ],
        [
            sg.Button(
                "Adicionar contato",
                key="-Add-",
                size=(15,1),
                pad=(0,(7,7)),    
            )
        ],
        inner_element_space(600),
    ]
    
    layout = [
        inner_element_space(600),
        [
            sg.Frame(
                "Configurações da lista",
                frame_list,
                element_justification="c",
                )
        ],
        [
          sg.Frame(
              "Importar contatos",
              frame_import,
              element_justification ="c",
              pad = ((0,0),(7,7))
          )  
        ],
        [
            sg.Frame(
                "Adicionar contato",
                frame_add,
                element_justification = "c",
                pad = ((0,0),(7,7))
            )
        ],
        [
            sg.Button(
                "Voltar",
                key="-Back-",
                size=(15,1),
                pad = (0,(7,7)),
            )
        ],
        inner_element_space(600),
    ]
    return layout


def get_window():
    sg.theme("DarkBlue14")
    return sg.Window(
        "Editor de lista",
        get_layout(),
        element_justification = "c",
        )