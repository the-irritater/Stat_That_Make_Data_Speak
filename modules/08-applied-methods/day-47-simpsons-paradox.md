# Day 47: Simpson's Paradox

*The overall data says one thing. The subgroups say another. Which do you trust?*

---

## Learning Objective

Understand Simpson's Paradox — when a trend reverses after disaggregation — and why subgroup analysis is essential.

---

## The Concept

**Simpson's Paradox** occurs when a trend appears in separate groups but reverses when the groups are combined.

### Classic example:

Treatment A appears worse overall but is actually better within each group.

| Group | Treatment A Success | Treatment B Success |
|-------|-------------------|-------------------|
| Men | 80% (of 100) | 75% (of 400) |
| Women | 90% (of 400) | 85% (of 100) |
| **Combined** | **88%** | **78%** |

Wait — Treatment A is better in both groups AND overall? The paradox occurs when group sizes are unequal, making the combined data misleading.

### Why it happens:

A **lurking variable** (group membership, severity, demographic) affects both the treatment and outcome. Combining groups hides this confounder.

### How to protect yourself:

1. Always check results within relevant subgroups
2. Ask: "Could group composition be driving this result?"
3. Report both overall and subgroup findings

---

## Real-World Example

A university's overall acceptance rate favors one gender. But within each department, the opposite is true. The paradox arises because the disadvantaged gender applied more to competitive departments with lower acceptance rates overall.

---

## 🔑 Key Takeaway

> Overall data can sometimes mislead. Always check important subgroups before making decisions — the story may reverse when you look closer.

---

[← Day 46: Correlation Matrix](day-46-correlation-matrix.md) · [Next: Day 48 – Confounding Variable →](day-48-confounding-variable.md)
