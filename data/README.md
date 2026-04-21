# Data Manifest

Raw data files are intentionally excluded from the repository. Place required datasets in this directory only when rerunning the notebook locally.

## Expected Files

The notebook can use the following files when available:

```text
data/
├── Rwanda-2023-full-data.csv          # World Bank Enterprise Survey, Rwanda 2023
├── Rwanda-2023-full-data.dta          # optional original WBES Stata file
├── wfp_food_prices_rwa.csv            # WFP food prices, Rwanda
├── wfp_food_prices_uga.csv            # WFP food prices, Uganda
├── wfp_markets_rwa.csv                # WFP market metadata, Rwanda
├── wfp_markets_uga.csv                # WFP market metadata, Uganda
├── worldpop_rwa.zip                   # WorldPop Rwanda population data
├── worldpop_uga.zip                   # WorldPop Uganda population data
└── EC_2023_CSV/                       # Rwanda Establishment Census extracted tables
```

## Data Sources

- Rwanda Establishment Census 2023: National Institute of Statistics of Rwanda.
- World Bank Enterprise Surveys: Rwanda 2023 microdata, subject to World Bank access and use terms.
- WFP Vulnerability Analysis and Mapping food price data.
- WorldPop population grids.
- OpenStreetMap market and road data.
- FinScope digital readiness indicators, where available.

## Sharing Guidance

Do not commit raw microdata or large third-party datasets unless their license explicitly permits redistribution. For public repositories, prefer a data-acquisition script or clear download instructions over checked-in raw files.

Generated figures used by the paper are stored under `paper/figures/`, not here.

