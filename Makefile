PREFIX := $(shell if test "`whoami`" = "root";\
	then\
		printf "%s\n" "/usr/local";\
	else\
		printf "%s\n" "${HOME}/.local";\
	fi)

OUT_DIR = $(PREFIX)/bin

sumsize:
	@echo "Run 'make install' to install or 'make uninstall' to uninstall."

install:
	cp -f main.py "$(OUT_DIR)/sumsize"

uninstall:
	rm -f "$(OUT_DIR)/sumsize"

.PHONY: install uninstall
