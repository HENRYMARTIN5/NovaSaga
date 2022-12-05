# Contribution Guidelines

### Imports should be condensed onto the same line. (eg `from assets.util import logging, levelutil`)

### Indents should be tabs. No spaces, just tabs.

### There should be newlines before every `if` and `for` block as well as between blocks of repetitive code. 

### When printing any information, use the included library (`assets.util.logging`)

### Main.py is a basic entry point. Don't put any content/rendering in it.

### If requiring an external library, be sure to specify the exact version in `requirements.txt`. (`pip freeze` can help you get the exact versions of installed packages)

### When creating or updating sprites, ensure that you use the palette defined in `assets/sprites/player/palette.png`

### All audio files should be in `.wav` format (uncompressed)

That's it. Just write good code and you'll be fine.
