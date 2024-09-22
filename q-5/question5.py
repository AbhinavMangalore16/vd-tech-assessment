import time 
import threading
from collections import defaultdict
class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(list)
        self.lock = threading.Lock()
    def allow_req(self, user_id):
        current_time = time.time()
        with self.lock:
            self.requests[user_id] = [timestamp for timestamp in self.requests[user_id] if current_time-timestamp<60]
            if len(self.requests[user_id])<5:
                self.requests[user_id].append(current_time)
                return True
            return False
        
#Simulating some requests to demonstrate the situation
def rate_limiting(user_id, rate_limiter):
    for i in range(20):
        allowed = rate_limiter.allow_req(user_id)
        print(f"Request {i+1} for {user_id}: {'Allowed' if allowed else 'Denied'}")
        time.sleep(5)

rate_limiter = RateLimiter()

threads = []
for user in ['user1', 'user2', 'user3', 'user4']:  
    thread = threading.Thread(target=rate_limiting, args=(user, rate_limiter))
    threads.append(thread)

#starting all threads
for thread in threads:
    thread.start()

#waiting for all threads to finish
for thread in threads:
    thread.join()