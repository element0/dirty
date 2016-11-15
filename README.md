# dirtydir

`dirtydir.cgi` recursively expands a directory tree into HTML.

## dependencies ##

/bin/bash with "=~" regex functionality.  tested with 4.3.30 on Debian.


## what it does ##

Say you structure your content like so:

    fruit_of_the_month/
      apples.html
      bannanas.html
      cocain.html
    
if you're using jQuery put this in your pipe and smoke it:

    $.get("dirtydir.cgi?fruit_of_the_month", your_update_function );
    
And this HTML will be cranked into `your_update_function()`:

    <dir class="dirtydir" id="fruit_of_the_month">
      <dir class="dirtydirent" id="fruit_of_the_month/apples.html">
          wild, raw, unfiltered contents of the 'apples.html'
      </dir>
      <dir class="dirtydirent" id="fruit_of_the_month/bananas.html">
          wild, raw, unfiltered contents of the 'bananas.html'
      </dir>
      <dir class="dirtydirent" id="fruit_of_the_month/cocain.html">
          it's party time.
      </dir>
    </dir>
 
(And if you're wondering: No. I've never even touched the stuff -- and I don't plan on trying.  I'm just in a Slim Shady kind'a mood, man.)

## Installation ##

It's currently written in bash (oooh, oh so sexy.)  and it needs to be installed relative to the webpage like this:

    sitedir/
      index.html  <-- your file
      dirtydir.cgi
      cgi/
        dir-to-html.sh
        dirtywrap.cgi
      etc/
        dirtydir.conf
      css/
        dirtydir.css

## Configuration ##

`etc/dirtydir.conf`

    DIRCLASS="dirtydir"
    DIRENTCLASS="dirtydirent"

`cgi/dirtydir.sh` is where the html divs are constructed.  Pretty self explainitory.  You can hack it.
