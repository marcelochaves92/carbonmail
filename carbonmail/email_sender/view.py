import PySimpleGUI as sg
from carbonmail.utils import inner_element_space
from carbonmail.list_editor.manager import load_lists

lista = load_lists()

def get_layout():
    frame_campaign = [
        inner_element_space(500),
        [
            sg.Text("Selecione o código:"),
            sg.In(key="-Code-",size=(30,1)),
            sg.FileBrowse(
                "Selecionar",
                file_types=(("Códigos Python","*.py"),),
                size=(15,1),
            ),
        ],
        [
            sg.Text("Selecione a lista de destinatários"),
            sg.Combo(
                lista,
                lista[0],
                key="-Lists-",
                ), 
        ],
        inner_element_space(500),
    ]

    frame_email = [
        inner_element_space(500),    
        [sg.Text("Insira o título",font=("Helvetica 15"))],
        [sg.In(key="-Title-",size=(62,1))],
        [sg.Text("Insira o conteúdo",font=("Helvetica 15"))],
        [sg.MLine(key="-Content-",size=(62,1))],
        inner_element_space(500),
    ]
    
    layout = [
        inner_element_space(500),
        [
            sg.Frame(
                "Configurações da campanha",
                frame_campaign,
                element_justification="c"
            )
        ],
        [
            sg.Frame(
                "Configurações do email",
                frame_email,
                element_justification="c"
            )
        ],
        [
            sg.Button(
                "Enviar e-mail",
                key="-Send-",
                size=(15,1),
                pad=(10,(10,0)),
            ),
            sg.Button(
                "Gerenciar listas",
                key="-ListEditor-",
                size=(15,1),
                pad=(10,(10,0)),
            )
        ],
        inner_element_space(500),
    ]
    return layout


def get_window():
    sg.theme("DarkBlue14")
    return sg.Window(
        "Enviador de e-mails",
        get_layout(),
        element_justification ="c",
        )
    