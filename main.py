import sys
from ctypes import *
from ctypes.wintypes import *
import zmq
import colorama
import interception
from colorama import Fore
colorama.init(autoreset=True)

context = zmq.Context()
socket = context.socket(zmq.PULL)
try:
    socket.bind("tcp://*:12345")
except zmq.ZMQError as e:
    print(f"{Fore.RED}[-] ZMQ Error during binding: {e}")
    sys.exit(1)


from pystyle import Box, Center, Colorate, Colors, System, Write
BANNER = """








██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗     ██████╗ ██████╗ ██╗██╗   ██╗ █████╗ ████████╗███████╗
██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██║██║   ██║██╔══██╗╚══██╔══╝██╔════╝
███████║ ╚████╔╝ ██████╔╝█████╗  ██████╔╝    ██████╔╝██████╔╝██║██║   ██║███████║   ██║   █████╗  
██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗    ██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══╝  
██║  ██║   ██║   ██║     ███████╗██║  ██║    ██║     ██║  ██║██║ ╚████╔╝ ██║  ██║   ██║   ███████╗
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                        
"""
def main():

    interception.auto_capture_devices()

    # if not rzctl.init(): print("Failed to initialize rzctl")
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(BANNER), 1))
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter("-======================================$$======================================-"), 1))
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(""), 1))
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter("Github.com/hypr1x"), 1))
    
    while True:
        try:
            message = socket.recv_string()
        except:
            pass
        if message == "click":
            # rzctl.mouse_click(MOUSE_CLICK.LEFT_DOWN)
            # # time.sleep(1 / 1000)
            # rzctl.mouse_click(MOUSE_CLICK.LEFT_UP)
            pass
        else:
            x, y = map(int, message.split(','))
            interception.move_relative(x, y)
        # time.sleep(
        #     1 / 1000
        # )  # Sleep is needed to avoid razer service overflowing, which delays all your inputs



if __name__ == "__main__":
    main()
