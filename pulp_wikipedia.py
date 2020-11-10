"""[pulp で解けない例]
    https://ja.wikipedia.org/wiki/線型計画法 にある例題を考える。

    線型計画問題の例として以下の問題をとりあげる。
    農業を営む人が、小麦と大麦のための A 平方キロメートルの農地を持っていると仮定する。
    農家は限度 F で肥料、限度 P で殺虫剤を使用することができる。
    これらはそれぞれ単位面積あたり小麦が (F_{1},P_{1}) 、大麦が (F_{2},P_{2}) を必要とする。
    小麦の販売価格を S_{1} 、大麦の販売価格を S_{2} 、小麦を育てる領域を x_{1} 、大麦を育てる領域を x_{2} とすると、
    線型計画問題として大麦と小麦をどれだけ育てればいいかを表すことができる。

    最大化：   S_{1}x_{1}+S_{2}x_{2} 	(利益の最大化)
    制約条件： x_{1}+x_{2} ≦ A	(耕作地の制約)
               F_{1}x_{1}+F_{2}x_{2} ≦ F	(肥料の制約)
               P_{1}x_{1}+P_{2}x_{2} ≦ P	(殺虫剤の制約)
               x_{1} ≧ 0, x_{2} ≧ 0	(非負制約)

"""
import pulp


AREA = 100  # 農地の広さ
HIRYO = 5  # 肥料
KUSURI = 1  # 殺虫剤
KOMUGI_KAKAKU = 122  # 小麦価格
OMUGI_KAKAKU = 88  # 大麦価格


def main():
    problem = pulp.LpProblem('Wikipedia example', pulp.LpMaximize)

    # 変数の定義
    komugi_area = pulp.LpVariable("komugi_area", lowBound = 0, upBound = AREA)
    omugi_area = pulp.LpVariable("omugi_area", lowBound = 0, upBound = AREA)
    komugi_hiryo = pulp.LpVariable("komugi_hiryo", lowBound = 0, upBound = HIRYO)
    omugi_hiryo = pulp.LpVariable("omugi_hiryo", lowBound = 0, upBound = HIRYO)
    komugi_kusuri = pulp.LpVariable("komugi_kusuri", lowBound = 0, upBound = KUSURI)
    omugi_kusuri = pulp.LpVariable("omugi_kusuri", lowBound = 0, upBound = KUSURI)

    # 目的関数の定義
    problem += KOMUGI_KAKAKU * komugi_area + OMUGI_KAKAKU * omugi_area

    # 制約条件の定義
    problem += komugi_area + omugi_area <= AREA  # 耕作地の制約
    # 下記コードだと TypeError: Non-constant expressions cannot be multiplied が発生する
    # 定数 * 変数でないと解けない？
    problem += komugi_hiryo * komugi_area + omugi_hiryo * omugi_area <= HIRYO  # 肥料の制約
    problem += komugi_hiryo == HIRYO * komugi_area / AREA
    problem += omugi_hiryo == HIRYO * omugi_area / AREA
    problem += komugi_hiryo * komugi_area + omugi_hiryo * omugi_area <= KUSURI
    problem += komugi_hiryo == KUSURI * komugi_area / AREA
    problem += omugi_hiryo == KUSURI * omugi_area / AREA

    # 解く
    status = problem.solve()
    print(pulp.LpStatus[status])
    print('小麦広さ: ', komugi_area.value())
    print('大麦広さ: ', omugi_area.value())
    print('小麦肥料: ', komugi_hiryo.value())
    print('大麦肥料: ', omugi_hiryo.value())
    print('小麦殺虫剤: ', komugi_kusuri.value())
    print('大麦殺虫剤: ', komugi_kusuri.value())


if __name__ == '__main__':
    main()
