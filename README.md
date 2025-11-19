# Eco data 

Este projeto consiste em uma ferramenta de simulação desenvolvida em Python voltada para a análise e otimização do consumo energético em data centers. O foco principal é o gerenciamento térmico inteligente, demonstrando como o ajuste dinâmico dos sistemas de refrigeração (HVAC) baseado na carga de trabalho da CPU pode resultar em economia de energia e práticas mais sustentáveis.

## Descrição da Solução

A solução aborda o problema do desperdício de energia em sistemas de resfriamento estáticos, onde com essa análise dos padrões de temperatura seja possivel maximizar a eficiencia da refrigeração para que não hajá desperdicios.

O algoritmo implementado realiza as seguintes etapas:

1. Monitoramento: Coleta dados simulados de temperatura do servidor e carga de processamento minuto a minuto.

2. Controle de Feedback: Compara a temperatura atual com uma temperatura alvo ideal (Set Point).

3. Atuação Dinâmica: Ajusta a potência do sistema de refrigeração proporcionalmente ao erro térmico. Se a temperatura excede o alvo, a refrigeração aumenta; se está abaixo, a refrigeração diminui.

4. Resultado: O sistema mantém os servidores em temperatura segura utilizando apenas a energia estritamente necessária para aquele momento.

## Dados Utilizados e Metodologia

O projeto não utiliza bases de dados externas. Todos os dados são sintéticos, gerados proceduralmente pelo script para simular um cenário realista de 24 horas de operação.

### Parâmetros da Simulação

Carga da CPU: Gerada aleatoriamente, com perfis distintos para horário comercial (alta demanda) e horários ociosos (baixa demanda).

Fator de Aquecimento: Modelo físico simplificado onde o aumento da carga da CPU resulta em geração de calor (Joules).

Inércia Térmica: Considera que a temperatura não muda instantaneamente, havendo uma dissipação natural e uma curva de resposta ao resfriamento.

Temperatura Ambiente: Fixada em 20°C como base.

Temperatura Alvo: Definida em 24°C (baseado em recomendações de eficiência energética).


## Dependências

O projeto depende das seguintes bibliotecas Python:

pandas: Para estruturação e manipulação dos dados temporais.

matplotlib: Para visualização gráfica dos resultados.

## Instalação e Execução

Instalação das bibliotecas: Abra o terminal ou prompt de comando e execute:
Bash

    pip install pandas matplotlib
