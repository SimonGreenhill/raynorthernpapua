import csv
import dataclasses
from pathlib import Path
from typing import Optional

from pylexibank import Dataset as BaseDataset, FormSpec, Language as BaseLanguage, Lexeme as BaseLexeme


@dataclasses.dataclass
class Language(BaseLanguage):
    Identification: Optional[str] = None


@dataclasses.dataclass
class Lexeme(BaseLexeme):
    Page: Optional[str] = None


class Dataset(BaseDataset):
    dir = Path(__file__).parent
    id = "raynorthernpapua"
    language_class = Language
    lexeme_class = Lexeme

    # Cells list synonyms separated by ", " (e.g. "pelen, aun"); "(...)" holds optional material.
    form_spec = FormSpec(
        separators=",;", missing_data=("—", "-", "?"), strip_inside_brackets=True, replacements=[(" ", "_")])

    def cmd_download(self, args):
        pass

    def cmd_makecldf(self, args):
        args.writer.add_sources()
        languages = args.writer.add_languages(lookup_factory="Name")
        concepts = args.writer.add_concepts(id_factory=lambda c: c.id, lookup_factory="english")
        for path in sorted(self.raw_dir.glob("*.tsv")):
            with path.open(encoding="utf-8") as f:
                for row in csv.DictReader(filter(str.strip, f), delimiter="\t"):
                    if not row["Value"]:
                        continue
                    comment = row["Comment"].removeprefix("//").strip() or None
                    args.writer.add_forms_from_value(
                        Language_ID=languages[row["Language"]],
                        Parameter_ID=concepts[row["Gloss"]],
                        Value=row["Value"],
                        Comment=comment,
                        Page=row["Page"],
                        Source=["Ray1919"],
                    )
