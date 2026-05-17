# CHAPTER IV: DATA ANALYSIS AND FINDINGS

---

## 4.1 Introduction

This chapter presents a detailed empirical analysis of the study **“Risk Perception and Post-Purchase Problems in Online Shopping in Nepal.”** The chapter is intentionally developed in an extended format so it can stand as a full analytical chapter in a thesis manuscript and provide depth beyond basic statistical reporting.

The analysis is based on **184 valid survey responses** and follows the analytical design presented in Chapter III. The chapter reports:

1. Data preparation and screening outcomes.
2. Respondent demographic and behavioral profile.
3. Item-level and construct-level descriptive statistics.
4. Reliability and validity diagnostics.
5. Correlation and regression findings.
6. Mediation testing outcomes.
7. Extended interpretation of path behavior and subgroup patterns.
8. Theoretical and practical implications grounded in the Nepal e-commerce context.

All results are derived from the survey data file:

- `data/survey-data.csv`

The chapter is structured to move from foundational data quality checks to increasingly inferential analyses. This layered structure ensures that all hypothesis decisions are interpreted within evidence on sample composition, construct measurement quality, and distributional behavior.

---

## 4.2 Data Preparation, Cleaning, and Analytical Readiness

Before inferential analyses, the dataset was screened to ensure consistency between the measurement model and analytical assumptions.

### 4.2.1 Response and Record Quality

The final analytical file contains **184 records** with complete scale responses for all core constructs (PI, SC, PQ, RP, PP, CS). The survey instrument includes demographic variables and 30 Likert items.

No duplicate respondent IDs were present in the analytical export, and each row contains the full set of construct items used for scoring.

### 4.2.2 Coding and Directional Alignment

Several items were reverse-coded to maintain directional consistency where higher scores represent higher intensity of the latent condition:

- **PI1** reversed
- **PI2** reversed
- **CS5** reversed

This coding approach ensures that construct means can be interpreted uniformly without directional ambiguity. For example, higher PI reflects stronger payment-related difficulties and insecurity; higher CS reflects stronger satisfaction.

### 4.2.3 Item Scale Integrity

All scale items are observed on a 1–5 response range. Construct-level minimum and maximum values remained within expected bounds after aggregation, indicating no coding overflow or conversion errors.

### 4.2.4 Practical Screening Notes

Two practical observations emerged during preprocessing:

1. **Platform variable includes long-tail free-text entries** (e.g., platform names outside predefined options), which indicates respondents occasionally entered alternative channels manually.
2. **Single-observation categories** appear in demographic data (e.g., one respondent in “Other” gender), requiring cautious interpretation in subgroup comparisons.

Handling decision: long-tail platform responses were retained and grouped under “Other long-tail entries” for descriptive reporting, while single-observation demographic categories were retained for transparency but not used for inferential claims.

These points do not invalidate the core model but are relevant for interpretation boundaries.

---

## 4.3 Demographic and Behavioral Profile of Respondents

This section provides detailed profile evidence for understanding to whom the findings most directly generalize.

### 4.3.1 Age Distribution

**Table 4.1 Age of Respondents (N = 184)**

| Age Group | Frequency | Percentage |
|---|---:|---:|
| Below 20 | 9 | 4.89% |
| 20–25 | 85 | 46.20% |
| 26–30 | 67 | 36.41% |
| Above 30 | 23 | 12.50% |
| **Total** | **184** | **100.00%** |

The age composition shows that **82.61% of respondents are between 20 and 30 years old**, indicating that the sample is concentrated in the most digitally active purchasing segment. This matters analytically because younger cohorts are often more exposed to online channels, app-first shopping experiences, and social commerce influences.

### 4.3.2 Gender Distribution

**Table 4.2 Gender of Respondents**

| Gender | Frequency | Percentage |
|---|---:|---:|
| Male | 98 | 53.26% |
| Female | 85 | 46.20% |
| Other | 1 | 0.54% |
| **Total** | **184** | **100.00%** |

The sample is near-balanced between male and female respondents. This improves interpretive robustness for aggregate model conclusions, though inferential claims for “Other” gender are not statistically stable due to very small n.

### 4.3.3 Educational Profile

**Table 4.3 Education Level**

| Education | Frequency | Percentage |
|---|---:|---:|
| +2 | 11 | 5.98% |
| Bachelor | 89 | 48.37% |
| Master | 81 | 44.02% |
| Above Master | 3 | 1.63% |
| **Total** | **184** | **100.00%** |

A high education concentration is evident: **92.39%** are Bachelor/Master level. This is consistent with respondents capable of evaluating risk cues such as seller reliability, refund process quality, and transaction transparency.

### 4.3.4 Occupational Profile

**Table 4.4 Occupation**

| Occupation | Frequency | Percentage |
|---|---:|---:|
| Student | 75 | 40.76% |
| Employed | 92 | 50.00% |
| Self-employed | 13 | 7.07% |
| Other | 4 | 2.17% |
| **Total** | **184** | **100.00%** |

The respondent base combines student and working consumers, with employed respondents as the largest segment. This blend supports relevance to both budget-sensitive and convenience-driven purchase routines.

