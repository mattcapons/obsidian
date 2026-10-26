---
tags:
  - aapp
  - lecture
lecture: "10"
source: "[[lecture10PrimalityTest.pdf]]"
---
# Primality Testing and Cryptosystems

[[AAPP Index|Course index]] · Previous supplied lecture: [[Selection and Order Statistics]] · Next: [[Randomized Data Structures]] · Prerequisites: [[Randomized Algorithms#Las Vegas and Monte Carlo]] · [[Divide and Conquer#Exponentiation by squaring]]

## Overview

The deck moves from trial division to Fermat tests, explains why pseudoprimes and Carmichael numbers defeat a naive converse, and strengthens the test by detecting nontrivial square roots of 1 during modular exponentiation. Its application is public-key cryptography: encryption, signatures, RSA key generation, and modular inverses. The cover is labeled 2026–2027.

Source: [[lecture10PrimalityTest.pdf#page=2|Primality tests, pp. 2–15]] · [[lecture10PrimalityTest.pdf#page=16|Cryptosystems, pp. 16–26]]. Page 27 acknowledges Motwani–Raghavan and the Freiburg lectures.

## Primality and input length

An integer $n\ge2$ is prime when its only **positive** divisors are 1 and $n$. Otherwise it is composite. The adjective positive matters: the literal divisor implication on page 2 omits the domain of the divisor.

If $n=ab$ is composite with $1<a\le b$, then $a\le\sqrt n$; otherwise $ab>n$. This proves that trial division only needs potential factors through $\lfloor\sqrt n\rfloor$.

```text
TRIAL-PRIME(n)
    if n < 2: return false
    if n == 2: return true
    if n is even: return false
    d = 3
    while d*d <= n
        if n mod d == 0: return false
        d += 2
    return true
```

Every possible composite odd input has an odd factor checked by the loop. A found factor certifies compositeness; exhausting the loop proves primality. The worst case uses $\Theta(\sqrt n)$ trial divisions under a unit-cost arithmetic model. This is a worst-case count, not the cost for an even input rejected immediately.

The input is a binary integer of length $L=\lfloor\log_2n\rfloor+1$. Since $n$ can be approximately $2^L$, $\sqrt n$ is approximately $2^{L/2}$. Trial division is exponential in **bit length**, even though it looks polynomial in the numerical value $n$. A polynomial-time primality test must be polynomial in $L$.

Source: [[lecture10PrimalityTest.pdf#page=2|Trial division and the polynomial-time goal, pp. 2–3]].

## Fermat's theorem and pseudoprimes

Fermat's little theorem states that for prime $p$ and $0<a<p$,

$$
a^{p-1}\equiv1\pmod p.
$$

Therefore, if a chosen base $a$ produces $a^{n-1}\not\equiv1\pmod n$, the input is definitely composite. This is the contrapositive of the theorem. The converse is false: passing the congruence does not prove primality.

For example, $341=11\cdot31$ is composite, but $2^{10}=1024\equiv1\pmod{341}$, so $2^{340}=(2^{10})^{34}\equiv1$. It is a **base-2 pseudoprime**. Base 3 does expose it: $3^{340}\bmod341=56$.

```text
FERMAT-ROUND(n, a)
    if MOD-POWER(a, n-1, n) != 1: return COMPOSITE
    return POSSIBLY-PRIME
```

Randomizing the base changes which composites can escape a given run, but does not automatically provide a universal error bound. One must count the misleading bases for each fixed composite.

### Carmichael numbers

A Carmichael number is composite yet passes Fermat's congruence for **every coprime base**. The smallest is $561=3\cdot11\cdot17$. Thus repeating a Fermat test only on coprime bases cannot reject this input, however many repetitions are used. A noncoprime base can still reveal compositeness: if $1<\gcd(a,n)<n$, the gcd itself is a factor.

The distinction is between a **witness**, which exposes compositeness, and a **liar**, which lets a particular composite pass a particular test. The terms describe a base relative to the chosen input and test, not a global property of that base.

Source: [[lecture10PrimalityTest.pdf#page=4|Fermat test, pseudoprimes and Carmichael numbers, pp. 4–8]].

## Nontrivial square roots of 1

For prime $p$, the congruence $x^2\equiv1\pmod p$ implies

$$
(x-1)(x+1)\equiv0\pmod p.
$$

A prime dividing a product divides one factor, so $x\equiv1$ or $x\equiv-1\pmod p$. Consequently a residue satisfying $x^2\equiv1\pmod n$ with $x\not\equiv\pm1$ is a **certificate that $n$ is composite**.

For $n=35$, $6^2=36\equiv1$, yet $6\ne1,34$. In this example $\gcd(6-1,35)=5$ and $\gcd(6+1,35)=7$ also recover factors. The primality test only needs the certificate, not a complete factorization.

Source: [[lecture10PrimalityTest.pdf#page=9|Nontrivial square roots]].

## Modular exponentiation with a witness check

Exponentiation by squaring computes a half-power once, squares it, and multiplies by the base when the exponent is odd. Reduce **after every multiplication**: $(uv)\bmod n$ depends only on $u\bmod n$ and $v\bmod n$. This avoids constructing the enormous integer $a^{n-1}$.

The slide code stores a global flag. The following equivalent explanatory version returns a pair, making flag initialization and propagation explicit. Integer division of the exponent rounds down.

```text
CHECKED-POWER(a, e, n)              // return (a^e mod n, witnessFound)
    if e == 0: return (1, false)
    (x, bad) = CHECKED-POWER(a, floor(e/2), n)
    y = (x*x) mod n
    if y == 1 and x != 1 and x != n-1
        bad = true
    if e is odd: y = (a*y) mod n
    return (y, bad)

CHECKED-ROUND(n, a)                 // odd n >= 5, 2 <= a <= n-2
    (r, bad) = CHECKED-POWER(a, n-1, n)
    if r != 1 or bad: return COMPOSITE
    return POSSIBLY-PRIME
```

The returned residue is correct by induction on $e$, exactly as in [[Divide and Conquer#Following the calls and returns of POWER]]. A true `bad` flag records an actual nontrivial square root, so it can never reject a prime. If the final residue differs from 1, Fermat's theorem also justifies rejection. Passing requires both checks to succeed.

![[aapp-lecture10-root-check.png|720]]

*The slide checks the saved half-power before the optional odd-exponent multiplication. The test concerns the squaring that just produced residue 1.* [[lecture10PrimalityTest.pdf#page=13|Source slide 13]].

### Trace: exposing the pseudoprime 341

Use $a=2$, exponent 340, and modulus 341. The recursive exponents are

$$
340\to170\to85\to42\to21\to10\to5\to2\to1\to0.
$$

On return:

| Exponent $e$ | Saved residue $x$ | Square $x^2\bmod341$ | Returned residue after optional factor 2 |
|---|---|---|---|
| 0 | — | — | 1 |
| 1 | 1 | 1 | 2 |
| 2 | 2 | 4 | 4 |
| 5 | 4 | 16 | 32 |
| 10 | 32 | 1 | 1 |
| 21 | 1 | 1 | 2 |
| 42 | 2 | 4 | 4 |
| 85 | 4 | 16 | 32 |
| 170 | 32 | 1 | 1 |
| 340 | 1 | 1 | 1 |

At exponent 10, $32^2\equiv1$ but $32\ne1,340$, so the flag becomes true and remains true. The final Fermat residue is 1, but the strengthened test rejects. Indeed $\gcd(32-1,341)=31$ and $\gcd(32+1,341)=11$.

Source: [[lecture10PrimalityTest.pdf#page=10|Fast exponentiation and test code, pp. 10–14]]. The full numerical trace is supplementary.

### Cost in two models

Halving the exponent gives $O(\log n)=O(L)$ recursive levels, each with at most two modular multiplications. Thus one round uses $O(L)$ **modular arithmetic operations**, with $O(L)$ recursive frames. It is not an $O(L)$ bit-operation claim.

With ordinary multiplication and reduction of $L$-bit operands costing $O(L^2)$, one round has the sufficient bound $O(L^3)$ bit operations, and $k$ rounds $O(kL^3)$. Faster arithmetic changes this bound. The important contrast with trial division is polynomial versus exponential dependence on input length. A machine implementation must also avoid overflow before reduction; mathematical pseudocode assumes exact arithmetic.

## Miller–Rabin form and one-sided error

The slide's checked exponentiation can be understood using the standard repeated-square form. Write

$$
n-1=2^s d,\qquad d\text{ odd}.
$$

The residues $a^d,a^{2d},\ldots,a^{2^sd}$ form a squaring chain. For a prime, if this chain reaches 1, its predecessor must be $1$ or $-1$; tracing backward shows that either the first value is 1 or some earlier value is $-1$. This explains the standard strong probable-prime test:

```text
MILLER-RABIN(n, k)
    if n < 2: return COMPOSITE
    if n == 2 or n == 3: return PRIME
    if n is even: return COMPOSITE
    write n-1 = 2^s * d, with d odd
    repeat k times
        a = fresh uniform random integer in [2, n-2]
        x = MOD-POWER(a, d, n)
        if x == 1 or x == n-1: continue to next round
        passed = false
        for j = 1 to s-1
            x = (x*x) mod n
            if x == n-1
                passed = true
                break
            if x == 1: return COMPOSITE
        if not passed: return COMPOSITE
    return POSSIBLY-PRIME
```

This standard form is supplementary, included to clarify the slide's test rather than introduce another exam topic. With independent uniform bases, a fixed odd composite passes $k$ rounds with probability at most $4^{-k}$. A prime always passes. See [Menezes, van Oorschot and Vanstone, *Handbook of Applied Cryptography*, §4.2.3, Algorithm 4.24 and Fact 4.25](https://cacr.uwaterloo.ca/hac/about/chap4.pdf).

For target error $\delta$, choose

$$
k\ge\left\lceil\log_4(1/\delta)\right\rceil.
$$

Ten independent rounds give $4^{-10}=2^{-20}\approx9.54\times10^{-7}$. Rechecking the same randomly chosen base ten times supplies no such amplification.

> [!warning] What the probability statement means
> Page 3's output-conditioned wording is imprecise. The guarantee is: **for every fixed composite $n$**, the probability over random bases of reporting POSSIBLY-PRIME is at most $4^{-k}$. It is not automatically the posterior probability that $n$ is composite after observing a pass. The latter also depends on how candidate integers were selected; see HAC §4.4, Note 4.47. Relative to the question “is $n$ prime?”, this Monte Carlo test permits false positives, while a COMPOSITE answer is certain. This makes the slide's “false-biased” terminology precise.

> [!warning] Apparent count/domain error on page 15
> The slide says at most $(n-9)/4$ bases in $0<a<n$ let a composite pass. At $n=9$, both 1 and 8 pass, but the stated bound is zero. The smaller count is compatible with excluding both trivial bases in a suitable strong-test statement, not with the printed domain. Use the standard at-most-one-quarter bound with the explicit sampling domain above. The preceding slide samples $[2,n-1]$, which retains the always-passing base $n-1$; the pseudocode here uses the usual $[2,n-2]$ interval and handles small inputs separately.

Source: [[lecture10PrimalityTest.pdf#page=3|Error wording]] · [[lecture10PrimalityTest.pdf#page=15|Printed count theorem]].

## Secret keys, public keys, and security goals

In a symmetric system, communicating parties share a secret key. If each unordered pair among $N$ parties needs its own pairwise key, the number is $\binom N2=N(N-1)/2$. This is a count under that key-management arrangement, not a universal requirement for every network protocol.

In the deck's public-key abstraction, participant $A$ has a public transformation $P_A$ and a private inverse $S_A$. Both legitimate transformations are efficient, while recovering the private operation from public information is assumed computationally infeasible. The slides idealize them as mutual inverses on a message domain.

For **confidentiality from Alice to Bob**, Alice encrypts using **Bob's public key**: $C=P_B(M)$. Bob decrypts with **Bob's private key**: $M=S_B(C)$.

![[aapp-lecture10-public-key.png|720]]

*Encryption uses the recipient's public key, and decryption uses the recipient's private key. This diagram depicts confidentiality, not every security property simultaneously.* [[lecture10PrimalityTest.pdf#page=21|Source slide 21]].

For the deck's **signature abstraction**, Alice computes $\sigma=S_A(M')$ and sends $(M',\sigma)$. Bob or anyone else verifies using **Alice's public key**, checking $P_A(\sigma)=M'$. Verification is public; producing a valid signature is intended to require private information.

The goals on page 18 are confidentiality, integrity, sender authenticity, and “liability,” related to attributing an authenticated transmission. They are distinct: public-key encryption alone does not establish sender authenticity or integrity. The public key must itself be authenticated. The inverse-function signature diagram is an algebraic model, not a general construction for every signature scheme. [HAC, Chapter 8, §8.1](https://cacr.uwaterloo.ca/hac/about/chap8.pdf).

Source: [[lecture10PrimalityTest.pdf#page=17|Secret keys, security goals, encryption and signatures, pp. 17–23]].

## RSA key generation and operations

Choose distinct primes $p,q$, then set $n=pq$ and $\varphi=(p-1)(q-1)$. Select an exponent $e$ with

$$
1<e<\varphi,\qquad\gcd(e,\varphi)=1.
$$

Compute the multiplicative inverse $d=e^{-1}\bmod\varphi$, so $ed=1+t\varphi$ for some integer $t$. Publish $(e,n)$ and retain the private exponent $d$; factors $p,q$ must also be kept secret. Encode a message representative as an integer $0\le M<n$:

$$
C=M^e\bmod n,\qquad M=C^d\bmod n.
$$

> [!warning] RSA condition on page 24
> “$e$ does not divide $(p-1)(q-1)$” is insufficient. For example, $e=6$ does not divide 40, but $\gcd(6,40)=2$, so no inverse modulo 40 exists. The gcd condition printed immediately below is the required one. The slide's prime-size parameter is a historical course example, not a current deployment recommendation. These formulas describe textbook RSA; actual encryption/signature encodings are outside this deck.

The key conditions and message range agree with [HAC, §8.2.1, Algorithms 8.1 and 8.3](https://cacr.uwaterloo.ca/hac/about/chap8.pdf). The lecture's $2\ell$-bit message blocks fit because its $(\ell+1)$-bit primes satisfy $n\ge2^{2\ell}$, so $M<2^{2\ell}\le n$.

### Why decryption works, including noncoprime messages

For a message not divisible by $p$, Fermat's theorem gives

$$
M^{ed}=M^{1+t(p-1)(q-1)}\equiv M\pmod p.
$$

If $p$ divides $M$, both sides are zero modulo $p$, so the same conclusion holds. Repeat for $q$. Since $p,q$ are distinct primes, congruence modulo both implies congruence modulo $pq=n$. Thus $M^{ed}\equiv M\pmod n$ for **every** representative, including those not coprime to $n$. Applying Euler's theorem without checking coprimality would leave a hole in that proof.

This is a supplementary correctness derivation of [[lecture10PrimalityTest.pdf#page=24|RSA, pp. 24–25]]. Factoring $n$ reveals $\varphi$ and hence $d$; that explains why efficient prime testing is useful for key generation without providing an efficient factoring algorithm.

## Extended Euclid and a complete small RSA example

Extended Euclid returns $g,x,y$ such that $xa+yb=g=\gcd(a,b)$:

```text
EXTENDED-EUCLID(a, b)               // a,b >= 0, not both zero
    if b == 0: return (a, 1, 0)
    (g, u, v) = EXTENDED-EUCLID(b, a mod b)
    return (g, v, u - floor(a/b)*v)
```

Why do the returned coefficients work? Substitute $a\bmod b=a-\lfloor a/b\rfloor b$ into $ub+v(a\bmod b)=g$. The result is $va+(u-\lfloor a/b\rfloor v)b=g$. If $a=\varphi$ and $b=e$ with gcd 1, the coefficient of $e$ is its inverse modulo $\varphi$.

For an illustrative small instance, choose $p=5,q=11$, giving $n=55$ and $\varphi=40$. Let $e=3$. Euclid gives $40=13\cdot3+1$, so

$$
1=40-13\cdot3,\qquad d=-13\bmod40=27.
$$

Encrypt $M=7$: $C=7^3\bmod55=343\bmod55=13$. To decrypt, square successively:

$$
13^2\equiv4,\quad13^4\equiv16,\quad
13^8\equiv36,\quad13^{16}\equiv31\pmod{55}.
$$

Since $27=16+8+2+1$,

$$
13^{27}\equiv31\cdot36\cdot4\cdot13
\equiv16\cdot4\cdot13\equiv9\cdot13\equiv7\pmod{55}.
$$

The message is recovered. These tiny numbers illustrate the arithmetic only. In the signature model, signing representative 7 instead computes $7^{27}\bmod55=28$; verification gives $28^3\bmod55=7$. Encryption and signing use different parties' keys for different purposes.

Source: [[lecture10PrimalityTest.pdf#page=26|Extended Euclid]]. The numerical example and expanded coefficient proof are supplementary.

## Takeaways

- State whether complexity counts modular operations or bit operations.
- A passing Fermat congruence is necessary for primality, not sufficient.
- A nontrivial square root of 1 certifies compositeness.
- The strengthened randomized test is one-sided Monte Carlo, with independent-base amplification.
- Encryption uses the recipient's key pair; signing uses the sender's key pair.
- RSA needs an invertible exponent modulo $\varphi$, and correctness includes noncoprime messages.

## Exam practice

These are original exercises. Retrieved classification questions are in [[Past Exam Question Bank#Primality testing]].

**1. Explain a failure certificate.** For $n=65$, a modular calculation finds $x=14$ with $x^2\equiv1\pmod{65}$. What can be concluded? Recover factors using gcds.

> [!faq]- Worked solution
> $14^2=196=3\cdot65+1$ and $14\ne1,64$. Thus 65 is composite. The gcds are $\gcd(13,65)=13$ and $\gcd(15,65)=5$. Such a witness cannot arise modulo a prime.

**2. Choose an error budget.** How many independent strong-test rounds make the false-prime probability for every fixed composite at most $10^{-9}$? Does that bound directly state the probability that a randomly generated passing candidate is composite?

> [!faq]- Worked solution
> $k=\lceil\log_4(10^9)\rceil=15$. Fourteen give about $3.73\times10^{-9}$; fifteen about $9.31\times10^{-10}$. The guarantee conditions on a composite input. Reversing that condition needs a distribution of candidates and a Bayes calculation.

**3. Find a modular inverse.** Use $p=7,q=11,e=7$. Find $n,\varphi,d$, encrypt $M=2$, and verify decryption.

> [!faq]- Worked solution
> $n=77$, $\varphi=60$. Since $1=2\cdot60-17\cdot7$, $d=-17\bmod60=43$. Encryption gives $2^7\bmod77=51$. Since $ed=301=1+5\cdot60$, the correctness argument gives $51^{43}\bmod77=2$; repeated squaring confirms it. The inverse exists because $\gcd(7,60)=1$.

**4. Compare cost models.** Why is $\Theta(\sqrt n)$ trial division not polynomial time in input length, while $O(\log n)$ modular multiplications per round can give polynomial bit complexity?

> [!faq]- Worked solution
> An $L$-bit value can be near $2^L$, so trial division may use about $2^{L/2}$ divisions. Modular exponentiation uses $O(L)$ multiplications of bounded-length residues; even an $O(L^2)$ implementation per modular multiplication gives $O(L^3)$ bit work. Treating enormous-integer multiplication as one bit operation would be a model error.

## Revision questions

1. What does a Fermat witness prove?
2. Why do Carmichael numbers matter?
3. Where does the nontrivial-root check occur in recursive powering?
4. Why must each random round use fresh randomness?
5. What condition makes $e^{-1}\bmod\varphi$ exist?
6. Why is “encrypt with the sender's public key” wrong for confidentiality to Bob?

> [!faq]- Answer sketch
> 1. Compositeness. 2. Every coprime base passes the Fermat test, so that test lacks the desired universal amplification guarantee. 3. Immediately after squaring the saved half-power, before an optional multiplication by the base. 4. Reusing a liar repeats the same failure. 5. $\gcd(e,\varphi)=1$. 6. Bob needs to decrypt with his own private key, so Alice encrypts with Bob's public key.
