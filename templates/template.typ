#let verbale(
  titoloDocumento: "",
  abstract: "",
  tipo: "",
  responsabili: (),
  redattori: (),
  verificatori: (),
  destinatari: "",
  versioneAttuale: "",
  versioni: (),
  content: [],
) = {
  //Proprietà generali documento
  set text(lang: "it", size: 12pt)
  set page(margin: (x: 2cm, y: 2cm), paper: "a4")
  set par(justify: true)
  set document(title: titoloDocumento)
  show link: underline
  show enum: it => pad(
    left: 1em,
    {
      set enum(
        numbering: n => style(styles => {
          let num = numbering("1.", n)
          place(dx: -measure(num, styles).width, num)
        }),
      )
      it
    },
  )

  //Prima pagina
  align(top + center)[
    #image("../assets/img/Logo.svg", width: 30%)
    #text(size: 14pt)[
      #link("mailto: Sigma18Unipd@gmail.com")[Sigma18Unipd\@gmail.com]
    ]
  ]
  align(center + horizon)[
    #set text(size: 16pt)
    #text(size: 30pt, weight: "bold", titoloDocumento)
  ]
  align(bottom + center)[
    #set text(size: 14pt)
    #set table(
      stroke: none,
      gutter: 0.2em,
    )
    #grid(
      columns: (1fr, 1fr),
      rows: auto,
      align: horizon,
      grid.cell(
        table(
          columns: 2,
          align: left,
          table.vline(x: 1),
          align(right + horizon)[*Responsabile*], responsabili,
          align(right + horizon)[*Redattore*], redattori,
          align(right + horizon)[*Verificatore*], verificatori
        ),
      ),
      grid.cell(
        table(
          columns: 2,
          align: left,
          table.vline(x: 1),
          align(right + top)[*Versione*], versioneAttuale,
          align(right + top)[*Tipo*], tipo,
          align(right + top)[*Destinatari*], text(style: "italic", destinatari),
        ),
      )
    )
    #v(2em)
    #set par(spacing: 0.7em)
    #text(size: 16pt, weight: 800, style: "italic", "Abstract dei contenuti:")

    #text(size: 14pt, abstract)
  ]
  pagebreak()

  //Proprietà generali pagine successive
  set page(
    margin: (x: 2cm, y: 3cm),
    header: [
      #grid(
        align: horizon,
        columns: (1fr, 1fr),
        align(left)[#image("../assets/img/LogoSlim.svg", height: 30%)], align(right)[#text(size: 12pt, titoloDocumento)],
      )
      #line(length: 100%, stroke: 0.5pt)
    ],
    numbering: "1",
  )

  //Registro delle versioni
  if versioni.len() != 0 {
    heading("Registro delle versioni")
    v(1em)
    show table.cell.where(y: 0): strong
    table(
      columns: (auto, auto, auto, auto, 1fr),
      rows: auto,
      inset: 7pt,
      table.header([Versione], [Data], [Autore], [Verificatore], [Descrizione Modifiche]),
      ..versioni
    )
    pagebreak()
  }

  //Indice
  show outline.entry.where(level: 1): it => {
    strong(it)
  }
  outline(title: [Indice #v(0.5em)], indent: 1em)
  pagebreak()
  set heading(numbering: "1.")

  //Contenuto
  content
}

//Tabella attività programmate
#let tabellaAttivitaProgrammate(
  attivita: (),
) = {
  v(0.5em)
  table(
    columns: (1fr, 3fr),
    rows: auto,
    inset: 5pt,
    table.header([*Identificativo*], [*Descrizione*]),
    ..attivita,
  )
}
