# Importando a library PySimpleGui
import PySimpleGUI as sg

def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]
    
    return sg.Window("Gerenciador de Tarefas",layout=layout,finalize=True)

# Create window:
window = criar_janela_inicial()

# Criar regras dessa janela:
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'Nova Tarefa':
        window.extend_layout(window['container'], [[sg.Checkbox(''), sg.Input('')]])
        
    elif event == 'Resetar':
        window.close()
        window = criar_janela_inicial()


