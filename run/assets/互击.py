with open('pair_equivalence.txt', 'a', encoding='utf-8') as f:
  for zs in 'qwertasdfgzxcvb':
    f.write(f'{zs}_\t1.0\n')
    for ys in 'yuiophjkl;nm,./':
      a = zs + ys
      b = ys + zs
      f.write(f'{a}\t1.0\n')
      f.write(f'{b}\t1.0\n')
  for ys in 'yuiophjkl;nm,./':
      f.write(f'{ys}_\t1.0\n')
