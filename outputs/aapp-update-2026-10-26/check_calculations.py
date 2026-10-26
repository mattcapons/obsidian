from itertools import permutations, product
from math import comb,ceil,log2,gcd
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import json
checks={}
def partition(a,p,q):
 x=a[p];i=p
 for j in range(p+1,q+1):
  if a[j]<=x:i+=1;a[i],a[j]=a[j],a[i]
 a[p],a[i]=a[i],a[p];return i
A=[6,10,13,5,8,3,2,11];assert partition(A,0,7)==3 and A==[2,5,3,6,8,13,10,11]
A[4],A[6]=A[6],A[4];assert partition(A,4,7)==5 and A[4:]==[8,10,13,11]
assert sorted(A)[6]==11
for n in range(2,1001):
 sm=sum(max(k,n-1-k) for k in range(n));assert 4*sm<=3*n*n
 if n%2==0:m=n//2;assert sm==3*m*m-m
 else:m=n//2;assert sm==3*m*m+2*m
for n in range(50,10001):assert 12*(n//10)>=n
checks['selection']='Partition/rank trace, exact odd/even sums through n=1000, discard threshold through n=10000 passed.'
def checked(a,e,n):
 if e==0:return 1,False
 x,bad=checked(a,e//2,n);y=x*x%n;bad=bad or (y==1 and x not in (1,n-1))
 if e%2:y=a*y%n
 return y,bad
def mr(a,n):
 d=n-1;s=0
 while d%2==0:d//=2;s+=1
 x=pow(a,d,n)
 if x in (1,n-1):return True
 for j in range(1,s):
  x=x*x%n
  if x==n-1:return True
  if x==1:return False
 return False
assert pow(2,340,341)==1 and pow(3,340,341)==56 and checked(2,340,341)==(1,True)
assert [a for a in range(1,9) if checked(a,8,9)==(1,False)]==[1,8]
for n in range(5,300,2):
 composite=any(n%d==0 for d in range(2,int(n**.5)+1))
 passed=0
 for a in range(2,n-1):
  r,b=checked(a,n-1,n);ok=r==1 and not b;assert ok==mr(a,n)
  passed+=ok
 if composite:assert passed*4<=n-3
 else:assert passed==n-3
assert pow(7,3,55)==13 and pow(13,27,55)==7 and pow(7,27,55)==28 and pow(28,3,55)==7
assert 7*43%60==1 and pow(2,7,77)==51 and pow(51,43,77)==2
for n in [55,77]:
 e,d=(3,27) if n==55 else (7,43)
 assert all(pow(pow(m,e,n),d,n)==m for m in range(n))
assert 4**14<10**9<=4**15
checks['primality_and_RSA']='Fermat/root examples, checked-power versus standard strong tests for every base of odd n<300, quarter bound, both RSA instances on every message, and error budgets passed.'
def build(keys,prior):
 if not keys:return None
 k=min(keys,key=lambda k:prior[k]);return (k,build([x for x in keys if x<k],prior),build([x for x in keys if x>k],prior))
def visited(t,key):
 z=0
 while t:
  z+=1
  if t[0]==key:return z
  t=t[1] if key<t[0] else t[2]
 return z
def H(n):return sum((Fraction(1,i) for i in range(1,n+1)),Fraction())
for n in range(1,8):
 sums=[0]*n;miss=[0]*(n+1);num=0
 for perm in permutations(range(n)):
  prior=dict(zip(range(1,n+1),perm));t=build(list(prior),prior);num+=1
  for m in range(1,n+1):sums[m-1]+=visited(t,m)
  for m in range(n+1):miss[m]+=visited(t,m+.5)
 assert all(Fraction(sums[m-1],num)==H(m)+H(n-m+1)-1 for m in range(1,n+1))
 assert all(Fraction(miss[m],num)==H(m)+H(n-m) for m in range(n+1))
# Insert recursively with actual rotations, counting each pointer transformation.
def insert(t,k,p):
 if t is None:return [k,p,None,None],0
 if k<t[0]:
  t[2],cnt=insert(t[2],k,p)
  if t[2][1]<t[1]:
   q=t[2];t[2]=q[3];q[3]=t;t=q;cnt+=1
 else:
  t[3],cnt=insert(t[3],k,p)
  if t[3][1]<t[1]:
   q=t[3];t[3]=q[2];q[2]=t;t=q;cnt+=1
 return t,cnt
n=7;rot=[0]*n;num=0
for perm in permutations(range(n)):
 num+=1
 for m in range(1,n+1):
  t=None
  for k in range(1,n+1):
   if k!=m:t,_=insert(t,k,perm[k-1])
  t,r=insert(t,m,perm[m-1]);rot[m-1]+=r
assert all(Fraction(rot[m-1],num)==2-Fraction(1,m)-Fraction(1,n-m+1) for m in range(1,n+1))
checks['treaps']='Successful/unsuccessful path formulas verified over all priority orders through n=7; actual insertion rotations match exact expectation for every rank at n=7.'
def lcs(x,y):
 c=[[0]*(len(y)+1) for _ in range(len(x)+1)]
 for i,a in enumerate(x,1):
  for j,b in enumerate(y,1):c[i][j]=c[i-1][j-1]+1 if a==b else max(c[i-1][j],c[i][j-1])
 return c
assert lcs('ABAC','BAC')==[[0,0,0,0],[0,0,1,1],[0,1,1,1],[0,1,2,2],[0,1,2,3]]
assert lcs('ABA','BAA')==[[0,0,0,0],[0,0,1,1],[0,1,1,1],[0,1,2,2]]
c=lcs('ABCBDAB','BDCABA')
expected=[[0,0,0,0,0,0,0,0],[0,0,1,1,1,1,1,1],[0,0,1,1,1,2,2,2],[0,0,1,2,2,2,2,2],[0,1,1,2,2,2,3,3],[0,1,2,2,3,3,3,4],[0,1,2,2,3,3,4,4]]
assert list(map(list,zip(*c)))==expected
@lru_cache(None)
def calls(i,j):return 1 if i==0 or j==0 else 1+calls(i-1,j)+calls(i,j-1)
for i in range(11):
 for j in range(11):assert calls(i,j)==2*comb(i+j,i)-1
checks['LCS']='Both small tables, all 56 cells of the lecture table, and exact all-mismatch call counts through 10x10 passed.'
ite=lambda f,g,h:g if f else h
for a,b,c,d in product([False,True],repeat=4):
 F=a or b;G=a and c;Hh=b or d
 assert ite(F,G,Hh)==((a and c) or (not a and not b and d))
 assert ite(F,G,Hh)==ite(not F,Hh,G)
 assert ite(F,G,Hh)==(not ite(F,not G,not Hh))
# Build plain ROBDDs from full truth tables under specified orders, count reachable nodes.
def bdd_nodes(order,fn):
 uniq={};nextid=2
 def rec(level,ass):
  nonlocal nextid
  if level==len(order):return int(fn(ass))
  v=order[level];hi=rec(level+1,dict(ass,**{v:True}));lo=rec(level+1,dict(ass,**{v:False}))
  if hi==lo:return hi
  key=(v,hi,lo)
  if key not in uniq:uniq[key]=nextid;nextid+=1
  return uniq[key]
 rec(0,{});return len(uniq)
mux=lambda z:ite(z['s'],z['a'],z['b'])
assert bdd_nodes(['s','a','b'],mux)==3 and bdd_nodes(['a','b','s'],mux)==5
assert bdd_nodes(['a','b','c'],lambda z:z['b'])==1
checks['BDD']='All 16 assignments of the supplied ITE example, complement identities, composition/reduction example, and 3-versus-5-node ordering example passed.'
cap=s=cost=alloccost=0;oldphi=oldphi2=0;charges=charges2=0
for i in range(1,10001):
 c=1;a=1
 if cap==0:cap=1;a+=1
 elif s==cap:c+=s;a+=s+2*cap;cap*=2
 s+=1;cost+=c;alloccost+=a;phi=2*s-cap;phi2=6*s-3*cap
 charge=c+phi-oldphi;charge2=a+phi2-oldphi2;oldphi=phi;oldphi2=phi2
 assert charge==(2 if i==1 else 3) and charge2==(5 if i==1 else 7)
 charges+=charge;charges2+=charge2
 assert cost==i+cap-1 and alloccost==i+3*cap-2
 assert charges==cost+phi and charges2==alloccost+phi2
 if i==10:assert (cost,phi,charges,alloccost)==(25,4,29,56)
 if i==17:assert (cost,cap,phi,charges)==(48,32,2,50)
checks['amortized']='Exact copy/write and allocation-inclusive costs, both potentials, first-operation exceptions, and telescoping balances verified through 10000 appends.'
checks['skip_list']='64/8=8 expected level-4 keys, union bound 64/4096=1/64, and geometric expected height 2 checked analytically in note.'
p=Path('outputs/aapp-update-2026-10-26/calculations.json');p.write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
