import random

class Log:
    def __init__(self, Healthy, Type, endpoint, host):
        self.endpoint = endpoint # Set this first so it's always available
        self.host = host # Set the host attribute
        self.healthy = Healthy
        
        if self.healthy: # In Python, you can just check the boolean directly
            self.generate_success()
        else:
            self.generate_failure(Type)
    

    def generate_failure(self, cipher):
        
        # Mapping the cipher to different flavors of failure
        match True:
            case _ if cipher > 90:
                self.CPUSpike()
            case _ if cipher > 80:
                self.MemoryLeak()
            case _ if cipher > 70:
                self.IntermittentDBIssues() # New: 60% error rate, high latency
            case _ if cipher > 60:
                self.LimpingService()       # New: 20% error rate, high resource pressure
            case _ if cipher > 50:
                self.ShakyNetwork()         # New: 30% error rate, high jitter/variance
            case _ if cipher > 40:
                self.NetworkIssue()
            case _ if cipher > 30:
                self.DatabaseError()
            case _ if cipher > 20:
                self.CodeBug()
            case _ if cipher > 10:
                self.token_expiry()
            case _ if cipher > 5:
                self.BadRequest()
            case _:
                self.NotFound()

    
    def generate_success(self):
        cipher = random.randint(1, 100)
        # Adding in Noise and variance.
        match True:
            case _ if cipher > 95:
                self.LoadHeavy()
            case _ if cipher > 90:
                self.CPUBurst()        # New: High CPU, but 200 OK
            case _ if cipher > 85:
                self.Blip()
            case _ if cipher > 80:
                self.MemoryFluctuation() # New: Memory spike, but 200 OK
            case _ if cipher > 75:
                self.ResourceCreated()
            case _ if cipher > 70:
                self.UserErrorNoise()   # New: 400/404/401 with low resources
            case _ if cipher > 65:
                self.AsyncAccepted()
            case _ if cipher > 55:
                self.SystemRestart()
            case _:
                self.StandardSuccess()


        """
            Diffrent Types of Errors and causes that may be seen in a real world scenario.
            This is where you can add in more complexity and variance to your logs, which will make the training of your model more robust and realistic.
        """

    # --- Failure Type Definitions ---

    def CPUSpike(self):
        self.hostCPU = random.randint(90, 100)
        self.memoryUsage = random.randint(50, 80)
        self.latency = random.randint(500, 2000)
        
        if self.hostCPU > 95:
            self.status_code = 500
        else:
            self.status_code = 200

    def MemoryLeak(self):
        self.hostCPU = random.randint(50, 80)
        self.memoryUsage = random.randint(90, 100)
        self.latency = random.randint(500, 2000)
        
        if self.memoryUsage > 95:
            self.status_code = 500
        else:
            self.status_code = 200

    def NetworkIssue(self):
        self.status_code = 500
        self.latency = random.randint(500, 2000)
        self.hostCPU = 0
        self.memoryUsage = 0

    def DatabaseError(self):
        self.status_code = 500
        self.latency = random.randint(500, 2000)
        self.hostCPU = random.randint(50, 80)
        self.memoryUsage = random.randint(50, 80)

    def CodeBug(self):
        # Nested randomization for variance within the bug category
        cipher_inner = random.randint(1, 100)
        match True:
            case _ if cipher_inner > 60:
                self.status_code = 404
            case _:
                self.status_code = 500
        
        self.latency = random.randint(500, 1000)
        self.hostCPU = random.randint(50, 80)
        self.memoryUsage = random.randint(50, 80)

    def token_expiry(self):
        self.status_code = 401
        self.latency = random.randint(100, 200) 
        self.hostCPU = random.randint(50, 80)
        self.memoryUsage = random.randint(50, 80)

    def BadRequest(self):
        self.status_code = 400
        self.latency = random.randint(100, 200)
        self.hostCPU = random.randint(50, 80)
        self.memoryUsage = random.randint(50, 80)

    def NotFound(self):
        self.status_code = 404
        self.latency = random.randint(100, 200)
        self.hostCPU = random.randint(50, 80)
        self.memoryUsage = random.randint(50, 80)

    def IntermittentDBIssues(self):
        if random.random() > 0.4:  # 60% Failure Rate
            self.status_code = 500
            self.latency = random.randint(1500, 3000)
        else:
            self.status_code = 200
            self.latency = random.randint(800, 1500)
        
        self.hostCPU = random.randint(60, 85)
        self.memoryUsage = random.randint(50, 70)

    def LimpingService(self):
        if random.random() > 0.8:  # 20% Failure Rate
            self.status_code = 503
        else:
            self.status_code = 200
            
        self.latency = random.randint(400, 1200)
        self.hostCPU = random.randint(85, 95)
        self.memoryUsage = random.randint(70, 90)

    def ShakyNetwork(self):
        if random.random() > 0.7: # 30% Failure Rate
            self.status_code = 500
        else:
            self.status_code = 200
            
        self.latency = random.randint(100, 2000) # High variance
        self.hostCPU = random.randint(5, 15)
        self.memoryUsage = random.randint(5, 15)

