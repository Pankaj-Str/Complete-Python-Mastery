# Hypothesis Testing
**By Codes with Pankaj**  
---

### 1. What is Hypothesis Testing?

**Hypothesis Testing** is a statistical method used to make decisions or draw conclusions about a population based on sample data.

Think of it like a **court trial**:
- You have a **claim** (hypothesis).
- You collect **evidence** (data).
- You decide whether to **reject** the claim or **not reject** it.

**Real-life Example**:  
A medicine company claims their new drug reduces headache pain in less than 30 minutes on average.  
You test this claim using data from patients.

---

### 2. Null Hypothesis (H₀) vs Alternative Hypothesis (H₁)

- **Null Hypothesis (H₀)**: The "status quo" or "no effect" assumption. It is what we try to disprove.  
  Usually contains **=**, **≥**, or **≤**.

- **Alternative Hypothesis (H₁)**: What we actually believe or want to prove.  
  Contains **≠**, **>**, or **<**.

**Example**:
- H₀: Average time to reduce headache = 30 minutes (no improvement)
- H₁: Average time to reduce headache < 30 minutes (drug is better)

**Key Point**: We never "prove" H₁. We only say **"Reject H₀"** or **"Fail to reject H₀"**.

---

### 3. Significance Level (α) - The Risk Threshold

**α (alpha)** is the probability of making a **Type I error** (explained below).  
Common values: **0.05 (5%)** or **0.01 (1%)**.

- If p-value < α → **Reject H₀** (statistically significant result)
- If p-value ≥ α → **Fail to reject H₀**

**Simple Analogy**: α = 5% means you are willing to be wrong 5 times out of 100 when you reject H₀.

---

### 4. Type I and Type II Errors

| Error Type     | Meaning                                      | Real-life Example (Court)          | Probability |
|----------------|----------------------------------------------|------------------------------------|-------------|
| **Type I**     | Reject H₀ when H₀ is actually True         | Sending innocent person to jail   | α           |
| **Type II**    | Fail to reject H₀ when H₀ is actually False| Letting guilty person go free     | β (beta)    |

**Power of Test** = 1 - β (probability of correctly rejecting false H₀)

