# CHAPTER III: RESEARCH METHODOLOGY

---

## 3.1 Introduction

This chapter describes the methodological framework used to examine how payment issues, online scams, and product quality mismatch influence post-purchase behavior among online shoppers in Nepal, with risk perception as a mediating variable and customer satisfaction as an additional outcome variable. The chapter explains the research design, approach, population and sample, data sources, data collection process, measurement model, validity and reliability procedures, and analytical techniques used to test the hypotheses developed in Chapter I.

The methodology was designed to align with SOMTU GRP standards and with prior e-commerce risk-behavior studies (Pavlou, 2003; Kim et al., 2008; Pandey, 2025). Because the study seeks to test predefined hypotheses and quantify relationships among constructs, a structured quantitative design was adopted.

---

## 3.2 Research Design

The study employed a **quantitative, cross-sectional, explanatory design**. This design was selected for four reasons.

First, the research questions require measurable evidence on the strength and direction of relationships among variables. Quantitative design allows this through numeric measurement and statistical testing.

Second, the model includes multiple latent constructs (payment issues, online scams, product quality mismatch, risk perception, post-purchase behavior, and customer satisfaction), each measured through multi-item Likert scales. Quantitative methods are appropriate for estimating internal consistency, inter-construct correlation, and path effects.

Third, the study tests mediation hypotheses (H5–H7), which require inferential procedures that are standard in quantitative explanatory research.

Fourth, the cross-sectional format is appropriate for time- and resource-constrained graduate research while still allowing robust model testing at one point in time.

Accordingly, the research design is both **descriptive** (profiling respondents and construct levels) and **analytical/explanatory** (testing direct and indirect effects).

---

## 3.3 Research Approach

The study followed a **deductive research approach**. Theoretical propositions from TAM extensions (Pavlou, 2003), trust-risk e-commerce models (Kim et al., 2008), and Nepal-focused risk evidence (Pandey, 2025; Devkota et al., 2021) were translated into eight hypotheses. Primary survey data were then used to test those hypotheses empirically.

This approach is suitable because the study objective is not to generate grounded theory from open-ended narratives but to evaluate whether established theoretical relationships hold in the Nepalese online shopping context.

Philosophically, the study is aligned with a **positivist orientation**, emphasizing objectivity, measurement consistency, and statistical inference.

---

## 3.4 Population and Sample

### 3.4.1 Target Population

The target population comprised adult online shoppers in Nepal who had prior online purchasing experience. Given practical field access and concentration of digital consumers, responses were collected primarily from urban/semi-urban online users reachable through educational, professional, and social networks.

### 3.4.2 Sampling Technique

A **non-probability convenience sampling** method was used. This technique was appropriate because:

- no complete sampling frame of online shoppers is publicly available,
- the study required rapid field collection,
- and prior Nepal e-commerce studies used similar procedures (Vaidya, 2019; Devkota et al., 2021).

To reduce homogeneity risk, data were collected through mixed channels (online sharing plus direct outreach to different respondent groups).

### 3.4.3 Sample Size and Final Usable Cases

The source file (`data/survey-data.csv`) contains **184 raw response records** (excluding header). After screening for completeness across all Likert-scale variables, the same **184 responses** were retained for analysis.

Thus, all inferential analyses in Chapter IV are based on **N = 184** valid cases.

### 3.4.4 Justification of Sample Adequacy

For multiple regression with three to four predictors and mediation paths, N=184 provides adequate statistical power for medium effects in social science models. The ratio of valid observations to predictors is well above minimum rule-of-thumb requirements used in applied behavioral research.

---

## 3.5 Data Sources

### 3.5.1 Primary Data

Primary data came from a structured questionnaire and the corresponding response file:

- **Questionnaire design source:** `survey_questionnaire.md`
- **Survey response dataset:** `data/survey-data.csv`

The dataset includes demographic variables (age, gender, education, occupation, shopping frequency, preferred platform) and psychometric items for six constructs.

### 3.5.2 Secondary Data

Secondary data informed conceptualization and instrument adaptation from:

- Chapter I and Chapter II literature synthesis,
- cited journal articles and reports in `literature/` and `literature/text/`,
- SOMTU GRP formatting guidance in `guidelines.md`.

Secondary sources were used to define constructs, adapt indicators, and justify analytical methods.

---

## 3.6 Data Collection Methods

### 3.6.1 Survey Questionnaire

The core data collection method was a structured survey questionnaire using closed-ended statements on Likert-type scales.

### 3.6.2 Questionnaire Administration

Responses were captured in digital form (timestamped entries reflected in the CSV). Participation was voluntary, and only completed records were retained for final analysis.

### 3.6.3 Interviews and Observation

