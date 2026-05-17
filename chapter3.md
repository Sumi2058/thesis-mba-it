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

## 3.12 Data Screening, Cleaning, and Preparation Protocol

Before estimating any statistical model, the dataset was screened and prepared using a stepwise protocol to ensure analytical consistency and measurement integrity. The objective of this phase was to remove avoidable noise, verify coding logic, and produce construct-level variables suitable for inferential testing.

### 3.12.1 Data Integrity Checks

The first stage of cleaning focused on structural integrity of the CSV dataset. This included:

- verification of row-level completeness across mandatory fields,
- confirmation that all psychometric items were represented with numeric entries,
- checking for duplicate submissions based on timestamp proximity and response pattern similarity,
- and inspection for out-of-range values outside the expected Likert limits.

No values were found outside the administered 1–5 coding frame for construct items. Demographic fields were also examined for nonsensical labels, typographical variants, and inconsistent category naming. Where minor category spelling differences appeared, category harmonization was applied to preserve comparability in descriptive analysis.

### 3.12.2 Missing Data Handling

Because model estimation required complete information on all construct indicators, only records with complete psychometric entries were retained. This complete-case approach was selected for three reasons. First, the proportion of missingness in construct indicators was minimal. Second, imputation methods can introduce additional assumptions regarding response behavior. Third, the sample size remained sufficient for regression and mediation analysis after screening.

For transparency, missing-data treatment followed the rule:

1. If a respondent missed one or more required construct items, the case was excluded from multivariate model estimation.
2. If demographic variables were missing but psychometric indicators were complete, the case could still be retained for inferential model testing while being omitted from specific demographic cross-tabulations where required.
3. No synthetic responses were generated.

This conservative process supports the internal consistency of construct-level estimates and avoids distortion from arbitrary imputation.

### 3.12.3 Outlier and Response Pattern Screening

Outlier diagnostics were performed at both item and construct levels. Since all key constructs were measured through bounded Likert scales, extreme values were not automatically treated as errors. Instead, outliers were evaluated for plausibility through response patterns. Two forms of unusual patterns were reviewed:

- straight-lining behavior (same response option selected for almost all items),
- and contradictory response combinations (e.g., very low perceived risk with very high fear statements in closely related indicators).

Cases showing possible low-engagement patterns were cross-checked against completion quality. Because the retained sample remained internally coherent and reliability indicators were acceptable, no additional outlier-based deletion rule was applied beyond completeness criteria.

### 3.12.4 Reverse Coding and Directional Alignment

Several indicators in the instrument were positively phrased while other indicators in the same construct were negatively framed. To ensure that higher composite scores consistently represented higher intensity of the intended construct meaning, reverse coding was applied to directionally opposite items before index construction. This step was essential to prevent attenuation of reliability and artificial suppression of inter-item correlations.

Directional alignment procedures were documented and reproducible:

- original and transformed coding definitions were stored in analysis notes,
- transformed values were rechecked against expected min/max limits,
- and post-transformation descriptive checks confirmed plausible score distributions.

### 3.12.5 Composite Score Construction

Construct-level variables were formed by averaging the five aligned items per construct. Mean-based composite scoring was preferred over summed scoring because mean indices preserve interpretability within the original scale range. For example, a mean score of 4.0 directly indicates a high level of agreement/intensity on a 1–5 scale.

The following composites were generated:

- PI_mean, SC_mean, PQ_mean for the exogenous predictors,
- RP_mean for the mediator,
- PP_mean and CS_mean for outcome constructs.

Where necessary for reporting clarity, construct labels were translated into full narrative terms in tables and interpretation text.

### 3.12.6 Pre-Analysis Documentation

All cleaning and preparation decisions were documented before hypothesis testing to reduce researcher degrees of freedom. The sequence of operations (screening, coding checks, reverse coding, composite construction, reliability testing, inferential modeling) was locked prior to final coefficient interpretation. This practice strengthens methodological transparency and makes results easier to audit.

---

## 3.13 Respondent Profiling Framework

