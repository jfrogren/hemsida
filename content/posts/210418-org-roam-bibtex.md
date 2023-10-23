---
title: "Org Roam BibTeX - det ultimata akademiska arbetsverktyget?"
date: 2021-04-18T14:35:25+02:00
draft: false
tags: ["Emacs", "Zettelkasten"]
---

Nu när man genom [Doom Emacs](https://archive.fo/6YEPi) inte längre behöver välja sidan mellan [Vim](https://www.vim.org/) och [Emacs](https://www.gnu.org/software/emacs/) känns det som om kampen snarare står mellan [Markdown](https://en.wikipedia.org/wiki/Markdown) och [Org-mode](https://en.wikipedia.org/wiki/Org-mode). Har hittills lutat åt Markdown i den kampen men i fredags hittade jag detta YouTube-klipp som fick mig att inse att Org-mode har vissa styrkor som Markdown inte riktigt rår på:

{{< youtube Wy9WvF5gWYg>}}

Det som [Org Roam BibTeX](https://github.com/org-roam/org-roam-bibtex) (ORB) möjliggör är det som jag har saknat i mitt akademiska arbetsflöde nämligen att på ett smidigt sätt integrera de anteckningarna man gör när man läser akademiska texter med de mer genomarbetade så kallade *zettels* man skapar för att inkludera i sin [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten). Och inte bara det utan framför allt ligger problemet i hur man sedan på ett smidigt sätt vid läsning av en ny text kan relatera dessa komprimerade tankekort till den text man för tillfället läser. Här tycker jag att Zaeph i videon verkligen lyckas.

Till Org-modes nackdel är dock skulle jag säga den i jämförelse med Markdown och Rmarkdown något klumpigare och estetiskt mindre tilltalande syntaxen, och även - anar jag - exporteringsmöjligheterna, men här vet jag emellertid lite för lite för att kunna uttala mig.

På den [här](https://archive.fo/PWvJm) sidan hittade jag också ett sätt att konvertera `.md` eller `.Rmd` till `.org`, nämligen genom att köra följande kommando i terminalen:

```find . -name \*.md -type f -exec pandoc  -f markdown -t org -o {}.org {} \;```

På detta sätt erhåller filerna en org-syntax som motsvarar markdown-syntaxen. Dock får de konverterade filerna ändelsen `.md.org` eller`.Rmd.org` istället för bara `.org`. Hur man kan ändra detta annat än manuellt har jag ännu inte kommit underfund med.

Sympatiskt nog finns det ett [diskussionsforum för Org Roam](https://archive.fo/DyfgT), där det finns många kunniga personer som kan bistå med hjälp när det gäller att sätta upp sitt eget system i Emacs. Från signaturen *cobblepot* hittade jag [detta inlägg](https://archive.fo/RHldi) som mycket väl beskriver den frustration man kan känna som ny Emacs-användare. Motsatt till vad som formuleras i tråden tycker jag ändå att Doom Emacs har varit en nödvändig tröskel för mig, men jag inser också att det är en genväg som stundtals straffar sig eftersom man har skaffat sig ett system som man bara begriper till en liten del. Att helt börja om från början med Vanilla Emacs ser jag dock inte som ett alternativ i dagsläget. 

Som jag tänker mig mitt eget arbetsflöde så kommer jag att den närmaste framtiden att hålla mig till Markdown åtminstone för det egna skrivandet, men fortsättning följer i jakten på det ultimata akademiska arbetsflödet. 
