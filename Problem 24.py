import statistics
def calc_avg(list1):
    print (statistics.mean(list1))

list1=list(map(int,input().split()))
calc_avg(list1)