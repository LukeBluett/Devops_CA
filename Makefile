
CC=python
APP=Application.py
TEST=TestApplication.py
FILES=Application.py TestApplication.py Makefile Run.sh
VCC=git commit
VCA=git add

commit:
	${VCA} ${FILES}
	${VCC} ${FILES}

test:
	${CC} ${TEST}

run:
	${CC} ${APP}