Descriptive profiling was conducted not only to summarize who participated in the study, but also to contextualize interpretation of risk-related perceptions and post-purchase reactions. Because online shopping behavior is often shaped by age, education, digital familiarity, and shopping frequency, respondent profiling was treated as an analytical foundation rather than a purely descriptive annex.

### 3.13.1 Demographic Dimensions

The following profile dimensions were extracted from the survey:

- age group,
- gender,
- education level,
- occupation category,
- shopping frequency,
- and preferred online platform/channel.

Each dimension was summarized through frequency and percentage tables. Percentages were interpreted carefully in relation to category base sizes to avoid overstatement of small subgroup variations.

### 3.13.2 Behavioral Relevance of Profile Variables

Although the main hypothesis model focuses on latent constructs, demographic patterns provide interpretive depth. For example:

- higher shopping frequency may coincide with higher scam awareness due to exposure,
- education level may affect ability to evaluate platform credibility,
- and occupation may indirectly influence both purchasing power and complaint behavior after poor purchase outcomes.

Therefore, profile findings were considered as contextual inputs for discussing why some construct means may be elevated or suppressed in Chapter IV.

### 3.13.3 Descriptive Quality Standards

To maintain methodological quality, descriptive reporting followed these standards:

1. Present both absolute frequency and percentage.
2. Use mutually exclusive and collectively meaningful category labels.
3. Avoid causal language in descriptive sections.
4. Maintain consistency in table totals and denominator definitions.
5. Distinguish between valid percent and total percent when exclusions apply.

This approach ensured that respondent profiling remained objective and useful for later interpretation of inferential findings.

---

## 3.14 Measurement Model Detailing

The present study employed a multi-construct measurement model where each latent concept was represented by five reflective indicators. This section expands the operational logic, indicator intent, and construct-domain boundaries to strengthen conceptual clarity.

### 3.14.1 Payment Issues (PI)

Payment Issues capture frictions or uncertainty during payment and refund stages. The construct includes concerns such as:

- fear of transaction failure,
- delayed refunds,
- payment gateway reliability,
- confidence in payment completion,
- and payment-mode trust.

In Nepal's evolving digital commerce environment, payment reliability remains a central determinant of perceived transactional safety. PI indicators were designed to reflect both technical and psychological dimensions of payment experience.

### 3.14.2 Online Scams (SC)

Online Scams represent perceived exposure to fraudulent sellers, deceptive listings, and trust-breaking experiences in online marketplaces. Indicators capture:

- fear of being deceived,
- awareness of scam incidents,
- confidence in seller legitimacy checks,
- perceived prevalence of fake sellers,
- and trust erosion due to scam narratives.

This construct is especially relevant in social-commerce and marketplace contexts where seller verification quality varies.

### 3.14.3 Product Quality Mismatch (PQ)

Product Quality Mismatch measures the gap between expected and received product characteristics. Indicator coverage includes:

- mismatch between displayed and received product,
- perceived inferior quality,
- concern regarding misleading descriptions,
- probability of defects,
- and uncertainty around authenticity or durability.

PQ is operationalized as a post-purchase realization risk that can influence future buying behavior and dissatisfaction outcomes.

### 3.14.4 Risk Perception (RP)

Risk Perception is conceptualized as the consumer's cognitive evaluation of possible adverse outcomes in online shopping. It integrates:

- financial risk,
- data/privacy concern,
- uncertainty before ordering,
- perceived vulnerability to platform or seller misconduct,
- and anticipated regret in case of transaction failure.

As the mediating construct, RP links transactional/experience stressors (PI, SC, PQ) with behavioral outcomes (PP, CS).

### 3.14.5 Post-Purchase Behavior (PP)

Post-Purchase Behavior captures reactive tendencies after negative or uncertain shopping outcomes. Measured behaviors include:

- complaint intention,
- product return tendency,
- negative word-of-mouth sharing,
- avoidance of previously used sellers/platforms,
- and caution in future transactions.

Higher PP scores in this model indicate stronger corrective/defensive responses rather than passive acceptance.

### 3.14.6 Customer Satisfaction (CS)

Customer Satisfaction assesses the evaluative outcome of online purchase experience. Indicators capture:

