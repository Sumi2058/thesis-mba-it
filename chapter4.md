# CHAPTER IV: DATA ANALYSIS AND FINDINGS

---

## 4.1 Introduction

This chapter presents the empirical results of the study, based on the cleaned dataset of 184 valid respondents. The analysis follows the sequence specified in Chapter III: demographic profile, descriptive statistics, reliability and validity diagnostics, correlation analysis, hypothesis testing, regression/path analysis, and interpretation of findings against the research objectives.

All analyses were conducted using the survey file located at `data/survey-data.csv`.

---

## 4.2 Demographic Analysis

### 4.2.1 Age Distribution

**Table 4.1 Age of Respondents (N = 184)**

| Age Group | Frequency | Percentage |
|---|---:|---:|
| Below 20 | 9 | 4.89% |
| 20–25 | 85 | 46.20% |
| 26–30 | 67 | 36.41% |
| Above 30 | 23 | 12.50% |
| **Total** | **184** | **100.00%** |

The sample is dominated by younger respondents (20–30 years = 82.61%), indicating that the analysis primarily reflects digitally active age cohorts.

### 4.2.2 Gender Distribution

**Table 4.2 Gender of Respondents**

| Gender | Frequency | Percentage |
|---|---:|---:|
| Male | 98 | 53.26% |
| Female | 85 | 46.20% |
| Other | 1 | 0.54% |
| **Total** | **184** | **100.00%** |

The sample is relatively balanced by gender, with a slight male majority.

### 4.2.3 Educational Profile

**Table 4.3 Education Level**

| Education | Frequency | Percentage |
|---|---:|---:|
| +2 | 11 | 5.98% |
| Bachelor | 89 | 48.37% |
| Master | 81 | 44.02% |
| Above Master | 3 | 1.63% |
| **Total** | **184** | **100.00%** |

Most respondents are Bachelor or Master level (92.39%), consistent with the educated digital consumer profile expected in online shopping studies.

### 4.2.4 Occupational Profile

**Table 4.4 Occupation**

| Occupation | Frequency | Percentage |
|---|---:|---:|
| Student | 75 | 40.76% |
| Employed | 92 | 50.00% |
| Self-employed | 13 | 7.07% |
| Other | 4 | 2.17% |
| **Total** | **184** | **100.00%** |

The data represent both student and working populations, with employed respondents forming the largest group.

### 4.2.5 Online Shopping Frequency

**Table 4.5 Shopping Frequency**

| Frequency | Frequency | Percentage |
|---|---:|---:|
| Rarely | 24 | 13.04% |
| Sometimes | 92 | 50.00% |
| Often | 57 | 30.98% |
| Very Often | 11 | 5.98% |
| **Total** | **184** | **100.00%** |

Half of respondents shop online “sometimes,” while over one-third shop “often/very often,” indicating regular but not uniformly high-frequency engagement.

### 4.2.6 Preferred Platforms (Multiple Response)

**Table 4.6 Preferred Online Platforms (Multiple Response)**

| Platform | Mentions | % of Respondents |
|---|---:|---:|
| Daraz | 155 | 84.24% |
| Social Media sellers/pages | 109 | 59.24% |
| Jeevee | 32 | 17.39% |
| Hamrobazar | 28 | 15.22% |
| SastoDeal | 11 | 5.98% |
| Muncha | 3 | 1.63% |

Daraz is the dominant platform, followed by social media commerce channels. The platform pattern confirms a hybrid ecosystem where formal marketplaces and informal social channels coexist.

---

## 4.3 Descriptive Statistics

Construct scores were computed as item means after directional coding adjustments (PI1 and PI2 reversed; CS5 reversed). The analytical dataset includes 5 indicators per construct (30 total scale items).

**Table 4.7 Descriptive Statistics of Core Constructs**

| Construct | Mean | Std. Deviation | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Payment Issues (PI) | 3.978 | 0.663 | 2.20 | 5.80 |
| Online Scams (SC) | 4.228 | 0.663 | 1.00 | 5.00 |
| Product Quality Mismatch (PQ) | 3.577 | 0.675 | 1.00 | 5.00 |
| Risk Perception (RP) | 3.673 | 0.742 | 1.00 | 5.00 |
| Post-Purchase Behavior (PP) | 4.034 | 0.719 | 1.00 | 5.00 |
| Customer Satisfaction (CS) | 3.573 | 0.634 | 1.40 | 5.00 |

