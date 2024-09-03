#CANDIDATO JULIO HSU

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento.values())

percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}

print("Percentual de representação de cada estado no faturamento mensal:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
