# Projeto e Requisitos

O projeto desenvolvido opera da seguinte forma: o dispositivo sensor (end device) coleta os dados e os transmite por meio da rede sem fio LoRa.

Um gateway próximo capta esses dados e os encaminha para a The Things Network (TTN) via internet.

A TTN armazena as informações e as disponibiliza para uso em aplicações.

Agora que entendemos o funcionamento do projeto, é importante definir os requisitos necessários para possibilitar sua replicação.

Este projeto utiliza dois tipos de dispositivos: Gateway e End Device.

## Gateway/Concentradores

Um **Gateway LoRaWAN** é responsável por atuar como ponte entre os **dispositivos finais (end devices)** e a **rede (internet)**. Ele recebe os sinais LoRa enviados pelos sensores e os encaminha para um **servidor de rede LoRaWAN** através de uma conexão com a internet (como Ethernet, Wi-Fi ou 4G).

Agora que entendemos o papel do gateway, podemos definir como será sua implementação neste projeto.

O gateway definido para este projeto será do tipo **LoRaWAN monocanal**, ou seja, operará em uma única frequência. Para isso, será utilizada a **placa Heltec WiFi LoRa 32 (V2)**, que possui suporte à comunicação LoRa e conectividade Wi-Fi integradas.

Este tipo de gateway é mais simples e econômico, ideal para fins educacionais, protótipos ou ambientes de testes controlados. É importante destacar que gateways monocanal apresentam limitações em termos de capacidade de comunicação simultânea. Por essa razão, são recomendados apenas para aplicações não críticas, onde a confiabilidade e a escalabilidade da rede não sejam fatores determinantes.

### Definição de hardware:

- **Tipo:** Gateway LoRaWAN monocanal (opera em uma única frequência)
- **Placa microcontroladora:** Heltec WiFi LoRa 32 (V2)
- **Frequência de operação:** 868–915 MHz (dependendo da região)
- **Conectividade:** Comunicação LoRa com os dispositivos finais e Wi-Fi para acesso à internet
- **Aplicação:** Recepção dos dados enviados pelos end devices e encaminhamento ao servidor de rede LoRaWAN

## End Device

Os **end devices**, ou **dispositivos finais**, são os nós da rede responsáveis pela coleta de dados no ambiente monitorado. Esses dispositivos são equipados com sensores e módulos de comunicação LoRa, permitindo que transmitam informações de forma remota e com baixo consumo de energia.

Neste projeto, o end device será implementado com a **placa ESP32-DEVKIT-V1**, associada a um **módulo LoRaWAN da Radioenge**. A comunicação entre o end device e o gateway será realizada utilizando o protocolo LoRa, com alcance que pode variar de algumas centenas de metros até vários quilômetros, dependendo das condições do ambiente (como obstáculos físicos, elevação do terreno e interferências eletromagnéticas).

O end device pode ser programado para operar em diferentes modos, como envio periódico, envio por evento (quando um valor ultrapassa determinado limite) ou acionamento manual. Essa flexibilidade permite adaptar o funcionamento do dispositivo às necessidades específicas da aplicação. Esse conceito será abordado com mais profundidade ao longo do projeto.

### Definição de hardware:

- **Tipo:** End Device LoRaWAN
- **Placa microcontroladora:** ESP32-DEVKIT-V1
- **Módulo LoRa:** Módulo LoRaWAN Radioenge
- **Frequência de operação:** 868–915 MHz (dependendo da região)
- **Conectividade:** Comunicação via protocolo LoRa
- **Aplicação:** Coleta e transmissão de dados de sensores ambientais

## Software, Dependências e Bibliotecas

Para o desenvolvimento e a configuração tanto do **gateway** quanto do **end device**, será utilizada a **Arduino IDE**, versão **2.0.17**, escolhida por sua ampla compatibilidade com placas ESP32 e sua facilidade de integração com bibliotecas de terceiros.

Abaixo estão listadas todas as **bibliotecas necessárias** para o correto funcionamento do projeto, cada uma com sua respectiva versão e autor. Essas bibliotecas devem ser instaladas por meio do **Gerenciador de Bibliotecas** da Arduino IDE ou manualmente, movendo os arquivos para o diretório de bibliotecas do Arduino (C:/<Usuário>/Documents/Arduino/libraries).

