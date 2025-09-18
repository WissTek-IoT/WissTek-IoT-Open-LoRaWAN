{{ include('includes/EM_DESENVOLVIMENTO.md') }}

<style>
.md-content-none {
  display: none !important;
}
</style>
<div class="md-content-none">
# Problemas Comuns e Soluções

| Problema                     | Solução                                                                   |
| ---------------------------- | ------------------------------------------------------------------------- |
| Placa não aparece na IDE     | Instale o driver CP210x corretamente                                      |
| Código não carrega           | Verifique GPIO5, GPIO12, GPIO15 e botão "EN" durante o upload             |
| Display OLED não mostra nada | Confirme a instalação da biblioteca SSD1306 (ThingPulse)                  |
| Comunicação falha (LoRa)     | Verifique se ambas placas usam a mesma frequência e antena está conectada |
| RSSI muito fraco             | Aumente a distância da antena da placa e evite obstáculos metálicos       |

</div>
