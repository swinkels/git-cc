# make this target from the root of the repo to run the unit tests
.PHONY: tests
tests:
	python -m unittest discover tests/

import-working-tree:
	cd git_cc ; dos2unix version.py ; chmod 644 version.py
	cd git_cc ; dos2unix __init__.py ; chmod 644 __init__.py
	cd git_cc ; dos2unix cache.py ; chmod 644 cache.py
	cd git_cc ; dos2unix checkin.py ; chmod 644 checkin.py
	cd git_cc ; dos2unix clearcase.py ; chmod 644 clearcase.py
	cd git_cc ; dos2unix common.py ; chmod 644 common.py
	cd git_cc ; dos2unix gitcc.py ; chmod 644 gitcc.py
	cd git_cc ; dos2unix init.py ; chmod 644 init.py
	cd git_cc ; dos2unix rebase.py ; chmod 644 rebase.py
	cd git_cc ; dos2unix reset.py ; chmod 644 reset.py
	cd git_cc ; dos2unix status.py ; chmod 644 status.py
	cd git_cc ; dos2unix sync.py ; chmod 644 sync.py
	cd git_cc ; dos2unix tag.py ; chmod 644 tag.py
	cd git_cc ; dos2unix update.py ; chmod 644 update.py
	cd git_cc ; dos2unix clearcase.py ; chmod 644 clearcase.py
