#import "../../../templates/template.typ": *

#show: content => verbale(
  titoloDocumento: "Prima Riunione",
  abstract: "Incontro conoscitivo, definizione del nome e del logo, definizione e creazione dei canali di comunicazione e discussione dei capitolati.",
  responsabili: "Carmelo Russello",
  redattori: "Mirco Borella",
  verificatori: "Alessandro Bernardello",
  tipo: "Verbale Interno",
  destinatari: "Sigma18",
  versioneAttuale: "1.0.1",
  content: content,
)

= Riferimenti generali
Il seguente documento contiene il resoconto della riunione interna del gruppo _Sigma18_ tenutasi in modalità *virtuale* tramite la piattaforma _Discord_, avvenuta in data *05 Marzo 2025* e dalla durata di un'*ora*.

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
== Presentazione dei membri del gruppo
La riunione è iniziata con una breve presentazione iniziale dei membri del gruppo.

== Definizione del nome del gruppo
Sono state proposte numerose alternative per quanto concerne il nome rappresentativo. A seguito di una votazione, è stato confermato il nome _*Sigma18*_ come denominazione del gruppo.

== Creazione del logo del gruppo
Successivamente alla definizione del nome del gruppo, si è proceduto alla creazione del logo. Sono stati valutati diversi design. A seguito di iterazioni sulla proposta più vicina alle aspettative, si è arrivati ai seguenti risultati approvati all'unanimità:

#figure(
  image("../../../assets/img/Logo.svg", width: 35%),
  caption: [
    Logo in versione estesa
  ],
)
#v(2em)
#figure(
  image("../../../assets/img/LogoSlim.svg", width: 25%),
  caption: [
    Logo in versione compatta
  ],
)
#v(2em)

== Definizione dei canali di comunicazione
Abbiamo deciso di utilizzare le seguenti piattaforme per la comunicazione *interna*:
- _Whatsapp_ per comunicazioni testuali;
- _Discord_ come piattaforma di comunicazione per riunioni virtuali;

Per le comunicazioni *esterne*, è stata creata una casella di posta elettronica dedicata:
#align(center)[
  #link("mailto: Sigma18Unipd@gmail.com")[*Sigma18Unipd\@gmail.com*]
]

== Analisi degli strumenti
È stato deciso di utilizzare _Git_ come sistema di versionamento del codice e _GitHub_ come piattaforma di hosting e gestione _issue_.
Dopo ragionamenti sui principali modi di redigere documenti, si è scelto di utilizzare _Typst_ assieme ad un sistema di _template_ per facilitare la stesura della documentazione.

== Discussione sui capitolati
Sono stati brevemente discussi i capitolati proposti per il secondo lotto. Si è deciso di approfondire la conoscenza di tutti i capitolati e di discuterne in riunioni successive.

= Conclusioni
La riunione si è conclusa concordando un successivo incontro per *Venerdi 7 Marzo* per discutere in modo più approfondito i capitolati d'appalto.
