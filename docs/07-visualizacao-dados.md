{{ include('includes/EM_DESENVOLVIMENTO.md') }}

<style>
.md-content-none {
  display: none !important;
}
</style>
<div class="md-content-none">
# Visualização dos Dados

Durante os testes:

- Os dados são exibidos diretamente no display OLED da placa:
  - Texto: "Sending packet: X"
  - RSSI e tamanho do pacote recebido
- Você pode também usar o **Serial Monitor** da IDE do Arduino para depuração:
  - `Serial.println()` pode mostrar os mesmos dados visíveis no display
  </div>
