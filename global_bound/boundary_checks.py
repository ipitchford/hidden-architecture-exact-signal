#!/usr/bin/env python3
"""Independent checks of the boundary theorem; standard library only.

Exact fractions validate stationary balance and observable identities. Floating
point inequalities are diagnostics; the analytic proofs carry certification.
No assert statement is used, so verification remains active with python -O.
"""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import random


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def solve(a, b):
    n = len(b)
    c = [list(map(F, row)) + [F(bi)] for row, bi in zip(a, b)]
    for i in range(n):
        p = next(j for j in range(i, n) if c[j][i])
        c[i], c[p] = c[p], c[i]
        d = c[i][i]
        c[i] = [v / d for v in c[i]]
        for j in range(n):
            if j != i:
                d = c[j][i]
                c[j] = [x - d * y for x, y in zip(c[j], c[i])]
    return [c[i][-1] for i in range(n)]


def stationary(q):
    n = len(q)
    a = [[q[j][i] for j in range(n)] for i in range(n - 1)]
    return solve(a + [[F(1)] * n], [F(0)] * (n - 1) + [F(1)])


def j(x, y):
    x, y = float(x), float(y)
    if x == y:
        return 0.0
    if x == 0 or y == 0:
        return math.inf
    return (x - y) * math.log(x / y)


def phi(a):
    if a >= 1:
        return 0.0
    if a <= 0:
        return math.inf
    d = math.sqrt((1 - a) * (1 + a))
    return 4 * d * math.atanh(d)


def statistics(q, block):
    pi = stationary(q)
    outside = [i for i in range(len(q)) if i not in block]
    entry = [sum(pi[a] * q[a][i] for a in outside) for i in block]
    t = [sum(q[i][a] for a in outside) for i in block]
    r = sum(entry)
    alpha = [v / r for v in entry]
    mu = [pi[i] / r for i in block]
    beta = [u * v for u, v in zip(mu, t)]
    m = sum(mu)
    f0 = sum(a * ti for a, ti in zip(alpha, t))
    entropy = sum(j(pi[i] * q[i][l], pi[l] * q[l][i])
                  for i in range(len(q)) for l in range(i + 1, len(q)))
    require(sum(alpha) == sum(beta) == 1, "Entry/exit normalisation")
    for col, state in enumerate(block):
        require(sum(mu[row] * q[other][state]
                    for row, other in enumerate(block)) == -alpha[col],
                "Occupation identity")
    return r, m, f0, alpha, beta, entropy


def reset_q(r, m, d, big_m):
    sa = r / (1 - r * m)
    alpha = [(1 + d) / 2, (1 - d) / 2]
    t = [(1 - d) / m, (1 + d) / m]
    return [[-sa, sa * alpha[0], sa * alpha[1]],
            [t[0], -(1 + 2 * big_m) / m, (2 * big_m + d) / m],
            [t[1], (2 * big_m - d) / m, -(1 + 2 * big_m) / m]]


