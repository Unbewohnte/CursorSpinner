from spinner import Spinner
import pynput,sys

spinner = Spinner()
print("Created Spinner object")

keyboard = pynput.keyboard.Controller()

def proc_exit():
	print("DESTROYED")
	sys.exit(0)

def wait(button):
	if button == pynput.keyboard.Key.esc: #Kills itself by pressing "esc"
		proc_exit()
	else: #Still alive
		pass

def activate(button):
    try:
        if button == pynput.keyboard.Key.up: #Starting only when up arrow key`s pressed
            spinner.update_m_pos()
            spinner.calculate(circles = 70,radius = 60,angle_change = 30,rad_change = 0)# less angle_change - more circular circle
            spinner.spin(press = True)#Be careful, this thing is UNSTOPABLE, you can`t exit when it`s spinning :)
        else:
            pass
    except Exception as e:
        pass


with pynput.keyboard.Listener(
        on_press=activate,
        on_release=wait) as listener:
    listener.join()
