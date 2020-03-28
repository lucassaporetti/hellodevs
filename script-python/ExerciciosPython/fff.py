from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)

    print('Running. Press CTRL-C to exit.')
    while True:
        # Do nothing and hog CPU forever until SIGINT received.
        pass