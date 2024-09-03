#CANDIDATO JULIO HSU

import json

def processar_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as f:
            dados = json.load(f)
        
        # Lista para armazenar os valores de faturamento
        valores = []
        
        for item in dados:
            valor = item.get('valor')
            if valor is not None and valor > 0:
                valores.append(valor)
        
        if not valores:
            return None, None, 0
        
        menor_valor = min(valores)
        maior_valor = max(valores)
        media_mensal = sum(valores) / len(valores)
        dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
        
        return menor_valor, maior_valor, dias_acima_media

    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
    except Exception as e:
        print(f"Erro ao processar o arquivo JSON: {e}")

# Exemplo de uso
try:
    menor, maior, dias_acima_media = processar_json('dados.json')
    if menor is not None:
        print(f"Menor valor: R${menor:.2f}")
        print(f"Maior valor: R${maior:.2f}")
        print(f"Número de dias acima da média: {dias_acima_media}")
    else:
        print("Nenhum dado válido encontrado.")
except Exception as e:
    print(f"Erro ao processar o arquivo JSON: {e}")
