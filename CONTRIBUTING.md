# Contributing

Thanks for helping! Seen a mistake or an unclear card?
[Open an issue](https://github.com/jupsh/anki-ap-physics-1/issues). Pull requests are welcome
too.

## Making changes

Cards live in `ap_physics_1/content/u1.py` … `u8.py`, one file per unit, grouped into the course
framework's topics. `B(front, back, ...)` makes a basic card and `C(text, ...)` a cloze; see
`ap_physics_1/cards.py`. Diagrams are drawn in code in `ap_physics_1/diagrams.py`.

- Math uses MathJax delimiters, `\( \)` inline and `\[ \]` for display. Write `<` as `\lt` in math
  or `&lt;` in text, since fields are HTML.
- Build with `uv run python ap_physics_1/build.py --html out.html` and check your cards in
  `out.html`. The build stops on common mistakes, such as unbalanced math delimiters or a cloze
  with no deletions. Every push and pull request is also built on GitHub.
- Note GUIDs come from the section and the card text, so editing a card's text makes it a new
  note on re-import. Keep edits to existing cards for real corrections.

## Versioning and releases

Releases are numbered `x.y`:

- `y` goes up for content changes: new, corrected or removed cards, or new diagrams.
- `x` goes up when users would lose a lot of progress on upgrade, for example when many cards are
  reworded.

To release:

1. Update the counts in `README.md` if they changed, and commit.
1. Tag the commit and push the tag, e.g. `git tag v1.1 && git push origin v1.1`.
1. GitHub builds the deck and creates a **draft release** with the `.apkg` attached.
1. Write the release notes from a user's point of view (what changed, by unit), then publish
   the release.
1. Update the deck on [AnkiWeb](https://ankiweb.net/decks/): import the new `.apkg` into Anki,
   sync, then select _Actions_ > _Share_ on the deck, update the description if needed, tick the
   _Copyright_ box and click _Share_.
