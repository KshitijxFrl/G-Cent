import PySimpleGUI as ui
import sqlite3
from LIB.DB import izDB as cdb
from LIB.TOOLS import json_controller as jc
from LIB.TOOLS import kit

#///////////////////////////////////////////////////////////--Check--////////////////////////////////////////////////////////////////////
db_check  = jc.oneTimeCheck()

if db_check == False:
    cdb.createDB()
    jc.oneTimeEntry()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////--UI--///////////////////////////////////////////////////////////////////////
def create_window():
    ui.theme("DarkTeal9")
    title = 'MTZ_SIGMA01(G Cent)'

    col1 = ui.Column([
      [ui.Frame('ENTER DETAILS', 
      [[ui.Spin(['IN  ','Out ','INV '],key='TAG')],
       [ui.Text("Date      "),ui.Input(key='DATE')],
       [ui.Text("Titel      "),ui.Input(key='HEADING')],
       [ui.Text("Amount "),ui.Input(key='AMOUNT')],
       [ui.Button('Submitte', key='BT1')],
      ])],

      [ui.Frame('Statemt',
      [[ui.Input(key='Output',disabled=False)]
      ])],

      [ui.Frame('GENERATE | CHECK',
      [[ui.Spin(['IN  ','Out ','INV ','ALL'],key='TAG2')],
       [ui.Input("From:",key='FROM'),ui.Input("TO:",key='TO')],
       [ui.Input("File Name:",key='fname')],
       [ui.Button('Load',key='BT2'),ui.Button('Check', key='BT3'),ui.Button('Graph', key='BT4'),ui.Button('Get File', key='BT5')] 
      ])],
    ])



    layout = [
        [[col1]],

        [ui.Button('Help', key='BT6'),ui.Button('Exit', key='BT7')]]
    return ui.Window(title,layout,default_element_size=(30,40),resizable=False)    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#//////////////////////////////////////////////////////////////--Variables--/////////////////////////////////////////////////////////////
window = create_window()
db = sqlite3.connect("mtzDB.db")
cursor = db.cursor()
container = 0;
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#///////////////////////////////////////////////////////////////--Driver--///////////////////////////////////////////////////////////////
while True:
    event, values = window.read()
    if event == ui.WIN_CLOSED or event == 'BT7': 
        break
    if event=='BT1':
        date    = values['DATE']
        tag     = values['TAG']
        titel   = values['HEADING']
        ammount = values['AMOUNT']
        db.execute('INSERT INTO record VALUES(?,?,?,?)',(date,tag,titel,ammount))
        db.commit()

    if event=='BT2':
        
        fromm = values['FROM']
        to = values['TO']       
        
        cursor.execute('select * from record where DATE BETWEEN ? AND ?;',(fromm,to))
        temp = cursor.fetchall()

        container = kit.KIT(temp)
        
        
    if event=='BT3':
        ini,ino,inv = container.a_kit()
        window['Output'].update(f"In: {ini} Out: {ino} Inv: {inv}")
        

    if event=='BT4':
        tag2 = values['TAG2'] 
        container.g_kit(tag2)    

    if event=='BT5':
        tag3 = values['TAG2']
        newf_name = values['fname']
        container.f_kit(tag3,newf_name)
     
window.close()    