from pathlib import Path
import re

bank_path = Path('University/Advanced Algorithms and Parallel Programming/Past Exam Question Bank.md')
out = Path('outputs/performance-review-2026-10-30')

feedback = {
1: r'''**Assessment: partly correct, but you give a prediction law instead of the general definition.** You recognize how parallelizable work and processor count affect ideal speedup. However, your formula mixes an undefined $f$ with $t$. Use one symbol consistently, and define the fraction in terms of sequential execution time. Amdahl's law applies under additional assumptions; it is not the definition of speedup.

**Suggested exam answer:** Speedup is the ratio of the sequential execution time to the parallel execution time for the same problem and input: $S_p(n)=T_{\mathrm{seq}}(n)/T_p(n)$. With the course's best sequential baseline, write $S_p(n)=T^*(n)/T_p(n)$. A speedup of 4 means the parallel run takes one quarter of the sequential time.

**Your Amdahl formula, corrected:** If $f$ is the parallelizable fraction of the fixed-size sequential runtime, then ideal speedup is $S_p=1/((1-f)+f/p)$. This assumes ideal division of that parallel part and no additional overhead. It gives $S_p>1$ when $f>0$ and $p>1$; $p=1$ or $f=0$ gives 1. Measured speedup can be below 1 if a parallel implementation is slower.

**Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=11|slide 11]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

2: r'''**Assessment: mostly correct intuition; specify what remains fixed and how the fractions are measured.** You correctly connect Amdahl to strong scaling and Gustafson to scaled workloads. Both laws compare a sequential time with a parallel time; the distinction is not whether the program was initially sequential or already parallelized. Speedup is a dimensionless factor, usually expressed as “times faster,” rather than a percentage.

**Suggested exam answer:** Amdahl considers a **fixed-size problem**. If $s_A$ is the serial fraction of its sequential runtime, ideal speedup on $p$ processors is $S_A(p)=1/(s_A+(1-s_A)/p)$, with a ceiling of $1/s_A$ when $s_A>0$. Gustafson considers a **scaled problem at fixed parallel runtime**. If $s_G$ is the serial fraction of that parallel run, its scaled speedup is $S_G(p)=s_G+(1-s_G)p$. Its sequential comparison executes that same scaled workload. The two serial fractions use different runtime baselines. Both ideal formulas omit additional parallel overhead.

**Scaling qualification:** Strong scaling fixes total problem size. Weak scaling fixes work per processor while total work grows with $p$; approximately constant runtime is the desired outcome, rather than a guarantee. Gustafson's fixed-time viewpoint explains the benefit of growing the parallel workload.

**Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=28|slide 28]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

3: r'''**Assessment: correct True/False choice, but the explanation is insufficient.** False is the intended answer. Saying that one formula uses a fraction and the other a multiplication describes their algebra, not why they are compatible. Both formulas contain a serial fraction and processor count.

**Suggested exam answer:** False. Gustafson challenges applying a fixed-problem-size assumption to workloads that grow with the available processors; he does not invalidate Amdahl's calculation under its assumptions. Amdahl holds problem size fixed, whereas Gustafson considers scaling the parallel workload within a fixed runtime. Their serial fractions are measured relative to the sequential and parallel runtimes respectively. For the same execution, using the corresponding fractions gives the same speedup. See [Gustafson, *Reevaluating Amdahl's Law*, fixed-size and scaled-size models](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf#page=2).

**Example:** A sequential run takes 100 seconds: 20 serial and 80 parallelizable. With four ideal processors it takes $20+80/4=40$ seconds, so speedup is $2.5$. Amdahl uses $s_A=20/100=0.2$ and gives $1/(0.2+0.8/4)=2.5$. Gustafson uses $s_G=20/40=0.5$ and gives $0.5+0.5\cdot4=2.5$. Substituting the same numerical fraction into both formulas would describe different assumptions.

**Study:** [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

4: r'''**Assessment: correct.** You give the course's formula and correctly identify the best sequential baseline. State that both times refer to the same problem and input size. $T^*$ need not equal $T_1$, the time of the parallel algorithm run on one processor.

**Suggested exam answer:** The speedup of a PRAM algorithm on $p$ processors is $S_p(n)=T^*(n)/T_p(n)$, where $T^*(n)$ is the execution time of the best sequential algorithm used as the baseline and $T_p(n)$ is the parallel execution time on $p$ processors for the same problem and input. It measures the factor by which parallel execution reduces runtime.

