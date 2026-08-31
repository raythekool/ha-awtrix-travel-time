# AWTRIX Travel Time per Home Assistant

Blueprint Home Assistant per mostrare il tempo di percorrenza di un sensore su
un display AWTRIX tramite MQTT.

L'app visualizza un'icona automobile e il tempo in minuti. Il colore comunica le
condizioni del traffico rispetto al tempo normale configurato:

- verde: ritardo inferiore alla soglia gialla;
- giallo: ritardo uguale o superiore alla soglia gialla;
- rosso: ritardo uguale o superiore alla soglia rossa.

## Installazione

1. Scaricare
   [`travel_time.yaml`](blueprints/automation/awtrix/travel_time.yaml).
2. In Home Assistant aprire **Impostazioni → Automazioni e scene → Blueprint →
   Importa blueprint** e importare il file.
3. Creare una nuova automazione dal blueprint **AWTRIX: tempo di viaggio**.

## Configurazione

Il blueprint richiede l'integrazione MQTT configurata in Home Assistant e AWTRIX
connesso allo stesso broker. Inserire il prefisso MQTT del display (per esempio
`awtrix_123456`): il blueprint pubblica su
`<prefisso>/custom/<nome_app>`.

Scegliere il sensore che espone il tempo di viaggio corrente in minuti e impostare
il tempo di percorrenza normale, senza traffico rilevante. Le due soglie sono
percentuali di ritardo rispetto a quel valore; mantenere la soglia rossa maggiore
della gialla. L'icona predefinita è `car`; sostituirla con l'identificativo di
un'altra icona disponibile sul proprio AWTRIX se necessario.
