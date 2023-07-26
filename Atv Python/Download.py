tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Convertendo o tamanho do arquivo para bits (1 byte = 8 bits)
tamanho_arquivo_bits = tamanho_arquivo_mb * 8 * 1024 * 1024

# Calculando o tempo aproximado de download em segundos
tempo_download_segundos = tamanho_arquivo_bits / (velocidade_internet_mbps * 1024 * 1024)

# Convertendo o tempo para minutos
tempo_download_minutos = tempo_download_segundos / 60

print(f"Tempo aproximado de download: {tempo_download_minutos:.2f} minutos e em segundos seria {tempo_download_segundos} segundos")