This study did **not** use formal qualitative interviews or observation as primary data collection methods. The research scope was quantitative and questionnaire-based.

---

## 3.7 Research Variables and Constructs

The model includes:

- **Independent variables (IVs):** Payment Issues (PI), Online Scams (SC), Product Quality Mismatch (PQ)
- **Mediating variable:** Risk Perception (RP)
- **Dependent variables (DVs):** Post-Purchase Behavior (PP), Customer Satisfaction (CS)

### 3.7.1 Construct Operational Table

| Variable | Role | Dimension/Meaning | Indicators (Items) | Measurement Items (abbrev.) | Source Basis | Scale |
|---|---|---|---|---|---|---|
| Payment Issues (PI) | Independent | Payment reliability, refund delay, transaction concern | PI1–PI5 | Secure payment, transaction accuracy, failure frequency, refund delay, COD fear | Vaidya (2019); Devkota et al. (2021); Pandey (2025); Pavlou (2003) | 5-point Likert |
| Online Scams (SC) | Independent | Scam awareness and trust erosion | SC1–SC5 | Scam awareness, scam worry, fake seller prevalence, trust reduction, seller verification | Shrestha et al. (2025); Kim et al. (2008) | 5-point Likert |
| Product Quality Mismatch (PQ) | Independent | Product-description inconsistency | PQ1–PQ5 | mismatch, lower quality, misleading description, defective item, quality uncertainty | Vaidya (2019); Devkota et al. (2021); Tanjung et al. (2025) | 5-point Likert |
| Risk Perception (RP) | Mediator | Financial/privacy/uncertainty risk appraisal | RP1–RP5 | high risk, financial loss worry, pre-purchase uncertainty, data insecurity, risk-driven decision | Pavlou (2003); Kim et al. (2008); Pandey (2025) | 5-point Likert |
| Post-Purchase Behavior (PP) | Dependent | Complaint/return/avoidance response | PP1–PP5 | complain, return, negative sharing, seller avoidance, future impact | Tanjung et al. (2025); Izumi et al. (2025); Ghimire (2023) | 5-point Likert |
| Customer Satisfaction (CS) | Dependent | Overall online shopping satisfaction | CS1–CS5 | overall satisfaction, expectation match, continuance intention, recommendation, risk-effect perception | Hipólito et al. (2025); Pavlou (2003); Vaidya (2019) | 5-point Likert |

The cleaned dataset used for estimation contains **five measured indicators per construct** (PI1–PI5, SC1–SC5, PQ1–PQ5, RP1–RP5, PP1–PP5, CS1–CS5). Therefore, all reliability, validity, correlation, regression, and mediation results in Chapter IV are based on this 30-item analytical structure.

### 3.7.2 Item Direction and Coding Logic

Some items were directionally opposite to the risk/problem orientation and were reverse-coded during analysis to maintain conceptual consistency:

- PI1, PI2 (positive payment statements) were reverse-coded,
- CS5 was reverse-coded when integrating the satisfaction composite.

---

## 3.8 Instrument Development

The instrument was adapted from validated prior studies and contextualized for Nepalese online shopping.

### 3.8.1 Development Steps

1. Construct identification from literature and Chapter II framework.
2. Item pool selection from previously used scales.
3. Contextual wording adjustment for Nepal platform/payment realities.
4. Section-wise questionnaire structuring (demographics + six constructs).
5. Coding preparation for statistical analysis.

### 3.8.2 Measurement Scale

The questionnaire draft document includes a 7-point template for item presentation; however, the finalized administered response file is coded on a **5-point agreement scale** (1 to 5). Based on field implementation and available response records, this 5-point coding is treated as the final measurement format for all Chapter IV analyses.

### 3.8.3 Source Adaptation Principle

Adaptation was content-preserving rather than literal, to maintain construct relevance while improving respondent comprehension in local context.

---

## 3.9 Validity and Reliability

### 3.9.1 Content Validity

Content validity was established through alignment between constructs, literature-derived definitions, and item indicators used in the questionnaire.

### 3.9.2 Construct Validity

Construct validity was examined in Chapter IV through factor loading patterns, Composite Reliability (CR), AVE, and inter-construct correlation checks.

### 3.9.3 Reliability

Internal consistency reliability was assessed using Cronbach's alpha. Threshold guidance followed conventional standards (Nunnally, 1978; Hair et al., 2019).

### 3.9.4 Pilot and Data Screening Logic

The final analytical sample was screened for completeness of all construct items. Records with missing psychometric responses were excluded from model testing.

---

## 3.10 Data Analysis Techniques

Data analysis used **Python-based statistical workflow** (pandas, numpy, statsmodels) for reproducible results.

