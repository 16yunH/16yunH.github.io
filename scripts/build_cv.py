#!/usr/bin/env python3
"""Compile the editable LaTeX CVs using Tectonic or XeLaTeX.

python3 scripts/build_cv.py             # build both into output/pdf/
python3 scripts/build_cv.py --sync      # also update website PDFs in data/
python3 scripts/build_cv.py --lang zh   # build only the Chinese CV
"""
from pathlib import Path
import argparse
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'cv'


def compile_cv(engine, language, output):
    name = f'CV_{language}'
    executable = shutil.which(engine)
    if not executable:
        raise RuntimeError(f'{engine} is not installed or is missing from PATH.')
    if engine == 'tectonic':
        command = [executable, '--keep-logs', '--outdir', str(output), f'{name}.tex']
    elif engine == 'latexmk':
        command = [executable, '-xelatex', '-interaction=nonstopmode', '-halt-on-error',
                   f'-outdir={output}', f'{name}.tex']
    else:
        command = [executable, '-interaction=nonstopmode', '-halt-on-error',
                   f'-output-directory={output}', f'{name}.tex']
    # Remove only this generated output, so a failed build cannot pass as current.
    pdf = output / f'{name}.pdf'
    pdf.unlink(missing_ok=True)
    for _ in range(2 if engine == 'xelatex' else 1):
        subprocess.run(command, cwd=SOURCE, check=True)
    if not pdf.is_file():
        raise RuntimeError(f'Compiler did not produce {pdf}')
    log = (output / f'{name}.log').read_text(errors='replace')
    defects = [line for line in log.splitlines()
               if 'Overfull \\hbox' in line or 'Overfull \\vbox' in line or 'Missing character:' in line]
    if defects:
        raise RuntimeError(f'{name}: fix layout/font errors before syncing:\n' + '\n'.join(defects))
    return pdf


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--lang', choices=['en', 'zh', 'all'], default='all')
    parser.add_argument('--engine', choices=['auto', 'tectonic', 'latexmk', 'xelatex'], default='auto')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'output/pdf')
    parser.add_argument('--sync', action='store_true', help='Copy successful builds to website data/. Does not publish.')
    parser.add_argument('--copy-to', type=Path, help='Also copy successful builds to an explicit directory, e.g. a personal CV folder.')
    args = parser.parse_args()
    engine = args.engine
    if engine == 'auto':
        engine = next((e for e in ['tectonic', 'latexmk', 'xelatex'] if shutil.which(e)), None)
        if engine is None:
            parser.error('Install Tectonic, or a TeX distribution providing XeLaTeX, then retry.')
    output = args.output_dir.expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    languages = ['en', 'zh'] if args.lang == 'all' else [args.lang]
    try:
        # Build every requested language before replacing any website PDF.
        pdfs = [compile_cv(engine, language, output) for language in languages]
        destinations = ([ROOT / 'data'] if args.sync else [])
        if args.copy_to:
            destinations.append(args.copy_to.expanduser().resolve())
        for destination in destinations:
            destination.mkdir(parents=True, exist_ok=True)
            for pdf in pdfs:
                target = destination / pdf.name
                if pdf.resolve() != target.resolve():
                    shutil.copy2(pdf, target)
                print(f'Synced: {target}')
        for pdf in pdfs:
            print(f'Built: {pdf}')
    except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
        print(f'CV build failed: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
