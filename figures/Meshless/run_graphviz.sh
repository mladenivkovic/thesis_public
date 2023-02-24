#!/bin/bash

# basename=tasks_hydro_zeroth_order
# basename=tasks_hydro_first_order
# basename=tasks_hydro_second_order
# basename=tasks_hydro_nompi
basename=tasks_hydro_only

dot -Tpdf $basename.dot > $basename.pdf

okular $basename.pdf

