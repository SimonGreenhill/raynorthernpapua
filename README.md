# CLDF dataset derived from Ray's "The Languages of Northern Papua" from 1919

## How to cite

If you use these data please cite
- the original source
  > Ray, Sidney H. 1919. The Languages of Northern Papua. The Journal of the Royal Anthropological Institute of Great Britain and Ireland 49: 317-341.
- the derived dataset using the DOI of the [particular released version](../../releases/) you were using

## Description


This dataset is licensed under a CC-BY-4.0 license

Available online at https://github.com/SimonGreenhill/raynorthernpapua

## Notes

# Notes

Source: Ray, Sidney H. 1919. The Languages of Northern Papua. JRAI 49: 317–341. doi:10.2307/2843447.

## Data
- `raw/*.tsv` is one file per printed table (`Page, Language, Gloss, Value, Comment`), transcribed by eye from the page scans.
- Pages 323–326b: pronouns, possessive suffixes and words, verb subject markers.
- Pages 327–331: numerals 1–10 and 20.
- Pages 332–339: vocabulary of 20 concepts.
- `Page` on each form gives the printed page.
- Empty cells ("—" in print) are not in the FormTable.

## Forms
- `Value` keeps Ray's orthography:
  - ŋ stands for his dotted n.
  - Breve and macron are kept.
  - č, š, ž, δ, χ, γ, ġ and dot-below ḍ, ṣ are as printed.
- Cells with ", " are split into synonyms.
- Parenthesised optional material, e.g. `tĭlīnă(k)`, is dropped from `Form` and kept in `Value`.
- Segments come from `etc/orthography.tsv`, which `etc/make_orthography.py` generates from Ray's "Note on orthography" (p. 323):
  - ŋ = ng in "sing".
  - t'/ty → c, d'/dy → ɟ.
  - y → j, j → dʒ.
  - ġ/γ → ɣ, χ → x.
  - Vowels as in German: breve → short, macron → ː.
- Rows tagged UNCERTAIN are editorial guesses:
  - ng → ŋg; ny/ñ → ɲ; l' → ʎ.
  - q → kʷ, from the Kâte mission spelling.
  - δ → ð; ḍ/ṣ → ɖ/ʂ.
  - ts/dz/ds as affricates; ch/tsh → tʃ.
  - Circumflex → long; acute ignored; ä → ɛ; ė → ə; ü → y except in hiatus.
- Ray's ṙ (palatal r) does not occur in the tables.

## Concepts
- Concepticon v3.4.0:
  - Areca Nut → BETEL NUT (2369).
  - "Foot, Leg" → FOOT OR LEG.
  - "Hand, Arm" → ARM OR HAND.
- Pronouns map to I, THOU, HE OR SHE, WE (INCLUSIVE/EXCLUSIVE), YOU, THEY and the dual sets.
- Possessive words map to MY, YOUR (SINGULAR), HIS OR HER.
- Unmapped: trial pronouns, possessive suffixes and verb subject markers. Concepticon has no sets for these.

## Languages
- `Name` is Ray's spelling as printed in the tables, after merging three variants (Bokajim→Bogajim, Maragum→Maragam, Wogeo→Wokeo).
- `Identification` and `Glottocode` are the editor's identification (Glottolog v5.3; see Glottolog reference 91072).
- Weak identifications:
  - Kopoam → Olo (two words)
  - Waria River → Zia/Binanderean (four words)
  - Morobe → Suena (one word)
  - Mangut → Angoram (one word)
  - Waso → Lemio (two words, via TransNewGuinea.org)
- Unidentified: Mabu, Mangut (if Angoram is rejected), Waso (if Lemio is rejected), and the unnumbered "K. Augusta River" (pp. 326, 338–339). The three numbered K. Augusta River lists on p. 330 are identified separately.

## Catalogs
Glottolog v5.3, Concepticon v3.4.0, CLTS v2.3.0.



## Statistics


[![CLDF validation](https://github.com/SimonGreenhill/raynorthernpapua/workflows/CLDF-validation/badge.svg)](https://github.com/SimonGreenhill/raynorthernpapua/actions?query=workflow%3ACLDF-validation)
![Glottolog: 98%](etc/badge_languages.svg)
![Concepticon: 96%](etc/badge_concepts.svg)
![Source: 100%](etc/badge_sources.svg)
![BIPA: 100%](etc/badge_bipa.svg)
![CLTS SoundClass: 100%](etc/badge_sc.svg)

- **Varieties:** 116 (linked to 59 different Glottocodes)
- **Concepts:** 63 (linked to 48 different Concepticon concept sets)
- **Lexemes:** 2,499
- **Sources:** 1
- **Synonymy:** 1.12
- **Invalid lexemes:** 0
- **Tokens:** 11,506
- **Segments:** 48 (0 BIPA errors, 0 CLTS sound class errors, 48 CLTS modified)
- **Inventory size (avg):** 17.16

## Possible Improvements:

- Languages missing glottocodes: 4/116 (3.45%%)


# Contributors

Name | GitHub user | Description | Role
--- | --- | --- | ---
Simon J. Greenhill | @SimonGreenhill | data extraction, language identification | Editor, DataEntry




## CLDF Datasets

The following CLDF datasets are available in [cldf](cldf):

- CLDF [Wordlist](https://github.com/cldf/cldf/tree/master/modules/Wordlist) at [cldf/cldf-metadata.json](cldf/cldf-metadata.json)