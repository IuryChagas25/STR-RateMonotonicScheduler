import json

# Abrindo o arquivo "tarefas.json"
with open("tarefas.json") as tarefas:
    tasks = json.load(tarefas)["tasks"]

# Calculando a utilização total das tarefas
N = len(tasks)
U = 0
for i in range(N):
    U += tasks[i]['execution_time'] / tasks[i]['period']

# Verifica se o escalonamento é viável
cond_suficiente = N * (2 ** (1 / N) - 1)
if U <= cond_suficiente:
    viabilidade = "viable"
else:
    viabilidade = "not viable"

# Ordenação de tarefas pelo período (menor período, maior prioridade) segundo o RM
for k in range(N - 1):
    min_idx = k
    for j in range(k + 1, N):
        if tasks[min_idx]['period'] > tasks[j]['period']:
            min_idx = j
    aux = tasks[min_idx]
    tasks[min_idx] = tasks[k]
    tasks[k] = aux

# Criando  uma lista para o escalonamento sugerido com as prioridades
sugestao_escalonamento = []
for idx, task in enumerate(tasks):
    sugestao_escalonamento.append({
        "id": task["id"],
        "priority": idx + 1
    })

# Criando o formato do arquivo json a ser exportado
saida = {
    "schedulability": viabilidade,
    "suggested_schedule": sugestao_escalonamento
}

# Exportando o arquivo json
with open("resultado.json", "w") as arquivo_saida:
    json.dump(saida, arquivo_saida, indent=4)

print("O resultado foi salvo no arquivo 'resultado.json'.")
