import random as rand
from queue import PriorityQueue


def random_generator():
    num = rand.randint(0, 31)
    return bin(num)[2:].zfill(5)


def crossOver(bin1, bin2, cp):
    bin1 = str(bin1)
    bin2 = str(bin2)
    temp = bin1
    bin1 = bin1[0:cp] + bin2[cp:len(bin2)]
    bin2 = bin2[0:cp] + temp[cp:len(temp)]
    return [bin1, bin2]


def mutation(bin1, bin2, m):
    ran1 = rand.randint(0, 4)
    ran2 = rand.randint(0, 4)
    if m == 0:
        if bin1[ran1] == '0':
            bin1 = bin1[:ran1] + '1' + bin1[ran1 + 1:]
        else:
            bin1 = bin1[:ran1] + '0' + bin1[ran1 + 1:]
        if bin2[ran2] == '0':
            bin2 = bin2[:ran2] + '1' + bin2[ran2 + 1:]
        else:
            bin2 = bin2[:ran2] + '0' + bin2[ran2 + 1:]
    elif m == 1:
        temp = list(bin1)
        var = temp[ran1]
        temp[ran1] = temp[ran2]
        temp[ran2] = var
        bin1 = "".join(temp)
        temp = list(bin2)
        var = temp[ran1]
        temp[ran1] = temp[ran2]
        temp[ran2] = var
        bin2 = "".join(temp)
    return [bin1, bin2]


def function(num):
    return int(num, 2)


def genetic_algo(p, c, m, t, x, i):
    queue = PriorityQueue()
    childqueue = []
    for j in range(0, p):
        num = random_generator()
        queue.put((-1 * function(num), num))
    # print(queue.queue)

    if t == 1:
        for j in range(0, i):
            for k in range(0, queue.qsize()):
                if queue.qsize() > 1:
                    temp = crossOver(queue.get()[1], queue.get()[1], 1)
                    childqueue.extend(mutation(temp.pop(), temp.pop(), 0))
                    # print(childqueue)
                else:
                    while len(childqueue):
                        num = childqueue.pop();
                        queue.put((-1 * function(num), num))
                    break
            # print(queue.qsize())
    return queue.get()[1]


# t = 1 -> predefined iterations up to i;
print(function(genetic_algo(7, 2, 1, 1, 10, 100)))