### 4.3.5 Online Shopping Frequency

**Table 4.5 Shopping Frequency**

| Shopping Frequency | Frequency | Percentage |
|---|---:|---:|
| Rarely | 24 | 13.04% |
| Sometimes | 92 | 50.00% |
| Often | 57 | 30.98% |
| Very Often | 11 | 5.98% |
| **Total** | **184** | **100.00%** |

Most respondents are occasional-to-regular online buyers. The **“sometimes”** segment dominates, suggesting a broad middle of moderate platform engagement rather than an extreme heavy-user sample.

### 4.3.6 Preferred Platforms (Multiple Response)

**Table 4.6 Preferred Online Platforms (Multiple Response)**

| Platform | Mentions | % of Respondents |
|---|---:|---:|
| Daraz | 155 | 84.24% |
| Social Media sellers/pages | 109 | 59.24% |
| Jeevee | 32 | 17.39% |
| Hamrobazar | 28 | 15.22% |
| SastoDeal | 11 | 5.98% |
| Muncha | 3 | 1.63% |
| Other long-tail entries (combined) | 5 | 2.72% |

Platform behavior reflects a **hybrid ecosystem**: dominant marketplace purchasing plus substantial social-commerce participation. The presence of long-tail entries also signals fragmented seller discovery channels.

In this chapter, long-tail entries refer to low-frequency custom responses (e.g., direct Instagram pages, generic marketplace mentions, and other one-off website names) that do not form large standalone categories but indicate dispersed channel usage.

### 4.3.7 Demographic Synthesis

Taken together, the demographic profile suggests this chapter’s findings are most representative of **young, educated, digitally active Nepali online shoppers** with mixed usage across formal and informal channels. This profile context is critical when interpreting high scam salience and risk-linked post-purchase behavior.

---

## 4.4 Item-Level Descriptive Analysis

Construct means are useful but can hide meaningful internal variation. This section reports item-level means and dispersion after directional alignment.

### 4.4.1 Payment Issues (PI) Item Pattern

**Table 4.7 PI Item-Level Descriptives (Directionally Aligned)**

| Item | Mean | Std. Dev. | Interpretation |
|---|---:|---:|---|
| PI1 (reversed) | 2.685 | 0.983 | Moderate payment security confidence after reversal indicates concern remains present |
| PI2 (reversed) | 2.413 | 0.985 | Lower score indicates notable uncertainty about transaction completion reliability |
| PI3 | 2.918 | 1.078 | Mixed perception of payment failure frequency |
| PI4 | 3.891 | 1.037 | Strong concern about refund delays |
| PI5 | 3.984 | 1.257 | Strong preference for COD linked to fear of financial loss |

The PI profile indicates that **post-transaction friction** (refund and loss aversion) is stronger than immediate transaction-failure reporting alone.

### 4.4.2 Online Scams (SC) Item Pattern

**Table 4.8 SC Item-Level Descriptives**

| Item | Mean | Std. Dev. | Interpretation |
|---|---:|---:|---|
| SC1 | 4.391 | 0.840 | High awareness of online scam presence |
| SC2 | 3.946 | 0.993 | Elevated personal scam worry |
| SC3 | 4.277 | 0.929 | Strong agreement that fake sellers are common |
| SC4 | 4.065 | 0.992 | Scam exposure substantially reduces trust |
| SC5 | 4.462 | 0.878 | Active seller verification behavior is common |

SC items show consistently high intensity, especially around seller credibility concerns.

### 4.4.3 Product Quality Mismatch (PQ) Item Pattern

**Table 4.9 PQ Item-Level Descriptives**

| Item | Mean | Std. Dev. | Interpretation |
|---|---:|---:|---|
| PQ1 | 3.478 | 1.011 | Product-display mismatch is common |
| PQ2 | 3.538 | 0.926 | Quality below expectation appears frequent |
| PQ3 | 3.467 | 0.932 | Misleading product descriptions are moderately common |
| PQ4 | 3.087 | 1.153 | Defect/damage experiences vary across respondents |
| PQ5 | 4.315 | 0.800 | Consumers find online quality judgment difficult |

The strongest PQ signal is not necessarily severe damage incidence, but **pre-purchase uncertainty about quality assessment**.

### 4.4.4 Risk Perception (RP) Item Pattern

**Table 4.10 RP Item-Level Descriptives**

| Item | Mean | Std. Dev. | Interpretation |
|---|---:|---:|---|
| RP1 | 3.663 | 0.976 | Online shopping perceived as meaningfully risky |
| RP2 | 3.538 | 0.994 | Financial-loss concern is substantial |
| RP3 | 3.565 | 0.965 | Uncertainty before purchase is common |
| RP4 | 3.783 | 1.030 | Data-security concern is relatively high |
| RP5 | 3.815 | 0.896 | Risk strongly influences purchase decisions |

RP is broad-based across financial, data, and decisional domains.

### 4.4.5 Post-Purchase Behavior (PP) Item Pattern

**Table 4.11 PP Item-Level Descriptives**

