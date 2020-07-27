import time
import sys
from lsl_trigger import LSLTriggerHandler

def main(how_often=5):

    trigger = LSLTriggerHandler(stream_name="unix_time_stamp_test")

    while True:
        try:
            trigger.send_float_trigger(time.time())
            time.sleep(how_often)
        except KeyboardInterrupt:
            print("Closing.")
            sys.exit()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(how_often=int(sys.argv[1]))
    else:
        main()
