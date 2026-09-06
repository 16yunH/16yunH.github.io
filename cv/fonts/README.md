# Bundled Chinese fonts

Noto Sans SC, SIL Open Font License 1.1; see `OFL.txt` and the copyright/name
records embedded in each font.

Source: [Noto CJK upstream](https://github.com/notofonts/noto-cjk),
[`Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf`](https://github.com/notofonts/noto-cjk/blob/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf).
Downloaded 2026-09-06; source SHA-256:
`d68bafcb48a2707749396aa12bbbd833cb70401f3a9a689fd2902c7e0d295964`.

The bundled files are static TrueType instances at `wght=400` (Regular) and
`wght=700` (Bold), generated using fontTools 4.64.0
`instantiateVariableFont(font, {"wght": weight}, inplace=True, updateFontNames=True)`.
Both retain the source's full 30,890-code-point character map; they are not
subsets of the current CV text, so future edits can use additional characters.
fontTools is only needed to regenerate these font assets, not to build the CVs.

Static TTF files are used because the first local Tectonic 0.16.9 test with
Fandol CFF/OTF fonts compiled but failed Chinese rendering and text extraction.
