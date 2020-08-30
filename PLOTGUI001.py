import PySimpleGUI as sg

def pxxteste01():

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
# def pxxteste02():  

    
#     # Green & tan color scheme      
#     sg.ChangeLookAndFeel('GreenTan') 
#     sg.SetOptions(text_justification='right')      

#     layout = [[sg.Text('Pesquisa', font=('Helvetica', 16))],      
#               [sg.Text('JOGO De:', size=(10, 1)), sg.In(), size=(6, 1)), sg.Text('Até', size=(18, 1)), sg.In(), size=(6, 1))],      
#               [sg.Text('Data DQ', size=(10, 1)), sg.In(default_text='6', size=(10, 1)), sg.Text('nn', size=(15, 1)),      
#                sg.In(default_text='10', size=(10, 1))],      
#               [sg.Text('q', size=(15, 1)), sg.In(default_text='ff', size=(10, 1)), sg.Text('ngram', size=(15, 1)),      
#                sg.In(default_text='5', size=(10, 1))],      
#               [sg.Text('l', size=(15, 1)), sg.In(default_text='0.4', size=(10, 1)), sg.Text('Layers', size=(15, 1)),      
#                sg.Drop(values=('BatchNorm', 'other'), auto_size_text=True)],      
#               [sg.Text('_'  * 100, size=(65, 1))],      
#               [sg.Text('Flags', font=('Helvetica', 15), justification='left')],      
#               [sg.Checkbox('Normalize', size=(12, 1), default=True), sg.Checkbox('Verbose', size=(20, 1))],      
#               [sg.Checkbox('Cluster', size=(12, 1)), sg.Checkbox('Flush Output', size=(20, 1), default=True)],      
#               [sg.Checkbox('Write Results', size=(12, 1)), sg.Checkbox('Keep Intermediate Data', size=(20, 1))],      
#               [sg.Text('_'  * 100, size=(65, 1))],      
#               [sg.Text('Loss Functions', font=('Helvetica', 15), justification='left')],      
#               [sg.Radio('Cross-Entropy', 'loss', size=(12, 1)), sg.Radio('Logistic', 'loss', default=True, size=(12, 1))],      
#               [sg.Radio('Hinge', 'loss', size=(12, 1)), sg.Radio('Huber', 'loss', size=(12, 1))],      
#               [sg.Radio('Kullerback', 'loss', size=(12, 1)), sg.Radio('MAE(L1)', 'loss', size=(12, 1))],      
#               [sg.Radio('MSE(L2)', 'loss', size=(12, 1)), sg.Radio('MB(L0)', 'loss', size=(12, 1))],      
#               [sg.Submit(), sg.Cancel()]]      

#     window = sg.Window('PESQUISA', layout, font=("Helvetica", 12))      

#     event, values = window.read()  

#______________________________________________________
def pxxteste03():
  

    sg.ChangeLookAndFeel('GreenTan')      

    # ------ Menu Definition ------ #      
    menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
                ['Help', 'About...'], ]      

    # ------ Column Definition ------ #      
    column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      

    layout = [      
        [sg.Menu(menu_def, tearoff=True)],      
        [sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],    
        [sg.Text('Here is some text.... and a place to enter text')],      
        [sg.InputText('This is my text')],      
        [sg.Frame(layout=[      
        [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],      
        [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],      
        [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),      
            sg.Multiline(default_text='A second multi-line', size=(35, 3))],      
        [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),      
            sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],      
        [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],      
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),      
            sg.Frame('Labelled Group',[[      
            sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),      
            sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),      
            sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),      
            sg.Column(column1, background_color='#F7F3EC')]])],      
        [sg.Text('_'  * 80)],      
        [sg.Text('Choose A Folder', size=(35, 1))],      
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
            sg.InputText('Default Folder'), sg.FolderBrowse()],      
        [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
    ]      


    window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)      

    event, values = window.read()      

    window.close()    

    sg.popup('Title',      
                'The results of the window.',      
                'The button clicked was "{}"'.format(event),      
                'The values are', values)  

#______________________________________________________
def pxxteste04():

    sg.ChangeLookAndFeel('GreenTan')      

    # ------ Menu Definition ------ #      
    menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
                ['Help', 'About...'], ]      

    # ------ Column Definition ------ #      
    column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      

    layout = [      
        [sg.Menu(menu_def, tearoff=True)],      
        [sg.Text('Opções de Seleção e Consulta!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],    
        [sg.Text('PESQUISA, informe:')],  
        #[sg.Text('Jogo De: ', size=(5, 1)), sg.InputText()), sg.Text(' Até: ', size=(5, 2), sg.InputText())],      
        [sg.Text('Jogo De: ', size=(7, 0)), sg.Input(size=(5,0), key='jde'), sg.Text(' Ate: ', size=(3, 0)), sg.InputText(size=(5,0), key='jate')],
        #[sg.Text(' Ate: ', size=(20, 0)), sg.InputText(size=(5,0), key='jate')],  
        #[sg.InputText('This is my text')],



        #[sg.Frame(layout=[      
        # [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],      
         #[sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],      
        
        # [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),      
        #     sg.Multiline(default_text='A second multi-line', size=(35, 3))],      
        # [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),      
        #     sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],      
        # [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],      
        # [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),      
        #     sg.Frame('Labelled Group',[[      
        #     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),      
        #     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),      
        #     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),      
        #     sg.Column(column1, background_color='#F7F3EC')]])],      
        # [sg.Text('_'  * 80)],      
        # [sg.Text('Choose A Folder', size=(35, 1))],      
        # [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
        #     sg.InputText('Default Folder'), sg.FolderBrowse()],      
        [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
    ]      


    window = sg.Window('Menu de Opções da Lotofacil', layout, default_element_size=(40, 1), grab_anywhere=False)    
    event, values = window.read()  
    window.Maximize()    
    window.close()    

    sg.popup('Title',      
                'The results of the window.',      
                'The button clicked was "{}"'.format(event),      
                'The values are', values)      
        

#______________________________________________________
pxxteste04()
pxxteste03()
a=1