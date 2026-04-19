# From Hawking to Intelligent Markets

This repository contains the LaTeX source, figures, and supporting materials for the research paper:

**From Hawking to Intelligent Markets: Federated Learning and Economic Inclusion in African Retail**

## Description
This project presents a comprehensive study on the application of federated learning to market formalization and economic inclusion in African retail, with a focus on Rwanda and Uganda. The paper includes:
- A federated learning pipeline for market prediction tasks
- Economic and spatial analysis of modular retail interventions
- Multi-country benchmarking and ablation studies
- All LaTeX source files, figures, and data used for reproducibility

## Repository Structure
- `FromHawking_DLIndaba2026.tex` — Main LaTeX manuscript
- `ijcai26.sty` — IJCAI-ECAI-26 conference style file
- `data/` — Figures and data used in the paper
- `.venv/` — (Optional) Python virtual environment for figure generation (not required for LaTeX build)

## How to Build
1. Ensure you have a LaTeX distribution installed (e.g., TeX Live, MiKTeX).
2. Compile the main manuscript:
   ```
   pdflatex FromHawking_DLIndaba2026.tex
   bibtex FromHawking_DLIndaba2026
   pdflatex FromHawking_DLIndaba2026.tex
   pdflatex FromHawking_DLIndaba2026.tex
   ```
3. The output PDF will be `FromHawking_DLIndaba2026.pdf`.

## Notes
- All figures are included as PNGs in the `data/` directory.
- The Python environment is only needed if you wish to regenerate figures (not required for building the paper).
- Please cite appropriately if using or building upon this work.

---

**Repository Title:** From Hawking to Intelligent Markets
**Description:** Federated learning, economic inclusion, and market formalization in African retail — LaTeX source, figures, and reproducibility materials for the 2026 IJCAI-ECAI submission.
