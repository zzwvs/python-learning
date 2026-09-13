import matplotlib.pyplot as plt
import numpy as np

# 模型参数（单位：B）
models = ['2B', '3B', '4B']
params_b = [2, 3, 4]

# 不同精度的每参数显存 (GB per 1B params)
fp16_per_b = 2.0   # 2 bytes/param
q4_per_b   = 0.5   # 0.5 bytes/param

# 权重显存
fp16_weight = [p * fp16_per_b for p in params_b]
q4_weight   = [p * q4_per_b   for p in params_b]

# 额外开销 (KV cache + 激活值，按较长上下文估算)
extra_overhead = 1.5  # GB，适用于 2~4B 模型

# 总显存
fp16_total = [w + extra_overhead for w in fp16_weight]
q4_total   = [w + extra_overhead for w in q4_weight]

# 设置柱状图位置
x = np.arange(len(models))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(x - width/2, fp16_total, width, label='FP16 (高精度)', color='#d62728', alpha=0.8)
bars2 = ax.bar(x + width/2, q4_total,   width, label='Q4 量化 (4-bit)', color='#1f77b4', alpha=0.8)

# 添加数值标签
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.1f} GB', xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.1f} GB', xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

# 参考线（常见显卡显存）
ax.axhline(y=6,  color='gray', linestyle='--', linewidth=1, alpha=0.7, label='6 GB (RTX 3060)')
ax.axhline(y=8,  color='gray', linestyle=':',  linewidth=1, alpha=0.7, label='8 GB (RTX 3070)')
ax.axhline(y=10, color='gray', linestyle='-.', linewidth=1, alpha=0.7, label='10 GB (RTX 3080)')

ax.set_ylabel('显存需求 (GB)')
ax.set_xlabel('模型参数量')
ax.set_title('2B~4B 模型推理显存对比 (含 KV cache 开销, 上下文 ≈2048)')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend(loc='upper left')
ax.grid(axis='y', linestyle=':', alpha=0.4)

plt.tight_layout()
plt.show()