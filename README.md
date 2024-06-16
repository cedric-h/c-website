# using the C preprocessor as an HTML templating engine

example:

## `header.html`
```html
    <head>
        <meta charset="utf-8" />
        <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📜</text></svg>">
        <title>ced.quest ⚔️ </title>
        <style>
        </style>
    </head>
```

## `index.template.html`
```html
<!DOCTYPE html>
<html lang="en">
#include "header.html"

    <body>
        <p> hi ben! </p>
    </body>
</html>
```

command:

`cpp -P index.template.html index.html`

note: `cpp` is "C Preprocessor," comes with GCC installs.

-P inhibits the output of linemarkers, which may be useful for debugging complicated macros. (please do not make complicated macros)

## `index.html` (output)
```html
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="utf-8" />
        <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📜</text></svg>">
        <title>ced.quest ⚔️ </title>
        <style>
        </style>
    </head>


    <body>
        <p> hi ben! </p>
    </body>
</html>

```
