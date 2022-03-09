import time
from datetime import datetime
from multiprocessing import Process, Pipe
import multiprocessing as mp
import codecs


def str_cur_time():
    return datetime.now().strftime("%h:%m:%s")


def get_msg(msg):
    return str_cur_time() + ": " + msg + '\n'


def process_a_instructions(sender, receiver):
    try:
        while True:
            time.sleep(5)
            receiver.send(sender.recv().lower())
    except Exception:
        pass


def process_b_instructions(receiver, sender):
    try:
        while True:
            sender.send(codecs.encode(receiver.recv(), "rot_13"))
    except Exception:
        pass


def main():
    # basically, m stands for main process, a is Process A, b is Process B
    ma, am = Pipe(duplex=True)
    ab, ba = Pipe(duplex=True)
    mb, bm = Pipe(duplex=True)

    a = Process(target=process_a_instructions, args=(am, ab))
    a.start()
    b = Process(target=process_b_instructions, args=(ba, mb))
    b.start()

    with open("./artifacts/hard.txt", "w") as file:
        try:
            while True:
                timestamp = str_cur_time() + ": "
                msg = input(timestamp)
                file.write(timestamp + msg + '\n')
                ma.send(msg)
                res = bm.recv()
                full_msg = get_msg(res)
                print(full_msg)
                file.write(full_msg + '\n')
        except KeyboardInterrupt:
            print('Finished interprocess communication')
    a.join()
    b.join()


if __name__ == '__main__':
    main()