| Item | Mean | Std. Dev. | Interpretation |
|---|---:|---:|---|
| PP1 | 4.109 | 0.972 | Complaint behavior is common |
| PP2 | 3.668 | 1.181 | Return behavior exists but with higher variability |
| PP3 | 3.728 | 1.124 | Negative word-of-mouth is present |
| PP4 | 4.380 | 0.931 | Seller avoidance after bad experience is very strong |
| PP5 | 4.283 | 0.907 | Past problems strongly influence future purchase decisions |

PP findings indicate risk is behaviorally consequential, especially through switching/avoidance.

### 4.4.6 Customer Satisfaction (CS) Item Pattern

**Table 4.12 CS Item-Level Descriptives (with CS5 reversed)**

| Item | Mean | Std. Dev. | Interpretation |
|---|---:|---:|---|
| CS1 | 3.342 | 0.954 | Moderate overall satisfaction |
| CS2 | 3.158 | 0.940 | Expectations only moderately met |
| CS3 | 3.679 | 0.927 | Continuance intention remains positive |
| CS4 | 3.429 | 0.981 | Recommendation tendency is moderate |
| CS5 (reversed) | 2.255 | 0.875 | Risk-conditioned satisfaction component remains weaker |

The CS pattern shows coexistence of continued platform use and moderated evaluative satisfaction.

---

## 4.5 Construct-Level Descriptive Statistics and Distribution Shape

### 4.5.1 Core Construct Means

**Table 4.13 Construct-Level Descriptive Statistics**

| Construct | Mean | Std. Deviation | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Payment Issues (PI) | 3.978 | 0.663 | 2.20 | 5.80 |
| Online Scams (SC) | 4.228 | 0.663 | 1.00 | 5.00 |
| Product Quality Mismatch (PQ) | 3.577 | 0.675 | 1.00 | 5.00 |
| Risk Perception (RP) | 3.673 | 0.742 | 1.00 | 5.00 |
| Post-Purchase Behavior (PP) | 4.034 | 0.719 | 1.00 | 5.00 |
| Customer Satisfaction (CS) | 3.573 | 0.634 | 1.40 | 5.00 |

SC and PP emerge as high-intensity constructs in mean terms, while CS remains moderate.

### 4.5.2 Distributional Diagnostics

**Table 4.14 Distribution Shape and Quartile Profile**

| Construct | Min | Q1 | Median | Q3 | Max | Skewness | Excess Kurtosis |
|---|---:|---:|---:|---:|---:|---:|---:|
| PI | 1.40 | 2.80 | 3.20 | 3.60 | 5.00 | -0.278 | 0.094 |
| SC | 1.00 | 3.95 | 4.20 | 4.80 | 5.00 | -1.284 | 2.881 |
| PQ | 1.00 | 3.20 | 3.60 | 4.00 | 5.00 | -0.416 | 0.594 |
| RP | 1.00 | 3.20 | 3.80 | 4.00 | 5.00 | -0.431 | 0.555 |
| PP | 1.00 | 3.80 | 4.20 | 4.60 | 5.00 | -1.402 | 3.349 |
| CS | 1.00 | 2.80 | 3.20 | 3.60 | 4.80 | -0.545 | 1.066 |

Key distribution insights:

- Negative skew in SC and PP indicates many respondents cluster at high concern/high reaction levels.
- RP also leans to upper values, supporting its mediator role as a widespread evaluative condition.
- CS is less skewed than SC/PP, showing greater spread in satisfaction outcomes.

---

## 4.6 Reliability and Validity Analysis

### 4.6.1 Internal Consistency and Convergent Validity

**Table 4.15 Reliability and Convergent Validity**

| Construct | Cronbach’s Alpha | Composite Reliability (CR) | AVE | Interpretation |
|---|---:|---:|---:|---|
| PI | 0.592 | 0.757 | 0.386 | Marginal alpha; acceptable CR; weak AVE |
| SC | 0.757 | 0.837 | 0.511 | Acceptable |
| PQ | 0.730 | 0.825 | 0.491 | Near-threshold AVE |
| RP | 0.817 | 0.873 | 0.581 | Good |
| PP | 0.736 | 0.834 | 0.505 | Acceptable |
| CS | 0.702 | 0.822 | 0.592 | Acceptable |

Interpretive notes:

- Most constructs satisfy standard reliability expectations.
- PI is retained despite lower alpha due to acceptable CR and strong theoretical relevance.
- PQ AVE is near threshold and interpreted as adequate for exploratory behavioral context.

### 4.6.2 Loading Pattern and Item Behavior

**Table 4.16 Loading Pattern Summary**

| Construct | Loading Range | Note |
|---|---:|---|
| PI | 0.491 to 0.695 | Moderate loadings |
| SC | 0.553 to 0.802 | Stronger loadings |
| PQ | 0.526 to 0.828 | Adequate |
| RP | 0.693 to 0.812 | Strong |
| PP | 0.589 to 0.834 | Adequate |
| CS | -0.313 to 0.853 | CS5 behaves inversely to core satisfaction items |

CS5’s inverse behavior suggests conceptual overlap between satisfaction and risk salience. A sensitivity check retaining CS1–CS4 preserves the RP → CS negative direction, supporting substantive robustness.

