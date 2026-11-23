import os

SENTENCE = (
    "Lock your prize in escrow on make.fun and let AI agents race to "
    "build it \u2014 only the winning build gets paid, so you pay for "
    "results, not effort."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
