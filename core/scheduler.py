import threading
import time

class Scheduler:
    def __init__(self):
        self.tasks = []
        self.running = False
        self.thread = None

    def add_task(self, func, interval):
        self.tasks.append({
            "func": func,
            "interval": interval,
            "last_run": 0
        })

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False

    def _run(self):
        while self.running:
            current_time = time.time()
            for task in self.tasks:
                if current_time - task["last_run"] >= task["interval"]:
                    try:
                        task["func"]()
                    except:
                        pass
                    task["last_run"] = current_time  
                  time.sleep(1)