- overall satisfaction,
- expectation-performance congruence,
- willingness to continue online shopping,
- recommendation inclination,
- and perceived impact of risk factors on satisfaction.

Within the integrated model, CS provides a complementary outcome perspective to PP by reflecting emotional and attitudinal evaluation.

### 3.14.7 Reflective Measurement Rationale

All constructs were specified as reflective because indicators are assumed to be manifestations of an underlying latent perception domain. Changes in latent risk concerns are expected to produce corresponding directional movement across associated indicators. This model choice aligns with prior e-commerce trust-risk studies and supports reliability and validity procedures used in Chapter IV.

---

## 3.15 Reliability and Validity Evaluation Plan

Measurement quality was assessed through a layered evaluation plan combining internal consistency checks, convergent validity indicators, and discriminant validity diagnostics. This section specifies the decision criteria used.

### 3.15.1 Internal Consistency Reliability

Cronbach's alpha was used as the baseline reliability metric for each construct. Interpretation followed standard cutoffs used in behavioral studies:

- alpha ≥ 0.70: acceptable,
- alpha ≥ 0.80: good,
- alpha ≥ 0.90: excellent (subject to redundancy caution).

Constructs below 0.70 were flagged for item-level inspection before final inferential interpretation.

### 3.15.2 Composite Reliability (CR)

CR complements alpha by incorporating standardized loading contributions and is less sensitive to equal-loading assumptions. The accepted threshold was CR ≥ 0.70. CR values were interpreted alongside alpha to ensure convergent evidence of reliability.

### 3.15.3 Average Variance Extracted (AVE)

AVE was used to assess convergent validity, with AVE ≥ 0.50 indicating that the construct explains at least half of variance in its indicators on average. Where AVE approached threshold values, interpretation considered the balance between AVE, loadings, and reliability metrics.

### 3.15.4 Discriminant Validity Logic

Discriminant validity was examined by comparing inter-construct correlations and conceptual overlap risk. If two constructs showed excessively high correlation, theoretical distinctiveness and item content separation were reviewed before drawing path-level conclusions.

### 3.15.5 Item-Level Diagnostic Rules

Indicators with weak loading patterns, strong cross-domain ambiguity, or reliability suppression potential were subject to diagnostic review. However, item removal decisions were made cautiously to preserve content validity and comparability with adapted literature scales.

### 3.15.6 Reporting Standards

Reliability and validity outputs were reported in structured tables including:

- alpha, CR, and AVE per construct,
- indicator-level loadings,
- and a correlation matrix for construct-level relationships.

This reporting format supports transparent evaluation of measurement adequacy before structural inference.

---

## 3.16 Inferential Modeling Strategy

Hypothesis testing required a structured inferential sequence to avoid misinterpretation of direct and indirect relationships. The strategy comprised progressive modeling stages from bivariate association to mediated path estimation.

### 3.16.1 Correlation Stage

Pearson correlation coefficients were first computed to establish linear association direction and preliminary strength among constructs. Correlation findings were interpreted as association evidence only, not causation proof.

### 3.16.2 Regression Stage for Direct Effects

Ordinary least squares regression was used to estimate:

1. RP_mean as a function of PI_mean, SC_mean, and PQ_mean,
2. PP_mean as a function of RP_mean,
3. CS_mean as a function of RP_mean.

These models directly map onto the proposed hypothesis structure and provide coefficient-level evidence for direct-path hypotheses.

### 3.16.3 Expanded PP Model for Mediation Context

An additional PP model including PI_mean, SC_mean, PQ_mean, and RP_mean was estimated to separate:

- direct effects of exogenous risk drivers on post-purchase behavior,
- and mediated effects transmitted through RP_mean.

This decomposition improves interpretive precision when discussing whether perceived risk partially or substantially channels predictor impacts.

### 3.16.4 Significance and Practical Interpretation

Statistical significance was evaluated using p-values and confidence intervals, while practical interpretation considered coefficient magnitude and theoretical plausibility. Emphasis was placed on substantive meaning, not only threshold crossing.

### 3.16.5 Multicollinearity Monitoring

