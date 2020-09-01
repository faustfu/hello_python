import threading
import queue


def washer(dishes, queue):
    for dish in dishes:
        print('washing', dish, 'dish')
        queue.put(dish)  # create a task


def dryer(tasks):
    while True:
        dish = tasks.get()  # get a task
        if dish is None:
            break
        print('drying', dish, 'dish')
        tasks.task_done()  # commit the task


if __name__ == '__main__':
    threads = []
    dish_queue = queue.Queue()  # create a queue for dishes.

    # create two threads for processing the queue.
    for n in range(2):
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
        dryer_thread.start()
        threads.append(dryer_thread)

    dishes = ['a', 'b', 'c', 'd']
    washer(dishes, dish_queue)
    dish_queue.join()  # wait for all tasks in the queue to be done to continue.

    for i in range(2):
        dish_queue.put(None)  # stop every workers

    for t in threads:
        t.join()  # wait for all workers
