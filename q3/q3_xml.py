#CANDIDATO JULIO HSU

import xml.etree.ElementTree as ET

def processar_xml(caminho_arquivo):
    try:
        # Parse do arquivo XML
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()
        
        # Lista para armazenar os valores de faturamento
        valores = []
        
        # Iterar sobre cada elemento <row>
        for row in root.findall('row'):
            valor = row.find('valor').text
            if valor is not None:
                try:
                    valor_float = float(valor)
                    if valor_float > 0:
                        valores.append(valor_float)
                except ValueError:
                    continue
        
        if not valores:
            return None, None, 0
        
        menor_valor = min(valores)
        maior_valor = max(valores)
        media_mensal = sum(valores) / len(valores)
        dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
        
        return menor_valor, maior_valor, dias_acima_media

    except ET.ParseError as e:
        print(f"Erro de parsing do XML: {e}")
    except Exception as e:
        print(f"Erro ao processar o arquivo XML: {e}")

# Exemplo de uso
try:
    menor, maior, dias_acima_media = processar_xml('dados.xml')
    if menor is not None:
        print(f"Menor valor: R${menor:.2f}")
        print(f"Maior valor: R${maior:.2f}")
        print(f"Número de dias acima da média: {dias_acima_media}")
    else:
        print("Nenhum dado válido encontrado.")
except Exception as e:
    print(f"Erro ao processar o arquivo XML: {e}")
