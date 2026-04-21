# Privacy-Preserving Market Analytics for Informal Urban Economies in Africa

This repository contains the paper source, figures, and reproducibility notebook for a study of federated learning and scenario-based spatial planning for informal market analytics in African cities.

The work has two main components:

1. Federated market analytics for formalization prediction and food price forecasting.
2. Scenario-based planning for modular retail infrastructure and district-level unit allocation.

The machine-learning results are evaluated on observed datasets using leakage-controlled and temporal-split settings. The income and deployment analyses are scenario estimates under stated assumptions.

## Repository Structure

```text
.
|-- paper/
|   |-- FromHawking_DLIndaba2026.tex
|   |-- references.bib
|   |-- ijcai26.sty
|   |-- named.bst
|   `-- figures/
|       |-- federated_results.png
|       |-- comparative_benchmark.png
|       |-- economic_impact.png
|       `-- spatial_optimization.png
|-- notebooks/
|   `-- Model.ipynb
|-- data/
|   `-- README.md
|-- requirements.txt
`-- README.md
```

## Setup

Create a Python environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Data

Raw datasets are not stored in this repository. To rerun the notebook, place the required files in `data/` using the filenames listed in `data/README.md`.

The main external datasets are:

- Rwanda Establishment Census 2023.
- World Bank Enterprise Survey, Rwanda 2023.
- WFP food price and market data for Rwanda and Uganda.
- WorldPop population data.
- OpenStreetMap market and road data.
- FinScope digital readiness indicators.

## Running The Notebook

Start Jupyter:

```bash
jupyter notebook notebooks/Model.ipynb
```

Run the notebook from top to bottom after placing the required data files in `data/`.

The notebook produces:

- Leakage-controlled formalization prediction results.
- Centralized and federated formalization baselines.
- Price forecasting baselines and federated comparisons.
- Economic sensitivity analysis for foot-traffic assumptions.
- Figure files used in the paper.

## Building The Paper

Compile the LaTeX source from the `paper/` directory:

```bash
cd paper
pdflatex -interaction=nonstopmode FromHawking_DLIndaba2026.tex
bibtex FromHawking_DLIndaba2026
pdflatex -interaction=nonstopmode FromHawking_DLIndaba2026.tex
pdflatex -interaction=nonstopmode FromHawking_DLIndaba2026.tex
```

The generated PDF will appear in `paper/`.

## Main Results Reported In The Paper

- Formalization prediction is reported after removing registration-status variables and direct proxies.
- Price forecasting is evaluated with temporal held-out splits.
- Economic gains are presented as scenario estimates, not field-validated causal effects.
- Spatial allocation results are model-based planning outputs for a 100-unit pilot scenario.

## Reproducibility Notes

- Keep raw third-party datasets out of version control unless their license permits redistribution.
- Keep notebook outputs cleared before committing if they contain local paths or machine-specific state.
- Rebuild the paper after updating figures or tables.

