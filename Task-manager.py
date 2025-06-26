def add_new_tasks():

    while True:
        x=input("please enter number of tasks: ")
        if x.isdigit() and int(x)>0:
           break
        print('please enter valid value for number of tasks(numbers in digit more than zero )')
    for i in range (int(x)):
     title=input(f"enter the title of task no: {i+1} :")
     while True:
              duration = input(f"What is the duration of '{title}' in minutes (0-60)? ")
              if duration.isdigit() and 0 < int(duration) <= 60:
               break
              print("Please enter a number between 0 and 60")
     while   True:
         priority=input(f"enter the pr of task '{title}' :")
         if priority.isdigit():
            break
         print("please enter numaric value for proirity")
     tasks.append([title,duration,priority])
def is_empty(list):
   return len(list)==0
def priority_check(tasks: list):
    if is_empty(tasks):
        return None  

    lowest_index = 0
    lowest_priority = int(tasks[0][2])  

    for i in range(1, len(tasks)):
        current_priority = int(tasks[i][2])
        if current_priority < lowest_priority:
            lowest_priority = current_priority
            lowest_index = i
    return tasks[lowest_index] 
def peek(peektask:list):
   if  is_empty(peektask):
      return("queqe is empty")
   next_task=priority_check(peektask)
   return(f"next task to be done title is :'{next_task[0]}' its duration is: {next_task[1]} wich has priority: {next_task[2]}")


def complete_task(list):
    list.remove(priority_check(list))
    return(list)
def sort_duration(task:list):
   ascending_sorted_list=task.copy()
   for i in range(1,len(ascending_sorted_list)):
      key=ascending_sorted_list[i]
      j=i-1
      while j>=0 and ascending_sorted_list[j][1]>key[1]:
         ascending_sorted_list[j+1]=ascending_sorted_list[j]
         j-=1
         ascending_sorted_list[j+1]=key
   return ascending_sorted_list
def search_for_task(task:list,target):
   low=0
   high=len(task)-1
   while low<=high:
      mid=(low+high)//2
      if task[mid][0]==target:  
       return task[mid]
      elif task[mid][0]<target:
         low=mid+1
      else: high=mid-1
   return (f"{target} not found")
tasks=[]
print('welcome to Task manager')
tasks=[]
add_new_tasks()
print(tasks)
peek(tasks)
print("tasks sorted according to duration the new list of tasks is :",sort_duration(tasks))
complete_task(tasks)
print("task completed \nthe new list is",tasks)
while True:
     y = input("Do you want to search for a specific task? (y/n): ").lower()
     if y in ["y", "n"]:
        break
     print(" Please enter only 'y' or 'n'.")


if y=="y"or y=="Y":
      target=input("please enter title for task to search for")
      print(search_for_task(tasks,target)) 
else:
   exit()


