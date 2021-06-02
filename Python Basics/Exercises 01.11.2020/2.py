bad_evaluation = int(input())
task_name = input()
evaluation = int(input())
count_bad_evaluation = 0
count_tasks = 0
score = 0
last_task = 'a'


while task_name != 'Enough':
    count_tasks += 1
    score += evaluation
    last_task = last_task
    if evaluation > 4:
        task_name = input()
        if task_name == 'Enough':
            print(f'Average score: {score / count_tasks:.2f}\nNumber of problems: {count_tasks}\nLast problem: {last_task}')
            break
        evaluation = int(input())
        last_task = task_name
    else:
        count_bad_evaluation += 1
        if count_bad_evaluation == bad_evaluation:
            print(f'You need a break, {bad_evaluation} poor grades.')
            break
        task_name = input()
        evaluation = int(input())

#else:
    #print(f'Average score: {score / count_tasks:.2f}\nNumber of problems: {count_tasks}\nLast problem: {task_name}')