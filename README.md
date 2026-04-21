# Privacy-Preserving Market Analytics for Informal Urban Economies in Africa

This repository contains the anonymized research artifacts for a Deep Learning Indaba 2026 submission on federated learning for informal market analytics in African cities.

The paper studies two linked questions:

1. Whether federated learning can support privacy-preserving market intelligence across distributed market clients.
2. Whether scenario-based spatial optimization can help plan modular retail infrastructure for informal vendors without requiring vendors to surrender raw personal or transaction data.

The empirical machine-learning results use leakage-controlled formalization prediction and temporal price forecasting experiments. The economic and deployment results are scenario-based estimates intended for policy simulation and pilot planning, not field-validated causal income effects.

## Repository Contents

```text
.
├── paper/
│   ├── FromHawking_DLIndaba2026.tex   # anonymized LaTeX source
│   ├── references.bib                 # bibliography
│   ├── ijcai26.sty                    # conference style needed to compile
│   ├── named.bst                      # bibliography style needed to compile
│   └── figures/                       # paper figures generated from experiments
├── notebooks/
│   └── Model.ipynb                    # cleaned notebook with outputs removed
├── data/
│   └── README.md                      # data manifest and acquisition notes
├── requirements.txt                   # Python dependencies for rerunning analyses
└── .gitignore                         # excludes raw data, build products, and local state
```

## What Is Included

- Anonymized LaTeX source for the paper.
- Figure assets required by the LaTeX file.
- A cleaned notebook with cell outputs removed to avoid exposing local file paths or machine-specific state.
- Reproducibility instructions for obtaining external datasets.

## What Is Not Included

Raw datasets are not included in this package. Some source datasets may have redistribution limits, large file sizes, or access terms that should be respected. In particular, this repository does not include:

- World Bank Enterprise Survey microdata.
- WFP food price CSV files.
- WorldPop raster/ZIP files.
- Full Rwanda Establishment Census spreadsheets or extracted raw tables.
- Local virtual environments, Jupyter runtime files, LaTeX build artifacts, or editor settings.

To reproduce the experiments, place the required raw files under `data/` using the filenames described in `data/README.md`.

## Reproducing the Paper

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook:

```bash
jupyter notebook notebooks/Model.ipynb
```

The notebook contains the analysis workflow and reviewer-revision cells used to produce leakage-controlled formalization results, price forecasting baselines, federated-learning summaries, and scenario sensitivity estimates.

To compile the paper:

```bash
cd paper
pdflatex -interaction=nonstopmode FromHawking_DLIndaba2026.tex
bibtex FromHawking_DLIndaba2026
pdflatex -interaction=nonstopmode FromHawking_DLIndaba2026.tex
pdflatex -interaction=nonstopmode FromHawking_DLIndaba2026.tex
```

The compiled PDF is intentionally not committed by default. This avoids accidentally circulating a pre-publication paper from an identifiable public GitHub account during review.

## Anonymity And Publication Note

The paper source currently uses `Anonymous Authors`. If this repository is made public before review decisions, it may compromise double-blind review even if the PDF itself is anonymized, because the GitHub owner can reveal author identity.

Recommended practice:

- Keep this repository private during review.
- If an artifact must be shared during double-blind review, use an anonymous artifact repository or remove identifying metadata.
- Add the compiled paper PDF publicly only after acceptance, after checking the conference preprint and anonymity policy.

## Should The IJCAI-ECAI-26 Instructions Be Included?

This package includes only the files required to compile the paper: `ijcai26.sty` and `named.bst`.

Do not include the full IJCAI-ECAI formatting-instructions folder unless the license and conference instructions clearly allow redistribution. A cleaner approach is to cite or link to the official formatting instructions in the repository documentation and keep only the style files needed for reproducible compilation.

## Evidence Boundary

The paper separates empirical results from scenario estimates:

- Formalization prediction is evaluated empirically on WBES data after removing registration-status leakage and direct proxies.
- Price forecasting is evaluated empirically on WFP time-series data using temporal held-out splits.
- Income gains, demand-pull multipliers, and spatial deployment results are scenario analyses under stated assumptions.

This distinction is central to interpreting the contribution and should be preserved in future revisions.

