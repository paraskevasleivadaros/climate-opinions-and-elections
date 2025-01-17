# climate-opinions-shift-elections-policies
How do people's attitudes toward climate change shift before and after an election, and how do policies in place during that period further shape their opinions

### Relevance of research question
My research question is highly relevant as it explores the relationship between political events, policies, and society's attitudes toward climate change. Climate change is one of the most important global challenges at the moment. For this reason, understanding how elections and policies shape public opinion is crucial. This knowledge is important for policymakers and researchers working to connect political decisions with public involvement in tackling climate change.

### Causal Discovery or Causal Inference?
In this research report I will be using causal inference, as my primary interest lies in understanding the effect of specific factors (elections and policies) on people's attitudes toward climate change.

### Why Causal Inference?
- **Known causal structure:** My research already hypothesizes relationships; elections and policies influence attitudes toward climate change. I am not trying to discover the causal graph from scratch.
- **Quantifying effects:** I want to measure how much (e.g., the magnitude of the shift in attitudes) and in what way (e.g., positive or negative) elections and policies influence attitudes.

### Sub-Questions
I am focusing on causal inference which is most suited to sub-questions that aim to **quantify causal effects** or determine the **mechanisms** through which certain variables (e.g., elections, policies) influence others (e.g., attitudes toward climate change). Here's a breakdown of the sub-questions:

1. **Election Timing and Attitudes**
  - How do people's attitudes toward climate change change in the months leading up to an election?
    - Causal Inference Role: Quantify the causal effect of the election campaign period on attitudes by comparing pre-election and election-period data.
    - Methods: Difference-in-Differences (DiD), time-series analysis
  - What differences, if any, are observed in attitudes immediately after an election compared to before?
    - Causal Inference Role: Measure the causal impact of the election outcome on attitudes
    - Methods: Regression discontinuity design (if election results are close), DiD
  - Do shifts in attitudes differ depending on the election's outcome (e.g., political party or candidate elected)?
    - Causal Inference Role: Examine the effect of different political outcomes on public attitudes
    - Methods: Instrumental variables (e.g., close elections as instruments), stratified analyses
2. **Role of Policies**
  - How do climate change policies announced during the election campaign affect public attitudes toward climate change?
    - Causal Inference Role: Evaluate the causal effect of policy announcements on attitudes
    - Methods: Propensity score matching, DiD (pre- and post-policy announcement)
  - Are policies introduced after an election perceived differently in shaping public opinion compared to those introduced before?
    - Causal Inference Role: Compare the causal impact of timing (pre- vs. post-election) on public attitudes
    - Methods: Mediation analysis, DiD
3. **Contextual and Demographic Factors**
  - How do demographic factors (e.g., age, education, political affiliation) influence shifts in attitudes toward climate change before and after an election?
    - Causal Inference Role: Investigate heterogeneous treatment effects (how causal effects vary by subgroup)
    - Methods: Subgroup analysis in causal inference models, propensity score stratification
  - Do regional or national differences in climate policy frameworks affect how attitudes shift during election periods?
    - Causal Inference Role: Explore causal effects across different contexts (e.g., regions, policy environments)
    - Methods: Multi-level models, stratified analysis
 
**Methods:**
- **Stratified Analysis** is a method used to examine causal relationships or associations within specific subgroups (strata) of a population, rather than across the entire dataset. It helps determine whether the effect of a treatment, exposure, or intervention varies across different levels of a stratifying variable, such as demographic, geographic, or temporal factors. In this context of how people's attitudes toward climate change shift before and after elections, and how policies shape their opinions, stratified analysis can help identify how these effects differ across subgroups (e.g., age, political affiliation, region, or socioeconomic status).
- **Regression Discontinuity (RD)** designs are a causal inference technique that can be applied to study causal effects in contexts where an assignment to treatment depends on a threshold in a continuous variable. In the context of this research question about shifts in attitudes toward climate change before and after an election, RD could be particularly useful if we find a "threshold" event such as the election day itself or a narrow electoral margin that determines the political outcome.
- **Difference-in-Differences (DiD)** is a causal inference method that estimates the effect of a treatment or intervention by comparing the before-and-after differences in outcomes for a treated group to those for a control group. It is particularly well-suited to contexts where you have data from two time periods (pre- and post-treatment) and two groups (treated and untreated). In the context of my research question about shifts in attitudes toward climate change before and after an election, DiD can help estimate the causal effect of elections and policies on public attitudes.
- **Instrumental Variables (IV)** is a causal inference technique used to estimate the causal effect of a treatment or variable of interest when there is endogeneity; a situation where the treatment is correlated with unobserved confounders that also affect the outcome. IV uses an external variable (the "instrument") that is correlated with the treatment but does not directly affect the outcome, except through the treatment. In the context of studying how people's attitudes toward climate change shift before and after an election, and how policies shape those opinions, IV can be applied to address potential confounders that make it hard to estimate causal effects. I will use this as part of my **EDA**.
- **Propensity Score Matching (PSM)** is a statistical technique used to estimate causal effects by creating comparable groups (treated vs. untreated) based on their likelihood (propensity) of receiving the treatment. In your context, it can help estimate how people's attitudes toward climate change shift before and after elections and how policies shape those attitudes by balancing the groups on observed characteristics.
- **Mediation analysis** is a causal inference method used to understand how and why a treatment or exposure affects an outcome by decomposing the effect into direct and indirect pathways. In this context, mediation analysis could help explore how elections and policies influence attitudes toward climate change and whether other variables, like media coverage or public discourse, mediate these effects.
- **Multi-level models (MLMs)**, also known as hierarchical or mixed-effects models, are a statistical approach used to analyze data with a nested or hierarchical structure. In this context, they are particularly useful for analyzing how elections, policies, and other factors influence attitudes toward climate change while accounting for variations at different levels, such as individuals, regions, or time periods.