def main():
    rng = random.Random(20261026017)
    report = {"seed": 20261026017, "exact_sharp_families": [],
              "random_chain_count": 0, "positive_floor_count": 0,
              "probability_inequality_count": 0, "reversible_count": 0,
              "controls": []}
    largest_gap_violation = 0.0
    for n in range(3, 10):
        for _ in range(30):
            q = [[F(rng.randint(1, 99), rng.randint(1, 10)) if i != k else F(0)
                  for k in range(n)] for i in range(n)]
            for i in range(n):
                q[i][i] = -sum(q[i])
            block = list(range(rng.randint(1, n - 1)))
            r, m, f0, alpha, beta, entropy = statistics(q, block)
            affinity = sum(math.sqrt(float(a * b)) for a, b in zip(alpha, beta))
            require(affinity ** 2 <= float(m * f0) + 3e-13, "Affinity bound")
            boundary = float(r) * sum(j(a, b) for a, b in zip(alpha, beta))
            require(entropy + 3e-11 >= boundary, "Log-sum boundary contraction")
            if m * f0 < 1:
                bound = float(r) * phi(math.sqrt(float(m * f0)))
                require(entropy > bound - 3e-11, "Full entropy bound")
                largest_gap_violation = max(largest_gap_violation, bound - entropy)
                report["positive_floor_count"] += 1
            report["random_chain_count"] += 1

    for n in (2, 3, 5, 12):
        for _ in range(100):
            p = [rng.random() ** 3 + 0.0001 for _ in range(n)]
            q = [rng.random() ** 3 + 0.0001 for _ in range(n)]
            p = [x / sum(p) for x in p]
            q = [x / sum(q) for x in q]
            affinity = sum(math.sqrt(x * y) for x, y in zip(p, q))
            require(sum(j(x, y) for x, y in zip(p, q)) + 5e-12 >= phi(affinity),
                    "Sharp probability inequality")
            report["probability_inequality_count"] += 1

    for qval in (F(1, 20), F(1, 4), F(1, 2)):
        s = 1 + qval
        r, m, d = s / 3, 2 / s, (1 - qval) / s
        row = {"q": str(qval), "r": str(r), "m": str(m), "d": str(d),
               "floor": float(F(2, 3) * (1 - qval)) * math.log(1 / float(qval)),
               "models": []}
        for big_m in (F(1, 2), F(1), F(10), F(100)):
            q = reset_q(r, m, d, big_m)
            rr, mm, f0, alpha, beta, entropy = statistics(q, [1, 2])
            require(rr == r and mm == m and f0 == 2 * qval / s,
                    "Exact three-statistic preservation")
            predicted = float(r) * (4 * float(d) * math.atanh(float(d))
                + float(d) * math.log(float((big_m + d / 2) / (big_m - d / 2))))
            require(abs(entropy - predicted) < 3e-14, "Exact entropy formula")
            # Independently invert the 2x2 resolvent at three rational z.
            for z in (F(1, 3), F(1), F(3)):
                t = [q[1][0], q[2][0]]
                a, b = z - q[1][1], -q[1][2]
                c, dd = -q[2][1], z - q[2][2]
                det = a * dd - b * c
                direct = (alpha[0] * (dd * t[0] - b * t[1])
                          + alpha[1] * (-c * t[0] + a * t[1])) / det
                formula = ((1 - d * d) * m * z + 1 + 4 * big_m + d * d) / (
                    m * m * z * z + 2 * m * (1 + 2 * big_m) * z
                    + 1 + 4 * big_m + d * d)
                require(direct == formula, "Exact rational full transform")
            row["models"].append({"M": str(big_m), "sigma": entropy,
                                   "strict_gap": entropy - row["floor"]})
        report["exact_sharp_families"].append(row)

    for k in (F(5, 4), F(2), F(10)):
        r, m = F(1, 3), F(2)
        w = [1 - 1 / (4 * k - 3), 1 / (4 * k - 3)]
        mu = [m * wi for wi in w]
        t = [1 / (2 * m), (2 * k - 1) / m]
        alpha = [u * v for u, v in zip(mu, t)]
        sa = r / (1 - r * m)
        q = [[-sa, sa * alpha[0], sa * alpha[1]],
             [t[0], -t[0], F(0)], [t[1], F(0), -t[1]]]
        rr, mm, f0, aa, bb, entropy = statistics(q, [1, 2])
        require((rr, mm, mm * f0, entropy) == (r, m, k, 0.0),
                "Exact zero branch")
        report["reversible_count"] += 1

    # A directed ring has f0=0 and infinite entropy, as required.
    q = [[F(-1), F(1), F(0)], [F(0), F(-1), F(1)],
         [F(1), F(0), F(-1)]]
    r, m, f0, alpha, beta, entropy = statistics(q, [1, 2])
    require(f0 == 0 and math.isinf(entropy), "One-way f0=0 control")
    report["controls"].append("Directed ring: f0=0, infinite entropy")
    # Reversible two-state equality k=1.
    q = [[F(-2), F(2)], [F(3), F(-3)]]
    r, m, f0, alpha, beta, entropy = statistics(q, [1])
    require(m * f0 == 1 and entropy == 0, "Two-state equilibrium endpoint")
    report["controls"].append("Reversible two-state: k=1, zero entropy")
    report["largest_floating_violation"] = largest_gap_violation
    report["status"] = "PASS"
    out = Path(__file__).with_name("boundary_checks.json")
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
