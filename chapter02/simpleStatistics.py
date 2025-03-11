import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def EvaluateSignificance(p_value: float) -> str:
    if p_value > 0.05:
        return "n.s."
    elif p_value <= 0.01:
        return "***"
    else:
        return "*"

if __name__ == "__main__":
    np.random.seed(12345)

    group_a = np.random.normal(5, 3, 100)
    group_b = np.random.normal(10, 5, 100)

    means = [np.mean(group_a), np.mean(group_b)]
    errors = [stats.sem(group_a), stats.sem(group_b)]

    t_stat, p_value = stats.ttest_ind(group1, group2)

    fig, ax = plt.subplots()
    bars = ax.bar(["Group a", "Group b"], means, yerr=errors, capsize=5, color=["blue", "orange"])

    x1, x2 = 0, 1
    y_max = max(means) + max(errors) + 0.5

    ax.plot([x1, x1, x2, x2], [y_max, y_max + 0.3, y_max + 0.3, y_max], color="black")
    ax.text((x_1+x_2)/2, y_max + 0.35, EvaluateSignificance(p_value), ha="canter", fontsize=12)
    ax.set_title("significance evaluation")

    plt.show()
    
    sys.exit(0)
    