**Mnemonic**:  
- Type I = **False Positive** (you said there *is* an effect, but there isn't)  
- Type II = **False Negative** (you said there *isn't* an effect, but there is)

---

### 5. Test Statistic and P-value

- **Test Statistic**: A number calculated from sample data (e.g., t-score, z-score, chi-square).
- **P-value**: Probability of getting a test statistic **as extreme as** (or more extreme than) the one observed, **assuming H₀ is true**.

**Rule of Thumb**:
- Very **small p-value** (e.g., < 0.05) → Strong evidence against H₀.
- Large p-value → Data is consistent with H₀.

---

### 6. Statistical Significance vs Practical Significance

- **Statistical Significance**: Result is unlikely due to chance (based on p-value).
- **Practical Significance**: Result is **meaningful in real life** (effect size matters).

**Classic Example**:
- A new teaching method reduces exam failure rate from 20% to 19.8%.  
  With huge sample, p-value < 0.01 → **Statistically significant**.  
  But saving only 0.2% students? → **Not practically significant**.

**Always check effect size** (Cohen's d, correlation, etc.) along with p-value.

---

## Python Example: One Sample T-Test

**Problem**:  
A school claims average marks of students in a new batch is **75**.  
You take a sample of 30 students and get mean = 72. Is the claim true?

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Sample data (marks of 30 students)
np.random.seed(42)
sample_marks = np.random.normal(loc=72, scale=8, size=30)

# Hypotheses
# H0: mu = 75
# H1: mu != 75

# Perform One Sample T-test
t_stat, p_value = stats.ttest_1samp(sample_marks, popmean=75)

print("Test Statistic (t):", round(t_stat, 4))
print("P-value:", round(p_value, 4))

alpha = 0.05
if p_value < alpha:
    print("Result: Reject H0 → Average marks are significantly different from 75")
else:
    print("Result: Fail to reject H0 → No significant difference from 75")
```
---
---
### 1. What is Hypothesis Testing?

**Hypothesis Testing** is a statistical method that helps us make decisions about a large group (population) using a small set of data (sample).

**Simple Analogy**: It is like a court trial.  
- We start with a claim (hypothesis).  
- We collect evidence (data).  
- We decide whether to reject the claim or not.

---

### 2. Null Hypothesis (H₀) vs Alternative Hypothesis (H₁)

| Hypothesis              | Meaning                                      | Example (Medicine)                          |
|-------------------------|----------------------------------------------|---------------------------------------------|
| **H₀ (Null)**           | No change or no effect (default assumption) | The drug takes exactly 30 minutes to work. |
| **H₁ (Alternative)**    | There is a change or effect                  | The drug works in less than 30 minutes.    |

**Important Rules**:
- H₀ usually contains **=**, **≥**, or **≤**.
- We try to reject H₀, but we never fully prove H₁.

---

### 3. Significance Level (α) – How Much Risk Are We Willing to Take?

**α** is the maximum risk we accept for making a Type I error.  
The most common value is **0.05** (5%).

- If **p-value < α** → Reject H₀ (the result is significant).  
- If **p-value ≥ α** → Do not reject H₀.

**Simple Analogy**: α = 5% means you are okay with being wrong 5 times out of 100 when you reject H₀.

---


### 4. How to Interpret Test Statistic and P-value?

- **Test Statistic** (like t-score or z-score): Shows how far the sample data is from the null hypothesis.  
- **P-value**: The probability of getting results as extreme as what we observed, **if H₀ is true**.

**Simple Rule**:
- Small p-value (less than 0.05) → Strong evidence against H₀.  
- Large p-value → The data supports H₀.

**Common Mistake**: The p-value does **not** tell you the probability that H₀ is true.

---

### 5. Type I Error and Type II Error



| Error Type     | What It Means                                      | Probability | Court Example                     |
|----------------|----------------------------------------------------|-------------|-----------------------------------|
| **Type I**     | Reject H₀ when it is actually true                | = α         | Sending an innocent person to jail |
| **Type II**    | Fail to reject H₀ when it is actually false       | = β         | Letting a guilty person go free   |

**Power of the Test** = 1 – β (higher power means lower chance of Type II error).

---

### 6. Statistical Significance vs Practical Significance

**Statistical Significance**: The result is unlikely to happen by chance (small p-value).  
**Practical Significance**: The result is actually useful or important in real life.

**Real-Life Example**:
- A new teaching method reduces student failure rate from 20% to 19.8%.  
- With a very large sample, p-value < 0.01 → Statistically significant.  
- But the improvement is only 0.2% → Not practically significant.

**Tip**: Always check the effect size (how big the difference really is), not just the p-value.

---

## Python Code Example: One Sample T-Test

**Problem**: A school claims the average student marks are **75**.  
You have a sample of 30 students with average **72**. Is the claim wrong?

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Sample data
np.random.seed(42)
sample_marks = np.random.normal(loc=72, scale=8, size=30)

# Hypotheses
# H0: average = 75
# H1: average != 75

t_stat, p_value = stats.ttest_1samp(sample_marks, popmean=75)

print("Test Statistic (t):", round(t_stat, 4))
print("P-value:", round(p_value, 4))

alpha = 0.05
if p_value < alpha:
    print("✅ Reject H0 → Average marks are significantly different from 75")
else:
    print("❌ Fail to reject H0")
```

**Typical Output**:  
`P-value: 0.0421` → Reject H₀ at 5% level.

---

## Complete Step-by-Step Process of Hypothesis Testing

1. State the hypotheses (H₀ and H₁).  
2. Choose the significance level (usually α = 0.05).  
3. Collect the sample data.  
4. Calculate the test statistic.  
5. Find the p-value.  
6. Make a decision (compare p-value with α).  
7. Interpret the result (statistical + practical).  
8. Check the assumptions (normality, sample size, etc.).

---

**Practice Question**:  
A company claims the average weight of potato chip packets is 50g.  
Sample of 25 packets: mean = 48.5g, standard deviation = 3g.  
Test at α = 0.05. (Try writing the code!)

---
**Happy Learning!**  
**Pankaj Chouhan**  
*Codes with Pankaj* 🚀
