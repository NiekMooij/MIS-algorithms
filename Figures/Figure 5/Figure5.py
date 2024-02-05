import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
import pandas as pd
import sys

cud_palette = [
    '#0101fd',  # Blue
    '#E69F00',  # Orange
    '#000000',  # Black
    '#ff0101',   # Red
    '#0072B2',  # Blue
    '#D55E00',  # Vermilion
    '#CC79A7',  # Reddish Purple
    '#F95C99',  # Reddish Pink
    '#999999',  # Gray
    '#CC61B0',  # Pink
    '#F95C99',  # Reddish Pink
]

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(ncols=2, nrows=3, figsize=(10,10))
fig.subplots_adjust(wspace=0.3, hspace=0.6)
plt.suptitle("Random bipartite", fontsize=18, y=0.96)

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Probability_Performance_size60
df = pd.read_pickle(os.path.join(sys.path[0], f"data/Probability_Performance_size60/data.pkl"))

ax2.errorbar(df['p_connection'], df['LV_app'], yerr=(df['LV_app'] - df['LV_app_CI_lower'], df['LV_app_CI_upper'] - df['LV_app']), marker='s', color=cud_palette[0], capsize=3)
ax2.scatter([], [], label='LV', marker='s', color=cud_palette[0])

ax2.errorbar(df['p_connection'], df['continuation_app'], yerr=(df['continuation_app'] - df['continuation_app_CI_lower'], df['continuation_app_CI_upper'] - df['continuation_app']), marker='o', color=cud_palette[1], capsize=3)
ax2.scatter([], [], label='CLV', marker='o', color=cud_palette[1])

ax2.errorbar(df['p_connection'], df['greedy_app'], yerr=(df['greedy_app'] - df['greedy_app_CI_lower'], df['greedy_app_CI_upper'] - df['greedy_app']), marker='^', color=cud_palette[2], capsize=3)
ax2.scatter([], [], label='Greedy', marker='^', color=cud_palette[2])

