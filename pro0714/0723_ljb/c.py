# author_='xqh';
# date: 2021/7/23 15:19

print('\n'.join([' '.join([f"{j}x{i}={i * j}" for j in range(1, i + 1)]) for i in range(1, 10)]))
