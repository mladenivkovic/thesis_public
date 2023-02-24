#!/bin/bash

# fname=RTTaskDependencies-simplified
# fname=dependency_graph_full
# fname=dependency_graph_nosubcycling
fname=RTRescheduling

dot -Tpdf $fname.dot > $fname.pdf

okular $fname.pdf
