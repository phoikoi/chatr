# chatr

## A testbed for learning Django channels + websockets

* Initial version 2017-04-06, PWH
* Added MIT license, 2017-04-07

### Notes

* This project uses `/home/pi` in various places (mostly in the `conf`
directory's files, for `supervisor` and `nginx`) because I'm running
this project on a Raspberry Pi.  You'll probably want to adjust this.
* You'll need to figure out how to secure the connections with TLS
if you're actually using a variant of this on the actual internet. I'll
probably add this in at some future point too.
* Because I'm not using this on the actual internet (yet), I am not
particularly doing things in a completely secure manner.  You need to
pay attention to how to do things properly if you use it out in the wild.
Have fun!

