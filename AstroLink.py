import pandas as pd
import sys
import PySimpleGUI as sg

class Zodiac: 

  def get_zodiac_sign(month, day):
      day = int(day)
      if (month == 'January' and 20 <= day <= 31) or (month == 'February' and 1 <= day <= 18):
        zodiac = 'Aquarius (Jan 20 - Feb 18)'
        sg.popup('The Zodiac is Aquarius!',title='calculated zodiac:')
      if (month == 'February' and 19 <= day <= 29) or (month == 'March' and 1 <= day <= 20):
        zodiac = 'Pisces (Feb 19 - March 20)'
        sg.popup('The Zodiac is Pisces!',title='calculated zodiac:')
      if (month == 'March' and 21 <= day <= 31) or (month == 'April' and 1 <= day <= 19):
        zodiac = 'Aries (Mar 21 - Apr 19)'
        sg.popup('The Zodiac is Aries!',title='calculated zodiac:')
      if (month == 'April' and 20 <= day <= 30) or (month == 'May' and 1 <= day <= 20):
        zodiac = 'Taurus (Apr 20 - May 20)'
        sg.popup('The Zodiac is Taurus!',title='calculated zodiac:')
      if (month == 'May' and 21 <= day <= 31) or (month == 'June' and 1 <= day <= 21):
        zodiac = 'Gemini (May 21 - Jun 21)'
        sg.popup('The Zodiac is Gemini!',title='calculated zodiac:')
      if (month == 'June' and 22 <= day <= 30) or (month == 'July' and 1 <= day <= 22):
        zodiac = 'Cancer (Jun 22 - Jul 22)'
        sg.popup('The Zodiac is Cancer!',title='calculated zodiac:')
      if (month == 'July' and 23 <= day <= 31) or (month == 'August' and 1 <= day <= 22):
        zodiac = 'Leo (Jul 23 - Aug 22)'
        sg.popup('The Zodiac is Leo!',title='calculated zodiac:')
      if (month == 'August' and 23 <= day <= 31) or (month == 'September' and 1 <= day <= 22):
        zodiac = 'Virgo (Aug 23 - Sep 22)'
        sg.popup('The Zodiac is Virgo!',title='calculated zodiac:')
      if (month == 'September' and 23 <= day <= 30) or (month == 'October' and 1 <= day <= 23):
        zodiac = 'Libra (Sep 23 - Oct 23)'
        sg.popup('The Zodiac is Libra!',title='calculated zodiac:')
      if (month == 'October' and 24 <= day <= 31) or (month == 'November' and 1 <= day <= 21):
        zodiac = 'Scorpio (Oct 24 - Nov 21)'
        sg.popup('The Zodiac is Scorpio!',title='calculated zodiac:')
      if (month == 'November' and 20 <= day <= 30) or (month == 'December' and 1 <= day <= 21):
        zodiac = 'Sagittarius (Nov 22 - Dec 21)'
        sg.popup('The Zodiac is Sagittarius!',title='calculated zodiac:')
      if (month == 'December' and 22 <= day <= 31) or (month == 'January' and 1 <= day <= 19):
        zodiac = 'Capricorn (Dec 22 - Jan 19)'
        sg.popup('The Zodiac is Capricon!',title='calculated zodiac:')
      return zodiac

  def enter_zodiac_sign(zodiac):
    if zodiac == 'Aquarius':
      zodiac_date = 'Aquarius (Jan 20 - Feb 18)'
    elif zodiac == 'Pisces':
      zodiac_date = 'Pisces (Feb 19 - March 20)'
    elif zodiac == 'Aries':
      zodiac_date = 'Aries (Mar 21 - Apr 19)'
    elif zodiac == 'Taurus':
      zodiac_date = 'Taurus (Apr 20 - May 20)'
    elif zodiac == 'Gemini':
      zodiac_date = 'Gemini (May 21 - Jun 21)'
    elif zodiac == 'Cancer':
      zodiac_date = 'Cancer (Jun 22 - Jul 22)'
    elif zodiac == 'Leo':
      zodiac_date = 'Leo (Jul 23 - Aug 22)'
    elif zodiac == 'Virgo':
      zodiac_date = 'Virgo (Aug 23 - Sep 22)'
    elif zodiac == 'Libra':
      zodiac_date = 'Libra (Sep 23 - Oct 23)'
    elif zodiac == 'Scorpio':
      zodiac_date = 'Scorpio (Oct 24 - Nov 21)'
    elif zodiac == 'Sagittarius':
      zodiac_date = 'Sagittarius (Nov 22 - Dec 21)'
    elif zodiac == 'Capricorn':
      zodiac_date = 'Capricorn (Dec 22 - Jan 19)'
    return zodiac_date

  def compatibility(zodiac1,zodiac2):
    data = pd.read_csv("compatibility.csv",index_col=0)
    cross_section = data.loc[zodiac1,zodiac2]
    compatibility_info = ''
    for i in cross_section.split()[:-3]:
      compatibility_info += str(i) + ' '
    compatibility_rating = (cross_section.split()[-3])+' '+(cross_section.split()[-2])+' '+(cross_section.split()[-1])
    return compatibility_rating, compatibility_info
  
