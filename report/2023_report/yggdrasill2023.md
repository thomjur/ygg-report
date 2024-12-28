---
title: Yggdrasill Jahresrückblick 2023
author: thomas jurczyk
layout: article
exclude: true
category: short_contributions
---

<sub>**Aktueller Stand**: 28. Dezember 2023</sub>

## Einführung
Die folgenden Visualisierungen und Statistiken basieren auf Beiträgen, die während des Jahres 2023 auf der religionswissenschaftlichen Informationsliste [Yggdrasill](https://www.lists.uni-marburg.de/lists/sympa/info/yggdrasill) veröffentlicht wurden. Laut Beschreibung auf der offiziellen Webseite, die von der Universität Marburg gehostet wird, handelt es sich bei Yggdrasill um eine ...

>  ... religionswissenschaftliche Diskussions- und Informationsliste (...) \[Yggdrasill] ist eine Dienstleistung der Europäischen Gesellschaft für Religionswissenschaft (European Association for the Study of Religions, EASR). Die Diskussionen bei "Yggdrasill" werden hauptsächlich auf Deutsch geführt. Yggdrasill wird gegenwärtig von Carmen Becker (Leibniz Universität Hannover) betreut.[^1]

Anders als in den Vorjahren enthält die Yggdrasill Analyse für 2023 auch Kennzahlen zu allen bisher auf Yggdrasill veröffentlichten Beiträgen seit der Gründung der Liste (1997). Dies wurde unter anderem durch die freundliche Unterstützung von Frau Carmen Becker ermöglicht, die mir Zugriff auf das Mailarchiv gewährt hat. Allerdings wird in diesem Jahr aufgrund akuten Zeitmangels auf zeitintensive Analysen wie bspw. die Klassifizierung einzelner Beiträge oder die Status-Analyse der Beitragenden verzichtet. Falls ich in den kommenden Jahren wieder mehr Kapazitäten haben sollte, werde ich diese jedoch wieder aufnehmen. Im Fokus der diesjährigen Analysen stand der Versuch, große Teile automatisiert auswerten zu lassen.

Die folgenden statistischen Übersichten über die Diskussionsthemen sowie -teilnehmenden auf Yggdrasill verfolgen kein spezifisches Ziel. Sie sind vor allem aus dem Interesse und der Freude an der Generierung, Verarbeitung sowie Visualisierung digitaler Daten heraus entstanden.[^2]

Ein besonderes Augenmerk lag darauf, die Analysen und deren Visualisierungen so abstrakt zu halten, dass keine Rückschlüsse auf einzelne Listenmitglieder möglich bzw. sinnvoll sind. Falls sich dennoch jemand unbeabsichtigterweise angesprochen oder gar an den Pranger gestellt fühlt, bitte ich darum, mich zu kontaktieren, damit ich entsprechende Änderungen vornehmen kann.

Über Feedback, Hinweise (gerne auch technischer Natur) sowie Ideen für weitere Auswertungen würde ich mich sehr freuen. Gerne können Sie mich unter meiner Mailadresse <thomas.jurczyk-q88 _at_ rub.de> erreichen.

## Die Datenbasis
Die vollständige Datenbasis aller bisher auf Yggdrasill veröffentlichten Beiträge umfasst **14.756** Einträge. Die Datenbasis 2023 besteht aus aktuell **647** Mailbeiträgen (-15 zum Vorjahr), die im Laufe des Jahres 2023 auf Yggdrasill veröffentlicht wurden.[^3] Die Beiträge wurden entweder aus dem mir zur Verfügung gestellten Mailarchiv entnommen oder  manuell in meinem Mailprogramm gespeichert und von dort exportiert. Es wurden nach Möglichkeit nur Beiträge berücksichtigt, die dezidiert für Yggdrasill bestimmt waren. Beiträge, die gleichzeitig auf mehreren Listen erschienen sind und mehrere Listenkürzel in der Betreffzeile führten, sind in der Regel nicht berücksichtigt worden, zumindest in der manuellen Auslese aus meinem Mailprogramm. Trotzdem der Versuch unternommen wurde, alle Beiträge einzubeziehen, kann es sein, dass einige Beiträge übersehen bzw. aufgrund technischer Probleme nicht angezeigt wurden. Die folgenden absoluten Zahlen sind entsprechend mit Vorsicht zu interpretieren und sollten nur als allgemeine Trends gelesen werden.

Die Datenverarbeitung und -analyse wurde mit Python vorgenommen. Der Code findet sich in meinem [GitHub Repository](https://github.com/thomjur/ygg-report) (da große Teile des Codes in 2023 neu geschrieben und noch nicht überarbeitet wurden, ist der Code gerade für Außenstehende wahrscheinlich noch schwer nachvollziehbar; eine Dokumentation und Struktur soll aber folgen).

## Yggdrasill 2023 Auswertung

### Übersicht über alle Beiträge
Der folgende Plot zeigt die Anzahl der Beiträge/Jahr seit Gründung der Yggdrasill-Liste (1997).

![Yggdrasill Beiträge/Jahr seit 1997.](yearly_stats.png)

### Anzahl der Beiträge pro Monat plus die Top-Themen
Der folgende Plot zeigt die Anzahl der Beiträge pro Monat im Jahr 2023.

![Yggdrasill Beiträge/Monat im Jahr 2023.](posts_in_2023.png)

Es fällt auf, dass die intensivsten Diskussionen zu Beginn des Jahres geführt wurden, während die Anzahl an Beiträgen nach März 2023 merklich absinkt.

### Die Top 5 Themen 2023 (monatsübergreifend)

Es folgt die Liste der Top 5 Themen, die im Jahr 2023 auf Yggdrasill diskutiert wurden. Da die Zählung automatisiert erfolgte, wurde der Versuch unternommen, die Betreffzeilen der Mails durch Bereinigungen möglichst zu vereinheitlichen, bspw. durch das Löschen von "Aw:", was allerdings nicht immer gelungen ist. 

| Thema                                                                                                                                           |   Anz. Beiträge |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------|----:|
| was? schon drei nicht-theologische professuren für religionswissenschaft in deutschland?                                                                                                                           |  32 |
| religionswissenschaftliche lehre und ki                                                                                                         |  30 |
| déjà-vu: zeugen jehovas und sektendebatte                                                                               |  19 |
| religiös motivierter terrorismus?                                                                                                                            |  11 |
| neueste erkenntnisse aus der religionswissenschaft |  11 |

Bei dem Thema "Was? Schon drei nicht-theologische Professuren für Religionswissenschaft in Deutschland?" ging es um die Frage des Verhältnisses zwischen Religionswissenschaft und Theologie im institutionellen Gefüge deutscher Universitäten. Dies zeigt auch eine erste Analyse der Worthäufigkeiten, in der Wörter wie "Theologie", "Religionswissenschaft", "Universität", "Stelle" und "Deutschland" dominieren.[^4]

Bei dem zweithäufigsten Thema "Religionswissenschaftliche Lehre und KI" ging es, wie der Name bereits vermuten lässt, vor allem um die Frage nach dem Einfluss von ChatGPT und Co. auf die universitäre Lehre. Im Fokus standen allgemeine Bewertungsfragen und die Möglichkeit, mit großen Sprachmodellen entstandene Studienleistungen aufzudecken.[^5] In Ansätzen wurde jedoch auch der Einfluss von KI auf die spezifisch religionswissenschaftliche Forschung und Lehre diskutiert.

Beim dritten Thema "Déjà-vu: Zeugen Jehovas und Sektendebatte" war der Ausgangspunkt die Tat eines Amokläufers, die in überregionalen Medien im Kontext der "Zeugen Jehovas" als negativ bewerteter "Sekte" diskutiert und eingeordnet wurde. Dies wurde als Ausgangspunkt genommen, allgemein über den Sektenbegriff und die (nicht-religionswissenschaftliche) pejorative Darstellung von religiösen Gruppierungen und Minderheiten in der Gesellschaft zu diskutieren. Bezeichnend ist, dass aus einer textstatistischen Perspektive Begriffe aus dem Bereich der Gewalt dominierten, darunter "Täter", "Gewalt", "Opfer", "Terrorismus" und "Mord".

### Anzahl der Beitragenden
Der automatisierten Auswertung zufolge wurden Beiträge von **210** verschiedenen E-Mail Adressen gesendet. Dies entspricht jedoch *nicht* 210 individuellen Beitragenden, da einige Personen Beiträge von unterschiedlichen Mailadressen gesendet haben. Im Falle von 210 Personen würde dies einem durchschnittlichen Beitragsmenge von ca. 3 Posts/Person entsprechen. Der folgende Plot mit der kumulativen Summe der Beiträge/Person (absteigend beginnend mit der Person bzw. Mailadresse mit den meisten Beiträgen) zeigt jedoch, dass knapp ein Viertel der Beitragenden/Adressen beinahe zwei Drittel aller Beiträge auf Yggdrasill veröffentlicht hat, was in Anbetracht der absoluten Zahlen (ca. 52 Personen bzw. Adressen) auf eine recht große Community verweist, die keineswegs nur aus wenigen Power-Beitragenden besteht.

![Kumulative Summe der Beiträge auf Yggdrasill 2023.](cumsum_2023.png)

### Anzahl der Beiträge nach Geschlecht
Das folgende Tortendiagramm zeigt die relative Anzahl an Beiträgen auf Yggdrasill in 2023 nach Geschlecht der Verfasser:innen. Das Label "e" (=else) wurde vergeben, wenn Listenbeiträge von Organisationen oder nicht identifizierbaren Personen verfasst wurden. Es kann als durchaus problematisch betrachtet werden, dass die Kategorisierung in männlich oder weiblich hier lediglich binär erfolgt und dies auch noch rein auf Basis der Namen. Der Verfasser ist sich dieses Problems bewusst.

![Yggdrasill Gender-Analyse 2023.](gender_pie.png)

Wie in den vorherigen Jahren zeigt sich auch in diesem Jahr, dass die Geschlechterparität auf Yggdrasill hinsichtlich der absoluten Anzahl an Beiträgen durchaus vorhanden ist. 


## Fußnoten
***
[^1]: [Yggdrasill Beschreibung Uni Marburg](https://www.lists.uni-marburg.de/lists/sympa/info/yggdrasill). 

[^2]: Dabei wurden insbesondere die Programmiersprache [Python](https://www.python.org/) sowie die Python Bibliotheken [matplotlib](https://matplotlib.org/), [spaCy](https://spacy.io/) und [pandas](https://pandas.pydata.org/) verwendet.

[^3]: Stand 28. Dezember 2023.

[^4]: An dieser Stelle sei allgemein auf die Schwierigkeiten automatisierter Textanalysen von E-Mails hingewiesen, da der Inhalt einer E-Mail häufig die vorangegangenen E-Mails als Zitate ebenfalls enthält, was zu einer "künstlichen" Vergrößerung der Textmenge führt, die wiederum Einfluss auf die Auswertung hat.

[^5]: Dies zeigt sich auch in den am häufigsten vorkommenden Wörtern, wozu neben "KI" und "ChatGPT" auch "Studierende", "Seminararbeit" und "Text" gehören.