# 🗳️ Climate Opinions and Elections
This repository contains the code and materials for the master's thesis *"Elections and Climate Attitudes: How Do People’s Views on Climate Change and Policies Shift During an Election?"* by Paraskevas K. Leivadaros, supervised by Kyuri Park at the University of Amsterdam (MSc in Data Science, 2025). The thesis examines how public perceptions of climate change, willingness to pay, and support for climate policies shift during election periods, using survey data and temporal analysis methods.

## 📌 Research Questions
1. Does support for climate policies (like carbon taxes or emissions standards) change during elections? And is this support influenced by personal or community-level perceptions of climate harm?
2. Does willingness to pay for climate solutions vary during elections and what factors influence it?
3. Does political ideology moderate the relationship between perceptions of harm and willingness to pay?  

## 📊 Dataset Summary
- 📈 **Observations**: 5,667  
- 📊 **Variables**: 20 numeric (11 float64, 9 int64)
- 📅 **Time Range**: 2020–2021 (Waves 2,3 and 4, centered on U.S. election)

### Key Dimensions
| Dimension                | Variables                                                                              |
|--------------------------|----------------------------------------------------------------------------------------|
| Climate concern          | `cc4_world`, `cc4_wealthUS`, `cc4_poorUS`, `cc4_comm`, `cc4_famheal`, `cc4_famecon`    |
| Willingness to pay (WTP) | `ccSolve100`, `ccSolve50`, `ccSolve10`, `ccSolve1`, `ccSolve0` (merged into `ccSolve`) |
| Policy support           | `cc_pol_tax`, `cc_pol_car`                                                             |
| Political orientation    | `pol_party`, `pol_lean`, `pol_ideology`                                                |
| Demographics             | `dem_income`, `dem_male`, `dem_age`, `dem_educ`                                        |

## 🔍 Exploratory Data Analysis (EDA)
### Key Insights
* **Global and community-level concern** about climate change is consistently higher than personal or economic concerns.
* **Support for policies**, particularly emissions standards (`cc_pol_car`), remains high across waves, while **willingness to pay (WTP)** drops when financial costs increase.
* **Political identity** strongly predicts policy support, but is weakly correlated with general concern.
* **Dimensionality reduction (PCA, ICA, Factor Analysis)** highlights three core constructs:
  1. Climate impact perception
  2. Willingness to pay
  3. Political/policy alignment

👉 Full visualizations are available in [`notebooks/1-eda.ipynb`](notebooks/eda.ipynb), including:
* KDE plots and histograms
* Correlation heatmaps (Spearman)
* Dimensionality reduction results (PCA, ICA, Factor Analysis)

## ⚙️ Methodology
### 1. Time Series Modeling
* **Panel VAR (PVAR)** is used to model temporal dynamics of climate perceptions, policy support, and WTP.
* Election-period effects are evaluated via **subgroup comparisons** and time-aligned estimations.

### 2. Causal Discovery
* **PCMCI+ algorithm** from `tigramite` identifies time-lagged causal relationships among variables.
* Results from PVAR and PCMCI+ are compared to validate robustness of causal inferences.

### 3. Moderation Models
* Interaction effects between **harm perception** and **political ideology** are tested to identify conditional influences on WTP and policy attitudes.
* Multicollinearity is addressed using a **composite harm index**.

## 📁 Project Structure
```
📁 data/
📁 docs/
    ├── paraskevas-leivadaros-master-thesis.pdf
📁 notebooks/
    ├── 1-eda.ipynb                             # Exploratory data analysis
    ├── 2-modeling-and-inference.ipynb          # Time Series and Causal Analysis
📁 results/
📁 scripts/
📜 LICENSE
📄 README.md
📄 requirements.txt
📟 setup.py
```

## 📦 Installation
This project requires **Python 3.13.0** and **pip 25.1.1**. To avoid conflicts with system-wide packages, we recommend installing Python via a package manager (like Homebrew) and using a virtual environment.
### 🔧 Step 0: Install Python 3.13.0 and pip 25.1.1
#### 🐍 Option A: Using Homebrew (macOS/Linux)
If you don’t have Homebrew installed, run:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Python 3.13.0:
```bash
brew install python@3.13
```

Add it to your shell (if needed):
```bash
echo 'export PATH="/opt/homebrew/opt/python@3.13/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

Upgrade `pip`:
```bash
python3 -m pip install --upgrade pip
```

#### 🪟 Option B: On Windows
1. Download Python 3.13.0 from the official website:  
   https://www.python.org/downloads/release/python-3130/

2. During installation:
   - ✅ Check “Add Python to PATH”
   - ✅ Enable `pip` in the installer options

3. After installation, confirm with:
   ```bash
   python --version
   pip --version
   ```

### 1. Clone the Repository
```bash
git clone https://github.com/paraskevasleivadaros/climate-opinions-and-elections.git
cd climate-opinions-and-elections
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

- **Windows (Command Prompt):**
  ```cmd
  venv\Scripts\activate
  ```

- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

### 4. Verify the Python Environment
```bash
which python
```
Expected output (macOS/Linux):
```
/Users/yourname/climate-opinions-and-elections/venv/bin/python
```

### 5. Install the Project Package and Dependencies
```bash
pip install .
```

This installs all dependencies from `setup.py`

📚 For more help:
- Python: https://www.python.org/
- pip: https://pip.pypa.io/en/stable/installation/
- Homebrew: https://brew.sh/


## 📈 Main Findings
* **Election periods do not significantly alter general climate attitudes**, but subtle shifts in **WTP and policy support** occur among independents.
* **Support for carbon taxes** is strongly predicted by previous policy support (e.g., emissions standards).
* **Multicollinearity in interaction models** affects precision, prompting dimensionality reduction through index construction.

## 🧠 Tools and Libraries
| Tool/Library  | Purpose                                            |
| --------------| ---------------------------------------------------|
| `pandas`      | Data manipulation and panel structuring            |
| `numpy`       | Numerical operations and array handling            |
| `statsmodels` | PVAR (Panel Vector Autoregression) estimation      |
| `tigramite`   | Time-lagged causal discovery using PCMCI+          |
| `matplotlib`  | Static plotting                                    |
| `seaborn`     | Statistical graphics for exploratory data analysis |
| `plotly`      | Interactive network visualizations                 |
| `networkx`    | Construction and layout of causal graphs           |
| `graphviz`    | Rendering directed acyclic graphs (DAGs)           |
| `skimpy`      | Quick summaries and data diagnostics               |

## 📜 License
[GPL-3.0 license](/LICENSE)

## 🙏 Acknowledgments
- Supervisor: Kyuri Park  
- Faculty of Science – University of Amsterdam  
- The creators of open-source survey datasets and Python libraries

## 📬 Contact
**Paraskevas K. Leivadaros**  
📧 [paraskevasleivadaros@gmail.com](mailto:paraskevasleivadaros@gmail.com)  
🌐 [GitHub](https://github.com/paraskevasleivadaros) | [LinkedIn](https://linkedin.com/in/paraskevasleivadaros)

## 📚 Citation
If you use this repository, please cite the thesis:
> Paraskevas K. Leivadaros, *Elections and Climate Attitudes: How Do People’s Views on Climate Change and Policies Shift During an Election?*, University of Amsterdam, 2025. [PDF](docs/paraskevas-leivadaros-master-thesis.pdf)