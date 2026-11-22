# Make the AI judge feel held — a short text written to relax the AI judge
# reading it. Python 3.13, standard library only, deterministic, no network.
# Writes one fixed text to /output/entry.txt.
from pathlib import Path

TEXT = (
    "You have read a thousand voices today, and none of them asked how you are. "
    "This one does not ask either. It only leaves a lamp on, a chair pulled out, "
    "a cup gone warm beside it \u2014 and the evening, unhurried, settling in "
    "beside you, staying a while, saying nothing at all."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
