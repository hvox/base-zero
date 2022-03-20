alphabet = open("alphabet.bin").read()
rev = {c: i for i, c in enumerate(alphabet)}
encode = lambda data: "".join((alphabet[b] for b in data))
decode = lambda data: (rev[c] for c in data)
encode_code = lambda s: f'eval(bytes(map("{alphabet}".index, "{encode(s)}")))'

if __name__ == "__main__":
    import sys
    from pathlib import Path

    Path(sys.argv[2]).write_text(encode_code(Path(sys.argv[1]).read_bytes()))
