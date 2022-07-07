from collections import namedtuple
import time

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    @staticmethod
    # O(log(n))
    def find_greater(arr, n, k):
        l = 0
        r = n - 1
        leftGreater = n
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] > k:
                leftGreater = mid
                r = mid - 1
            else:
                l = mid + 1
        return n - leftGreater

    def process(self, request):
        if self.find_greater(self.finish_time, len(self.finish_time), request.arrived_at) == self.size:
            return Response(True, -1)
            
        self.finish_time.append(request.time_to_process + max(request.arrived_at, self.finish_time[-1] if self.finish_time else 0))
        return Response(False, self.finish_time[-1] - request.time_to_process)



def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    with open("tests/22", "r") as f:
        buffer_size, n_requests = map(int, f.readline().strip().split())
        requests = []
        for _ in range(n_requests):
            arrived_at, time_to_process = map(int, f.readline().strip().split())
            requests.append(Request(arrived_at, time_to_process))
        a = []
        buffer = Buffer(buffer_size)
        responses = process_requests(requests, buffer)
        for response in responses:
            a.append(response.started_at if not response.was_dropped else -1)
        return a

        

def test():
    with open("tests/22.a", "r") as f:
        lst = []
        for line in f:
            lst.append(int(line.strip()))
        assert lst == main()

if __name__ == "__main__":
    test()
    print("good")
