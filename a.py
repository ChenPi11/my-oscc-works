import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC']
plt.rcParams['font.serif'] = ['Noto Sans CJK SC']
plt.rcParams['axes.unicode_minus'] = False
# ---------- 法1：求和公式 ----------
def T_sum(n, T_NAND=4, T_NOR=4, T_NOT=2):
    """按 NAND/NOR 逐层交替、奇数层插入 NOT 的构造计算 #T"""
    total = 0
    layer = 0
    nk = n
    while nk > 1:
        nk_next = (nk + 1) // 2          # ceil(nk/2)
        gate_T = T_NAND if layer % 2 == 0 else T_NOR
        total += nk_next * gate_T
        if nk % 2 == 1:                  # 奇数输入 -> 插入 1 个 NOT
            total += T_NOT
        nk = nk_next
        layer += 1
    return total

# ---------- 数据 ----------
n_values = np.arange(2, 33)

f0  = [2 * n for n in n_values]                              # 法0: 2N
f1  = [T_sum(n) for n in n_values]                           # 法1: 求和
f2a = [14 * ((n + 1) // 2) - 8 for n in n_values]            # 法2a
f2b = [8 * n - 6 for n in n_values]                          # 法2b

# ---------- 绘图 ----------
plt.figure(figsize=(11, 6.5))

plt.plot(n_values, f0,  'o-',  color='tab:blue',   label='晶体管法')
plt.plot(n_values, f1,  's-',  color='tab:green',  label='法1')
plt.plot(n_values, f2a, '^-',  color='tab:orange', label='法2')
plt.plot(n_values, f2b, 'd--', color='tab:red',    label='法0')

plt.title('F3.3.2 多输入与非门的面积（门电路级）', fontsize=15)
plt.xlabel('输入数量 n', fontsize=12)
plt.ylabel('晶体管数量 #T', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(range(2, 33, 2))
plt.tight_layout()
plt.show()
