# AWTRIX Travel Time Display 🚗

[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Blueprint-41BDF5?style=flat-square&logo=home-assistant)](https://www.home-assistant.io/)
[![AWTRIX](https://img.shields.io/badge/AWTRIX-3-orange?style=flat-square)](https://blueforcer.github.io/awtrix3/)

Blueprint Home Assistant per mostrare su AWTRIX 3 il tempo di viaggio di un
sensore, con colore dinamico basato sul ritardo rispetto al tempo abituale.

## ✨ Funzionalita

- Aggiornamento immediato quando cambia il sensore e refresh automatico ogni minuto.
- Colore verde, giallo o rosso in base alle soglie di ritardo configurate.
- Visualizzazione compatta: icona configurata + minuti + `min.`.
- Selezione di uno o piu dispositivi AWTRIX rilevati via MQTT Discovery.
- Due fasce orarie opzionali, adatte per andata e ritorno.
- Durata e scorrimento del testo configurabili.

## ⚠️ Requisiti

1. Home Assistant 2024.6.0 o successivo.
2. Uno o piu dispositivi AWTRIX 3 configurati tramite MQTT.
3. MQTT Discovery di Home Assistant attiva nelle impostazioni MQTT di AWTRIX.
4. Un sensore che esponga il tempo di viaggio corrente in minuti.

## 📦 Installazione

### Importazione rapida

[![Importa blueprint in Home Assistant](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fraythekool%2Fha-awtrix-travel-time%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Fawtrix%2Ftravel_time.yaml)

Selezionare il pulsante e quindi **Importa blueprint** in Home Assistant.

### Installazione manuale

1. Scaricare [travel_time.yaml](blueprints/automation/awtrix/travel_time.yaml).
2. Copiarlo in `config/blueprints/automation/awtrix/` della configurazione Home
   Assistant.
3. Ricaricare le automazioni o riavviare Home Assistant.

## 🚀 Avvio rapido

1. Aprire **Impostazioni**, quindi **Automazioni e scene**.
2. Selezionare **Crea automazione**, poi **Usa un blueprint**.
3. Selezionare **AWTRIX Tempo di Viaggio**.
4. Configurare i parametri principali:

| Parametro                    | Esempio                  | Descrizione                                            |
| ---------------------------- | ------------------------ | ------------------------------------------------------ |
| Dispositivo AWTRIX           | Ulanzi TC001             | Uno o piu display AWTRIX 3 rilevati da MQTT Discovery. |
| Sensore del tempo di viaggio | `sensor.tempo_per_asilo` | Sensore con valore in minuti.                          |
| Nome dell'app AWTRIX         | `travel_time_asilo`      | Identificativo univoco dell'app personalizzata.        |
| Icona AWTRIX                 | `4532`                   | ID LaMetric o nome di file caricato in `/ICONS`.       |
| Tempo di percorrenza normale | `20` min                 | Tempo senza traffico rilevante.                        |
| Soglia gialla                | `20` %                   | Ritardo da cui usare il giallo.                        |
| Soglia rossa                 | `25` %                   | Ritardo da cui usare il rosso.                         |

## 📺 Formato display

L'app mostra l'icona scelta e il tempo, per esempio `12 min.`. Il colore viene
calcolato rispetto al tempo normale:

| Ritardo                               | Colore |
| ------------------------------------- | ------ |
| Inferiore alla soglia gialla          | Verde  |
| Dalla soglia gialla alla soglia rossa | Giallo |
| Uguale o superiore alla soglia rossa  | Rosso  |

## 🔧 Opzioni di configurazione

### Durata e scorrimento

- **Durata di visualizzazione**: secondi in cui l'app resta nel ciclo AWTRIX.
- **Disattiva scorrimento**: mantiene il testo statico. Disattivarlo se il nome
  dell'icona o future personalizzazioni richiedono lo scorrimento.

### Fasce orarie

Attivare **Limita a due fasce orarie** per limitare la pubblicazione a due
intervalli quotidiani. Configurare l'inizio e la fine di entrambe le fasce; al
termine di ciascuna, l'app viene rimossa automaticamente dal display.

Le fasce usano l'ora locale di Home Assistant e non possono attraversare la
mezzanotte. Per esempio: `07:30-09:00` per l'andata e `15:30-17:00` per il
ritorno.

### Icona AWTRIX

Il campo **Icona AWTRIX** accetta:

- un ID numerico della [galleria LaMetric](https://developer.lametric.com/icons),
  che AWTRIX scarica al primo utilizzo; oppure
- il nome, senza estensione, di un file gia caricato nella cartella `/ICONS` del
  display.

Il valore predefinito `4532` e l'icona LaMetric "car". Per un percorso verso
l'asilo, la galleria include l'icona community **Classroom** (ID `37482`):
verificarne l'aspetto nella galleria prima di usarla.

## 🐛 Risoluzione problemi

### Il display non si aggiorna

1. Verificare che il sensore selezionato abbia un valore numerico in minuti.
2. Controllare che AWTRIX sia online e collegato allo stesso broker MQTT di Home
   Assistant.
3. Abilitare **Home Assistant Discovery** nelle impostazioni MQTT del display e
   attendere che compaia come dispositivo selezionabile.
4. Se sono attive le fasce orarie, verificare che l'ora corrente rientri in una
   di esse.

### L'icona non compare

Usare un ID numerico LaMetric, come `4532`, oppure il nome di un file realmente
presente in `/ICONS`. Una parola generica come `car` non e un ID valido e non
viene risolta dal display.

### Colore non previsto

Confrontare il valore del sensore con il tempo normale. La soglia rossa deve
essere maggiore della soglia gialla; entrambe indicano percentuali di ritardo.

## 🤝 Contributi

Segnalazioni e proposte sono benvenute tramite le
[issue del repository](https://github.com/raythekool/ha-awtrix-travel-time/issues).

## 📄 Licenza

Distribuito con licenza MIT. Consultare [LICENSE](LICENSE).

## 🙏 Crediti

- [AWTRIX 3](https://github.com/Blueforcer/awtrix3)
- [LaMetric Icon Gallery](https://developer.lametric.com/icons)
- [Home Assistant](https://www.home-assistant.io/)
