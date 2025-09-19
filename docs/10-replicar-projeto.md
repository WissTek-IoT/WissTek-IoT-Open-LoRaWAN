{{ include('includes/EM_DESENVOLVIMENTO.md') }}

<div class="md-content-none">
# Como Replicar o Projeto

1. Adquira 2 placas ESP32 com LoRa + antenas
2. Conecte a antena antes de ligar cada placa
3. Instale e configure o Arduino IDE conforme descrito
4. Carregue o exemplo `OLED_LoRa_Sender` em uma placa
5. Carregue o exemplo `OLED_LoRa_Receiver` em outra
6. Monitore os pacotes recebidos no display OLED ou via Serial
7. Ajuste a frequência se necessário (433, 868 ou 915 MHz)
</div>
