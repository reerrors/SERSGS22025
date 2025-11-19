import random
import pandas as pd
import matplotlib.pyplot as plt

# Configurações da Simulação
NUM_HORAS = 24
LEITURAS_POR_HORA = 60  # Minuto a minuto
TEMP_AMBIENTE = 20      # Graus Celsius
TEMP_ALVO = 24          # Temperatura ideal de operação (ASHRAE recomenda entre 18-27)
FATOR_AQUECIMENTO = 0.5 # Quanto a CPU esquenta por % de carga
FATOR_RESFRIAMENTO = 0.8 # Quanto o sistema de refrigeração resfria por % de potência

def simular_data_center():
    dados = []
    
    # Condições Iniciais
    temp_atual = TEMP_AMBIENTE
    potencia_refrigeracao = 0 # 0 a 100%
    
    total_minutos = NUM_HORAS * LEITURAS_POR_HORA
    
    print("Iniciando simulação de 24h")

    for minuto in range(total_minutos):
        # 1. Simulação da Carga da CPU (Varia durante o dia)
        # Mais carga durante o horário comercial (minuto 480 a 1080)
        if 480 <= minuto <= 1080:
            carga_cpu = random.randint(50, 95) # Carga alta
        else:
            carga_cpu = random.randint(10, 40) # Carga ociosa (madrugada)
            
        # 2. Física Simplificada (Calor gerado)
        calor_gerado = carga_cpu * FATOR_AQUECIMENTO * 0.1
        
        # 3. Lógica de Controle (A Solução Sustentável)
        # Se a temperatura sobe acima do alvo, aumentamos a refrigeração
        # Se está abaixo, diminuímos para economizar energia
        erro = temp_atual - TEMP_ALVO
        
        if erro > 0:
            potencia_refrigeracao += 2.0 # Aumenta refrigeração agressivamente
        elif erro < -1: # Histerese para não oscilar demais
            potencia_refrigeracao -= 1.0 # Reduz refrigeração suavemente
            
        # Trava a potência entre 0% e 100%
        potencia_refrigeracao = max(0, min(100, potencia_refrigeracao))
        
        # 4. Aplicar Resfriamento
        resfriamento_real = potencia_refrigeracao * FATOR_RESFRIAMENTO * 0.1
        
        # Atualiza a temperatura (Inércia térmica)
        # Temp = Anterior + (Aquecimento - Resfriamento) + Perda natural para ambiente
        temp_atual = temp_atual + calor_gerado - resfriamento_real - ((temp_atual - TEMP_AMBIENTE) * 0.05)
        
        # Registra os dados
        dados.append({
            "Minuto": minuto,
            "Carga_CPU (%)": carga_cpu,
            "Temp_Servidor (°C)": temp_atual,
            "Energia_Refrigeracao (%)": potencia_refrigeracao
        })

    return pd.DataFrame(dados)

# --- Execução e Análise ---

df = simular_data_center()

# Cálculo de Eficiência
media_refrigeracao = df["Energia_Refrigeracao (%)"].mean()
print(f"\nSimulação concluída.")
print(f"Média de uso do sistema de refrigeração: {media_refrigeracao:.2f}% da capacidade total.")
print(f"Temperatura Máxima Atingida: {df['Temp_Servidor (°C)'].max():.2f}°C")

# --- Visualização ---
plt.figure(figsize=(12, 8))

# Gráfico 1: Carga da CPU vs Temperatura
plt.subplot(2, 1, 1)
plt.plot(df["Minuto"], df["Temp_Servidor (°C)"], color='red', label='Temperatura Servidor (°C)')
plt.axhline(y=TEMP_ALVO, color='green', linestyle='--', label='Temp Alvo (Ideal)')
plt.ylabel("Temperatura (°C)")
plt.title("Monitoramento Térmico e Carga de Trabalho")
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)

# Eixo gêmeo para mostrar a carga da CPU no mesmo gráfico
ax2 = plt.gca().twinx()
ax2.fill_between(df["Minuto"], df["Carga_CPU (%)"], color='gray', alpha=0.2, label='Carga CPU (%)')
ax2.set_ylabel("Carga CPU (%)")
ax2.legend(loc='upper right')

# Gráfico 2: Consumo de Energia da Refrigeração
plt.subplot(2, 1, 2)
plt.plot(df["Minuto"], df["Energia_Refrigeracao (%)"], color='blue', label='Potência Refrigeração (%)')
plt.xlabel("Tempo (Minutos ao longo de 24h)")
plt.ylabel("Uso de Energia (%)")
plt.title("Atuação do Algoritmo de Eficiência Energética")
plt.fill_between(df["Minuto"], df["Energia_Refrigeracao (%)"], color='blue', alpha=0.1)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
