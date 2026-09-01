# AWTRIX Travel Time per Home Assistant

[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
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
connesso allo stesso broker, con la **scoperta automatica Home Assistant**
attiva nelle impostazioni MQTT del display: solo così AWTRIX compare come
dispositivo selezionabile nel campo **Dispositivo AWTRIX**. Non è necessario
inserire manualmente alcun prefisso: il topic viene ricavato automaticamente
dal dispositivo scelto ed è possibile selezionarne più di uno.

Scegliere il sensore che espone il tempo di viaggio corrente in minuti e impostare
il tempo di percorrenza normale, senza traffico rilevante. Le due soglie sono
percentuali di ritardo rispetto a quel valore; mantenere la soglia rossa maggiore
della gialla.

### Testo senza destinazione

Disattivando **Mostra il testo della destinazione** il testo mostra solo i
minuti (es. `12 min.`), utile quando l'icona identifica già il contesto (per
esempio l'asilo).

### Fasce orarie

Attivando **Limita a due fasce orarie** l'app viene mostrata solo negli
intervalli configurati (per esempio andata e ritorno da un percorso abituale) e
viene rimossa automaticamente dal display al termine di ciascuna fascia. Le
fasce si riferiscono all'ora locale del server Home Assistant e non gestiscono
intervalli che attraversano la mezzanotte.

## Icona

La blueprint usa per impostazione predefinita l’icona `car`, inclusa nelle icone
AWTRIX/LaMetric: non sono necessari file aggiuntivi o script di upload. Per
usare un’icona diversa, inserire il relativo identificativo nel campo **Icona
AWTRIX** della blueprint.

Per un percorso verso l'asilo, la [galleria icone LaMetric](https://developer.lametric.com/icons)
non include un'icona curata "kindergarten/preschool"; tra le icone caricate
dalla community, la più pertinente trovata è **Classroom** (ID `37482`). Le
icone della community non sono verificate da LaMetric: si consiglia di
visualizzarla nella galleria prima di usarla e, in alternativa, di generarne
una personalizzata con **Create Icon**.
