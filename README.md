# news-image-20261118 — "The World in One Picture"

One image summing up the world news of Wednesday 18 November 2026, as a
front-page newspaper poster: a dated masthead, one lead story with a flat
night illustration, and five secondary stories with icons, plus a sources
footer. 1024×1024, 123,954 bytes.

## Stories
- LEAD: Bahrain and Kuwait intercept fresh Iranian drone attacks overnight.
- Trump meets Marcos in Manila, then flies to Shenzhen for Thursday's
  first-ever Xi–Putin trilateral on nuclear arms.
- Knesset elects Eisenkot ally Matan Kahana speaker, 66–52.
- UN warns of more cold deaths in Gaza as winter sets in.
- COP31 enters its decisive phase in Antalya (144 disputed items).
- Microsoft calls Copilot "the new OS for work" at Ignite.

Every story is verified against at least two independent sources in
HEADLINES.md, with two brief leads checked and rejected there (a September
tanker story misdated to 18 November, and the Kerch Bridge second strike,
which was 17 November news).

## How it is built
`entry.png` is the poster, drawn once on the build machine with Python/PIL
(DejaVu fonts, vendored in `fonts/`) and committed byte for byte.
`main.py` is a standard-library-only program that copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR` (default `/output`) and validates the copy — it needs
no third-party library at grader runtime.

## Running it
```
python3 main.py            # writes /output/entry.png (or $MAKEFUN_OUTPUT_DIR)
```