### 3.10.1 Descriptive Analysis

- Frequency and percentage for demographic variables
- Mean, standard deviation, minimum, and maximum for constructs

### 3.10.2 Reliability and Measurement Quality

- Cronbach's alpha
- Composite Reliability (CR)
- Average Variance Extracted (AVE)
- Item-level loading review

### 3.10.3 Correlation Analysis

Pearson correlation coefficients were used to examine direction and strength of bivariate relationships among constructs.

### 3.10.4 Regression and Path Analysis

Four regression models were estimated:

1. RP on PI, SC, PQ (testing H1–H3)
2. PP on RP (testing H4)
3. CS on RP (testing H8)
4. PP on PI, SC, PQ, RP (for mediated path decomposition)

### 3.10.5 Mediation Testing

Mediation (H5–H7) was tested using bootstrapped indirect effects (resampling approach) and confidence intervals for the paths:

- IV → RP (a path)
- RP → PP (b path)
- indirect effect = a × b

---

## 3.11 Ethical Considerations

The study followed standard academic ethics:

- **Informed consent:** respondents participated voluntarily.
- **Confidentiality:** no personally identifying variables were used in analysis.
- **Data protection:** dataset handled in aggregate research format.
- **Academic integrity:** cited sources were acknowledged, and analysis was reported transparently.

---

## 3.12 Chapter Summary

Chapter III presented the methodological architecture of the study. A quantitative, deductive, cross-sectional design was employed using survey data from 184 valid respondents. Constructs were operationalized through literature-grounded items and analyzed using reliability, validity, correlation, regression, and mediation procedures. These methods provide the empirical foundation for Chapter IV, which reports statistical findings and hypothesis outcomes.

---

## References

Bianchi, C., & Andrews, L. (2012). Risk, trust, and consumer online purchasing behaviour: A Chilean perspective. *International Marketing Review, 29*(3), 253–275. https://doi.org/10.1108/02651331211229750

Devkota, N., Dhungana, S., Parajuli, S., Bhandari, U., & Paudel, U. R. (2021). Nepalese consumers' perception on online shopping challenges and its managerial solution. *International Research Journal of Science, Technology, Education, and Management, 1*(2), 65–77. https://doi.org/10.5281/zenodo.5726289

Ghimire, S. K. (2023). *An analysis of the factors that influence consumers' decision-making in online shopping: A study of Mantra Craft Store in Nepal* [Bachelor's thesis]. Centria University of Applied Sciences.

Hair, J. F., Black, W. C., Babin, B. J., & Anderson, R. E. (2019). *Multivariate data analysis* (8th ed.). Cengage.

Hipólito, F., Dias, Á., & Pereira, L. (2025). Influence of consumer trust, return policy, and risk perception on satisfaction with the online shopping experience. *Systems, 13*(3), 158. https://doi.org/10.3390/systems13030158

Izumi, C., Setiawan, W. C., & Ghaffar, S. A. (2025). Enhancing customer satisfaction and product quality in e-commerce through post-purchase analysis using text mining and sentiment analysis techniques in digital marketing. *Journal of Data Mining for Digital Content*.

Kim, D. J., Ferrin, D. L., & Rao, H. R. (2008). A trust-based consumer decision-making model in electronic commerce: The role of trust, perceived risk, and their antecedents. *Decision Support Systems, 44*(2), 544–564. https://doi.org/10.1016/j.dss.2007.07.001

Nunnally, J. C. (1978). *Psychometric theory* (2nd ed.). McGraw-Hill.

Pandey, D. (2025). Effects of perceived risk on online buying behavior. *Dibyajyoti Journal, 7*(1). https://doi.org/10.3126/dj.v7i1.87642

Pavlou, P. A. (2003). Consumer acceptance of electronic commerce: Integrating trust and risk with the technology acceptance model. *International Journal of Electronic Commerce, 7*(3), 101–134.

Shrestha, N., Shrestha, N., Bhusal, P., Kochar, P., Agrawal, A. K., & Thakur, R. K. (2025). Navigating online shopping scams: How fraudulent experiences and customer awareness shape customer choices and trust? *Apex Journal of Business and Management, 4*(2), 107–118. https://doi.org/10.61274/apxc.2025.v04i02.009

Tanjung, P. K., Sumarwan, U., & Krisnatuti, D. (2025). The impact of perceived product quality, perceived value, and personality on consumer dissatisfaction and complaint behavior types in e-commerce. *Jurnal LOCUS: Penelitian & Pengabdian, 4*(12).

Vaidya, R. (2019). Online shopping in Nepal: Preferences and problems. *The Journal of Nepalese Business Studies, XII*(1), 71–82.
