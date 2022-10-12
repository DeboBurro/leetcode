import time

# Token bucket algorithm
class TokenBucket:
    def __init__(self, success_clbk, failed_clbk, num_tokens_in_bucket=10,  hz=10, max_bucket_size=20):
        self.hz = hz
        self.rate = 1.0 / self.hz
        self.max_bucket_size = max_bucket_size
        self.num_tokens_in_bucket = num_tokens_in_bucket
        self.success_clbk = success_clbk
        self.failed_clbk = failed_clbk
        self.last_check = time.time()

    def handle(self, request):
        current = time.time()
        time_passed = current - self.last_check
        self.last_check = current
        print(f'time passed : {time_passed} s')
        self.num_tokens_in_bucket = self.num_tokens_in_bucket + time_passed * self.rate
        print(f'num of tockens in the bucket : {self.num_tokens_in_bucket}')
        if self.num_tokens_in_bucket >  self.max_bucket_size:
            self.num_tokens_in_bucket = self.max_bucket_size

        if self.num_tokens_in_bucket < 1:
            self.failed_clbk(request)
        else:
            self.num_tokens_in_bucket -= 1
            self.success_clbk(request)

def success_send(request):
    print(f'Success send the request {request}')

def fail_send(request):
    print(f'Fail send the request {request}')

if __name__ == '__main__':
    rate_limiter = TokenBucket(success_send, fail_send, hz =10)
    request = 0
    while True:
        time.sleep(0.5)
        rate_limiter.handle(request)
        request += 1
