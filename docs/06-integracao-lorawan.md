{{ include('includes/EM_DESENVOLVIMENTO.md') }}

<style>
.md-content-none {
  display: none !important;
}
</style>
<div class="md-content-none">
### 📄 `integracao.md`

```markdown
# Integração com LoRaWAN

Este exemplo inicial usa **comunicação ponto-a-ponto** (peer-to-peer), sem rede LoRaWAN.

Se desejar integrar com servidores como **The Things Network (TTN)**:

1. Crie um aplicativo na TTN Console
2. Registre os dispositivos (OTAA ou ABP)
3. Adicione as bibliotecas LoRaWAN (como LMIC)
4. Configure os parâmetros (DevEUI, AppEUI, AppKey ou DevAddr, NwkSKey, AppSKey)

> ⚠️ O projeto atual não usa LoRaWAN, apenas comunicação direta LoRa.
```

</div>
