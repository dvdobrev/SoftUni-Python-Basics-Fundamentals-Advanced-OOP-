jobs = [int(el) for el in input().split(", ")]
task_index = int(input())

task_number = jobs[task_index]
clock_counter = 0
min_num = min(jobs)


while True:
    min_num_index = jobs.index(min_num)
    if not min_num_index == task_index:
        clock_counter += min_num
        jobs[min_num_index] = task_number + 1
        min_num = min(jobs)
    else:
        clock_counter += min_num
        print(clock_counter)
        break