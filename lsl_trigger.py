from pylsl import StreamInfo, StreamOutlet
import time

class LSLTriggerHandler(object):
    def __init__(self, stream_name="default_name"):
        self.info = StreamInfo(name=f"{stream_name}", type='Markers', channel_count=1,
                  channel_format='float32', source_id='1321')
        self.outlet = StreamOutlet(self.info)
        print("Trigger Handler Created.")


    def send_float_trigger(self, trigger_float):

        self.outlet.push_sample(x=[trigger_float])
        print(f"Trigger --- {trigger_float} --- Pushed")
