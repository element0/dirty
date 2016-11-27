# franz

`franz.cgi` recursively expands a directory tree into HTML.

## dependencies ##

/bin/bash with "=~" regex functionality.  tested with 4.3.30 on Debian.


## what it does ##

Say you structure your content like so:

    fruit_of_the_month/
      apples.html
      bannanas.html
      goji.html
    
if you're using jQuery, put this in your pipe and smoke it:

    $.get("franz.cgi?fruit_of_the_month", your_update_function );
    
And this HTML will be cranked into `your_update_function()`:

    <dir class="franz-list" id="fruit_of_the_month">
      <dir class="franz-list-item" id="fruit_of_the_month/apples.html">
          wild, raw, unfiltered contents of the 'apples.html'
      </dir>
      <dir class="franz-list-item" id="fruit_of_the_month/bananas.html">
          wild, raw, unfiltered contents of the 'bananas.html'
      </dir>
      <dir class="franz-list-item" id="fruit_of_the_month/goji.html">
          it's party time.
      </dir>
    </dir>
 

## Installation ##

It's currently written in bash (oh so sexy) and it needs to be installed relative to the webpage like this:

    sitedir/
      index.html  <-- your file
      franz.cgi
      franzpage.cgi
      bin/
        dir-to-html.sh
      etc/
        franz.conf
      css/
        franz.css
      example/
      	...

`franzpage.cgi` is just to test it as a stand-alone html page.  you should move `franzpage.cgi` into `bin/` (or delete it) if you don't need it. 

`example/` should be deleted.  it's just there to test.  point your browser at:
	
	sitedir/franzpage.cgi?example

The CSS is just a starter skeleton.


## Reserved Metafiles ##

Metafiles start with `.` or `_` and are ignored except for `_header.html` which is inserted into the output before the list contents.


## Configuration ##

`etc/franz.conf`

    # CSS classes

    DIRCLASS="franz-list"
    DIRENTCLASS="franz-list-item"

    HEADERFILE="_header.html"
    HEADERCLASS="franz-list-header"

    DIRHEAD_FORE=""
    DIRHEAD_AFT=""

    DIRENT_HEAD_FORE=""
    DIRENT_HEAD_AFT=""

## Support Files ##

`bin/dir-to-html.sh` is where the html output is constructed.

