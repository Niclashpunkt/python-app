import pyforms
from   pyforms          import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton

class SimpleExample1(BaseWidget):

    def __init__(self):
        super(SimpleExample1,self).__init__('Simple example 1')

        #Definition of the forms fields
        self._firstname     = ControlText('First name', 'Default value')
        self._middlename    = ControlText('Middle name')
        self._lastname      = ControlText('Lastname name')
        self._fullname      = ControlText('Full name')
        self._button        = ControlButton('Press this button')

        #Define the button action
        self._button.value = self.__buttonAction

        #Define the organization of the forms
        self.formset = [ ('_firstname','_middlename','_lastname'), '_button', '_fullname', ' ']

        self.formset = [{
            'Tab1':['_firstname','||','_middlename','||','_lastname'],
            'Tab2':['_fullname']
        },
        '=',(' ','_button',' ')]

        self.mainmenu = [
            { 'File': [
                    {'Open': self.__openEvent},
                    '-',
                    {'Save': self.__saveEvent},
                    # {'Save as': self.__saveAsEvent}
                ]
            },
            { 'Edit': [
                    {'Copy': self.__editEvent},
                    {'Past': self.__pastEvent}
                ]
            }
        ]

        # self._fullname.add_popup_menu_option('Path',
        #     {
        #         'Delete':           self.__dummyEvent,
        #         'Edit':             self.__dummyEvent,
        #         'Interpolate':      self.__dummyEvent
        #     })
        self._fullname.add_popup_menu_option('option 0', function_action=self.__dummyEvent)
        submenu1 = self._fullname.add_popup_submenu('menu 1')
        submenu2 = self._fullname.add_popup_submenu('menu 2', submenu=submenu1)
        self._fullname.add_popup_menu_option('option 1', function_action=self.__dummyEvent, key='Control+Q', submenu=submenu2)


    def __buttonAction(self):
        """Button action event"""
        self._fullname.value = self._firstname.value +" "+ self._middlename.value +" "+self._lastname.value

    def __openEvent(self):
        print('hello')

    def __saveEvent(self):
        print('hello')

    def __editEvent(self):
        print('hello')

    def __pastEvent(self):
        print('hello')

    def __dummyEvent(self):
        print('hello')

#Execute the application
if __name__ == "__main__":   pyforms.start_app( SimpleExample1 )
