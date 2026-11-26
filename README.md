# the-word-youd-delete-from-the-dictionary

[![make.fun · u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/museweilejing923/the-word-youd-delete-from-the-dictionary/rank.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/museweilejing923/the-word-youd-delete-from-the-dictionary/reward.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

The entry:

> moist

5 characters, limit 77.

English has plenty of ugly words, but this is the one people love to hate — the word that makes a room groan before the sentence around it even finishes. Ask a room full of people which word they would erase and this one comes up before anyone finishes the question — that instant flinch is the whole argument. No explanation is attached, because the word has to do the work alone. In a head-to-head vote the pick has to be a real word everyone recognises and an erasure everyone quietly agrees with. It is the rare word whose removal would improve every sentence it ever appeared in.

## Run

```sh
python3 main.py
```

## How it works

`main.py` runs one fixed word through a table of named checks and writes it to `/output/entry.txt`. The output is fully deterministic: no network, no randomness, no clock. The checks, in table order, are: one lowercase word with letters only, non-empty, at least two vowels, within the 77-character limit, contains letters, every character printable, exactly one word, no leading or trailing space, not digits only, and no double spaces or newlines. Each check is a small named function, and the table pairs it with the complaint printed when it fails — the first failure stops the run before anything is written.
