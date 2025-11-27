import nbformat
from pathlib import Path

def clean_notebook(path: Path):
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    meta = nb.get("metadata", {})
    if "widgets" in meta:
        print(f"Removing widgets metadata in {path}")
        meta.pop("widgets", None)
        nb["metadata"] = meta
        nbformat.write(nb, path)

def main():
    root = Path(".")
    for ipynb in root.rglob("*.ipynb"):
        clean_notebook(ipynb)

if __name__ == "__main__":
    main()