The highest mean appears for online scam concerns (SC = 4.228), indicating strong fraud/scam salience in respondents’ experience. Post-purchase response tendency is also high (PP = 4.034), suggesting that consumers actively react after problematic transactions.

---

## 4.4 Reliability and Validity Analysis

### 4.4.1 Internal Consistency and Convergent Validity

**Table 4.8 Reliability and Convergent Validity**

| Construct | Cronbach’s Alpha | Composite Reliability (CR) | AVE | Interpretation |
|---|---:|---:|---:|---|
| PI | 0.592 | 0.757 | 0.386 | Marginal alpha; acceptable CR; weak AVE |
| SC | 0.757 | 0.837 | 0.511 | Acceptable |
| PQ | 0.730 | 0.825 | 0.491 | Near-threshold AVE |
| RP | 0.817 | 0.873 | 0.581 | Good |
| PP | 0.736 | 0.834 | 0.505 | Acceptable |
| CS | 0.702 | 0.822 | 0.592 | Acceptable |

Interpretation:

- Most constructs satisfy conventional reliability thresholds (alpha ≥ 0.70) except PI, which is marginal but retained due to theoretical relevance and acceptable CR.
- AVE is satisfactory for SC, RP, PP, and CS; PI and PQ are slightly below/near the 0.50 criterion, indicating moderate convergent validity.

### 4.4.2 Factor Loading Diagnostics

**Table 4.9 Selected Loading Pattern Summary**

| Construct | Loading Range | Note |
|---|---:|---|
| PI | 0.491 to 0.695 | Moderate loadings |
| SC | 0.553 to 0.802 | Stronger loadings |
| PQ | 0.526 to 0.828 | Adequate |
| RP | 0.693 to 0.812 | Strong |
| PP | 0.589 to 0.834 | Adequate |
| CS | -0.313 to 0.853 | CS5 behaves inversely to core satisfaction items |

The negative loading behavior of CS5 indicates conceptual tension between overall satisfaction indicators and risk-impact wording. CS5 was retained in the main model to preserve content coverage of risk-conditioned satisfaction in the original instrument, but interpretation is cautious. A sensitivity check using only CS1–CS4 preserved the negative sign of RP → CS, although statistical strength decreased; therefore, the reported model is retained with an explicit measurement caveat.

### 4.4.3 Discriminant Validity (Fornell-Larcker Check)

Square roots of AVE: PI=0.622, SC=0.715, PQ=0.701, RP=0.762, PP=0.711, CS=0.769.

These were generally higher than corresponding inter-construct correlations, supporting acceptable discriminant validity at the construct level.

---

## 4.5 Correlation Analysis

**Table 4.10 Correlation Matrix**

| Construct | PI | SC | PQ | RP | PP | CS |
|---|---:|---:|---:|---:|---:|---:|
| PI | 1.000 | 0.287 | 0.289 | 0.432 | 0.040 | -0.267 |
| SC | 0.287 | 1.000 | 0.304 | 0.501 | 0.337 | 0.004 |
| PQ | 0.289 | 0.304 | 1.000 | 0.373 | 0.357 | -0.223 |
| RP | 0.432 | 0.501 | 0.373 | 1.000 | 0.319 | -0.210 |
| PP | 0.040 | 0.337 | 0.357 | 0.319 | 1.000 | 0.082 |
| CS | -0.267 | 0.004 | -0.223 | -0.210 | 0.082 | 1.000 |

Interpretation:

- RP is positively related to PI, SC, and PQ, consistent with model logic.
- PP has moderate positive correlation with SC, PQ, and RP.
- CS is negatively associated with PI, PQ, and RP, indicating reduced satisfaction under higher risk/problem conditions.

---

## 4.6 Hypothesis Testing

### 4.6.1 Regression Results for Direct Paths

**Table 4.11 Direct Effect Models**

| Path | Std. Beta (β) | p-value | Decision |
|---|---:|---:|---|
| PI → RP (H1) | 0.274 | <0.001 | Supported |
| SC → RP (H2) | 0.366 | <0.001 | Supported |
| PQ → RP (H3) | 0.183 | 0.0046 | Supported |
| RP → PP (H4) | 0.319 | <0.001 | Supported |
| RP → CS (H8) | -0.210 | 0.0041 | Supported |

