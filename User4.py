from pyactor.context import set_context, create_host, sleep, shutdown, interval, later, Host, serve_forever

import Tracker
import Sequencer
import User


if __name__ == '__main__':

    set_context()

    #User Host
    h = create_host('http://127.0.0.1:1244')
    user = h.spawn("user4", User.User)
    user.setID(4)

    #Tracker Host
    host = h.lookup_url('http://127.0.0.1:1220', Host)
    tracker = host.lookup_url('http://127.0.0.1:1220/TrackerID', Tracker.Tracker)
    user.joinTracker(tracker,h)
    user.setTracker(tracker)
    user.init_start(h)


    #Sequencer Host
    host2 = h.lookup_url('http://127.0.0.1:1230', Host)
    user.setHosts(h,host2)

    sleep(25)
    user.multicast("TASK")
    #user.multicastLamport("TASK")

    sleep(60)
    user.process_msg()
    #user.process_msg_Lamport()

    sleep(1)
    serve_forever()
