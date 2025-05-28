# 🗳️ Elections and Climate Attitudes  
**How Do People’s Views on Climate Change and Policies Shift During an Election?**  
By Paraskevas K. Leivadaros  
Supervised by Kyuri Park  
University of Amsterdam | MSc in Data Science (2025)

## 📘 Overview
This repository contains the code and data analysis for my master's thesis, which investigates how the 2020 U.S. elections influenced public perceptions of climate change, policy support, and financial willingness to act.

The analysis uses a combination of **causal discovery (PC algorithm)** and **dynamic modeling (VAR and GVAR)** to uncover how climate attitudes evolve over time and are shaped by political affiliation and ideological positioning.

## 📌 Research Questions
1. How do attitudes toward carbon taxes or emissions standards shift around election periods?
2. Does willingness to pay for climate solutions change during electoral cycles?
3. Do perceived harms (e.g., to family or community) drive support for climate policies?
4. How do political identity and ideology moderate climate-related attitudes?

## 📊 Dataset Summary
- 📈 **Observations**: 4,520  
- 📊 **Variables**: 11 numeric (8 float64, 3 int64), standardized to 1–5 Likert scales  
- 📅 **Time Range**: 2020–2021 (Waves 2–4, centered on U.S. election)

### Key Dimensions
| Dimension                    | Variables                                                |
|-----------------------------|----------------------------------------------------------|
| Climate concern             | `cc4_world`, `cc4_comm`, `cc4_famheal`, `cc4_famecon`... |
| Willingness to pay (WTP)    | `ccSolve` (scaled & merged from ccSolveX variables)      |
| Policy support              | `cc_pol_tax`, `cc_pol_car`                               |
| Political orientation       | `pol_party`, `pol_ideology`                              |

- Variables initially varied in scale (1–4, 1–3, 1–5) and were harmonized to a 1–5 Likert scale.
- The `ccSolve` variable was created by dollar-weighting and normalizing responses from a randomized cost-assigned policy question.
- ~80% of original `ccSolveX` variables had missing values by design; merged approach eliminates that issue.

## 🔍 Exploratory Data Analysis (EDA)
### Key Insights
- **Climate concern** is higher at the global/community level than at the personal or economic level.
- **Support for policy** (especially `cc_pol_car`) is consistently higher than **WTP**, which is lowest when high costs are introduced.
- **Political identity and ideology** strongly correlate with support for policies, more than with general climate concern.
- **PCA & ICA** suggest three major latent dimensions:
  1. Climate impact perception
  2. Willingness to pay
  3. Political/policy alignment

👉 See [`notebooks/eda.ipynb`](notebooks/eda.ipynb) for full visualizations:  
- Histograms & KDE plots  
- Spearman correlation heatmaps  
- PCA, ICA, Factor Analysis  

## ⚙️ Methodology
### 1. Causal Discovery
- **PC Algorithm** (constraint-based DAG learning)
- Guides selection and ordering of variables for time series modeling

### 2. Time Series Modeling
- **VAR (Vector Autoregression)**: Captures lagged interdependencies across time
- **GVAR (Graphical VAR)**: Adds regularization using learned causal graph
- **Event Split**: Observations segmented pre- and post-2020 U.S. Election for comparative modeling

## 📁 Project Structure
```
📁 data/
    └── 4-cleaned_data.csv               # Final dataset (standardized & imputed)
📁 notebooks/
    ├── eda.ipynb                        # Exploratory data analysis
📄 README.md
📄 requirements.txt
```

## 📦 Installation
```bash
git clone https://github.com/paraskevasleivadaros/climate-opinions-shift-elections-policies.git
cd climate-opinions-shift-elections-policies
pip install -r requirements.txt
```

## 📈 Preliminary Findings
- Election timing appears to *moderate* attitudes, particularly among independents.
- Climate concern and support for emission regulations remain relatively high, but **WTP remains low**, especially among conservative-leaning respondents.
- **VAR and GVAR results pending** — will be updated soon.

## 🧠 Tools and Libraries
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- `networkx` (PC algorithm)
- `statsmodels` (VAR)
- `graphicalvar`, `factor_analyzer`
- `skimpy`, `FastICA`

## 📜 License
[GPL-3.0-1-ov-file](/LICENSE)

## 🙏 Acknowledgments
- Supervisor: Kyuri Park  
- Faculty of Science – University of Amsterdam  
- The creators of open-source survey datasets and Python libraries

## 📬 Contact
**Paraskevas K. Leivadaros**  
📧 [paraskevasleivadaros@gmail.com](mailto:paraskevasleivadaros@gmail.com)  
🌐 [GitHub](https://github.com/paraskevasleivadaros) | [LinkedIn](https://www.linkedin.com/in/paraskevasleivadaros)