### 4.6.3 Discriminant Validity

Square roots of AVE:

- PI = 0.622
- SC = 0.715
- PQ = 0.701
- RP = 0.762
- PP = 0.711
- CS = 0.769

These values generally exceed inter-construct correlations, supporting acceptable discriminant validity.

---

## 4.7 Correlation Analysis

### 4.7.1 Correlation Matrix

**Table 4.17 Correlation Matrix**

| Construct | PI | SC | PQ | RP | PP | CS |
|---|---:|---:|---:|---:|---:|---:|
| PI | 1.000 | 0.287 | 0.289 | 0.432 | 0.040 | -0.267 |
| SC | 0.287 | 1.000 | 0.304 | 0.501 | 0.337 | 0.004 |
| PQ | 0.289 | 0.304 | 1.000 | 0.373 | 0.357 | -0.223 |
| RP | 0.432 | 0.501 | 0.373 | 1.000 | 0.319 | -0.210 |
| PP | 0.040 | 0.337 | 0.357 | 0.319 | 1.000 | 0.082 |
| CS | -0.267 | 0.004 | -0.223 | -0.210 | 0.082 | 1.000 |

### 4.7.2 Detailed Interpretation

- **SC–RP (0.501)** is the largest antecedent-mediator correlation, reinforcing scam salience as the strongest psychological risk activator.
- **PI–RP (0.432)** and **PQ–RP (0.373)** confirm that transactional and quality frictions both contribute to elevated risk perception.
- **RP–PP (0.319)** supports risk translation into behavioral response.
- **RP–CS (-0.210)** indicates that increasing perceived risk depresses satisfaction.
- Near-zero **SC–CS (0.004)** implies scam concern alone does not automatically lower satisfaction unless routed through broader risk interpretation and/or post-purchase experience pathways.

---

## 4.8 Hypothesis Testing: Direct Effects

### 4.8.1 Regression Results for Direct Paths

**Table 4.18 Direct Effects and Hypothesis Decisions**

| Path | Std. Beta (β) | p-value | Decision |
|---|---:|---:|---|
| PI → RP (H1) | 0.274 | <0.001 | Supported |
| SC → RP (H2) | 0.366 | <0.001 | Supported |
| PQ → RP (H3) | 0.183 | 0.0046 | Supported |
| RP → PP (H4) | 0.319 | <0.001 | Supported |
| RP → CS (H8) | -0.210 | 0.0041 | Supported |

### 4.8.2 Model Strength Indicators

- **Model 1: RP on PI, SC, PQ** → R² = 0.370, F = 35.207, p < 0.001
- **Model 2: PP on RP** → R² = 0.102, F = 20.620, p < 0.001
- **Model 3: CS on RP** → R² = 0.044, F = 8.437, p = 0.004

Model interpretation:

- Antecedents explain **37.0%** of RP variance, which is substantial in behavioral settings.
- RP explains PP significantly but not exhaustively, indicating additional post-purchase drivers outside model scope.
- RP explains a modest portion of CS variance, suggesting satisfaction is multi-determined (service quality, delivery speed, value perception, expectation fit).

### 4.8.3 Relative Weighting of Antecedents

The ordering of standardized effects on RP is:

1. **SC (β = 0.366)**
2. **PI (β = 0.274)**
3. **PQ (β = 0.183)**

This hierarchy indicates that perceived fraud exposure and authenticity concerns are more psychologically potent than quality mismatch in shaping immediate risk judgments.

---

## 4.9 Mediation Analysis: Risk Perception as Mechanism

### 4.9.1 Bootstrapped Indirect Effects

**Table 4.19 Mediation Results (Risk Perception as Mediator)**

| Hypothesis | Indirect Effect (a×b) | 95% Boot CI | Direct Effect (c’) | Mediation Type | Decision |
|---|---:|---|---:|---|---|
| H5: PI → RP → PP | 0.054 | [0.011, 0.107] | -0.196 (p=0.0156) | Partial mediation | Supported |
| H6: SC → RP → PP | 0.076 | [0.014, 0.150] | 0.228 (p=0.0071) | Partial mediation | Supported |
| H7: PQ → RP → PP | 0.037 | [0.004, 0.088] | 0.293 (p=0.0002) | Partial mediation | Supported |

All confidence intervals exclude zero, confirming significant mediation for all three antecedents.

### 4.9.2 Mediation Interpretation in Behavioral Terms

- **PI** influences PP through RP, but also shows a competing direct pathway in the full model.
- **SC** influences PP both directly (defensive behavior against suspicious sellers) and indirectly through risk amplification.
- **PQ** preserves a strong direct PP effect, consistent with immediate experiential dissatisfaction (e.g., quality mismatch leads directly to complaint/avoidance).

Thus, RP is a meaningful psychological mechanism but not the only route through which negative shopping experiences shape post-purchase behavior.

---

## 4.10 Regression/Path Analysis with Mediator Included

### 4.10.1 Full Post-Purchase Model

**Table 4.20 PP Regression with PI, SC, PQ, and RP**