ax2.legend()
ax2.set_xlabel('p')
ax2.set_ylabel('Approximation factor')
ax2.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0.0', '0.2', '0.4', '0.6', '0.8', '1.0'])
ax2.set_yticks([0.8, 0.85, 0.90, 0.95, 1.0], ['0.8', '0.85', '0.90', '0.95', '1.00'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Size_Performance_p02
df = pd.read_pickle(os.path.join(sys.path[0], f"data/Size_Performance_sparse/data.pkl"))

ax3.errorbar(df['size'], df['LV_app'], yerr=(df['LV_app'] - df['LV_app_CI_lower'], df['LV_app_CI_upper'] - df['LV_app']), marker='s', color=cud_palette[0], capsize=3)
ax3.scatter([], [], label='LV', marker='s', color=cud_palette[0])

ax3.errorbar(df['size'], df['continuation_app'], yerr=(df['continuation_app'] - df['continuation_app_CI_lower'], df['continuation_app_CI_upper'] - df['continuation_app']), marker='o', color=cud_palette[1], capsize=3)
ax3.scatter([], [], label='CLV', marker='o', color=cud_palette[1])

ax3.errorbar(df['size'], df['greedy_app'], yerr=(df['greedy_app'] - df['greedy_app_CI_lower'], df['greedy_app_CI_upper'] - df['greedy_app']), marker='^', color=cud_palette[2], capsize=3)
ax3.scatter([], [], label='Greedy', marker='^', color=cud_palette[2])

ax3.legend()
ax3.set_xlabel('Size (n)')
ax3.set_ylabel('Approximation factor')
ax3.set_xticks([50, 100, 150, 200], ['50', '100', '150', '200'])
ax3.set_yticks([0.80, 0.85, 0.90, 0.95, 1.0], ['0.80', '0.85', '0.90', '0.95', '1.00'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Size_Performance_p0.5
df = pd.read_pickle(os.path.join(sys.path[0], f"data/Size_Performance_p05/data.pkl"))

ax5.errorbar(df['size'], df['LV_app'], yerr=(df['LV_app'] - df['LV_app_CI_lower'], df['LV_app_CI_upper'] - df['LV_app']), marker='s', color=cud_palette[0], capsize=3)
ax5.scatter([], [], label='LV', marker='s', color=cud_palette[0])

ax5.errorbar(df['size'], df['continuation_app'], yerr=(df['continuation_app'] - df['continuation_app_CI_lower'], df['continuation_app_CI_upper'] - df['continuation_app']), marker='o', color=cud_palette[1], capsize=3)
ax5.scatter([], [], label='CLV', marker='o', color=cud_palette[1])

ax5.errorbar(df['size'], df['greedy_app'], yerr=(df['greedy_app'] - df['greedy_app_CI_lower'], df['greedy_app_CI_upper'] - df['greedy_app']), marker='^', color=cud_palette[2], capsize=3)
ax5.scatter([], [], label='Greedy', marker='^', color=cud_palette[2])

ax5.legend()
ax5.set_xlabel('Size (n)')
ax5.set_ylabel('Approximation factor')
ax5.set_xticks([50, 100, 150, 200], ['50', '100', '150', '200'])
ax5.set_yticks([0.94, 0.96, 0.98, 1.0], ['0.94', '0.96', '0.98', '1.00'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Output_Counts_Histogram_size60_p05
df = pd.read_pickle(os.path.join(sys.path[0], f"data/Output_Counts_Histogram_size60_p01/data.pkl"))

uniform = np.array((df['count_uniform'])) / sum(list(df['count_uniform']))
lv = np.array(df['count_LV']) / sum(list(df['count_LV']))

bars1 = ax1.bar(list(df['value']), uniform, label='Uniform', alpha=0.7, color=cud_palette[3], hatch='//')
bars2 = ax1.bar(list(df['value']), lv, label='LV', alpha=0.7, color=cud_palette[0], hatch='\\\\')

ax1.legend()
ax1.set_xlabel(r'$|S|$')
ax1.set_ylabel('Frequency')
ax1.set_xticks([16, 18, 20, 22, 24, 26, 28, 30, 32], [16, 18, 20, 22, 24, 26, 28, 30, 32])
ax1.set_yticks([0.0, 0.2, 0.4, 0.6], [0.0, 0.2, 0.4, 0.6])
ax1.set_ylim(0, 0.7)

# Manually define position and size for the inset plot
inset_x = 0.175
inset_y = 0.79
inset_width = 0.14
inset_height = 0.082

ax_inset = fig.add_axes([inset_x, inset_y, inset_width, inset_height])

ax_inset.bar(list(df['value']), uniform, label='Uniform', alpha=0.7, color=cud_palette[3], hatch='//')
ax_inset.bar(list(df['value']), lv, label='LV', alpha=0.7, color=cud_palette[0], hatch='\\\\')

ax_inset.set_yscale('log')
ax_inset.set_xticks([16, 20, 24, 28, 32], [16, 20, 24, 28, 32])
ax_inset.set_yticks([ 10**-5, 10**-4, 10**-3, 10**-2 , 10**-1 ], [ r'$10^{-5}$', r'$10^{-4}$', r'$10^{-3}$', r'$10^{-2}$', r'$10^{-1}$' ])
ax_inset.set_ylim(0, 0.6)

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Size / Efficiency - p=log(n)/n
df = pd.read_pickle(os.path.join(sys.path[0], f"data/Size_Efficiency_sparse/data.pkl"))

ax4.plot(df['size'], df['LV_eff'], marker='s', color=cud_palette[0])
ax4.scatter([], [], label='LV', marker='s', color=cud_palette[0])

ax4.plot(df['size'], df['continuation_eff'], marker='o', color=cud_palette[1])
ax4.scatter([], [], label='CLV', marker='o', color=cud_palette[1])

ax4.plot(df['size'], df['greedy_eff'], marker='^', color=cud_palette[2])
ax4.scatter([], [], label='Greedy', marker='^', color=cud_palette[2])

ax4.legend()
ax4.set_xlabel('Size (n)')
ax4.set_ylabel('Percentage MIS')

ax4.set_xticks([50, 100, 150, 200], ['50', '100', '150', '200'])
ax4.set_yticks([0.00, 0.25, 0.50, 0.75, 1.0], ['0.00', '0.25', '0.50', '0.75', '1.00'])

# formatter = ticker.FormatStrFormatter('%.2f')
# ax4.yaxis.set_major_formatter(formatter)

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Size_Efficiency_p05
df = pd.read_pickle(os.path.join(sys.path[0], f"data/Size_Efficiency_p05/data.pkl"))

ax6.plot(df['size'], df['LV_eff'], marker='s', color=cud_palette[0])
ax6.scatter([], [], label='LV', marker='s', color=cud_palette[0])

ax6.plot(df['size'], df['continuation_eff'], marker='o', color=cud_palette[1])
ax6.scatter([], [], label='CLV', marker='o', color=cud_palette[1])

ax6.plot(df['size'], df['greedy_eff'], marker='^', color=cud_palette[2])
ax6.scatter([], [], label='Greedy', marker='^', color=cud_palette[2])

ax6.legend()
ax6.set_xlabel('Size (n)')
ax6.set_ylabel('Percentage MIS')
ax6.set_xticks([50, 100, 150, 200], ['50', '100', '150', '200'])
ax6.set_yticks([0.85, 0.90, 0.95, 1.0], ['0.85', '0.90', '0.95', '1.00'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

numbers = [ 'a', 'b' ]
for index, ax in enumerate([ ax1, ax2 ]):
    if index == 0:
        ax.text(0.5, 1.05, f'({numbers[index]}) ' + r'$n=60$', ha='center', transform=ax.transAxes, fontsize=12)     
    else:
        ax.text(0.5, 1.05, f'({numbers[index]})', ha='center', transform=ax.transAxes, fontsize=12)    
    
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_xlabel( ax.get_xlabel(), fontsize=12)
    ax.set_ylabel( ax.get_ylabel(), fontsize=12)
    ax.legend(loc='lower left')
    
numbers = [ 'c', 'd' ]
for index, ax in enumerate([ ax3, ax4 ]):
    ax.text(0.5, 1.05, f'({numbers[index]}) ' + r'$p = \log(n/2)/(n/2)$', ha='center', transform=ax.transAxes, fontsize=12)    
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_xlabel( ax.get_xlabel(), fontsize=12)
    ax.set_ylabel( ax.get_ylabel(), fontsize=12)
    ax.legend(loc='lower left')
    
numbers = [ 'e', 'f' ]
for index, ax in enumerate([ ax5, ax6 ]):
    ax.text(0.5, 1.05, f'({numbers[index]}) ' + r'$p = 1/2$', ha='center', transform=ax.transAxes, fontsize=12)    
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_xlabel( ax.get_xlabel(), fontsize=12)
    ax.set_ylabel( ax.get_ylabel(), fontsize=12)
    ax.legend(loc='lower left')

plt.savefig(os.path.join(sys.path[0], 'Figure5.pdf'), transparent=True, dpi=900, bbox_inches='tight')
plt.show()