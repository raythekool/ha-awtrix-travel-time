# AWTRIX Travel Time per Home Assistant

[![GitHub License](https://img.shields.io/github/license/raythekool/ha-awtrix-travel-time?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/raythekool/ha-awtrix-travel-time?style=flat-square)](https://github.com/raythekool/ha-awtrix-travel-time/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/raythekool/ha-awtrix-travel-time?style=flat-square)](https://github.com/raythekool/ha-awtrix-travel-time/issues)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Blueprint-41BDF5?style=flat-square&logo=home-assistant)](https://www.home-assistant.io/)
[![AWTRIX](https://img.shields.io/badge/AWTRIX-3-orange?style=flat-square)](https://blueforcer.github.io/awtrix3/)

Blueprint Home Assistant per mostrare il tempo di percorrenza di un sensore su
un display AWTRIX tramite MQTT.

L'app visualizza un'icona automobile e il tempo in minuti. Il colore comunica le
condizioni del traffico rispetto al tempo normale configurato:

- verde: ritardo inferiore alla soglia gialla;
- giallo: ritardo uguale o superiore alla soglia gialla;
- rosso: ritardo uguale o superiore alla soglia rossa.

## Installazione

### Importazione automatica

[![Importa blueprint in Home Assistant](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fraythekool%2Fha-awtrix-travel-time%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Fawtrix%2Ftravel_time.yaml)

1. Selezionare il pulsante per aprire Home Assistant e precompilare
   l'importazione della blueprint.
2. Selezionare **Importa blueprint**.
3. Creare una nuova automazione dal blueprint **AWTRIX: tempo di viaggio**.

### Importazione manuale

1. In Home Assistant aprire **Impostazioni → Automazioni e scene → Blueprint →
   Importa blueprint**.
2. Incollare l'URL della blueprint:

   ```text
   https://github.com/raythekool/ha-awtrix-travel-time/blob/main/blueprints/automation/awtrix/travel_time.yaml
   ```

3. Selezionare **Anteprima**, quindi **Importa blueprint**.

## Configurazione

Il blueprint richiede l'integrazione MQTT configurata in Home Assistant e AWTRIX
connesso allo stesso broker. Inserire il prefisso MQTT del display (per esempio
`awtrix_123456`): il blueprint pubblica su
`<prefisso>/custom/<nome_app>`.

Scegliere il sensore che espone il tempo di viaggio corrente in minuti e impostare
il tempo di percorrenza normale, senza traffico rilevante. Le due soglie sono
percentuali di ritardo rispetto a quel valore; mantenere la soglia rossa maggiore
della gialla.

## Icona

La blueprint usa per impostazione predefinita l’icona `car`, inclusa nelle icone
AWTRIX/LaMetric: non sono necessari file aggiuntivi o script di upload. Per
usare un’icona diversa, inserire il relativo identificativo nel campo **Icona
AWTRIX** della blueprint.
