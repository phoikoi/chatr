# chatr

## A testbed for learning Django channels + websockets

* Initial version 2017-04-06, PWH
* Added MIT license, 2017-04-07

### Notes

* **This project uses Python 3 (specifically, 3.6+)** It will not
work with Python 2.
* To be clear, this project isn't meant as a tutorial for other
people to learn django-channels and websockets.  *I'm* using it
to learn these things myself.  If you want to use it to learn too,
hey, that's great.  But I make no guarantees of it being proper,
correct, or indeed functional or fit for any particular purpose.
Your mileage may vary, offer void where prohibited by law,
*para su seguridad, permanezca sentado con las manos, brazos, pies,
y piernas dentro el vehiculo*, etc., etc.
* This project uses `/home/pi` in various places (mostly in the `conf`
directory's files, for `supervisor` and `nginx`) because I'm running
this project on a Raspberry Pi.  You'll probably want to adjust this.
* You'll need to figure out how to secure the connections with TLS
if you're actually using a variant of this on the actual internet. I'll
probably add this in at some future point too.
* Because I'm not using this on the actual internet (yet), I am not
particularly doing things in a completely secure manner.  You need to
pay attention to how to do things properly if you use it out in the wild.
* You might notice that I have the `static`, `media`, and `logs`
directories in the git repo, but also listed in the `.gitignore` file.
This is because their contents are site-specific and so shouldn't be
in the repo (thus the entries in `.gitignore`) but they do need to exist
so that `nginx` and `supervisor` can access things where they expect them
to be. I do this by adding a hidden empty file in each directory called
`.gitkeep`, and these are added to the repo.  Anything else in the directory
is ignored.  This works because git only adds *files* to its repos--
it doesn't add *directories*.
* I am using my own method of managing Django's `settings` module, using
my own `config` module, which reads the values from INI-style files.  This
works for me, and keeps things nice and tidy.  You can probably grok how
it works by reading the `settings.py` file and the `site.ini_example` file.
Feel free to use the `config` module in your own projects.

