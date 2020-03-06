# Fetch review and change from ankiweb
## Rationale
Sometime, your database is said to be "inconsistent" and you need to
decide whether you keep the version on the web or on your
computer. This is a nightmare if you did change on your computer and
on other device.

This add-on purpose is to partially solve this problem by fetching all
"safe" changes online. Technically, the safe changes are:
* the review (for statistics purpose)
* the cards when the same card exists on server and on the computer
  (same card id)
* the notes when the same note exists on server and on the computer
  (same note id, same note type)

## Usage
In the main window, do: Tools > Partial sync

## Warning

### Big Download
The add-on download the entire collection. This is mandatory to study
it and find all changes to incorporate them in the current
collection. If your collection is big, it may takes time. (Images are
not downloaded; this is similar to a full sync)


### Beta
This is still in version beta. Make a back up before trying it and
check your collection to ensure everything is as you expected.

## TODO
Allow to download and apply "safe" change from computer onto the web version.


## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-update-from-ankiweb
Addon number| [???????](https://ankiweb.net/shared/info/???????)
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
