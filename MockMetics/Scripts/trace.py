import random
# Assuming your Log class is in a file named log.py
from log import Log 

class Trace: 
    def __init__(self, endpoint, host):
        self.logs = []
        logs_per_trace = random.randint(1, 50)
        # 10% chance of a failure (if > 90)
        cipher = random.randint(1, 100)
        Type = random.randint(1, 100)

        self.healthy = cipher <= 90  # Healthy if cipher is 90 or below

        for i in range(logs_per_trace):
            # Create the Log instance and append it to the list
            new_log = Log(self.healthy, Type, endpoint, host)
            self.logs.append(new_log)

    def TrainingTrace(self):
        return self.logs, self.healthy

    def TestingTrace(self):
        return self.logs

    def print_trace(self):
        for log_entry in self.logs:
            print(f"Endpoint: {log_entry.endpoint} | Status: {log_entry.status_code} | Latency: {log_entry.latency}ms | Host: {log_entry.host} | Host Memory: {log_entry.memoryUsage}% | Host CPU: {log_entry.hostCPU}% | Healthy: {log_entry.healthy}")
