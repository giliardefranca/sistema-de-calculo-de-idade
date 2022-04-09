import datetime
from datetime import date, datetime
import PySimpleGUI as sg
from datetime import date
import re
import time


sg.theme('Dark Grey 13')

#sg.theme_previewer()
def Menu():
    linha = [[sg.Text("Nome Completo", font=30, size=(16,1), text_color="white"), sg.Input(key="nome", size=(30,3), do_not_clear=False, text_color="white")],
             [sg.Text("Data de Nascimento", font=30, text_color="white"), sg.Input(key="nascimento", size=(15,10), do_not_clear=False, text_color="white")],
             [sg.Checkbox("Masculino", default=False, font=("Arial",15), key="m", text_color="red"), sg.Checkbox("Feminina", default=False, font=("Arial",15), key="f", text_color="red")]
             ]

    layout = [
        [sg.Frame('Consulte sua idade aqui', layout=linha, size=(500, 130), font=60)],
        [sg.Button("Consultar", button_color="black", key="button")]
    ]

    return sg.Window("consulte", layout=layout, finalize=True)


def inicio():
    window = Menu()
    while True:
        event, values = window.read()

        name = values["nome"]

        birh = values['nascimento']
        m = values["m"]
        f = values["f"]
        verificacao_de_nome = re.findall('\w+[a-z]', name)

        if verificacao_de_nome:
            try:
                data_convertida  = datetime.strptime(birh, '%d/%m/%Y').date()
                if m and f:
                    sg.popup_no_wait("Marque Apenas uma Opcão", text_color="white", button_color="red")
                elif m or f:
                    days_in_year = 365.2425
                    age = int((date.today() - data_convertida).days / days_in_year)
                    if age < 18:
                        sg.popup_no_wait(f"{name} sua idade é {age} anos e você é Menor de idade", font=("Arial", 12), text_color="white", button_color="red")
                    else:
                        sg.popup_no_wait(f"{name} sua idade é {age} anos e você é Maior de idade", font=("Arial", 12),
                                         text_color="white", button_color="red")
                else:
                    sg.popup_no_wait("Marque uma opcão", text_color="white", button_color="red")

            except ValueError:
                sg.popup_no_wait("Preenche a Data no formato dd/mm/yy", text_color="white", button_color="red")

        else:
            sg.popup_no_wait("Campos Vazihos ou Incorretos!", text_color="white", button_color="red")


try:
    inicio()
except TypeError:
    sg.popup_no_wait("Até mais Tarde! By", font=15, text_color="white", button_color="red")
    time.sleep(1)

