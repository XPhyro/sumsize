OUT_DIR := $(shell if test "`whoami`" = "root";\
	then\
		printf "%s\n" "/usr/local/bin";\
	else\
		printf "%s\n" "${HOME}/.local/bin";\
	fi)

install:
	cp -f main.py "$(OUT_DIR)/sumsize"

uninstall:
	rm -f "$(OUT_DIR)/sumsize"

.PHONY: install uninstall
