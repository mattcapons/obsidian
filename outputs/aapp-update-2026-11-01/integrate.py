from pathlib import Path
course=Path('University/Advanced Algorithms and Parallel Programming')
def replace(path, old, new):
 s=path.read_text(); assert s.count(old)==1,(path,old[:100],s.count(old));path.write_text(s.replace(old,new))
p=course/'Notes/Competitive Analysis.md'
start=p.read_text().index('**6. Explain the advantage of future knowledge')
end=p.read_text().index('\n## Revision questions',start)
replace(p,p.read_text()[start:end],'''**6. Explain the advantage of future knowledge with correct quantifiers.** Two-frame demand-paging caches start empty. Reveal $A,B,C$. After an online strategy serves $C$, let an adversary choose a final request from $\\{A,B\\}$ that is absent from its cache. Compare its total faults with OPT. Why does this not produce one fixed sequence that defeats every online strategy?

> [!faq]- Worked solution
> The first three distinct pages force at least three faults. After $C$ is loaded, at most one of $A,B$ fits alongside it, so the adversary can request an absent page and force a fourth fault. OPT, knowing which final page will be needed, retains that page and evicts the other when loading $C$, giving exactly three faults. The continuation depends on the online strategy's eviction. For a fixed chosen sequence, a strategy can coincidentally make the offline-optimal choice; the claim is “for every strategy, some sequence,” not “one sequence defeats every strategy.” This argument uses the stated demand-paging model, with the requested page resident after service and no free prefetching.
''')
p=course/'AAPP Index.md'
replace(p,'fourteen currently available slide decks (537 PDF pages)','fifteen currently available slide decks (577 PDF pages)')
row='| 14 | [[Amortized Analysis]] | Dynamic tables, aggregate, accounting and potential methods | [[lezione14AmortizedAnalysis.pdf\\|Amortized analysis]] |'
replace(p,row,row+'\n| 15 | [[Competitive Analysis]] | Online/offline models, MTF and inversion potentials, LRU versus MIN paging | [[lezione15CompetitiveAnalysis.pdf\\|Competitive analysis]] |')
route='- **Separate expected and amortized costs:** [[Randomized Data Structures#Comparing guarantees]] → [[Amortized Analysis#Worst-case per operation versus worst-case sequence]] → [[Amortized Analysis#Aggregate method]] → [[Amortized Analysis#Potential method]].'
replace(p,route,route+'\n- **Compare an online strategy with offline OPT:** [[Amortized Analysis#Potential method]] → [[Competitive Analysis#Competitive guarantees and the additive constant]] → [[Competitive Analysis#The inversion potential]] → [[Competitive Analysis#Proving paid-model MTF is 4-competitive]] → [[Competitive Analysis#LRU\'s competitive guarantee]].')
replace(p,'- [[Amortized Analysis#Exam practice]] — exact prefix costs, potentials and allocation models.','- [[Amortized Analysis#Exam practice]] — exact prefix costs, potentials and allocation models.\n- [[Competitive Analysis#Exam practice]] — list-update cost models, inversion accounting, startup terms, paging traces and online decisions.')
replace(p,'The fourteen decks establish','The fifteen decks establish')
replace(p,'Selection, primality/cryptosystems, treaps/skip lists, LCS, BDDs and dynamic-table amortization now have dedicated notes. Still awaiting lecture-specific decks for approximation, competitive/online methods (including move-to-front), further string-matching topics, and the broader parallel tools and patterns announced by the introduction.','Selection, primality/cryptosystems, treaps/skip lists, LCS, BDDs, dynamic-table amortization, and competitive/online methods now have dedicated notes. [[Competitive Analysis]] covers move-to-front and LRU versus offline MIN, including the paid/free list models and the distinct paging guarantee. Still awaiting lecture-specific decks for approximation, further string-matching topics, and the broader parallel tools and patterns announced by the introduction.')
replace(p,'[[Course Workflow#Current gaps and scope — 2026-10-26|current verification limits]]','[[Course Workflow#Current gaps and scope — 2026-11-01|current verification limits]]')
p=course/'Notes/Amortized Analysis.md'
replace(p,'Previous: [[Binary Decision Diagrams]] · Related:','Previous: [[Binary Decision Diagrams]] · Next: [[Competitive Analysis]] · Related:')
anchor='## Cost-model changes and limits'
replace(p,anchor,'''### From one-state costs to two-state comparisons

[[Competitive Analysis#The inversion potential]] applies the same telescoping identity to a potential $\\Phi(L_i,L_i^*)$ measuring disagreement between an online list and an offline comparator. The goal changes from a constant append charge to $\\widehat c_i\\le4c_i^*$, a bound relative to the comparator's cost. Summing gives $C_{\\mathrm{MTF}}(S)\\le4C_{\\mathrm{OPT}}(S)+\\Phi_0$, because final potential is nonnegative. This explains how amortized analysis can prove a competitive guarantee without proving constant actual time per request. See [[Competitive Analysis#Proving paid-model MTF is 4-competitive]] for the complete four-set derivation.

'''+anchor)
p=course/'Notes/Course Introduction.md'
replace(p,'[[Dynamic Programming and LCS]], [[Binary Decision Diagrams]], and [[Amortized Analysis]] now develop three further syllabus areas.','[[Dynamic Programming and LCS]], [[Binary Decision Diagrams]], [[Amortized Analysis]], and [[Competitive Analysis]] develop further syllabus areas, including move-to-front lists and LRU paging.')
replace(p,'fourteen supplied decks','fifteen supplied decks')
replace(p,'These short distinctions explain the syllabus categories; detailed approximation and competitive algorithms still await their lecture material.','[[Competitive Analysis]] now develops online list update and paging, while dedicated approximation material remains unavailable.')
replace(p,'fourteen PDFs currently supplied','fifteen PDFs currently supplied')
row='| [[Amortized Analysis]] | Sum resize costs, maintain credit, telescope potentials, handle first insertion and allocation models |'
replace(p,row,row+'\n| [[Competitive Analysis]] | State online/offline and cost models, derive MTF\'s inversion bound, trace LRU/MIN, interpret capacity and startup terms |')
replace(p,'fourteen decks currently available','fifteen decks currently available')
p=course/'Past Exam Question Bank.md'
replace(p,'## Online algorithms and competitive analysis\n\n*No dedicated study note is currently available for this topic.*','## Online algorithms and competitive analysis\n\nRelated study note: [[Competitive Analysis]] — online/offline models, move-to-front and its potential proof, and LRU versus MIN paging. The paid/free cost distinction matters for the competitive factor.')
p=course/'Exam Recap.md'
replace(p,'*Pending — bank section 16, AAPP-16-001–AAPP-16-015 (15 questions).* No dedicated theory note is currently linked in the bank.','*Pending — bank section 16, AAPP-16-001–AAPP-16-015 (15 questions).* Theory: [[Competitive Analysis]].')
p=course/'Course Workflow.md'
replace(p,'Last collection review: 2026-10-26','Last collection review: 2026-11-01')
replace(p,'1, 2, 3, 4, 4b, 5, 6, 7, 8, 10, 11, 12, 13, 14.','1, 2, 3, 4, 4b, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15.')
replace(p,'The current mapping covers fourteen PDFs and 537 physical pages.','On 2026-11-01, those fourteen hashes still match and lecture 15 is the sole new deck. The current mapping covers fifteen PDFs and 577 physical pages.')
row='| [[lezione14AmortizedAnalysis.pdf]] | 44 | [[Amortized Analysis]] | 1–44: tables/aggregate method (3–20), accounting (21–25), potential/telescoping/first insertion (26–42), conclusions/acknowledgments (43–44) |'
replace(p,row,row+'\n| [[lezione15CompetitiveAnalysis.pdf]] | 40 | [[Competitive Analysis]] | 1–40: cover/roadmap (1–2), list model and online/average-case analysis (3–10), MTF and competitive models (11–15), inversion potential and proof (16–29), free moves/startup/interpretation (30–32), paging/LRU/MIN (33–37), implementation examples/takeaways/references (38–40) |')
replace(p,'See [[#Current gaps and scope — 2026-10-26]] for current availability and coverage.','See [[#Current gaps and scope — 2026-11-01]] for current availability and coverage.')
replace(p,'## Current gaps and scope — 2026-10-26\n','## Current gaps and scope — 2026-10-26\n\n*Historical collection state; see [[#Current gaps and scope — 2026-11-01]] for the latest review.*\n')
print('Integrated new lecture; existing properties and exam-entry bodies retained.')
