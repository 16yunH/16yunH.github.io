# Website and CV maintenance

- Personal-information changes must be synchronized across `index.html`,
  `cv/CV_zh.tex`, and `cv/CV_en.tex`. This includes research, education,
  publications, internships, projects, awards, and dates.
- Maintain shared contact details and the content review date in
  `cv/profile.tex`, and publication metadata in `cv/publication.tex`.
- After editing CV content, rebuild both languages with
  `python3 scripts/build_cv.py`, inspect every PDF page and extracted text,
  then sync both tracked `data/CV_*.pdf` files using `--sync`, which also versions
  the homepage links by PDF content hash. Do not deliver a source-only
  update that leaves website downloads stale.
- Keep ongoing research distinct from demonstrated results. Describe the
  user's contribution without presenting team results as personal work.
- Before a user-authorized release, check the staged files and local links.
  After pushing, verify the Pages deployment and follow the exact live homepage
  CV links to check PDF bytes; do not add a test-only cache-busting query.
