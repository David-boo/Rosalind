# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Messy code, working but improvable. TODO.

data = open('./rosalind_LGIS.txt', 'r').read().splitlines()

maxnum = int(data[0])
perm   = [int(x) for x in data[1].split()]

def lgis(maxnum, perm):
  levels = []
  graph  = {}
  for i in perm:
    if len(levels) == 0:
      levels.append([i])
      graph[i] = 0
    else:
      for lev in reversed(range(len(levels) + 1)):
        if i in graph.keys():
          break
        if lev == 0:
          levels[0].append(i)
          graph[i] = 0
          break
        lower_lev = levels[lev-1]
        lt = [x for x in lower_lev if x < i]
        if len(lt) > 0:
          if len(levels) == lev:
            levels.append([i])
          else:
            levels[lev].append(i)
            lev_gt = [x for x in levels[lev] if x > i]
            levels[lev] = list(set(levels[lev]).difference(set(lev_gt)))
          graph[i] = lt[0]

# Get now the returned answer table

  res = []
  i = levels[-1][0]
  while(i != 0):
    res.append(i)
    i = graph[i]
  res = list(reversed(res))
  return res

print(" ".join([str(x) for x in lgis(maxnum, perm)]))
print(" ".join(
  list(reversed([str(x) for x in lgis(maxnum, list(reversed(perm)))]))))