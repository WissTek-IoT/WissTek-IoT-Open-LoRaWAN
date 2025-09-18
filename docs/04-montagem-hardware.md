# Montagem do Hardware

## Conexões

A placa utilizada já possui display OLED e rádio LoRa integrados ao ESP32, dispensando fios externos para testes iniciais.

## Cuidados Importantes

- **Nunca energize a placa sem a antena LoRa conectada**. Isso pode danificar o rádio.
- Para gravar o código corretamente, os seguintes pinos devem estar:
  - GPIO5 = LOW
  - GPIO12 = LOW
  - GPIO15 = HIGH
