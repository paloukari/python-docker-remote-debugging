import ptvsd
from time import sleep

ptvsd.enable_attach("my_secret", address=('0.0.0.0', 3000))

def main():

    #ptvsd.wait_for_attach()
    i = 0 

    while True:
        sleep(1)
        print('looped')


if __name__ == "__main__":
    main()
