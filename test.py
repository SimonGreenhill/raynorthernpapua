NLANG, NCONCEPT, NFORM = 116, 63, 2499


def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


def test_counts(cldf_dataset):
    assert len(list(cldf_dataset["LanguageTable"])) == NLANG
    assert len(list(cldf_dataset["ParameterTable"])) == NCONCEPT
    assert len(list(cldf_dataset["FormTable"])) == NFORM


def test_special_glyph(cldf_dataset):
    forms = {(f["Language_ID"], f["Parameter_ID"], f["Form"]) for f in cldf_dataset["FormTable"]}
    assert ("Nupanob", "n2", "aδit") in forms  # Greek delta, not ð or đ


def test_segments(cldf_dataset):
    segs = {f["Form"]: " ".join(f["Segments"]) for f in cldf_dataset["FormTable"]}
    assert segs["ġalub"] == "ɣ a l u b"  # Ray: ġ = Dutch g in 'gij'