**Study:** [[PRAM#Performance quantities]]; [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=11|slide 11]].''',

5: r'''**Assessment: no self-contained answer supplied.** Your earlier explanation contains the main idea, but “I already answered this” does not supply the requested definition. Write the formula and specify what its serial fraction measures.

**Suggested exam answer:** Gustafson defines scaled speedup by comparing the runtime of a scaled problem on $p$ processors with the time a sequential processor would need for that same scaled problem. Normalize the parallel runtime to 1, and let $s_G$ be its serial fraction. The serial part still takes $s_G$ sequentially, while the parallel part would take $p(1-s_G)$. Therefore $S_G(p)=s_G+p(1-s_G)=p-(p-1)s_G$. The model scales the parallel workload to use additional processors while keeping parallel runtime fixed. This is the [scaled-size construction in Gustafson's original paper](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf#page=2).

**Example:** If a four-processor run takes 10 seconds, with 2 serial seconds and 8 parallel seconds, the corresponding sequential time is $2+4\cdot8=34$ seconds. Thus $s_G=0.2$ and $S_G=34/10=0.2+4\cdot0.8=3.4$.

**Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

6: r'''**Assessment: correct; refine the interpretation of inefficiency.** Your formula and distinction between one-processor runtime and allocated processor-time are correct. Idling is an important cause of low efficiency, but additional communication, scheduling, or synchronization overhead can also reduce efficiency on real systems. $pT_p$ measures allocated processor-time, including idle capacity, rather than only the operations actually performed.

**Suggested exam answer:** According to the course convention, efficiency is $E_p(n)=T_1(n)/(pT_p(n))$, where $T_1(n)$ is the time of the same parallel algorithm on one processor and $T_p(n)$ is its time on $p$ processors. It compares the one-processor runtime with the total allocated processor-time. Under ideal linear scaling, $T_p=T_1/p$ and $E_p=1$; a lower value indicates less effective use of the allocated processors relative to this baseline.

**Baseline caution:** The course defines speedup using $T^*$, so $E_p=S_p/p$ only when $T_1=T^*$. In general, $E_p=(T_1/T^*)\,S_p/p$. Keep this distinction, which you already handled correctly in question 004.

**Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].''',

7: r'''**Assessment: mostly correct; add the fixed-size/fixed-time assumptions and distinguish the fractions.** Your two runtime constructions are right. In Amdahl's model, $s+(1-s)/p$ is the normalized **parallel runtime**; speedup is its reciprocal. In Gustafson's model, $s+(1-s)p$ is the normalized **sequential runtime** of the scaled problem, and also its speedup because parallel runtime is normalized to 1. The two occurrences of $s$ therefore have different denominators.

**Suggested exam answer:** Amdahl assumes a fixed problem size with an unchanged serial component. Normalize its sequential runtime to 1; if the serial fraction is $s_A$, then ideal parallel runtime is $s_A+(1-s_A)/p$ and speedup is its reciprocal. Gustafson assumes that the parallel workload grows with processor count while parallel runtime remains fixed and the serial component does not grow in the ideal model. Normalize that parallel runtime to 1; with serial fraction $s_G$, the same scaled work would take $s_G+p(1-s_G)$ sequentially. Both models assume ideal distribution of the parallel part over comparable processors and omit additional parallel overhead. Their different workload assumptions explain why they do not contradict each other.

**Study:** [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',
}

original = bank_path.read_bytes()
text = original.decode('utf-8')
snapshot = (out / 'Past Exam Question Bank.md.snapshot').read_text()
for number, body in feedback.items():
    qid = f'AAPP-02-{number:03d}'
    pattern = rf'(^### {qid}\n.*?)(?=^### |^## |\Z)'
    match = re.search(pattern, text, re.M | re.S)
    before = re.search(pattern, snapshot, re.M | re.S)
    assert match and before, qid
    assert match[1] == before[1], f'{qid} changed during review'
    old = '> [!note]- Feedback\n> Not reviewed yet.'
    assert match[1].count(old) == 1, qid
    callout = '> [!note]- Feedback\n> **Reviewed: 2026-10-30.**\n>\n'
    callout += '\n'.join('> ' + line if line else '>' for line in body.splitlines())
    text = text[:match.start()] + match[1].replace(old, callout) + text[match.end():]

assert bank_path.read_bytes() == original, 'Note changed while preparing corrections'
bank_path.write_bytes(text.encode('utf-8'))
print('Added feedback to AAPP-02-001–007; original attempts preserved. Question 008 remains unanswered and unreviewed.')
