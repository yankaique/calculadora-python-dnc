from utils.calculator import calculadora
import PySimpleGUI as sg 

bw: dict = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F8F8F8")}
bt: dict = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F1EABC")}
bo: dict = {'size':(15,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#ECA527"), 'focus':True}
lastValue = '0.000'

layout: list = [
    [sg.Text('Calculadora', size=(50,1), justification='right', background_color="#272533", 
        text_color='white', font=('Franklin Gothic Book', 14, 'bold'))],
    [sg.Text('Última conta: ', size=(16), background_color="#272533", text_color='white', 
        font=('Digital-7',12)), sg.Text('0.0000', size=(16), background_color="#272533", text_color='white', 
        font=('Digital-7',12), key="_LASTCALC_")],
    [sg.Text('0.0000', size=(16,1), justification='right', background_color='black', text_color='red', 
        font=('Digital-7',48), relief='sunken', key="_DISPLAY_"), sg.Text('12')],
    [sg.Button('C',**bt), sg.Button('CE',**bt), sg.Button('%',**bt), sg.Button("/",**bt)],
    [sg.Button('7',**bw), sg.Button('8',**bw), sg.Button('9',**bw), sg.Button("*",**bt)],
    [sg.Button('4',**bw), sg.Button('5',**bw), sg.Button('6',**bw), sg.Button("-",**bt)],
    [sg.Button('1',**bw), sg.Button('2',**bw), sg.Button('3',**bw), sg.Button("+",**bt)],    
    [sg.Button('0',**bw), sg.Button('.',**bw), sg.Button('=',**bo, bind_return_key=True)]
]

window: object = sg.Window('Yan Marinho', layout=layout, background_color="#272533", size=(580, 660), return_keyboard_events=True)

var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':'', 'ultimo': 0.0}

def format_number() -> float:
    return float(''.join(var['front']) + '.' + ''.join(var['back']))


def update_display(display_value: str):
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)

def number_click(event: str):
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())
    

def clear_click():
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False 


def operator_click(event: str):
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()

def update_old_calc(display_value: str): 
    window['_LASTCALC_'].update(value='{:,.4f}'.format(display_value))

def calculate_click():
    global var
    var['y_val'] = format_number()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        update_old_calc(var['result'])
        clear_click()    
    except:
        update_display("ERROR! DIV/0")
        clear_click()


while True:
    event, values = window.read()

    if event is None:
        break
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        number_click(event)
    if event in ['Escape:27','C','CE']: # 'Escape:27 for keyboard control
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
        if event == 'CE':
            update_old_calc(0.0)
    if event in ['+','-','*','/']:
        operator_click(event)
    if event == '=':
        calculate_click()
    if event == '.':
        var['decimal'] = True
    if event == '%':
        update_display(var['result'] / 100.0)