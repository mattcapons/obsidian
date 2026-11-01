from itertools import permutations,product
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
import json
out=Path('outputs/aapp-update-2026-11-01');results={}
def inv(a,b):
 pos={x:i for i,x in enumerate(b)}
 return sum(pos[a[i]]>pos[a[j]] for i in range(len(a)) for j in range(i+1,len(a)))
def mtf(initial,seq):
 a=list(initial);rows=[]
 for x in seq:
  r=a.index(x)+1;a.remove(x);a.insert(0,x)
  rows.append({'request':x,'rank':r,'paid':2*r-1,'after':a.copy()})
 return rows
rows=mtf([12,3,50,14,17,4],[14,14,3,14]);assert [r['rank'] for r in rows]==[4,1,3,2];assert sum(r['paid'] for r in rows)==16
rows1=mtf('ABCD','CACD');assert [r['rank'] for r in rows1]==[3,2,2,4];assert sum(r['paid'] for r in rows1)==18
assert sum(r['rank'] for r in rows1)==11
results['mtf_locality_trace']=rows;results['practice1']=rows1
assert sum(p*r for p,r in zip([Fraction(1,10),Fraction(6,10),Fraction(3,10)],[1,2,3]))==Fraction(22,10)
assert sum(p*r for p,r in zip([Fraction(6,10),Fraction(3,10),Fraction(1,10)],[1,2,3]))==Fraction(15,10)
a=tuple('ECADB');b=tuple('CABDE');assert inv(a,b)==5
# Exhaustive local proof checks, including every possible adjacent comparator swap.
checked=0
for n in range(1,6):
 for a in permutations(range(n)):
  for b in permutations(range(n)):
   phi=2*inv(a,b)
   for x in a:
    r=a.index(x)+1;rs=b.index(x)+1
    aa={y for y in a[:r-1] if b.index(y)<rs-1};bb=set(a[:r-1])-aa
    nxt=(x,)+tuple(y for y in a if y!=x);delta=2*inv(nxt,b)-phi
    assert delta==2*(len(aa)-len(bb))
    assert 2*r-1+delta==4*len(aa)+1<=4*rs
    # Free-forward promotion by comparator, to every permitted earlier position.
    for j in range(rs):
     rest=[y for y in b if y!=x];free=tuple(rest[:j]+[x]+rest[j:])
     assert inv(nxt,free)<=inv(nxt,b)
     assert r+inv(nxt,free)-inv(a,b)<=2*rs
    for j in range(n-1):
     c=list(b);c[j],c[j+1]=c[j+1],c[j];full_delta=2*inv(nxt,c)-phi
     assert abs(2*inv(nxt,c)-2*inv(nxt,b))==2
     assert full_delta<=2*(len(aa)-len(bb)+1)
     assert 2*r-1+full_delta<=4*(rs+1)
    checked+=1
results['exhaustive_local_access_cases_n_le_5']=checked
# Exact offline paid costs: allow arbitrary paid rearrangements both before and after each search.
def paid_opt(initial,seq):
 states=list(permutations(initial));N=len(states);dist=[[inv(a,b) for b in states] for a in states]
 dp=[10**9]*N;dp[states.index(tuple(initial))]=0
 for x in seq:
  pre=[min(dp[i]+dist[i][j] for i in range(N)) for j in range(N)]
  access=[pre[j]+states[j].index(x)+1 for j in range(N)]
  dp=[min(access[i]+dist[i][j] for i in range(N)) for j in range(N)]
 return min(dp)
reverse=[]
for n in range(1,6):
 seq=tuple(reversed(range(n)));opt=paid_opt(tuple(range(n)),seq);cost=sum(r['paid'] for r in mtf(range(n),seq))
 assert opt==n*(n+1)//2;assert cost==n*(2*n-1);assert Fraction(cost,opt)==4-Fraction(6,n+1)
 reverse.append({'n':n,'MTF':cost,'OPT':opt})
results['reverse_order_exact_optima']=reverse
# Numeric potential examples.
a=tuple('ABCDE');b=tuple('EABCD');nxt=tuple('EABCD');after=tuple('EBACD')
assert 2*inv(a,b)==8 and inv(nxt,b)==0 and 2*inv(nxt,after)==2
assert 9+(2-8)==3
b=tuple('CAEBD');after=tuple('CAEDB');assert 2*inv(a,b)==8 and 2*inv(nxt,after)==10
assert 9+(10-8)==11
assert 4*40+12-6==166 and 4*40+12==172

def lru(seq,k):
 cache=[];rows=[]
 for x in seq:
  fault=x not in cache
  if not fault:cache.remove(x)
  elif len(cache)==k:cache.pop()
  cache.insert(0,x);rows.append((x,tuple(cache),fault))
 return sum(r[2] for r in rows),rows

def min_rule(seq,k):
 cache=set();rows=[]
 for i,x in enumerate(seq):
  fault=x not in cache;victim=None
  if fault:
   if len(cache)==k:
    nextpos=lambda p:seq.index(p,i+1) if p in seq[i+1:] else float('inf')
    victim=max(sorted(cache),key=nextpos);cache.remove(victim)
   cache.add(x)
  rows.append((x,tuple(sorted(cache)),fault,victim))
 return sum(r[2] for r in rows),rows

def paging_opt(seq,k):
 @lru_cache(None)
 def f(i,cache):
  if i==len(seq):return 0
  x=seq[i];cs=set(cache)
  if x in cs:return f(i+1,cache)
  if len(cs)<k:return 1+f(i+1,tuple(sorted(cs|{x})))
  return 1+min(f(i+1,tuple(sorted((cs-{v})|{x}))) for v in cs)
 return f(0,())
seq=tuple('ABCDABCD');L,lr=lru(seq,3);M,mr=min_rule(seq,3);assert (L,M,paging_opt(seq,3))==(8,5,5)
assert [''.join(r[1]) for r in lr]==['A','BA','CBA','DCB','ADC','BAD','CBA','DCB']
assert [''.join(r[1]) for r in mr]==['A','AB','ABC','ABD','ABD','ABD','BCD','BCD']
results['slide_paging_trace']={'LRU':lr,'MIN':mr}
seq=tuple('ABACAB');L,lr=lru(seq,2);M,mr=min_rule(seq,2);assert (L,M,paging_opt(seq,2))==(4,4,4)
assert [''.join(r[1]) for r in lr]==['A','BA','AB','CA','AC','BA']
results['practice4']={'LRU':lr,'MIN':mr}
# Exhaustively compare MIN with independent optimal set DP and the stated LRU bounds.
checked=0
for m in range(0,7):
 for seq in product(range(4),repeat=m):
  opts={k:paging_opt(seq,k) for k in range(1,5)}
  for k in range(1,5):
   L,_=lru(seq,k);M,_=min_rule(seq,k);assert M==opts[k]
   for h in range(1,k+1):assert L<=Fraction(k,k-h+1)*opts[h]+h
  checked+=1
results['exhaustive_paging_sequences_4_pages_length_le_6']=checked
assert Fraction(4,4-2+1)*12+2==18
for final in ['A','B']:
 seq=tuple('ABC'+final);assert paging_opt(seq,2)==3
results['all_assertions_passed']=True
(out/'calculations.json').write_text(json.dumps(results,indent=2));print(json.dumps({k:v for k,v in results.items() if k not in ['mtf_locality_trace','practice1','slide_paging_trace','practice4']},indent=2))