Because PI, SC, and PQ are conceptually related risk domains, multicollinearity diagnostics were reviewed to ensure stable coefficient estimation. Where predictor correlations were moderate, coefficients were interpreted with caution and in conjunction with overall model fit indications.

---

## 3.17 Mediation Analysis Procedure

Mediation hypotheses (H5–H7) require evaluation of whether risk perception carries part of the influence of PI, SC, and PQ on post-purchase behavior. To improve robustness beyond stepwise significance logic alone, a bootstrap-based indirect effect approach was used.

### 3.17.1 Conceptual Path Structure

For each exogenous predictor (X), mediation follows:

- a path: X → RP_mean,
- b path: RP_mean → PP_mean,
- c' path: X → PP_mean controlling RP_mean,
- indirect effect: a × b.

Significant indirect effects indicate mediation presence.

### 3.17.2 Bootstrap Resampling Rationale

Indirect effects often have non-normal sampling distributions. Therefore, bootstrap confidence intervals provide more reliable inference than normal-theory approximations. Repeated resampling was used to estimate the empirical distribution of a × b for each predictor-specific mediation path.

### 3.17.3 Decision Rules

Mediation interpretation followed:

1. If bootstrap confidence interval for a × b excludes zero, the indirect effect is supported.
2. If both indirect and direct effects are significant in same direction, partial mediation is inferred.
3. If indirect effect is significant while direct effect becomes weak/non-significant, stronger mediation evidence is indicated.

### 3.17.4 Comparative Mediation Strength

To discuss managerial relevance, standardized or scale-consistent effect comparisons were used to identify which antecedent (PI, SC, or PQ) transmits the strongest mediated impact through risk perception. This comparison supports prioritization of practical interventions.

---

## 3.18 Assumption Testing and Diagnostic Framework

Regression and mediation interpretations were supported by standard diagnostic checks to ensure that model assumptions were sufficiently met for valid inference.

### 3.18.1 Linearity

Construct relationships were reviewed for approximate linear trends. Given the aggregated nature of construct means and the bounded Likert framework, linear approximation was considered acceptable for explanatory modeling.

### 3.18.2 Independence of Errors

Survey responses were collected at the individual level with one record per respondent. The design did not involve repeated measures on the same respondent in the analytical file, supporting independence assumptions for residual errors.

### 3.18.3 Homoscedasticity

Residual spread consistency across fitted values was checked through diagnostic plotting logic. Minor heteroscedastic tendencies, if observed, were interpreted cautiously in terms of standard error robustness and substantive conclusions.

### 3.18.4 Normality of Residuals

Residual normality was assessed at a practical level because inferential focus included confidence intervals and bootstrapped indirect effects, which reduce strict dependency on normality in mediation estimation.

### 3.18.5 Influential Observations

Influence diagnostics were considered to ensure no small set of cases disproportionately drove coefficients. Unless extreme influence evidence was present, all valid cases were retained to preserve representativeness of observed response diversity.

### 3.18.6 Multicollinearity

Variance inflation indicators and predictor correlation patterns were reviewed to avoid unstable coefficient interpretation. Predictors were conceptually related but sufficiently distinct in domain meaning, allowing simultaneous inclusion in models.

---

## 3.19 Bias Control and Threats to Validity

Cross-sectional self-report survey research is vulnerable to specific validity threats. This section documents how these risks were recognized and mitigated.

### 3.19.1 Common Method Bias Risk

Because predictors, mediator, and outcomes were collected from the same instrument, common method variance can inflate observed associations. Mitigation steps included:

- construct separation in questionnaire flow,
- use of multiple-item scales with varied wording orientation,
- reverse coding of selected items,
- and interpretation that avoids overstating causal certainty.

### 3.19.2 Social Desirability Bias

Participants may underreport risky behavior or overstate cautious behavior. Neutral, non-judgmental item wording and anonymous response handling were used to reduce evaluation apprehension.

### 3.19.3 Sampling Bias

Convenience sampling may overrepresent digitally active and urban-linked respondents. The study addresses this by clearly delimiting generalization scope and by encouraging respondent diversity through multiple outreach channels.

### 3.19.4 Recall and Perception Bias

