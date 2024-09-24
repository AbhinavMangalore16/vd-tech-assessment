import time
import threading
import logging
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
logging.basicConfig(
    filename='rate_limiter.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(list)
        self.lock = threading.Lock()

    def allow_req(self, user_id):
        current_time = time.time()
        with self.lock:
            self.requests[user_id] = [timestamp for timestamp in self.requests[user_id] if current_time - timestamp < 60]
            if len(self.requests[user_id]) < 5:
                self.requests[user_id].append(current_time)
                logging.info(f"Request allowed for {user_id}")
                return True
            logging.info(f"Request denied for {user_id}")
            return False

# Simulating some requests to demonstrate the situation
def rate_limiting(user_id, rate_limiter):
    for i in range(20):
        allowed = rate_limiter.allow_req(user_id)
        logging.info(f"Request {i+1} for {user_id}: {'Allowed' if allowed else 'Denied'}")
        time.sleep(5)

rate_limiter = RateLimiter()

with ThreadPoolExecutor() as executor:
    users = ['user1', 'user2', 'user3', 'user4']
    futures = [executor.submit(rate_limiting, user, rate_limiter) for user in users]
