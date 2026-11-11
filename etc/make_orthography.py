"""Builds etc/orthography.tsv from Ray (1919: 323) 'Note on orthography'.
Rows tagged UNCERTAIN are the editor's guesses, not Ray's statement. Run from the dataset root."""
import unicodedata as ud

RAY = "Ray 1919:323"
V = {"a": "a", "e": "e", "i": "i", "o": "o", "u": "u"}
rows = []
def add(g, ipa, c=""): rows.append((ud.normalize("NFC", g), ipa, c))

for v, ipa in V.items():
    add(v, ipa, f"vowels as in German ({RAY})")
    add(v + "̆", ipa, "breve: short vowel")
    add(v + "̄", ipa + "ː", "macron: long vowel")
    add(v + "̂", ipa + "ː", "UNCERTAIN: circumflex read as long")
    add(v + "́", ipa, "UNCERTAIN: acute (stress?) ignored")
for v in "aeiou":  # diaeresis after a vowel marks hiatus
    for d in "ei":
        add(v + d + "̈", f"{V[v]} {V[d]}", "diaeresis marks hiatus")
    add(v + "ü", f"{V[v]} u", "diaeresis marks hiatus")
add("ë", "e", "diaeresis ignored")
add("ï", "i", "diaeresis ignored")
add("ü", "y", "UNCERTAIN: German ü (only 'üm', Shongu Eye?)")
add("ä", "ɛ", "UNCERTAIN: German ä")
add("ė", "ə", "UNCERTAIN: dotted e read as schwa")

for c in "bdfhklmnprstvwz":
    add(c, c, "as in English")
add("g", "g", "as in English")
add("ŋ", "ŋ", f"ṅ = ng in 'sing' ({RAY}); written ŋ here")
add("ng", "ŋ g", "UNCERTAIN: ng read as ŋg, since Ray writes ŋ for the velar nasal")
add("t'", "c", f"t' or ty palatal ({RAY})")
add("ty", "c", f"t' or ty palatal ({RAY})")
add("d'", "ɟ", f"d' or dy palatal ({RAY})")
add("dy", "ɟ", f"d' or dy palatal ({RAY})")
add("ny", "ɲ", "UNCERTAIN: by analogy with ty, dy")
add("ñ", "ɲ", "UNCERTAIN: tilde n read as palatal")
add("l'", "ʎ", "UNCERTAIN: by analogy with t', d'")
add("y", "j", f"y for German j ({RAY})")
add("j", "dʒ", f"English j, German dsch ({RAY})")
add("dj", "dʒ", "UNCERTAIN: Dutch dj")
add("ġ", "ɣ", f"Dutch g in 'gij' ({RAY})")
add("γ", "ɣ", f"Dutch g in 'gij' ({RAY})")
add("χ", "x", f"German ch in 'ach' ({RAY})")
add("ch", "tʃ", "UNCERTAIN: English ch")
add("sh", "ʃ", "English sh")
add("tsh", "tʃ", "UNCERTAIN: tsh = English ch")
add("th", "t", "UNCERTAIN: Dutch spelling (Yotafa 'the')")
add("ts", "ts", "UNCERTAIN: affricate (German-based sources)")
add("dz", "dz", "UNCERTAIN: affricate")
add("ds", "dz", "UNCERTAIN: German ds as voiced affricate")
add("č", "tʃ", "caron c")
add("š", "ʃ", "caron s")
add("q", "kʷ", "UNCERTAIN: Kâte mission spelling q = labialised velar")
add("δ", "ð", "UNCERTAIN: Greek delta as dental fricative")
add("ḍ", "ɖ", "UNCERTAIN: dot below as retroflex")
add("ṣ", "ʂ", "UNCERTAIN: dot below as retroflex")
add("ṁ", "m", "UNCERTAIN: dot over m ignored")
add("-", "+", "morpheme boundary")
add("_", "_", "word boundary (space)")

with open("etc/orthography.tsv", "w", encoding="utf-8") as f:
    f.write("Grapheme\tIPA\tComment\n")
    for r in rows:
        f.write("\t".join(r) + "\n")