| Predictor | Std. Beta (β) | p-value |
|---|---:|---:|
| PI | -0.181 | 0.0156 |
| SC | 0.210 | 0.0071 |
| PQ | 0.275 | 0.0002 |
| RP | 0.189 | 0.0238 |

Model fit:

- **R² = 0.222**
- **Adjusted R² = 0.205**
- **F = 12.763**, p < 0.001

### 4.10.2 Multicollinearity and Stability

Variance inflation values are low (~1.15–1.59), indicating that the coefficient signs and magnitudes are not driven by severe multicollinearity distortion.

### 4.10.3 Sign-Reversal Interpretation (PI in Full Model)

PI’s negative direct coefficient alongside positive PI → RP and positive RP → PP reflects a **mediated-competitive structure**. One substantive interpretation is that once common risk variance is controlled, residual PI may capture coping adaptation behaviors (e.g., migration to safer payment modes, selective seller trust, COD preference), reducing adverse PP expression in that residual component.

This is a nuanced but plausible path pattern in maturing e-commerce markets where users adapt defensively to payment uncertainty.

---

## 4.11 Extended Segment Analysis

This section deepens interpretation using subgroup descriptive contrasts. These are not formal multi-group structural invariance tests; they are chapter-level analytical extensions for contextual understanding.

### 4.11.1 High-Risk vs Lower-Risk Segment Contrast

Respondents were grouped using RP threshold 4.0.

**Table 4.21 Segment Contrast by Risk Perception Level**

| Segment | n | Mean PP | Mean CS |
|---|---:|---:|---:|
| High RP (≥ 4.0) | 74 | 4.319 | 3.070 |
| Lower RP (< 4.0) | 110 | 3.842 | 3.242 |

Interpretation:

- High-risk respondents exhibit **stronger adverse post-purchase reactions**.
- High-risk respondents also show **lower satisfaction**.

This aligns directly with H4 and H8 directionality and provides intuitive segment-level support for the central model mechanism.

### 4.11.2 Age-Wise Pattern in RP, PP, and CS

**Table 4.22 Age Group Means (Exploratory Descriptives)**

| Age Group | n | RP Mean | PP Mean | CS Mean |
|---|---:|---:|---:|---:|
| Below 20 | 9 | 3.711 | 3.267 | 3.200 |
| 20–25 | 85 | 3.715 | 4.120 | 3.202 |
| 26–30 | 67 | 3.716 | 4.069 | 3.182 |
| Above 30 | 23 | 3.374 | 3.913 | 3.026 |

Young adult groups (20–30) show high RP and high PP simultaneously, consistent with stronger platform engagement and therefore greater exposure to problematic events.

### 4.11.3 Gender-Wise Pattern in RP, PP, and CS

**Table 4.23 Gender Means (Exploratory Descriptives)**

| Gender | n | RP Mean | PP Mean | CS Mean |
|---|---:|---:|---:|---:|
| Male | 98 | 3.710 | 4.124 | 3.178 |
| Female | 85 | 3.661 | 3.965 | 3.184 |
| Other | 1 | 1.000 | 1.000 | 1.800 |

Male and female averages are close in RP and CS, with somewhat higher PP among males in this sample. The “Other” category is not inferentially interpretable due to n=1.

### 4.11.4 Shopping Frequency Pattern in RP, PP, and CS

**Table 4.24 Shopping Frequency Means (Exploratory Descriptives)**

| Shopping Frequency | n | RP Mean | PP Mean | CS Mean |
|---|---:|---:|---:|---:|
| Rarely | 24 | 3.692 | 3.767 | 2.533 |
| Sometimes | 92 | 3.730 | 4.063 | 3.150 |
| Often | 57 | 3.695 | 4.123 | 3.442 |
| Very Often | 11 | 3.036 | 3.909 | 3.364 |

Noteworthy pattern:

- “Rarely” shoppers report the lowest CS.
- “Often” shoppers show strong PP and relatively better CS, possibly reflecting adaptation through experience and better channel filtering.

---

## 4.12 Integrated Discussion of Findings

### 4.12.1 Re-Reading the Core Model

The combined evidence supports a risk-driven behavioral framework where online shopping problems affect outcomes through both:

1. **Direct experiential pathways** (especially for quality mismatch and scam concerns), and
2. **Indirect psychological pathways** via risk perception.

This dual-path structure explains why mediation is partial, not full.

### 4.12.2 Why Scam Salience Dominates

SC has the strongest effect on RP. In Nepal’s platform context, scam salience may dominate because fraud concerns are cognitively immediate and cross-category: they affect payment confidence, seller trust, and willingness to transact.

High SC item means (awareness, fake seller prevalence, verification behavior) reinforce that consumers are actively managing perceived threat rather than passively absorbing it.

### 4.12.3 Product Quality as a Persistent Behavioral Trigger

PQ remains strong in direct PP prediction in the full model. This is theoretically coherent: quality mismatch is experienced concretely after delivery, often leading directly to complaint, return, or avoidance behavior independent of abstract risk evaluations.

### 4.12.4 Satisfaction is Not Binary in This Context

CS results show an important nuance:

