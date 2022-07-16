from ListQueue import ListQueue


def main():
    lq = ListQueue()
    lq.print_queue()

    print('Enqueueing A and B')

    lq.enqueue('A')
    lq.enqueue('B')

    lq.print_queue()

    print('\nDequeue called and ' + lq.dequeue() + ' is removed.')
    lq.print_queue()

    print('\nEnqueueing C, D, E, F, and G')
    lq.enqueue('C')
    lq.enqueue('D')
    lq.enqueue('E')
    lq.enqueue('F')
    lq.enqueue('G')
    lq.print_queue()

    print('\nLength of queue: ' + str(lq.length()))

    print('\nFront of queue: ' + lq.get_front())
    

if __name__ == '__main__':
    main()
