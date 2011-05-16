import threading

def send_threaded(msg, fail_silently=True, *args):
    t = threading.Thread(target=msg.send, args=args, kwargs={'fail_silently': fail_silently})
    t.setDaemon(True)
    t.start()
