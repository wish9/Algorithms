def solution(progresses, speeds):
    answer = []

    while len(progresses) != 0:
        result = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            for item in progresses.copy():
                if item >= 100:
                    result += 1
                    progresses.pop(0)
                    speeds.pop(0)
                else:
                    break
            answer.append(result)
    return answer

def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1

    return [q[1] for q in Q]

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))