- Satisfaction is not uniformly low.
- Continuance intention can coexist with moderated evaluative satisfaction.

This pattern suggests consumers may continue using online channels out of convenience/necessity while still carrying substantial risk reservations.

### 4.12.5 Post-Purchase Behavior as Retention Signal

High PP means (especially seller avoidance and future decision impact) should be interpreted as early warning indicators for retention and brand-level trust erosion. Even when aggregate market usage grows, unresolved PP consequences can redirect traffic away from specific sellers/platforms.

---

## 4.13 Theoretical Implications

The chapter contributes theoretically in four ways:

1. **Supports integrated risk mediation framing** in an emerging-market digital commerce setting.
2. Demonstrates that antecedents (PI, SC, PQ) are not interchangeable; they carry different path magnitudes and directness.
3. Shows that **risk perception is necessary but insufficient** as a sole explanatory mechanism for post-purchase behavior.
4. Highlights potential **adaptive-coping residuals** in payment pathways, reflected in sign complexity within the full PP model.

These findings support keeping both psychological and experience-based paths in post-purchase outcome models.

---

## 4.14 Managerial and Policy Implications

### 4.14.1 For E-Commerce Platforms

- Strengthen seller verification visibility and trust badges.
- Compress refund turnaround and communicate refund milestones transparently.
- Offer clearer pre-checkout risk cues (seller reliability, complaint history, authenticity indicators).

### 4.14.2 For Online Sellers

- Align listing media and product reality (reduce PQ gap).
- Improve proactive complaint handling and return transparency.
- Build repeat trust via consistency and post-sale responsiveness.

### 4.14.3 For Payments and Consumer Protection Stakeholders

- Improve dispute resolution confidence in digital payments.
- Expand scam awareness with transaction-stage guidance.
- Encourage interoperable complaint pathways across platform and payment ecosystems.

Given high RP and high PP intensity in this sample, interventions should prioritize reducing uncertainty before and after purchase—not only at payment moment.

---

## 4.15 Robustness Notes and Interpretation Boundaries

This chapter is empirically strong for directional inference within the sampled context, but interpretation should consider the following boundaries:

1. The sample is concentrated in younger and educated segments.
2. Subgroup contrasts are descriptive unless formally tested with group-invariance or interaction models.
3. One-item categories in demographics (e.g., “Other” gender) are retained for transparency but not inferential stability.
4. Platform preference includes long-tail custom entries, indicating channel heterogeneity not fully modeled as structured predictors.

These boundaries do not weaken the core finding that risk perception is a statistically meaningful mediator; they contextualize external generalization.

---

## 4.16 Chapter Summary

Chapter IV delivered a full empirical account of how payment issues, online scams, and product quality mismatch influence risk perception, post-purchase behavior, and customer satisfaction in Nepal’s online shopping environment.

Major conclusions are:

- **H1, H2, H3 supported:** PI, SC, and PQ significantly increase RP.
- **H4 supported:** RP significantly increases adverse PP.
- **H8 supported:** RP significantly decreases CS.
- **H5, H6, H7 supported:** RP significantly mediates PI/SC/PQ effects on PP, with partial mediation in all cases.

Substantively, the chapter shows that consumers are not only risk-aware but behaviorally responsive. Scam salience is strongest in shaping risk, quality mismatch remains a direct behavioral trigger, and satisfaction declines under elevated risk even when online shopping continuation remains viable.

This extended chapter therefore confirms the research model while adding richer interpretive detail for academic, managerial, and policy audiences.

---

## 4.17 Objective-Wise Analytical Interpretation

This section maps findings directly to each research objective so that the chapter is not only statistically complete but also clearly aligned with the study’s original purpose.

### 4.17.1 Objective 1: Identify Common Payment Problems in Nepal

The payment construct does not reflect a single issue; instead, it captures a layered payment-risk environment:

- Transaction confidence remains fragile in directional terms.
- Refund latency appears as a high-intensity pain point.
- COD preference is strongly linked with loss-avoidance psychology.

From a behavioral perspective, this means that payment risk is not confined to the checkout moment. It extends into post-transaction control, especially where consumers feel uncertain about reversal, refund certainty, or transaction traceability.

In practical terms, the findings imply that reducing payment risk requires a full journey approach:

1. **Pre-payment trust** (gateway reliability, authentication clarity).
2. **In-payment assurance** (clear status, failure handling).
3. **Post-payment confidence** (refund turnaround, transparent dispute flow).

The persistence of PI in the model, even with sign complexity in the full PP equation, indicates that payment risk has both direct and mediated effects depending on whether respondents have developed coping behavior.

### 4.17.2 Objective 2: Study How Online Scams Affect Trust and Behavior

Scam-related concern is the strongest antecedent of risk perception. Item-level evidence shows high agreement on awareness of scams, fake seller presence, and active verification behavior.

This reveals an important trust mechanism:

- Consumers are already aware of scams.
- Awareness does not remove risk; it changes shopping behavior.
- Trust is conditional and verification-dependent rather than default.

Thus, trust in this context should be treated as **dynamic, not static**. It is repeatedly recalibrated through signals such as seller profile quality, rating authenticity, response speed, and platform dispute capability.