Model diagnostics:

- **Model 1 (RP on PI, SC, PQ):** R² = 0.370, F = 35.207, p < 0.001
- **Model 2 (PP on RP):** R² = 0.102, F = 20.620, p < 0.001
- **Model 3 (CS on RP):** R² = 0.044, F = 8.437, p = 0.004

The strongest predictor of RP is SC, followed by PI and PQ.

### 4.6.2 Mediation Test (Bootstrapped Indirect Effects)

**Table 4.12 Mediation Results (Risk Perception as Mediator)**

| Hypothesis | Indirect Effect (a×b) | 95% Boot CI | Direct Effect (c’) | Mediation Type | Decision |
|---|---:|---|---:|---|---|
| H5: PI → RP → PP | 0.054 | [0.011, 0.107] | -0.196 (p=0.0156) | Partial mediation | Supported |
| H6: SC → RP → PP | 0.076 | [0.014, 0.150] | 0.228 (p=0.0071) | Partial mediation | Supported |
| H7: PQ → RP → PP | 0.037 | [0.004, 0.088] | 0.293 (p=0.0002) | Partial mediation | Supported |

Since all confidence intervals exclude zero, all three indirect effects are significant.

---

## 4.7 Regression / Path Analysis

A regression-based path framework was used (instead of full covariance SEM) due to sample size and model simplicity.

### 4.7.1 Structural Interpretation

- PI, SC, and PQ significantly increase RP.
- RP significantly increases adverse PP responses.
- RP significantly reduces CS.
- Even after adding RP, SC and PQ remain positive predictors of PP, and PI shows a negative direct coefficient in the full model, indicating suppression/complex overlap effects after mediator entry. This sign reversal is interpreted as a mediated-competitive pattern: PI raises RP (which increases PP), but once shared variance with RP/SC/PQ is controlled, the residual PI component may reflect respondents who mitigate payment problems through coping strategies (e.g., safer payment choice), reducing direct adverse post-purchase reactions.

### 4.7.2 Full PP Model

**Table 4.13 PP Regression with Mediator Included**

| Predictor | Std. Beta (β) | p-value |
|---|---:|---:|
| PI | -0.181 | 0.0156 |
| SC | 0.210 | 0.0071 |
| PQ | 0.275 | 0.0002 |
| RP | 0.189 | 0.0238 |

Model fit: **R² = 0.222**, Adjusted R² = 0.205, F = 12.763, p < 0.001.

VIF values for predictors were low (approximately 1.15–1.59), indicating no serious multicollinearity concern.

---

## 4.8 Discussion of Findings

The findings substantiate the integrated risk-based framework proposed in Chapter II.

First, payment issues, scams, and product mismatch all significantly increase risk perception, with scam-related concern showing the largest standardized effect. This aligns with Nepal-focused evidence showing rising fraud salience and trust pressure in digital transactions (Shrestha et al., 2025; Pandey, 2025).

Second, risk perception significantly increases adverse post-purchase responses (complaints, avoidance, negative sharing), which is consistent with post-purchase dissatisfaction theory and complaint behavior studies (Tanjung et al., 2025).

Third, risk perception is negatively linked with customer satisfaction, supporting risk-trust-satisfaction logic from prior e-commerce research (Kim et al., 2008; Hipólito et al., 2025).

Fourth, mediation results confirm that risk perception is an active mechanism through which shopping problems translate into post-purchase outcomes. Because direct effects remain significant for all three IVs, mediation is partial rather than full.

Overall, the model indicates that online shopping problems in Nepal influence consumer outcomes through both direct experiential pathways and indirect psychological risk pathways.

---

## 4.9 Chapter Summary

Chapter IV presented the empirical analysis of 184 valid responses. Demographic and descriptive findings showed a young, educated, digitally active respondent base with high platform use concentration (especially Daraz and social media channels). Reliability and validity diagnostics were broadly acceptable with some measurement caution points. Correlation, regression, and mediation analyses provided strong support for H1–H7 and H8. The central conclusion is that risk perception plays a statistically significant and theoretically meaningful mediating role between online shopping problems and post-purchase behavioral outcomes.
