# dirtydir

`dirtydir.cgi` recursively expands a directory tree into HTML.

## dependencies ##

/bin/bash with "=~" regex functionality.  tested with 4.3.30 on Debian.


## what it does ##

Say you structure your content like so:

    fruit_of_the_month/
      apples.html
      bannanas.html
      goji.html
    
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
      <dir class="dirtydirent" id="fruit_of_the_month/goji.html">
          it's party time.
      </dir>
    </dir>
 

## Installation ##

It's currently written in bash (oooh, oh so sexy.)  and it needs to be installed relative to the webpage like this:

    sitedir/
      index.html  <-- your file
      dirty.cgi
      dirtywebpg.cgi
      bin/
        dir-to-html.sh
      etc/
        dirty.conf
      css/
        dirty.css
      example/
      	...

`dirtydirpage.cgi` is just to test it as a stand-alone html page.  you should move `dirtydirpage.cgi` into `bin/` if you don't need it. 

`example/` should be deleted.  it's just there to test.  point your browser at:
	
	sitedir/dirtywebpg.cgi?example

The CSS is bare bones.


## Reserved Metafiles ##

Metafiles start with `.` or `_` and are at present all ignnored except for `_header.html` which is inserted first into the output before a directory's contents.


## Configuration ##

`etc/dirty.conf`

    DIRCLASS="dirtydir"
    DIRENTCLASS="dirtydirent"

    HEADERCLASS="dirtydir-header"
    HEADERFILE="_header.html"

Also `cgi/dirty.sh` is where the html divs are constructed.  Pretty self explainitory.