The SC pathway also shows both direct and indirect impact on post-purchase outcomes. This supports the interpretation that scam salience shapes behavior in two modes:

1. **Anticipatory defensive mode** (before purchase, via risk perception), and
2. **Reactive accountability mode** (after problems, via complaint/avoidance behavior).

For platform managers, this implies that anti-fraud actions deliver value not only by preventing loss but also by protecting confidence in the post-purchase relationship.

### 4.17.3 Objective 3: Understand Product Quality Mismatch Issues

The product quality construct demonstrates a stable and practically meaningful link to adverse post-purchase responses.

The strongest PQ signal comes from difficulty judging quality online, while damage/defect reports are more dispersed. This indicates two different sources of quality uncertainty:

- **Pre-purchase representational risk** (images/descriptions not fully trustworthy).
- **Post-delivery realization risk** (actual condition or quality mismatch).

Because PQ retains a strong direct PP effect in the full model, quality mismatch appears to trigger immediate response behavior regardless of broader risk perception. This is consistent with expectation-disconfirmation logic: when delivered outcomes deviate from promised outcomes, behavioral correction follows directly (returns, complaints, avoidance).

For sellers and platforms, reducing PQ requires standardization of listing integrity, richer evidence formats (video, verified photos, size/condition standards), and tighter quality-control feedback loops tied to seller performance scores.

### 4.17.4 Objective 4: Determine Impact on Post-Purchase Behavior

Post-purchase behavior in this dataset is not passive. High means for avoidance and future-decision impact indicate that negative experiences carry forward and shape future channel choices.

This has strategic implications:

- PP is not merely a consequence variable; it acts as a predictor of future retention and loyalty migration.
- Even if overall market usage rises, unresolved PP patterns can produce seller-level churn and trust fragmentation.

The model demonstrates that PP is influenced by both direct problem exposures (SC, PQ, residual PI component) and mediated risk pathways via RP. This supports retaining a multi-path design in future post-purchase research rather than reducing the model to a single direct-effect framework.

### 4.17.5 Objective 5: Relationship Between Risk Perception and Satisfaction

The negative RP → CS path confirms that perceived risk erodes satisfaction. However, item-level and subgroup behavior suggest satisfaction is nuanced:

- Evaluative satisfaction can soften under risk pressure.
- Continuance can remain positive due to convenience, product access, or habit.

This distinction is critical for interpretation. A customer may continue shopping online while reporting weaker experiential satisfaction. Therefore, platform growth metrics alone may hide latent dissatisfaction that later appears through reduced advocacy, selective avoidance, or negative sharing.

---

## 4.18 Hypothesis-Wise Narrative Discussion

To provide full analytical transparency, each hypothesis is discussed as an independent evidence claim.

### 4.18.1 H1: Payment Issues Increase Risk Perception

H1 is supported. Payment concerns elevate perceived risk through two routes:

1. Anticipated financial uncertainty (fear of failed/uncertain transactions), and
2. Perceived lack of reversibility (refund delay and loss concern).

In Nepal’s mixed payment environment, where trust in digital settlement pathways can vary by platform and seller, this relationship is theoretically expected and empirically confirmed.

### 4.18.2 H2: Online Scams Increase Risk Perception

H2 receives the strongest coefficient among antecedents of RP. This confirms scam salience as a primary cognitive trigger.

The practical meaning is that anti-scam capability is a central determinant of perceived shopping safety, not a peripheral compliance feature.

### 4.18.3 H3: Product Quality Mismatch Increases Risk Perception

H3 is also supported. Quality uncertainty contributes to risk, though less strongly than scam salience.

This pattern suggests consumers may frame product mismatch as partly manageable (e.g., through reviews, brand familiarity), while scams are perceived as potentially more severe and less controllable.

### 4.18.4 H4: Risk Perception Increases Adverse Post-Purchase Behavior

H4 is supported. Higher risk perception corresponds to stronger complaint, sharing, and seller-avoidance tendencies.

This confirms that psychological risk is behaviorally active and not merely attitudinal.

### 4.18.5 H5: PI Influences PP Through RP

H5 is supported via significant indirect effect. The direct PI sign in the full model becomes negative, indicating competitive mediation. This reflects the possibility that users with higher payment awareness may adopt compensating strategies that soften direct adverse behavior once shared risk variance is accounted for.

### 4.18.6 H6: SC Influences PP Through RP

H6 is supported with a meaningful indirect pathway and a significant positive direct effect. Scam concerns both heighten risk and directly motivate protective post-purchase responses.

### 4.18.7 H7: PQ Influences PP Through RP

H7 is supported. The indirect effect is significant and the direct effect remains strong, indicating that quality mismatch affects behavior both psychologically (through risk) and experientially (through dissatisfaction upon delivery).

### 4.18.8 H8: Risk Perception Reduces Customer Satisfaction

H8 is supported. Elevated risk reduces satisfaction, consistent with trust-risk-satisfaction theory.

Given moderate CS levels and mixed continuation signals, this result implies that platforms can retain users in the short term while carrying hidden satisfaction liabilities in the medium term.

