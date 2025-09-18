{{ include('includes/EM_DESENVOLVIMENTO.md') }}

<style>
.md-content-none {
  display: none !important;
}
</style>
<div class="md-content-none">
# Configuração do Ambiente

1. Instale o Arduino IDE
2. Adicione a URL nas preferências:

```
https://dl.espressif.com/dl/package_esp32_index.json
```

3. Vá em Ferramentas → Placas → Gerenciador de Placas

- Pesquise por "esp32"
- Instale o pacote da Espressif

4. Instale o driver CP210x (USB-Serial):

- [Baixar driver no site da Silicon Labs](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)

5. Instale as bibliotecas:

- `Heltec ESP32 Dev-Boards`
- `ESP8266 and ESP32 Oled Driver for SSD1306 (ThingPulse)`
</div>