Some questions rely on respondent memory of past transactions or subjective risk interpretation. To reduce recall burden, items were phrased around recent or typical experiences rather than requiring highly specific historical details.

### 3.19.5 Non-Response Bias Consideration

Although complete non-response tracking was limited in open digital sharing mode, completion-based screening and consistency checks were used to ensure that retained cases represent engaged respondents.

### 3.19.6 Construct Contamination Risk

Risk-related constructs can partially overlap conceptually. This was addressed through:

- explicit construct definitions,
- indicator mapping to unique conceptual domains,
- and discriminant-validity-focused interpretation.

These safeguards improve confidence that observed relationships represent meaningful theoretical links rather than mere wording overlap.

---

## 3.20 Ethical Governance and Responsible Data Use (Expanded)

The ethical framework of this study extends beyond procedural consent to include responsible analysis, interpretation restraint, and respect for participant dignity.

### 3.20.1 Voluntary Participation

Participation was fully voluntary. Respondents were not coerced, and participation did not involve mandatory institutional pressure. The survey context emphasized participant discretion over whether to respond.

### 3.20.2 Confidentiality and Anonymity

The analytical dataset excluded personally identifying information. Findings are presented in aggregate form, and no individual-level response is singled out in a manner that could expose identity.

### 3.20.3 Minimal-Risk Research Context

The study addressed consumer perceptions and post-purchase responses, which generally constitute minimal-risk social research. Even so, careful wording was maintained to avoid inducing fear or discomfort.

### 3.20.4 Data Storage and Access Control

Data were treated as academic research material and used solely for thesis analysis. Access was limited to research processing needs, and no commercial reuse or third-party distribution was pursued.

### 3.20.5 Citation Integrity and Intellectual Honesty

Instrument adaptation and theoretical framing were grounded in prior scholarly work with proper acknowledgment. Statistical findings are reported transparently without selective omission of contradictory patterns.

### 3.20.6 Ethical Interpretation Principle

The study avoids stigmatizing language toward any demographic group, platform category, or seller class. Interpretation is framed around system-level risk management and consumer protection implications rather than blame assignment.

---

## 3.21 Chapter-Specific Limitations and Delimitations

Methodological rigor requires explicit identification of what the study can and cannot claim. The following delimitations and limitations guide interpretation.

### 3.21.1 Delimitations

The study is deliberately delimited to:

- online shoppers in Nepal with prior purchase experience,
- a quantitative questionnaire-based design,
- six focal constructs central to trust-risk-post-purchase dynamics,
- and cross-sectional data collected within a specific study window.

These boundaries allowed focused model testing aligned with thesis objectives.

### 3.21.2 Limitations

Despite rigorous procedures, several limitations remain:

1. Non-probability sampling constrains strict population-level generalization.
2. Cross-sectional data limits temporal and causal certainty.
3. Self-reported perceptions may contain subjective distortions.
4. Platform-type and product-category heterogeneity are not fully modeled as moderators.
5. External shocks (policy changes, major scam incidents, payment infrastructure changes) may alter perceptions over time.

Acknowledging these limitations supports honest interpretation and identifies opportunities for future research refinement.

### 3.21.3 Implications for Future Methodology

Future studies can build on this framework by:

- applying stratified or probability-based sampling designs,
- using longitudinal data to observe risk perception shifts over time,
- incorporating behavioral transaction records where ethically feasible,
- testing moderation by age, digital literacy, and platform governance quality,
- and combining survey findings with qualitative narratives for deeper mechanism explanation.

These directions can strengthen both external validity and theoretical specificity in Nepal-focused e-commerce risk research.

### 3.21.4 Operational Timeline of Method Execution

To preserve procedural discipline, the research process followed a phased operational timeline. This sequencing helped reduce analytical drift and ensured that each methodological decision was made at the appropriate stage rather than being adjusted retroactively after observing key results.

**Phase 1: Conceptual and Design Finalization**

During this phase, the research problem, objectives, and hypotheses were aligned with Chapter I and Chapter II. Construct boundaries were specified to avoid conceptual overlap in item selection. At this stage, the primary concern was internal coherence between theory and measurable variables.

**Phase 2: Instrument Structuring and Field Preparation**