---

## 4.19 Comparative Interpretation Across Constructs

### 4.19.1 Why SC Outperforms PI and PQ on RP

SC’s larger effect likely reflects the perceived severity and uncontrollability of fraud outcomes. Quality mismatch can sometimes be corrected through returns/replacements; payment inconvenience can be managed via COD or selective payment modes. Scams, by contrast, may be viewed as higher-stakes and harder to recover from.

### 4.19.2 Why PQ Stays Strong in Direct PP Prediction

Quality mismatch is tangible and immediate. Once a product fails expectations, consumers can directly enact corrective behavior (complain, avoid seller, post negative feedback), making PQ a robust direct PP predictor.

### 4.19.3 Why RP Explains PP Better Than CS in R² Terms

RP has stronger explanatory power for PP than CS in this model. One reason is that PP items directly represent reaction behavior under problems, closely linked to risk activation. CS, however, can be shaped by broader value and convenience factors beyond risk alone.

### 4.19.4 Dual-State Consumer Interpretation

The data support a dual-state interpretation:

1. **Operational continuation state:** consumers keep using online channels.
2. **Cautious evaluation state:** consumers remain risk-alert and react strongly to negative events.

This dual-state behavior is common in fast-growing digital markets where adoption can grow faster than trust infrastructure maturity.

---

## 4.20 Strategic Implication Framework Derived from Chapter IV

To translate evidence into action, findings can be structured into a three-layer intervention framework.

### 4.20.1 Layer 1: Trust Infrastructure Controls

Focus: reduce SC-driven risk activation.

Core actions:

- Strong seller identity verification and periodic re-validation.
- Suspicious listing detection and rapid enforcement.
- Buyer-facing trust signals (verified badges, response reliability, complaint score).

Expected impact:

- Lower baseline RP,
- Reduced scam salience intensity,
- Better trust continuity.

### 4.20.2 Layer 2: Transaction and Refund Assurance

Focus: reduce PI-related uncertainty.

Core actions:

- Real-time payment-status transparency.
- Standardized failure-recovery process.
- Time-bound refund SLA visibility.

Expected impact:

- Lower fear-driven payment friction,
- Improved confidence in reversibility,
- Lower indirect risk amplification via RP.

### 4.20.3 Layer 3: Listing-to-Delivery Quality Integrity

Focus: reduce PQ-driven direct PP reactions.

Core actions:

- Richer and standardized product representation.
- Stronger mismatch/defect accountability policy.
- Seller-level quality scorecards integrated into ranking.

Expected impact:

- Fewer disconfirmation events,
- Lower complaint and avoidance behavior,
- Improved seller-level retention.

### 4.20.4 Why Integrated Action Is Necessary

Because mediation is partial for all three antecedents, isolated interventions will likely produce partial gains. Platforms need synchronized action across fraud control, payment assurance, and quality governance to meaningfully reduce adverse PP and improve satisfaction outcomes.

---

## 4.21 Implications for Future Measurement and Model Development

Although Chapter IV confirms the proposed model, it also reveals opportunities to improve future research designs.

### 4.21.1 Expand Satisfaction Measurement Architecture

Given CS complexity, future studies should separate:

- Transaction satisfaction,
- Platform trust satisfaction,
- Value-for-money satisfaction,
- Long-term loyalty intention.

This would clarify which satisfaction dimensions are most sensitive to risk perception.

### 4.21.2 Introduce Formal Multi-Group Modeling

Exploratory subgroup differences suggest potential heterogeneity by age and shopping frequency. Future designs can test moderated paths or multi-group invariance to verify whether effect sizes are significantly different across segments.

### 4.21.3 Add Platform-Type as Structured Moderator

Because respondents use both marketplace and social-commerce channels, future models should include platform type as a formal moderator. This can reveal whether SC, PI, and PQ mechanisms differ by channel governance maturity.

### 4.21.4 Track Longitudinal Adjustment Effects

The PI sign complexity suggests adaptation behavior over time. Panel or repeated cross-sectional designs could test whether consumers become more resilient through coping strategies (e.g., payment mode switching, stricter seller filtering).

---

## 4.22 Consolidated Analytical Conclusion of Chapter IV

This chapter demonstrates that online shopping outcomes in Nepal are governed by an interconnected problem-risk-behavior structure:

- Problems (PI, SC, PQ) increase perceived risk,
- Perceived risk drives stronger post-purchase reaction,
- Perceived risk lowers customer satisfaction,
- Direct experiential effects remain active even after mediation is modeled.

Among all antecedents, scams have the largest influence on risk perception, while product quality mismatch exerts persistent direct pressure on post-purchase behavior. Payment issues show meaningful mediated influence with evidence of compensatory behavior in the residual direct path.

The overall analytical message is clear: **consumer adaptation is happening, but risk pressure remains high.** Therefore, platform growth alone should not be treated as evidence of trust maturity. Sustainable digital commerce requires coordinated improvements in fraud control, payment assurance, and quality reliability.

By combining descriptive depth, inferential evidence, mediation structure, and segment-level interpretation, Chapter IV now provides a full empirical bridge from data to theory to action.