class GUI:
  def zodiac_gui():
    Zodiac_List = ['Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn']
    other_Zodiac_List = ['Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn']
    month = ['January','February','March','April','May','June','July','August','September','October','November','December']
    other_month = ['January','February','March','April','May','June','July','August','September','October','November','December']
    day = [str(i).zfill(2) for i in range(1, 32)]
    other_day = [str(i).zfill(2) for i in range(1, 32)]
    layout = [[sg.VPush()],[sg.Text('What is your Zodiac?')],[sg.DD(Zodiac_List,size=(8)),sg.Button('Enter',key='Primary_Zodiac_Entered')],[sg.VPush()],[sg.Text('OR'),],[sg.VPush()],
              [sg.Text('When is your Birthday?')],[sg.DD(month,size=(8)),sg.DD(day,size=(8)),sg.Button('Enter',key='Primary_Birthday_Entered')],[sg.VPush()]] 
    window = sg.Window('Zodiac Calculator', layout, size=(400,400),resizable=True, element_justification='center')
    while True:
      event, values = window.read()
      if event == sg.WIN_CLOSED:
        sys.exit()      
      if event == 'Primary_Zodiac_Entered':
        if values[0] == '':
          sg.popup('Please enter a Zodiac',title='ERROR')
        else:
          zodiac = values[0]
          primary_zodiac_date = Zodiac.enter_zodiac_sign(zodiac)
          continue_ = sg.popup_yes_no('Would you like to find the compatibility of your zodiac with another persons?', title='Compatibility Checker')
          if continue_ == 'Yes':
            layout = [[sg.VPush()],[sg.Text('What is the other Zodiac?')],[sg.DD(other_Zodiac_List,size=(8)),sg.Button('Enter',key='Other_Zodiac_Entered')],[sg.VPush()],[sg.Text('OR'),],[sg.VPush()],
                      [sg.Text('When is the other persons Birthday?')],[sg.DD(other_month,size=(8)),sg.DD(other_day,size=(8)),sg.Button('Enter',key='Other_Birthday_Entered')],[sg.VPush()]]
            window = sg.Window('Zodiac Compatibility', layout, size=(400,400),resizable=True, element_justification='center')
      if event == 'Primary_Birthday_Entered':
        month = values[1]
        day = values[2]
        if month == '' or day == '':
          sg.popup('Please enter a Birthday',title='ERROR')
        elif (month == 'January' and int(day) <= 31) or (month == 'February' and int(day) <= 29) or (month == 'March' and int(day) <= 31) or (month == 'April' and int(day) <= 30) or (month == 'May' and int(day) <= 31) or (month == 'June' and int(day) <= 30) or (month == 'July' and int(day) <= 31) or (month == 'August' and int(day) <= 31) or (month == 'September' and int(day) <= 30) or (month == 'October' and int(day) <= 31) or (month == 'November' and int(day) <= 30) or (month == 'December' and int(day) <= 31):
          primary_zodiac_date = Zodiac.get_zodiac_sign(month,int(day))
          continue_ = sg.popup_yes_no('Would you like to find the compatibility of your zodiac with another persons?', title='Compatibility Checker')
          if continue_ == 'Yes':
            layout = [[sg.VPush()],[sg.Text('What is the other Zodiac?')],[sg.DD(other_Zodiac_List,size=(8)),sg.Button('Enter',key='Other_Zodiac_Entered')],[sg.VPush()],[sg.Text('OR'),],[sg.VPush()],
                      [sg.Text('When is the other persons Birthday?')],[sg.DD(other_month,size=(8)),sg.DD(other_day,size=(8)),sg.Button('Enter',key='Other_Birthday_Entered')],[sg.VPush()]]
            window = sg.Window('Zodiac Compatibility', layout, size=(400,400),resizable=True, element_justification='center')
        else:
          sg.popup('Please enter a real day of the year',title='ERROR')
      if event == 'Other_Zodiac_Entered':
        if values[0] == '':
          sg.popup('Please enter a Zodiac',title='ERROR')
        else:
          other_zodiac = values[0]
          other_zodiac_date = Zodiac.enter_zodiac_sign(other_zodiac)
          Rating,Info = Zodiac.compatibility(primary_zodiac_date,other_zodiac_date)
          sg.popup('                  '+Rating,Info,title=Rating)
          layout = [[sg.Text("Choose an option:")],[sg.Button("Restart"), sg.Button("Quit")]]
          window = sg.Window("Final Choice", layout)
      if event == 'Other_Birthday_Entered':
        other_month = values[1]
        other_day = values[2]
        if other_month == '' or other_day == '':
          sg.popup('Please enter a Birthday',title='ERROR')
        elif (other_month == 'January' and int(other_day) <= 31) or (other_month == 'February' and int(other_day) <= 29) or (other_month == 'March' and int(other_day) <= 31) or (other_month == 'April' and int(other_day) <= 30) or (other_month == 'May' and int(other_day) <= 31) or (other_month == 'June' and int(other_day) <= 30) or (other_month == 'July' and int(other_day) <= 31) or (other_month == 'August' and int(other_day) <= 31) or (other_month == 'September' and int(other_day) <= 30) or (other_month == 'October' and int(other_day) <= 31) or (other_month == 'November' and int(other_day) <= 30) or (other_month == 'December' and int(other_day) <= 31):
          other_zodiac_date = Zodiac.get_zodiac_sign(other_month,int(other_day))
          Rating,Info = Zodiac.compatibility(primary_zodiac_date,other_zodiac_date)
          sg.popup('                  '+Rating,Info,title=Rating)
          layout = [[sg.Text("Choose an option:")],[sg.Button("Restart"), sg.Button("Quit")]]
          window = sg.Window("Final Choice", layout)
        else:
          sg.popup('Please enter a real day of the year',title='ERROR')
      if event == 'Restart':
        GUI.zodiac_gui()
      if event == 'Quit':
        sys.exit()
        
if __name__ == '__main__':
  while True:
    GUI.zodiac_gui()