The survey instrument was organized into demographic and construct sections. Wording was reviewed for clarity, local contextual relevance, and response burden. The response coding structure was prepared in advance to minimize later transformation complexity.

**Phase 3: Data Collection Window**

Responses were collected through digital distribution channels. The key operational objective in this phase was obtaining adequate variation across respondent backgrounds while maintaining the minimum case requirement for multivariate testing.

**Phase 4: Data Screening and Coding Alignment**

Raw responses were screened for completeness and coding consistency. Reverse-coded items were transformed in a controlled sequence, and construct composites were built only after item orientation was harmonized.

**Phase 5: Measurement Quality Assessment**

Reliability and validity diagnostics were run before inferential regression modeling. This phase established whether construct indices were sufficiently robust for path-level interpretation.

**Phase 6: Hypothesis Testing and Mediation Estimation**

Direct and indirect path models were estimated according to predefined equations. Results were interpreted in relation to the hypothesis map and theoretical expectations.

**Phase 7: Interpretation, Cross-Checking, and Reporting**

Final interpretation incorporated both statistical evidence and contextual plausibility. Reporting emphasized transparent disclosure of assumptions, limitations, and analytical boundaries.

This phased execution model reduces the risk of selective reporting and supports replicability at the chapter level.

### 3.21.5 Variable Transformation and Analytical Coding Matrix

To improve methodological traceability, each variable class was assigned a coding role in the analysis workflow. The matrix below summarizes analytical treatment:

| Variable Class | Examples | Analytical Use | Transformation Rule |
|---|---|---|---|
| Demographic categorical | age group, gender, occupation | Descriptive profile tables | Standard category harmonization only |
| Behavioral categorical | shopping frequency, preferred platform | Contextual segmentation | Ordered labels retained where meaningful |
| Item-level psychometric | PI1–PI5, SC1–SC5, PQ1–PQ5, RP1–RP5, PP1–PP5, CS1–CS5 | Reliability and construct formation | Reverse-code directional items, then scale-check |
| Construct composites | PI_mean, SC_mean, PQ_mean, RP_mean, PP_mean, CS_mean | Correlation and regression models | Mean index computation from aligned items |
| Mediation path variables | X, RP_mean, PP_mean | Indirect effect estimation | Bootstrap resampling paths a, b, and a×b |

This matrix-driven coding process ensured that transformations remained consistent across descriptive and inferential stages. It also reduced risks of accidental variable redefinition during iterative analysis.

### 3.21.6 Statistical Interpretation Protocol

The study adopted a multi-criteria interpretation protocol to avoid overreliance on any single statistic. For each hypothesis-relevant relationship, interpretation considered:

1. **Direction consistency** with theoretical expectation.
2. **Statistical significance** (p-value and confidence interval logic).
3. **Effect magnitude** in practical behavioral terms.
4. **Model context**, including other predictors and potential shared variance.
5. **Measurement confidence**, informed by reliability/validity diagnostics.

This protocol is important because e-commerce behavior research often shows statistically significant but practically small effects, especially when multiple risk constructs overlap conceptually. The chapter therefore prioritizes balanced interpretation: significance is necessary for support claims, but substantive relevance determines managerial usefulness.

### 3.21.7 Construct-Level Interpretation Anchors

To strengthen consistency in Chapter IV interpretation, construct-specific anchors were predefined.

**Payment Issues (PI)**
- High PI_mean indicates elevated concern about payment reliability and refund processes.
- Interpretation anchor: transactional friction and financial process confidence.

**Online Scams (SC)**
- High SC_mean reflects stronger perceived exposure to fraudulent marketplace behavior.
- Interpretation anchor: trust fragility and fraud awareness climate.

**Product Quality Mismatch (PQ)**
- High PQ_mean indicates stronger expectation-reality gaps in product outcomes.
- Interpretation anchor: post-delivery reliability and informational authenticity.

**Risk Perception (RP)**
- High RP_mean reflects broad apprehension regarding adverse online shopping outcomes.
- Interpretation anchor: cumulative perceived vulnerability.

