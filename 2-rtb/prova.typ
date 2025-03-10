#import "../../../templates/template.typ": *

#show: content => verbale(
  titoloDocumento: "Seconda Riunione",
  abstract: "Discussione dei capitolati, raccolta e formulazione delle domande per i proponenti, definizione versionamento, templating e struttura repository",
  responsabili: "Carmelo Russello",
  redattori: "Pietro Crotti",
  verificatori: "Aleena Mathew",
  tipo: "Verbale Interno",
  destinatari: "Sigma18",
  versioneAttuale: "1.0.0",
  content: content,
)

= Riferimenti generali
Il seguente documento contiene il resoconto della riunione interna del gruppo _Sigma18_ tenutasi in modalità *virtuale* tramite la piattaforma _Discord_, avvenuta in data *07 Marzo 2025* e dalla durata di un'*ora* e *10 minuti*.

Nella riunione sono stati trattati i punti all'ordine del giorno.

== Partecipanti
- Alessandro Bernardello
- Mirco Borella
- Pietro Crotti
- Marco Egidi
- Matteo Marangon
- Aleena Mathew
- Carmelo Russello

= Ordine del giorno
== Discussione dei capitolati
Dopo una visione approfondita della documentazione fornita per i capitolati, il gruppo ha valutato i pro e contro delle proposte in base ai propri interessi personali e sulle tecnologie conosciute.
Da questa discussione è emersa in modo unanime la preferenza per il capitolato C3 proposto dall'azienda *Var Group S.P.A*, tenendo come seconda opzione il capitolato C4 proposto dall'azienda *Sync Lab S.R.L*.

Ulteriori valutazioni verranno specificate nel documento relativo alla valutazioni dei capitolati.

== Raccolta e formulazione delle domande per i proponenti
A seguito della discussione dei capitolati sono emersi alcuni dubbi riguardo le tecnologie e funzionalità dei prodotti richiesti.

In particolare sono state formulate domande per l'azienda *Var Group S.P.A* riguardo le tecnologie utilizzate, gli eventuali costi per l'API (_Application Programming Interface_) e i modi e la disponibilità dell'azienda per la formazione del gruppo sulle tecnologie proposte.

Il gruppo si impegna di contattare l'azienda all'indirizzo email fornito nella presentazione per chiarire i dubbi sorti in un eventuale incontro.

== Definizione versionamento della documentazione <versionamento>
Il gruppo ha optato per l'utilizzo di un sistema di versionamento così definito:
*X.Y.Z*, dove:
- *X*: Modifiche sostanziali e ristrutturazioni importanti
- *Y*: Aggiunta di nuovi paragrafi e correzioni concettuali
- *Z*: Correzioni sintattiche e grammaticali, modifiche minori e cambiamenti al template

== Definizione nomenclatura dei documenti
Si è deciso di adottare un sistema di nomenclatura _standard_ per l'assegnazione dei nomi dei verbali così definito: *[vi-ve]\_[DATA]\_[VERSIONE]*

Nello specifico:
- *vi*: Verbale Interno
- *ve*: Verbale Esterno
- *DATA*: Data di svolgimento del verbale in formato ISO 8601 (ad esempio: 20250307)
- *VERSIONE*: Versione del verbale in formato X.Y.Z come definito in #link(<versionamento>)[precedenza].

== Definizione struttura del repository
Il gruppo ha deciso di strutturare il repository della documentazione in modo da suddividere i documenti per varie fasi del progetto.

La struttura decisa e attuale (alla scrittura) per il repository è la seguente:
#align(center)[
  ```
  docs
    ├── assets
    │   └── img
    │       ├── LogoSlim.svg
    │       └── Logo.svg
    ├── readme.md
    ├── templates
    │   └── template.typ
    └── 1-candidatura
        └── verbali
            └── interni
                  └── vi_20250305_1.0.0.typ

  ```
]

= Conclusioni e decisioni prese
In conclusione il gruppo ha espresso maggior interesse per il capitolato C3 proposto dall'azienda *Var Group S.P.A* e ha incaricato *Carmelo Russello* di contattare l'azienda per fissare un incontro.

Segue un riepilogo delle decisioni prese:
- Preferenza per il capitolato C3 proposto dall'azienda *Var Group S.P.A*
- Utilizzo di un sistema di versionamento *X.Y.Z*
- Adozione di una nomenclatura standard per i verbali
- Struttura del repository

Il gruppo si impegna nella creazione degli strumenti dedicati alla consultazione della documentazione tra cui il sito web e le automazioni per la compilazione dei sorgenti in documenti fruibili e nell'aggiornare i documenti giá prodotti in base alle decisioni prese.

= Attività programmate
#tabellaAttivitaProgrammate(
  attivita: (
    link("https://github.com/Sigma18Unipd/docs/issues/2")[00002],
    "Organizzazione Incontro con Var Group S.P.A",
    link("https://github.com/Sigma18Unipd/docs/issues/3")[00003],
    "Stesura Verbale Interno 2025-03-07",
    link("https://github.com/Sigma18Unipd/docs/issues/4")[00004],
    "Creazione GitHub Action",
    link("https://github.com/Sigma18Unipd/docs/issues/5")[00005],
    "Creazione Sito Web Documentazione",
    link("https://github.com/Sigma18Unipd/docs/issues/7")[00007],
    "Stesura documento Valutazione dei Capitolati",
  ),
)
