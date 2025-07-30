task_list=[]
while True:
 try:
  user_input=int(input("Press 1 to add task\nPress 2 to see the list of tasks\npress 3 to remove the task\npress 4 to exit\n"))
  if user_input in [1,2,3,4]:
      if user_input==1:
            task=input("Enter the task\n")
            task_list.append(task)
            print(f"Your task {task} is added")
      elif user_input==2:
            if not task_list:
                 print("Your task list is empty")
            else:
                 print("Your task list is \n")
                 for index,task in enumerate (task_list):
                  print(f"{index+1}-{task}")
            
            
      elif user_input==3:
            a=int(input("Enter the serial number of task that you want to remove: "))
            if not task_list:
                 print("No task to remove")
            else:
                 if 1<=a<= len( task_list):
                  removed_task=task_list.pop(a-1)
                  print(f"Your task '{removed_task}' is removed at serial number {a} is removed")
  
      elif user_input==4:
            print("Exiting")
            break
  else:
        print("Please choose valid option by pressing 1,2,3,4\n")
 except ValueError:
     print("Invalid input\nPlease enter a number")

            
    

