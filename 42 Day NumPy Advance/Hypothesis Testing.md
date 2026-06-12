
# Hypothesis Testing –  
**By Codes with Pankaj**  

---

### 1. Hypothesis Testing Kya Hai? (Definition)

**Hypothesis Testing** ek statistical method hai jisme hum sample data se population ke baare mein decision lete hain.

**Simple Analogy**: Court mein case chal raha hai.  
- **Null Hypothesis (H₀)** = Accused innocent hai (default assumption)  
- **Alternative Hypothesis (H₁)** = Accused guilty hai  

Hum evidence (data) collect karte hain aur decide karte hain ki H₀ ko reject karna hai ya nahi.

---

### 2. Null Hypothesis (H₀) vs Alternative Hypothesis (H₁)

| Hypothesis       | Matlab                                      | Example (Medicine)                     |
|------------------|---------------------------------------------|----------------------------------------|
| **H₀ (Null)**    | Koi farak nahi / status quo                 | Drug se headache 30 min mein hi theek hota hai |
| **H₁ (Alternative)** | Farak hai / jo hum prove karna chahte hain | Drug se headache 30 min se kam time mein theek hota hai |

**Important Rules**:
- H₀ mein hamesha **=**, **≥**, ya **≤** hota hai
- Hum H₀ ko reject kar sakte hain, lekin kabhi fully prove nahi kar sakte

---

### 3. Significance Level (α) – Risk Kitna Lenge?

**α** = Maximum risk jo hum Type I error ka le sakte hain.  
Sabse common value: **0.05** (5%)

- Agar **p-value < α** → H₀ reject kar do (significant result)
- Agar **p-value ≥ α** → H₀ reject mat karo

**Analogy**: α = 5% matlab aap 100 baar mein se sirf 5 baar galti karne ko taiyar ho jab aap H₀ reject karte ho.

---




### 4. Test Statistic aur P-value Kaise Interpret Karein?

- **Test Statistic** (jaise t-score, z-score): Data kitna H₀ se door hai, yeh batata hai.
- **P-value**: Agar H₀ sach ho toh itna extreme result milne ki probability.

**Simple Rule**:
- Chhota p-value (< 0.05) → Strong evidence against H₀
- Bada p-value → Data H₀ ke saath consistent hai

**Galatfahmi**: P-value yeh nahi batata ki H₀ kitna sach hai. Yeh sirf “assuming H₀ is true” wali probability hai.

---

### 5. Type I Error aur Type II Error










| Error Type     | Kya Hota Hai?                              | Probability | Court Analogy                     |
|----------------|--------------------------------------------|-------------|-----------------------------------|
| **Type I**     | H₀ sach tha lekin humne reject kar diya   | = α         | Innocent ko jail bhej diya       |
| **Type II**    | H₀ galat tha lekin humne reject nahi kiya | = β         | Guilty ko chhod diya              |

**Power of Test** = 1 – β (jitna bada power, utna kam Type II error)

---

### 6. Statistical Significance vs Practical Significance

**Statistical Significance**: Result chance se nahi mila (p-value chhota hai).  
**Practical Significance**: Result real life mein kitna meaningful hai (effect size dekho).

**Real Example**:
- Naya teaching method se fail rate 20% se 19.8% ho gaya.
- Bahut bade sample mein p-value < 0.01 → Statistically significant.
- Lekin sirf 0.2% improvement? → **Practically insignificant**.

**Hamesha effect size (Cohen’s d, difference in means, etc.) bhi check karo.**




---

## Python Code Example: One Sample T-Test

**Problem**: School claim karta hai ki students ka average marks **75** hai.  
Sample of 30 students ka mean **72** aaya. Kya claim galat hai?

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Sample data
np.random.seed(42)
sample_marks = np.random.normal(loc=72, scale=8, size=30)

# Hypotheses
# H0: mu = 75
# H1: mu != 75

t_stat, p_value = stats.ttest_1samp(sample_marks, popmean=75)

print("Test Statistic (t):", round(t_stat, 4))
print("P-value:", round(p_value, 4))

alpha = 0.05
if p_value < alpha:
    print("✅ Reject H0 → Average marks 75 se significantly different hain")
else:
    print("❌ Fail to reject H0")
```

**Output (approx)**:  
`P-value: 0.0421` → Reject H₀ at 5% level.

---


**Happy Learning!**  
**Pankaj Chouhan**  
*Codes with Pankaj* 🚀

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
