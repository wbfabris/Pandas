import PySimpleGUI as sg
import PySimpleGUI as g

import os
def pxxteste01():

    # Green & tan color scheme      
    g.ChangeLookAndFeel('DarkBlue11') 
    #g.SetOptions(text_justification='left')      

    # sz = (60, 20, 20, 20, 10)
    # t = ('Longer label 1', 'Label 2', 'Label 3', 'Label 4')
    # r1 = [ g.Text(t[x], key='T'+str(x), size=(sz[x],1) ) for x in range(len(t)) ]
    # r2 = [ g.Input(key='I'+str(x), size=(sz[x],0) ) for x in range(len(t)) ]
    # r2.append( g.Button('Btn1', size=(sz[4],1)) )
    # ly = [ r1, r2 ]
    # w = g.Window('Layout with Texts + Inputs (1)', ly)

    # event, values = w.read()
    #a=1
  
    sz = (60, 40, 20, 20, 10)
    t = ('Longer label 1', 'Label 2', 'Label 3', 'Label 4')
    tk = '   ' # 3 spaces @ 0 pad, 4 @ dft
    r = [ g.Frame(tk+t[x], [[g.Input(key='I'+str(x), size=(sz[x],1))]], border_width=0) for x in range(len(t)) ]
    r.append( g.Button(' Btn1', size=(sz[4],1)) )
    ly = [ r ]
    w = g.Window('Layout with Frames (2)', ly, element_padding=((0,0),(5,5)) )
    event, values = w.read()

#_______________________________________________________
def pxxteste02():

    sg.ChangeLookAndFeel('DarkBlue11')      

    # ------ Menu Definition ------ #      
    menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
                ['Help', 'About...'], ]      

  #  
    column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      

    layout = [      
        [sg.Menu(menu_def, tearoff=True)],      
        [sg.Text('Opções de Seleção e Consulta!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],    
        [sg.Text('PESQUISA, informe:')],  
        #[sg.Text('Jogo De:', size=(5, 1)), sg.InputText()), sg.Text('Até:', size=(5, 1), sg.InputText())],      
        [sg.Text('Jogo De:', size=(7, 1)), sg.Input(size=(5,0), key='jde'), sg.Text('Ate:', size=(3, 0)), sg.InputText(size=(5,1), key='jate')],
        [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
    ]      

    window = sg.Window('Menu de Opções da Lotofacil', layout, default_element_size=(40, 1), grab_anywhere=False)    
    event, values = window.read()  
    #window.Maximize()    
    window.close()    

    sg.popup('Title',      
                'The results of the window.',      
                'The button clicked was "{}"'.format(event),      
                'The values are', values)

#_________________________________________________________
def pxxteste03():

    import PySimpleGUI as sg
    import time

    # ----------------  Create Form  ----------------
    layout = [
        [sg.Text('', background_color='black')],
        [sg.Text('00:00', size=(30, 1), font=('Helvetica', 30), justification='center',
            text_color='white', key='text', background_color='black')],
        [sg.Text('', background_color='black')],
        [sg.Button('Pause', key='button', button_color=('white', '#001480')),
        sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
        sg.Exit(button_color=('white', '#8B1A1A'), key='Exit', )],
    ]

    window = sg.Window('Running Timer', layout,
                background_color='black', font='Helvetica 18')

    # ----------------  main loop  ----------------
    current_time = 0
    paused = False
    start_time = int(round(time.time() * 100))
    while True:
        # --------- read and update window --------
        if not paused:
            event, values = window.read(timeout=0)
            current_time = int(round(time.time() * 100)) - start_time
        else:
            event, values = window.read()
        print(event, values) if event != sg.TIMEOUT_KEY else None

        if event == 'button':
            event = window[event].GetText()
        # --------- Do Button Operations --------
        
        if event in (None, 'Exit'):        # ALWAYS give a way out of program
            break
        
        if event == 'Reset':
            start_time = int(round(time.time() * 100))
            current_time = 0
            paused_time = start_time
        
        elif event == 'Pause':
            paused = True
            paused_time = int(round(time.time() * 100))
            element = window['button']
            element.update(text='Run')
        
        elif event == 'Run':
            paused = False
            start_time = start_time + int(round(time.time() * 100)) - paused_time
            element = window['button']
            element.update(text='Pause')

        # --------- Display timer in window --------
        window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                        (current_time //
                                                                        100) % 60,
                                                                        current_time % 100))
    # --------- After loop --------
    window.close()

#_________________________________________________
def pxxteste04():

    sg.ChangeLookAndFeel('DarkAmber') 
    frame_layout = [
                  [sg.T('Text inside of a frame')],
                  [sg.CB('01'), sg.CB('02'), sg.CB('03'), sg.CB('04'), sg.CB('05')],
                  [sg.CB('06'), sg.CB('07'), sg.CB('08'), sg.CB('09'), sg.CB('10')],
                  [sg.CB('11'), sg.CB('12'), sg.CB('13'), sg.CB('14'), sg.CB('15')],
                  [sg.CB('16'), sg.CB('17'), sg.CB('18'), sg.CB('19'), sg.CB('20')],
                  [sg.CB('21'), sg.CB('22'), sg.CB('23'), sg.CB('24'), sg.CB('25')],
               ]
    layout = [
            [sg.Frame('My Frame Title', frame_layout, font='Any 12', title_color='white')],
            [sg.Submit(), sg.Cancel()]
            ]

    window = sg.Window('Frame with buttons', layout, font=("Helvetica", 8))
    event, values = window.read()


#_________________________________________
def pxxteste05():
    # D:\Area de Documentos\\WBF

    layout = [
        [sg.Text('Please enter the name of the directory:')],[sg.InputText('D:\Area de Documentos\\WBF')],
        [sg.Text('Pesquisa')],
        [sg.Text('  Jogo De:'), sg.InputText(), sg.Text('Até')],[sg.InputText()],
        [sg.Text('  Data De:'), sg.InputText(), sg.Text('Até')],[sg.InputText()],
        [sg.Text('  Ano  De:'), sg.InputText(), sg.Text('Até')],[sg.InputText()],
        [sg.Text('  Mes  De:'), sg.InputText(), sg.Text('Até')],[sg.InputText()],
        [sg.Text()],
    
        [sg.Submit(), sg.Cancel()]
             ]

    window = sg.Window('Pesquisa Jogos da lotofacil', layout)
    event, values = window.read()
    sg.Print(event)
    window.close()

    i = -1
    for a in values : 
        i = i + 1
        print('valor´ & [i] ' = ' values[i])

    if event == 'Submit':
        #os.mkdirs(values[0])   
        os.getcwd(values[0]) 
             
#_________________________________________
pxxteste05()
#pxxteste04()
#pxxteste03()
#pxxteste02()
#pxxteste01()

a=1