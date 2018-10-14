import keyboard
import time
import re 


delayTime = 0

mydict = {"code":"import code:\nnext line\tthird line\t\n()",
        "jumpword":"code",
        "replace":"code boat",
        "jumpline":2,
        "next_word":None,
        "back":None,
        "back":None}

keyboard.press_and_release("ctrl+t")

def execute(command,input):
    if (command == 'code'):
        keyboard.write('a')
        sp = re.split("(\t|\n|\:)", input)
        for i in sp:
            if (i == '\n'):
                keyboard.press_and_release('enter')
                time.sleep(delayTime)
            elif (i == '\t'):
                keyboard.press_and_release('esc')
                keyboard.write('>>')
                keyboard.write('A')
                time.sleep(delayTime)
            elif (i == ':'):
                keyboard.press_and_release('shift+;')
                #keyboard.write(':')
                time.sleep(delayTime)
            else:
                keyboard.write(i)
                time.sleep(delayTime)
        keyboard.press_and_release('esc')
    elif (command == 'jumpline'):
        keyboard.write(str(input) + 'G')
        keyboard.press_and_release('enter')
        time.sleep(delayTime)
    elif (command == 'end_of_line'):
        keyboard.write('$')
        time.sleep(delayTime)
    elif (command == 'end_of_file'):
        keyboard.write('G')
        time.sleep(delayTime)
    elif (command == 'end_of_block'):
        keyboard.write('}')
        time.sleep(delayTime)
    elif (command == 'jumpword'):
        keyboard.write('/'+input)
        keyboard.press_and_release('enter')
        time.sleep(delayTime)
    elif (command == 'beg_of_line'):
        keyboard.write('g_')
        time.sleep(delayTime)
    elif (command == 'beg_of_file'):
        keyboard.write('gg')
        time.sleep(delayTime)
    elif (command  == 'beg_of_block'):
        keyboard.write('{')
        time.sleep(delayTime)
    elif (command == 'previous_word'):
        keyboard.write('b')
        time.sleep(delayTime)
    elif (command == 'next_word'):
        keyboard.write('e')
        time.sleep(delayTime)
    elif (command == 'back'):
        keyboard.write('a')
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('esc')
        time.sleep(delayTime)
    elif (command == '\\t'):
       keyboard.press_and_release('tab')
       time.sleep(delayTime)
    elif (command == '\\n'):
        keyboard.press_and_release('enter')
        time.sleep(delayTime)
    elif (command == 'replace'):
        rel = input.split()
        keyboard.write('/'+rel[0])
        keyboard.press_and_release('enter')
        keyboard.write('ciw')
        keyboard.write(rel[1])
        keyboard.press_and_release('esc')
        time.sleep(delayTime)
    else:
        keyboard.press_and_release('esc') 
        time.sleep(delayTime)

#time.sleep(2)
#for c in dict:
#    execute(c,dict[c])
#