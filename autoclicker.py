# ---------------------------------------
# https://raidforums.com/User-ch0colate
# ---------------------------------------
import pyautogui, datetime, sys
from pynput import keyboard
from colorama import Fore, Style

####################### EDIT ME #######################
delay = 10  # Here the default secconds you want to wait.
resume_key = keyboard.Key.f9  # You can change the resume,
pause_key = keyboard.Key.f10  # pause
exit_key = keyboard.Key.esc   # or edit keys here.
#######################################################

try:
    delay = sys.argv[1]
    delay = int(delay)
except Exception:
    delay = delay

pause = True
running = True
now = datetime.datetime.now()

def on_press(key):
    now = datetime.datetime.now()
    global running, pause

    if key == resume_key:
        pause = False
        time = now.strftime("%H:%M:%S")
        print("%s%s[%s%s%s]%s%s Resumed with delay: %s%s%s" % (Style.BRIGHT, Fore.GREEN, Fore.WHITE, time, Fore.GREEN, Style.RESET_ALL, Fore.WHITE, Style.BRIGHT, str(delay), Style.RESET_ALL))
    elif key == pause_key:
        pause = True
        time = now.strftime("%H:%M:%S")
        print("%s%s[%s%s%s]%s%s Paused.%s" % (Style.BRIGHT, Fore.GREEN, Fore.WHITE, time, Fore.GREEN, Style.RESET_ALL, Fore.WHITE, Style.RESET_ALL))
    elif key == exit_key:
        running = False
        time = now.strftime("%H:%M:%S")
        print("%s%s[%s%s%s]%s%s Exiting...%s" % (Style.BRIGHT, Fore.GREEN, Fore.WHITE, time, Fore.GREEN, Style.RESET_ALL, Fore.RED, Style.RESET_ALL))


def banner():
    print("%s%s .: %sPython AutoClicker by ch0colate%s :. %s" % (Style.BRIGHT, Fore.RED, Fore.WHITE, Fore.RED, Style.RESET_ALL))
    print()
    print("%s%s Usage:%s python3 %s <delay>" % (Style.BRIGHT, Fore.WHITE, Style.RESET_ALL, sys.argv[0]))
    print("%s%s Current delay is set to [%s%s%s] secconds." % (Style.BRIGHT, Fore.WHITE, Fore.BLUE, str(delay), Fore.WHITE))
    print(" Keys:")
    print("   %s%sF9%s  = %sResume" % (Style.BRIGHT, Fore.BLUE, Fore.WHITE, Style.RESET_ALL))
    print("   %s%sF10%s = %sPause" % (Style.BRIGHT, Fore.BLUE, Fore.WHITE, Style.RESET_ALL))
    print("   %s%sesc%s = %sExit" % (Style.BRIGHT, Fore.BLUE, Fore.WHITE, Style.RESET_ALL))
    print()
    print("%s%s=======================LOG=======================" % (Style.BRIGHT, Fore.GREEN))
    time = now.strftime("%H:%M:%S")
    print("%s%s[%s%s%s]%s%s Not running. Press F9 to start.%s" % (Style.BRIGHT, Fore.GREEN, Fore.WHITE, time, Fore.GREEN, Style.RESET_ALL, Fore.WHITE, Style.RESET_ALL))


def main():
    lis = keyboard.Listener(on_press=on_press)
    lis.start()
    banner()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()
    exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        time = now.strftime("%H:%M:%S")
        print("%s%s[%s%s%s]%s%s Ctrl+C detected... Bye!%s" % (Style.BRIGHT, Fore.GREEN, Fore.WHITE, time, Fore.GREEN, Style.RESET_ALL, Fore.RED, Style.RESET_ALL))

exit(1)
