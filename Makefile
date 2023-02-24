# make the pdf.

SUBDIRS = appendix head main main/ACACIA main/FV main/Meshless main/RHD tail
TEXFILES = $(wildcard *.tex $(foreach fd, $(SUBDIRS), $(fd)/*.tex))

main_file = main

default: ${main_file}.pdf

${main_file}.pdf: ${main_file}.tex ${TEXFILES}
	pdflatex ${main_file}.tex
	bibtex ${main_file}
	pdflatex ${main_file}.tex
	pdflatex ${main_file}.tex

clean:
	rm -f ${main_file}.pdf *.aux *.log *.out *.dvi *.bbl *.blg *.toc *.gz *.lof *.lot

.PHONY: clean
