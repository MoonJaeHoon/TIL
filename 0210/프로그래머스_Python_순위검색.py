from collections import defaultdict
d = defaultdict(list)
def extend_group(list_score): # list_score = [['java', 'backend', 'junior', 'pizza'], '100']
    global d
    ls0,ls1 = list_score[0], list_score[1]
    extend_list = [ ls0 ]
    for ind in range(4):    ## 1개씩 '-' 추가
        extend_list.append(ls0[:ind]+['-']+ls0[ind+1:])
    for ind in range(4):    ## 2개씩 '-' 추가
        for jnd in range(ind+1,4):
            extend_list.append( ls0[:ind]+['-']+ls0[ind+1:jnd]+['-']+ls0[jnd+1:] )
    for ind in range(4):    ## 3개씩 '-' 추가
        for jnd in range(ind+1,4):
            for knd in range(jnd+1,4):
                extend_list.append( ls0[:ind]+['-']+ls0[ind+1:jnd]+['-']+ls0[jnd+1:knd]+['-']+ls0[knd+1:])
    extend_list.append(['-']*4)
    return [extend_list,ls1]

def solution(info, query):
    d = defaultdict(list)
    new_info = []
    for i in info:
        i = i.split()
        new_info.append(extend_group([i[:-1],i[-1]]))
        
    new_info.sort(key=lambda x: int(x[1]), reverse=True)

    new_query = []
    for q in query:
        q = q.replace(' and ',' ').split()
        new_query.append([q[:-1],  q[-1]])
    
    answer_list=[]
    for nq in new_query:
        count=0
        for ninfo in new_info:
            if int(nq[1])<=int(ninfo[1]):                
                if nq[0] in ninfo[0]:
                    count+=1
            else:
                break
        answer_list.append(count)

    return answer_list