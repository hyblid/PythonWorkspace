from pythonds.basic import Queue
from printer import Printer
from task import Task
import random

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
        task = Task(currentSecond)
        printQueue.enqueue(task)
      #If the printer is not busy and if a task is waiting,  
      #Remove the next task from the print queue and assign it to the printer.
      #Subtract the timestamp from the currentSecond to compute the waiting time for that task.
      #Append the waiting time for that task to a list for later processing.
      #Based on the number of pages in the print task, figure out how much time will be required.
      if (not labprinter.isBusy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append(nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)
      #make print status IDLE
      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait {0:6.2f} secs {1:3d} tasks remaining.".format(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

if __name__ == "__main__":
  for i in range(10):
    simulation(3600,5)