import multiprocessing as mp


def washer(dishes, queue):
    for dish in dishes:
        print('washing', dish, 'dish')
        queue.put(dish)


def dryer(tasks):
    while True:
        dish = tasks.get()
        print('drying,', dish, 'dish')
        tasks.task_done()


if __name__ == '__main__':
    dish_queue = mp.JoinableQueue()  # create a queue for dishes.

    # fork a process for processing the queue.
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['a', 'b', 'c', 'd']
    washer(dishes, dish_queue)

    dish_queue.join()  # wait for all tasks to be done
