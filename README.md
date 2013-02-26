See you viewer
==============

"See you viewer" is a companion tool of [See you](https://github.com/mapio/see-you)
(and [Tristo Mietitore](https://github.com/mapio/tristo-mietitore)) that can be
used to assist in grading C practice and exam assignements.

It is a local web application based on the following awesome projects:

* [Bootstrap](http://twitter.github.com/bootstrap/),
* [jQuery](http://jquery.com/),
* [Mousetrap](http://craig.is/killing/mice), and
* [highlight.js](http://softwaremaniacs.org/soft/highlight/en/).


The results format
------------------

This viewer shows results sotored in a JSON file having a format described by
the following "BNF" grammar:

	RESULTS :=  { ( <UID>: { 'exercises': <EXERCISES>, 'signature': <SIGNAGURE> } )+ }

	EXERCISES := { ( <EXERCISE_NAME>: { 'sources': <SOURCES>, 'cases': <CASES> )+ }

	SIGNATURE := [ <UID>, <INFO>, <IP> ]  # this is what "Tristo mietitore" puts in SIGNATURE.tsv

	SOURCES := { ( <FILE_NAME>: CONTENT )* }

	CASES := { ( <CASE_NUM>: <CASE> )* }

	CASE := { # the format of this depends on "See you" xUnit approach (see testrunner.py)
				'name': <CASE_NAME>,
				'stdout': <STDOUT_CONTENT>,
				'stderr': <STDERR_CONTENT>,
				'failure': <FAILURE_MESSAGE>,
				'error': <ERROR_MESSAGE>,
				'type': <TYPE>
	}

	TYPE := 'compile' | 'execution' | 'diff' | 'ok'

and all non-terminals not detailed here are understood to be unicode strings.
