# 9.	Къщичка
# Напишете програма, която чете число n (2 ≤ n ≤ 100), въведено от потребителя, и печата къщичка с размер n x n:
# 3:      4:         5:         6:
# -*-     -**-       --*--      --**--
# ***     ****       -***-      -****-
# |*|     |**|       *****      ******
#         |**|       |***|      |****|
#                    |***|      |****|
#                               |****|
#



#n = int(input())
n = 4
roof_lines = None

roof_lines = int(n / 2) if n % 2 == 0 else int(n // 2 +1)

for row in range(0, roof_lines):
    print("-" * (n))