**Post-Purchase Behavior (PP)**
- High PP_mean represents stronger corrective, defensive, or retaliatory reactions.
- Interpretation anchor: behavioral response intensity after unfavorable experiences.

**Customer Satisfaction (CS)**
- High CS_mean indicates positive evaluative outcomes and stronger continuance orientation.
- Interpretation anchor: outcome evaluation and loyalty tendency.

By defining these anchors in advance, the chapter minimizes interpretive ambiguity when discussing coefficient signs and association patterns.

### 3.21.8 Procedural Controls for Result Credibility

The credibility of quantitative findings depends not only on statistical formulas but also on procedural discipline. The following controls were embedded in this study:

- **Predefined sequencing:** cleaning and measurement checks completed before path estimation.
- **Consistent scale treatment:** all construct items retained within the same 1–5 coding logic after transformation.
- **Transparent exclusion rule:** incomplete psychometric records excluded uniformly.
- **No post-hoc hypothesis rewriting:** inferential focus remained tied to originally defined hypotheses.
- **Cross-table verification:** key descriptive totals checked before inferential interpretation.
- **Cautious language policy:** association findings not overstated as deterministic causality.

These controls align with graduate-level research quality expectations and improve confidence that reported findings reflect observed data patterns rather than analysis-stage artifacts.

### 3.21.9 Analytical Decision Audit Trail

An internal audit trail was maintained to document why major analytical decisions were made. The audit trail included:

- rationale for adopting complete-case analysis,
- justification for reverse coding specific indicators,
- reasons for using mean-based composites,
- basis for selecting regression and bootstrap mediation tests,
- and explanation of generalization boundaries under convenience sampling.

The purpose of this audit trail is twofold. First, it supports methodological defensibility during academic review and viva discussions. Second, it allows future researchers to replicate or extend the model with clear understanding of decision points.

### 3.21.10 Sensitivity Awareness in Cross-Sectional Designs

Although this study does not claim strict causal proof, a sensitivity-aware interpretation framework was used to reduce common misreadings of cross-sectional findings. The framework recognizes that:

- relationships can be meaningful even without temporal sequencing,
- mediation in cross-sectional data indicates plausible process structure but not definitive temporal mechanism,
- and effect estimates may shift if macro-level trust events (e.g., high-profile scam incidents) occur between data windows.

Accordingly, results are interpreted as evidence of structured association consistent with theory, while recommending longitudinal validation for stronger temporal claims.

### 3.21.11 External Utility of the Methodological Model

The methodology developed in this chapter has practical transfer value beyond this single thesis context. With minor adaptation, the same model can be applied to:

- specific platform ecosystems (marketplace-only or social-commerce-only studies),
- sector-focused products (electronics, fashion, groceries, services),
- or comparative city-level trust-risk studies across Nepal.

The six-construct structure and mediation architecture provide a scalable framework for evaluating how transactional and experiential risks propagate into satisfaction and behavioral responses.

For practitioners, the model supports risk-priority diagnosis:

- If PI effects dominate, payment infrastructure and refund governance interventions become urgent.
- If SC effects dominate, seller verification and fraud communication controls should be prioritized.
- If PQ effects dominate, product authenticity assurance and listing quality governance become central.

Thus, the methodological framework is not only statistically testable but also managerially interpretable for e-commerce risk governance.

---

## 3.22 Chapter Summary

Chapter III established the full methodological architecture used to examine how payment issues, online scams, and product quality mismatch influence post-purchase behavior and customer satisfaction through risk perception among online shoppers in Nepal. The chapter detailed the quantitative, deductive, cross-sectional research design; justified population and sampling choices; documented instrument development and construct operationalization; and defined data collection and ethical protocols.

Beyond standard methodology coverage, the chapter provided expanded procedures for data cleaning, reverse coding, composite score construction, respondent profiling, measurement-quality evaluation, inferential sequencing, mediation estimation, assumption diagnostics, and bias mitigation. This integrated protocol ensures that Chapter IV results are interpreted from a transparent and methodologically defensible base.

In summary, the chapter demonstrates that the empirical strategy is coherent with the study's theoretical model, suitable for the available data context, and sufficiently rigorous for hypothesis testing at the MBA graduate research level.

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
