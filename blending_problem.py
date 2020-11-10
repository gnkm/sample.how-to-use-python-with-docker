"""[pulp ドキュメントの例]
    https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html にある例題を解く。

    目的関数: min 0.013 * x_1 + 0.008 * x_2
    制約条件
    1.000 * x1 + 1.000 * x2 = 100
    0.100 * x1 + 0.200 * x2 ≧ 8.0
    0.080 * x1 + 0.100 * x2 ≧ 6.0
    0.001 * x1 + 0.005 * x2 ≦ 2.0
    0.002 * x1 + 0.005 * x2 ≦ 0.4

    ファイルはあるのだが下記エラーが発生する。
    FileNotFoundError: [Errno 2] No such file or directory: '/usr/local/lib/python3.8/site-packages/pulp/apis/../solverdir/cbc/linux/64/cbc'
"""
from pulp import *


def main():
    prob = LpProblem("The Whiskas Problem",LpMinimize)

    # 変数の定義
    x1=LpVariable("ChickenPercent",0,None,LpInteger)
    x2=LpVariable("BeefPercent",0)

    # 目的関数の定義
    prob += x1 + x2 == 100, "PercentagesSum"

    # 制約条件の定義
    prob += 0.100*x1 + 0.200*x2 >= 8.0, "ProteinRequirement"
    prob += 0.080*x1 + 0.100*x2 >= 6.0, "FatRequirement"
    prob += 0.001*x1 + 0.005*x2 <= 2.0, "FibreRequirement"
    prob += 0.002*x1 + 0.005*x2 <= 0.4, "SaltRequirement"

    # 解く
    prob.solve()
    print("Status:", LpStatus[prob.status])
    print("Total Cost of Ingredients per can = ", value(prob.objective))
    

if __name__ == '__main__':
    main()
