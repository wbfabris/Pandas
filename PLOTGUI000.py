import PySimpleGUI as sg

def pxxteste01():

    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Some text on Row 1')],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()

#_______________________________________________
def pxxteste02():
    
    form = sg.FlexForm('PPP Simple data entry form')
    # begin with a blank form
    layout = [
            [sg.Text('Entre com Jogos, Data, DiaSemana, Linha, Dezena')]   
            [sg.Text('Pesquisa')]               
            [sg.Text('Jogo De: ', size=(5, 1), sg.InputText(), sg.Text(' Até: ', size=(5, 2), sg.InputText()))],           
            [sg.Text('E-mail Address', size=(15, 3), sg.InputText('email.com'))],
            [sg.Submit(), sg.Cancel()],
             ]

    # Create the Window
    window = sg.Window('My First App', layout)

    window=sg.Window('Earth Residents Contact Data', layout)
    button, values = window.Read()
    window.Close() # added to fix downstream problem
    print(button, values[0], values[1], values[2])
    quit()

#______________________________________________________
def pxxteste03():

    layout = [ [sg.Text("the feedback" , key="feedback")],
            [sg.Button("FORWARD")],
            [sg.Button("LEFT"),sg.Button("RIGHT")],
            [sg.Button("STOP")],
            [sg.Button("QUIT")]
            ]
    # Create the Window
    window = sg.Window('My First App', layout)
    # Event Loop to process "events"
    while True:
        event, values = window.read()
        window['feedback'].Update(event) # show the button in the feedback text
        print(event,values)
        if event in (None, 'QUIT'):
            break
    window.close()
    # The PySimplegui sg.window() call displays a window with the title and a layout definition (line 11). The window.read() will return events and values that have been changed (line 14). The feedback text element (line 5) is given a key name of  feedback, and this key name is used for updates to show the key press (line 15).

#___________________________________________________________

def main():

    sg.theme('Dark Blue 3')
    layout = [[sg.Text('Send an Email', font='Default 18')],
              [sg.T('From:', size=(8,1)), sg.Input(key='-EMAIL FROM-', size=(35,1))],
              [sg.T('To:', size=(8,1)), sg.Input(key='-EMAIL TO-', size=(35,1))],
              [sg.T('Subject:', size=(8,1)), sg.Input(key='-EMAIL SUBJECT-', size=(35,1))],
              [sg.T('Mail login information', font='Default 18')],
              [sg.T('User:', size=(8,1)), sg.Input(key='-USER-', size=(35,1))],
              [sg.T('Password:', size=(8,1)), sg.Input(password_char='*', key='-PASSWORD-', size=(35,1))],
              [sg.Multiline('Type your message here', size=(60,10), key='-EMAIL TEXT-')],
              [sg.Button('Send'), sg.Button('Exit')]]

    window = sg.Window('Send An Email', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Send':
            if sg.__name__ != 'PySimpleGUIWeb':     # auto close popups not yet supported in PySimpleGUIWeb
                sg.popup_quick_message('Sending your message... this will take a moment...', background_color='red')
            send_an_email(from_address=values['-EMAIL FROM-'],
                          to_address=values['-EMAIL TO-'],
                          subject=values['-EMAIL SUBJECT-'],
                          message_text=values['-EMAIL TEXT-'],
                          user=values['-USER-'],
                          password=values['-PASSWORD-'])

    window.close()

#___________________________________  
def pxxtest04():  

    # Green & tan color scheme      
    sg.ChangeLookAndFeel('GreenTan')      

    sg.SetOptions(text_justification='right')      

    layout = [[sg.Text('Machine Learning Command Line Parameters', font=('Helvetica', 16))],      
              [sg.Text('Passes', size=(15, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1)),      
               sg.Text('Steps', size=(18, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1))],      
              [sg.Text('ooa', size=(15, 1)), sg.In(default_text='6', size=(10, 1)), sg.Text('nn', size=(15, 1)),      
               sg.In(default_text='10', size=(10, 1))],      
              [sg.Text('q', size=(15, 1)), sg.In(default_text='ff', size=(10, 1)), sg.Text('ngram', size=(15, 1)),      
               sg.In(default_text='5', size=(10, 1))],      
              [sg.Text('l', size=(15, 1)), sg.In(default_text='0.4', size=(10, 1)), sg.Text('Layers', size=(15, 1)),      
               sg.Drop(values=('BatchNorm', 'other'), auto_size_text=True)],      
              [sg.Text('_'  * 100, size=(65, 1))],      
              [sg.Text('Flags', font=('Helvetica', 15), justification='left')],      
              [sg.Checkbox('Normalize', size=(12, 1), default=True), sg.Checkbox('Verbose', size=(20, 1))],      
              [sg.Checkbox('Cluster', size=(12, 1)), sg.Checkbox('Flush Output', size=(20, 1), default=True)],      
              [sg.Checkbox('Write Results', size=(12, 1)), sg.Checkbox('Keep Intermediate Data', size=(20, 1))],      
              [sg.Text('_'  * 100, size=(65, 1))],      
              [sg.Text('Loss Functions', font=('Helvetica', 15), justification='left')],      
              [sg.Radio('Cross-Entropy', 'loss', size=(12, 1)), sg.Radio('Logistic', 'loss', default=True, size=(12, 1))],      
              [sg.Radio('Hinge', 'loss', size=(12, 1)), sg.Radio('Huber', 'loss', size=(12, 1))],      
              [sg.Radio('Kullerback', 'loss', size=(12, 1)), sg.Radio('MAE(L1)', 'loss', size=(12, 1))],      
              [sg.Radio('MSE(L2)', 'loss', size=(12, 1)), sg.Radio('MB(L0)', 'loss', size=(12, 1))],      
              [sg.Submit(), sg.Cancel()]]      

    window = sg.Window('Machine Learning Front End', layout, font=("Helvetica", 12))      

    event, values = window.read()     

#______________________________________________________
#main()
#pxxteste02()
pxxtest04()