As bibliotecas envolvidas neste projeto possibilitam desde a comunicação LoRa até funcionalidades auxiliares como manipulação de JSON, controle de periféricos, conexão Wi-Fi, entre outras.

### Bibliotecas:

- `Adafruit_NeoPixel` — por Adafruit, v1.9.0  
  Permite o controle de LEDs RGB, útil como indicador visual de status do dispositivo.
- `aes`
  Permite a criptografia de dados, usada para segurança na transmissão de dados.
- `ArduinoJson` — por Benoit Blanchon, v6.14.0  
  Manipulação de objetos JSON para estruturação e envio de dados.
- `esp32-http-update` — por Matej Suchra, v2.1.145  
  Permite atualizações OTA (Over-the-Air) via HTTP.
- `ESP8266_Oled_Driver_for_SSD1306_display`
  Driver para displays OLED com controlador SSD1306, usado na visualização de informações locais.
- `gBase64` — por Densaugeo, v1.0.0  
  Codificação e decodificação de dados em Base64.
- `LoRaCode`
  Biblioteca utilizada para controle da comunicação via LoRa.
- `MCCI_LoRaWAN_LMIC_library` — por IBM, v4.1.1  
  Pilha de comunicação LoRaWAN compatível com a especificação oficial.
- `Streaming` — por Mikal Hart, v5.0.0  
  Permite a escrita simplificada em objetos de saída como `Serial`.
- `Time` — por Michal Margolis, v1.6  
  Permite a manipulação de tempo (relógio interno, timestamps etc.).
- `TinyGPSPlus` — v1.0.2b  
  Interpretação de dados de módulos GPS.
- `WiFiManager` — por tzapu, v2.0.16-rc.2  
  Permite a configuração da rede Wi-Fi sem necessidade de alterar o código fonte, permitindo ao usuário inserir SSID e senha via portal local.

## Pré-Requisitos

Vamos realizar um _recap_ dos requisitos para nos certificar de que todos eles serão atendidos:

- **Drivers USB** instalados para o microcontrolador (**CP210x**, usado em placas ESP32)
- **Permissões de acesso à porta serial** (necessário em sistemas **Linux** e **macOS**)
- **Acesso à internet** para instalação das bibliotecas e dependências
- **Ambiente de desenvolvimento configurado** para compilar e enviar código para os dispositivos (via **Arduino IDE 2.0.17**)

---

## Hardware Necessário

| Componente                     | Quantidade | Observações                                     |
| ------------------------------ | ---------- | ----------------------------------------------- |
| Placa Heltec WiFi LoRa 32 (V2) | 1          | Usada como gateway LoRaWAN monocanal            |
| ESP32 DEVKIT-V1                | 1+         | Usado como end device; pode haver mais de um    |
| Módulo LoRaWAN (ex: Radioenge) | 1+         | Um para cada end device (caso não use Heltec)   |
| Antenas LoRa                   | 2+         | Compatíveis com 868 MHz ou 915 MHz              |
| Cabos jumpers                  | Diversos   | Conexão entre módulos e microcontroladores      |
| Fonte de alimentação           | 2+         | Pode ser via USB, bateria LiPo ou fonte externa |

> 💡 **Nota:** A quantidade de dispositivos pode variar conforme o número de nós finais a serem utilizados nos testes.

---

## Software Necessário

| Software/Firmware      | Versão Recomendada      | Descrição                                           |
| ---------------------- | ----------------------- | --------------------------------------------------- |
| Arduino IDE            | 2.0.17                  | Ambiente de desenvolvimento principal para ESP32    |
| ESP32 Drivers (CP210x) | Atual                   | Necessário para upload de código via USB            |
| Bibliotecas            | Conforme seção anterior | Comunicação via LoRa e suporte ao protocolo LoRaWAN |

> 💡 **Nota:** Realize a instalação das bibliotecas via o **Gerenciador de Bibliotecas** da Arduino IDE ou manualmente.

<br />
<br />

  <div style="display: flex; justify-content: space-around; margin-top: 2em;">
  <a href="../01-introducao/" class="md-button md-button--primary" style="width: 360px; text-align: center;">Introdução</a>
  <a href="../03-configuracao-ambiente/" class="md-button md-button--primary" style="width: 360px; text-align: center;">Configuração do Ambiente</a>
  </div>
