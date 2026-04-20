from queue import Queue

log_queue = Queue()
alert_queue = Queue()

def add_log(data):
    log_queue.put(data)

def add_alert(data):
    alert_queue.put(data)
