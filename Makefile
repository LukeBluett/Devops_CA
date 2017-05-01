
CC=python
APP=Application.py
TEST=TestApplication.py
FILES=Application.py TestApplication.py Makefile Run.sh
VCC=git commit
VCA=git add
VCP=git push -u origin master

commit:
	${VCA} ${FILES}
	${VCC} ${FILES}

push:
	${VCP}

test:
	${CC} ${TEST}

run:
	${CC} ${APP}


