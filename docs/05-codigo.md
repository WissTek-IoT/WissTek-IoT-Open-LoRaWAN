# Código

## Exemplos inclusos na IDE:

Após configurar corretamente a placa na IDE do Arduino, acesse os exemplos:

`Arquivo → Exemplos → LoRa → OLED_LoRa_Sender`  
`Arquivo → Exemplos → LoRa → OLED_LoRa_Receiver`

### OLED_LoRa_Sender

- Envia pacotes numerados via LoRa
- Exibe no OLED: "Sending packet: X"

### OLED_LoRa_Receiver

- Recebe pacotes enviados
- Exibe no OLED:
  - RSSI (intensidade do sinal)
  - Tamanho do pacote
  - Número total de pacotes

### Frequência

No código, ajuste a frequência de operação conforme sua placa:

```cpp
LoRa.begin(433E6);  // ou 868E6 / 915E6
```
