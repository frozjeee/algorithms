import queue_with_LL

def max_sliding_window_naive(sequence, m):
    maximums = []
    queue = queue_with_LL.Queue_LL(len(sequence))
    for i in range(len(sequence)):
        try:
            queue.enqueue(sequence[i])
        except MemoryError:
            maximums.append()
            queue.dequeue()
            queue.enqueue(sequence[i])
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
