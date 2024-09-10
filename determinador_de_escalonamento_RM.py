import json

with open("tarefas.json") as tarefas:
    tasks = json.load(tarefas)["tasks"]

N = len(tasks)
U = 0
for i in range(N):
    U += tasks[i]['execution_time']/tasks[i]['period']

cond_suficiente = N*(2**(1/N) - 1)
if U <= cond_suficiente:
    print('O escalonamento é viável')
else:
    print('O escalonamento não é viável')

for k in range(N-1):
    min = k
    for j in range(k+1,N):
        if tasks[min]['period'] > tasks[j]['period']:
            min = j

    aux = tasks[min]
    tasks[min] = tasks[k]
    tasks[k] = aux
print(tasks)
