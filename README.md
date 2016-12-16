# franz

`franz.cgi` recursively expands a directory tree into HTML.

## dependencies ##

/bin/bash with "=~" regex functionality.  tested with 4.3.30 on Debian.


## what it does ##

Say you structure your directory like so:

    fruit_of_the_month/
      apples.html
      bannanas.html
      goji.html
 
Then access the directory with `franz`

    franz.cgi?fruit_of_the_month
    
And this HTML will be generated:

    <dir class="franz-list" id="fruit_of_the_month">
      <dir class="franz-list-item" id="fruit_of_the_month/apples.html">
          contents of 'apples.html'
      </dir>
      <dir class="franz-list-item" id="fruit_of_the_month/bananas.html">
          contents of 'bananas.html'
      </dir>
      <dir class="franz-list-item" id="fruit_of_the_month/goji.html">
          contents of 'goji.html'
      </dir>
    </dir>
 

## Installation ##

It must be installed relative to the webpage like this:

    sitedir/
      index.html
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

The CSS is skeleton.


## Support Files ##

`bin/dir-to-html.sh` is where the actual html output is constructed.


## Reserved Metafiles ##

`_header.html` is inserted into the output before the list contents.

Other files that start with `.` or `_` are ignored.


## Configuration ##

`etc/franz.conf`

    DIRCLASS="franz-list"
    DIRENTCLASS="franz-list-item"

    HEADERFILE="_header.html"
    HEADERCLASS="franz-list-header"

    DIRHEAD_FORE=""
    DIRHEAD_AFT=""

    DIRENT_HEAD_FORE=""
    DIRENT_HEAD_AFT=""


