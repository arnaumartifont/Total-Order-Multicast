from pyactor.context import set_context, create_host, sleep, shutdown, interval, later, Host, serve_forever

import Tracker
import Sequencer
import User


if __name__ == '__main__':

    set_context()

    #User Host
    h = create_host('http://127.0.0.1:1241')
    user = h.spawn("user2", User.User)

    #Tracker Host
    host = h.lookup_url('http://127.0.0.1:1220', Host)
    tracker = host.lookup_url('http://127.0.0.1:1220/TrackerID', Tracker.Tracker)
    
    user.joinTracker(tracker,h)
    user.setID(2)

    #Sequencer Host
    host2 = h.lookup_url('http://127.0.0.1:1230', Host)
    sequencer = host2.lookup_url('http://127.0.0.1:1230/SequencerID', Sequencer.Sequencer)


    sleep(15)
    user.multicast("PAU",tracker,sequencer)
    #user.multicastLamport("PAU",tracker,sequencer)
    
    sleep(70)
    user.process_msg()
    #user.process_msg_Lamport()

    sleep(1)
    serve_forever()