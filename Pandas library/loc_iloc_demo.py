#!/usr/bin/env python3
"""
loc_iloc_demo.py
A small, self-contained demo showing differences between .loc (label-based) and .iloc (position-based)
with several examples and edge cases.
"""

import pandas as pd


def main():
    df = pd.DataFrame({
        'A': [10, 20, 30, 40, 50],
        'B': [5, 4, 3, 2, 1],
        'C': [100, 200, 300, 400, 500],
        'D': ['x', 'y', 'z', 'w', 'v']
    }, index=['r1', 'r2', 'r3', 'r4', 'r5'])

    print("== DataFrame ==")
    print(df, "\n")

    print("== label-based .loc examples ==")
    print("Single row by label ('r3'):\n", df.loc['r3'], "\n")
    print("Slice by labels 'r2' to 'r4' (inclusive):\n", df.loc['r2':'r4'], "\n")
    print("Select specific columns for label 'r3' (A and C):\n", df.loc['r3', ['A', 'C']], "\n")
    print("Select rows where A > 20 and only columns B and C:\n", df.loc[df['A'] > 20, ['B', 'C']], "\n")

    print("== position-based .iloc examples ==")
    print("Single row by integer position 2:\n", df.iloc[2], "\n")
    print("Slice by positions 1:4 (end-exclusive):\n", df.iloc[1:4], "\n")
    print("Select row 3 and columns at positions 0 and 2:\n", df.iloc[3, [0, 2]], "\n")
    print("Select every other row (step=2):\n", df.iloc[::2], "\n")

    print("== integer index gotchas ==")
    df2 = pd.DataFrame({'val': [10, 20, 30, 40]}, index=[0, 1, 2, 3])
    print("Integer-index DataFrame:\n", df2, "\n")
    print("df2.loc[1] -> label 1:\n", df2.loc[1], "\n")
    print("df2.iloc[1] -> position 1:\n", df2.iloc[1], "\n")
    print("df2.loc[0:2] includes label 2 (end-inclusive):\n", df2.loc[0:2], "\n")
    print("df2.iloc[0:2] excludes position 2 (end-exclusive):\n", df2.iloc[0:2], "\n")

    print("== non-consecutive integer labels ==")
    df3 = pd.DataFrame({'val': [100, 200, 300]}, index=[10, 11, 12])
    print("df3:\n", df3, "\n")
    print("df3.loc[11] -> label 11:\n", df3.loc[11], "\n")
    print("df3.iloc[1] -> position 1 (the same row as label 11):\n", df3.iloc[1], "\n")

    print("== Summary ==")
    print("- .loc is label-based: it looks up index/column labels. Slices include the end label.")
    print("- .iloc is integer position-based: slicing is end-exclusive and uses Python-style indexing.")


if __name__ == '__main__':
    main()