# --- Successes Type Definitions ---

    def StandardSuccess(self):
        # Standard GET/UPDATE success
        self.status_code = 200
        self.latency = random.randint(20, 150)
        self.hostCPU = random.randint(5, 20)
        self.memoryUsage = random.randint(10, 30)

    def ResourceCreated(self):
        """Simulates a 201 Created - slightly higher overhead for DB writes."""
        self.status_code = 201
        self.latency = random.randint(100, 300)
        self.hostCPU = random.randint(15, 35)
        self.memoryUsage = random.randint(20, 40)

    def AsyncAccepted(self):
        """Simulates a 202 Accepted - fast response for a background task."""
        self.status_code = 202
        self.latency = random.randint(10, 50)
        self.hostCPU = random.randint(5, 15)
        self.memoryUsage = random.randint(5, 20)

    def Blip(self):
        self.status_code = random.choice([200, 201, 500, 503, 400, 404, 401])
        if random.choice([True, False]):
            self.latency = random.randint(800, 1500)
            self.hostCPU = random.randint(20, 40)
        else:
            self.latency = random.randint(50, 200)
            self.hostCPU = random.randint(70, 90)
        self.memoryUsage = random.randint(20, 50)

    def SystemRestart(self):
        self.status_code = 503
        self.latency = random.randint(500, 1000)
        self.hostCPU = random.randint(1, 10)
        self.memoryUsage = random.randint(5, 15)

    def LoadHeavy(self):
        self.status_code = random.choice([200, 201, 202])
        self.latency = random.randint(400, 1200)
        if random.choice([True, False]):
            self.hostCPU = random.randint(85, 98) 
            self.memoryUsage = random.randint(40, 60)
        else:
            self.hostCPU = random.randint(40, 60)
            self.memoryUsage = random.randint(85, 98)

# --- Noise Type Definitions ---
    
    def CPUBurst(self):
        """Simulates a background Cron job or compression task. High CPU, but 200 OK."""
        self.status_code = 200
        self.latency = random.randint(50, 200) 
        self.hostCPU = random.randint(80, 95) # The "Noise"
        self.memoryUsage = random.randint(20, 40)

    def MemoryFluctuation(self):
        """Simulates GC (Garbage Collection) or cache loading. Memory spikes, then drops."""
        self.status_code = 200
        self.latency = random.randint(30, 100)
        self.hostCPU = random.randint(10, 30)
        self.memoryUsage = random.randint(70, 85) # Temporary spike

    def TransientError(self):
        """A 'Blip' error. A single 500 or 503 that resolves immediately (Network hiccup)."""
        self.status_code = random.choice([500, 503])
        self.latency = random.randint(10, 50) # Fast failure
        self.hostCPU = random.randint(5, 20)
        self.memoryUsage = random.randint(10, 30)

    def UserErrorNoise(self):
        """Simulates 'fat-fingered' URLs or expired sessions. 4xx errors with perfect system health."""
        self.status_code = random.choice([400, 401, 404])
        self.latency = random.randint(5, 40)
        self.hostCPU = random.randint(2, 10) # System is idle
        self.memoryUsage = random.randint(5, 15) # System is idle