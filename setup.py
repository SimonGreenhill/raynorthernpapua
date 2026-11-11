from setuptools import setup
import json

with open("metadata.json") as fp:
    metadata = json.load(fp)

setup(
    name="lexibank_raynorthernpapua",
    description=metadata["title"],
    license=metadata.get("license", ""),
    py_modules=["lexibank_raynorthernpapua"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"lexibank.dataset": ["raynorthernpapua=lexibank_raynorthernpapua:Dataset"]},
    install_requires=["pylexibank>=4.0"],
    extras_require={"test": ["pytest-cldf"]},
)
