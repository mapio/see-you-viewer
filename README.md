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

This viewer shows results stored in a JSON file having a format described by
the following "BNF" grammar:

	RESULTS :=  [ ( RESULT )+ ]

	RESULT := { # the first three fields are the "signature" collected by "Tristo mietitore"
		'uid': <UID>,
		'info': <INFO>,
		'ip': <EXTRA>,
		'exercises': [ ( <EXERCISE> )+ ]
	}

	EXERCISE := {
		'name', <EXERCISE_NAME>,
		'sources': [ ( <SOURCE> )+ ],
		'cases': [ ( <CASE> )* ]
	}

	SOURCE := {
		'name': <SOURCE_NAME>,
		'content': <CONTENT>
	}

	CASE := { # the format of this depends on "See you" xUnit approach (see testrunner.py)
				'name': <CASE_NAME>,
				'stdout': <STDOUT_CONTENT>,
				'stderr': <STDERR_CONTENT>,
				'failure': <FAILURE_MESSAGE>,
				'error': <ERROR_MESSAGE>,
				'type': <TYPE>
	}

	TYPE := 'compile' | 'execution' | 'diff' | 'ok'

and all non-terminals not detailed here are understood to be unicode strings;
UID must be unique and, moreover, all the RESULT exercises must share the same
set of EXERCISE_NAME keys (but the same isn't required for SOURCE, or CASE
names).
