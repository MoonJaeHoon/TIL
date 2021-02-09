# 최적 경로
import sys
sys.stdin = open("input.txt")

def recursive(customers,customers_cost):

    # 먼저, {i_1}번째 사람으로부터 탐색한다면, 나머지 (N-1) 명의 사람들에게 다 가보는 알고리즘
    # 위를 구현할 수 있다면, 재귀로 짜면 됨.
    # 왜냐하면 두번째사람 {i_2}번째부터 시작하는 것은 다시 그 시점에서 나머지 (N-2)명의 사람들 다 가보면 되거든.
    
    # ex) home = [5,5], customers = [ [10,10], [15,15], [25,15] ],  company = [20,20]
    # 0. customers원본,  customers_cost = [ [10,10,10(거리)],    [15,15,20(거리)],    [25,15,(거리)] ]로 만들어졌다고 생각하고 구현시작

    # 1. [10,10]을 출발점으로   =>   [ [ [15,15,10(거리) ]   ,     [ [25,15], 20(거리) ] ]
    # 1번 구현방법 : current = customers[ind], customers.pop(0), customers[j][-1] += abs(customers[j][0]-current[0])+abs(customers[j][1]-current[1])
    # 2. [  ]
    
    if customers==[]:
        return 0
    else:
        ind=0
        current=customers.pop(ind)
        customers_cost.pop(ind)
        for j in range(len(customers)):
            
            
print(recursive(customers,customers_cost))


T=int(input())
for test_case in range(1,T+1):
    N= int(input())
    location_list = [int(i) for i in input().split()]
    company = location_list[:2]	# 출발
    home = location_list[2:4]	# 도착
    customers = [location_list[ind:ind+2] for ind in range(4,2*N+4,2)]
    

        

    #print(f"#{test_case} {answer}")