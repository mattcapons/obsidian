import json
from pathlib import Path
from functools import lru_cache
from itertools import combinations

root=Path(__file__).parent
answers={}
omp='[OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).'
cancelref='[OpenMP cancellation](https://openmp.org/spec-html/5.2/openmpse99.html).'
posix='[Linux man-pages: POSIX threads overview](https://man7.org/linux/man-pages/man7/pthreads.7.html).'
def add(sec,nums,body,ref=None):
    if isinstance(nums,int): nums=[nums]
    for n in nums:
        key=f'AAPP-{sec:02d}-{n:03d}'
        assert key not in answers,key
        answers[key]=body.strip()+(('\n\n**Reference:** '+ref) if ref else '')

# Transcribed from the original embedded exam pages, including every join edge.
graphs={
 '2023jan':({1:2,2:1,3:3,4:2,5:1,6:2,7:5,8:1},[(1,2),(1,3),(1,7),(2,4),(3,4),(3,5),(4,6),(5,6),(6,8),(7,8)]),
 '2023dec':({1:100,2:100,3:100,4:50,5:100,6:300,7:50,8:50,9:50,10:100},[(1,2),(1,3),(1,4),(2,5),(3,5),(4,7),(5,6),(7,8),(7,9),(6,10),(8,10),(9,10)]),
 '2024jul':({1:50,2:200,3:250,4:200,5:50,6:100,7:200,8:450,9:50},[(1,2),(1,3),(1,4),(1,8),(2,5),(3,5),(4,5),(5,6),(5,7),(6,9),(7,9),(8,9)]),
 '2025jan':({0:10,1:100,2:10,3:100,4:50,5:50,6:100,7:100,8:50,9:50,10:10},[(0,1),(0,2),(0,3),(1,4),(2,5),(2,6),(3,7),(4,8),(7,9),(5,10),(6,10),(8,10),(9,10)]),
 '2025jul':({i:1 for i in range(1,8)},[(1,2),(1,3),(2,4),(2,5),(3,6),(6,5),(6,7),(4,7),(5,7)]),
 '2025dec':({1:100,2:150,3:100,4:100,5:100,6:100,7:100},[(1,2),(1,3),(1,4),(2,5),(3,5),(4,6),(5,7),(6,7)]),
 '2026sep':({1:30,2:20,3:10,4:10,5:10,6:10,7:50,9:20,10:10,11:30},[(1,2),(1,4),(2,5),(3,6),(3,7),(5,6),(5,10),(7,6),(4,9),(10,9),(6,11)])
}
def topo(w,e):
    done=[]
    while len(done)<len(w):
        ready=sorted(v for v in w if v not in done and all(a in done for a,b in e if b==v))
        assert ready,'cycle'
        done.extend(ready)
    return done
def span(w,e):
    finish={}
    for v in topo(w,e): finish[v]=w[v]+max([finish[a] for a,b in e if b==v] or [0])
    return max(finish.values())
def opttime(w,e,p):
    nodes=sorted(w); bit={v:1<<k for k,v in enumerate(nodes)}; allmask=sum(bit.values())
    parents={v:sum(bit[a] for a,b in e if b==v) for v in nodes}
    @lru_cache(None)
    def solve(done,running):
        if done==allmask:return 0
        busy={v for v,t in running}
        ready=[v for v in nodes if not done&bit[v] and v not in busy and done&parents[v]==parents[v]]
        free=p-len(running); best=float('inf')
        for k in range(min(free,len(ready))+1):
            for chosen in combinations(ready,k):
                jobs=list(running)+[(v,w[v]) for v in chosen]
                if not jobs:continue
                dt=min(t for v,t in jobs); newdone=done
                for v,t in jobs:
                    if t==dt:newdone|=bit[v]
                remain=tuple(sorted((v,t-dt) for v,t in jobs if t>dt))
                best=min(best,dt+solve(newdone,remain))
        return best
    return solve(0,())
def taskcode(name):
    w,e=graphs[name]
    lines=['```c',f'int token[{max(w)+1}]; // dependence tokens; values are irrelevant', '#pragma omp parallel shared(token)', '{', '  #pragma omp single', '  {', '    #pragma omp taskgroup', '    {']
    for v in topo(w,e):
        pred=sorted(a for a,b in e if b==v)
        inclause=(' depend(in: '+', '.join(f'token[{a}]' for a in pred)+')') if pred else ''
        lines.extend([f'      #pragma omp task{inclause} depend(out: token[{v}])',f'      {{ Task{v}(); }}'])
    lines.extend(['    }','  }','}','```'])
    return '\n'.join(lines)+'\n\nA single generator creates sibling tasks in topological order. Each `depend` represents an actual edge; the token storage remains alive through the taskgroup. Tasks may run on any team thread. The taskgroup waits for the whole graph, without a global barrier between unrelated levels. Real task bodies must also obey the depicted data dependencies.'

add(20,1,r'''Total work is $W=17$. The critical path is $1\to3\to4\to6\to8$, of length $2+3+2+2+1=10$, so the unlimited-processor makespan/span is $D=10$ and average parallelism is $W/D=1.7$.

**Three threads** are needed to attain this span with indivisible nonpreemptive tasks. A schedule is: T1 on 0–2; T2 on 2–3, T3 on 2–5, T7 on 2–7; T4 on 5–7 and T5 on 5–6; T6 on 7–9; T8 on 9–10. Two threads cannot preserve the tight critical path while fitting both T7 and the required T2/T5 work into their available slots. Thus $\lceil W/D\rceil=2$ is only a lower bound on the required thread count.

'''+taskcode('2023jan'))
add(20,2,'Task parallelism represents a computation as a DAG: nodes are work units and edges are required predecessor relationships. Independent ready nodes may run concurrently. In OpenMP create a team, use a `single` region to generate tasks, and describe data dependencies with `depend(in/out/inout: ...)`. Use a `taskgroup` to await the group and descendants, or `taskwait` for the appropriate direct children. Keep dependent storage alive and generate sibling tasks in a suitable order; tasks are work units, not newly created operating-system threads.',omp)
add(20,3,r'''$W=1000$. A critical path is $1\to2\to5\to6\to10$ (also via T3), giving $D=700$ and $W/D=10/7\approx1.43$. Three threads give no ideal makespan improvement over two: with two, run T1 0–100; T2 and T3 100–200; T5 200–300 in one thread, while the other runs T4 200–250 and T7 250–300; then T6 300–600 while the other runs T8/T9 300–400; finally T10 600–700. Thus two suffice for the span; overhead can make a third less attractive.

'''+taskcode('2023dec'))
add(20,4,r'''Use **four threads** to minimize ideal execution time. $W=1550$ and the critical path $1\to3\to5\to7\to9$ has span $D=600$. Four threads run T2,T3,T4,T8 concurrently after T1, allowing T5 on 300–350, T7 on 350–550 and T9 on 550–600. Three threads cannot simultaneously meet the deadlines of the T8 branch and all three inputs of T5; their optimal nonpreemptive makespan is 750. The average parallelism $1550/600\approx2.58$ does not imply that three threads attain the span. This comparison ignores real thread-management overhead.''')
add(20,5,taskcode('2024jul'),omp)
add(20,6,r'''With enough threads, set **T3** to zero. It reduces the T5 input bottleneck from 250 to 200: the new span is $50+200+50+200+50=550$. Setting T7 to zero also gives span 550, because the T8 branch then becomes critical ($50+450+50$). Setting T1, T5 or T9 to zero gives 550 as well. Thus **T1, T3, T5, T7 and T9 tie**, each reducing span by 50; no single task eliminates both competing branches enough to do better. This is a span comparison; a fixed-thread optimum may have additional resource constraints.''')
add(20,7,r'''Assign each node its work/cost and draw every dependence edge. Total work is $W=\sum_v w_v$; span $D$ is the maximum weighted source-to-sink path, computed by $F(v)=w_v+\max_{u\to v}F(u)$. Average parallelism is $W/D$, and $T_p\ge\max(W/p,D)$. Inspect critical paths, widths, load balance, granularity and communication. These bounds do not by themselves give an attainable finite-thread schedule: precedence and indivisible tasks can require additional idle time.''')
add(20,8,r'''Including all tasks, $W=630$ and $D=270$, from $0\to3\to7\to9\to10$. Hence graph parallelism is $630/270=7/3\approx2.33$. If T0,T2,T10 are pure parallel-management overhead, a sequential implementation does useful work $W_{\rm useful}=630-30=600$. Its maximum theoretical speedup over this parallel graph is therefore $600/270=20/9\approx2.22$, not $630/270$. Keep the overhead on the parallel critical path; it disappears only from the sequential baseline.''')
add(20,9,taskcode('2025jan'),omp)
add(20,10,r'''Let each task cost one unit. There are seven tasks, so $W=7$. The longest path is $1\to3\to6\to5\to7$, with span $D=5$ and parallelism $7/5=1.4$. The edge $6\to5$ is essential: treating T5 as dependent only on T2 would underestimate the span. For equal cost $c$, work and span become $7c$ and $5c$, leaving the ratio unchanged.''')
add(20,11,taskcode('2025jul')+'\n\nTasks with `depend` fit this nontrivial DAG better than a single `sections` block, whose sections do not by themselves express these producer/consumer edges. In particular, T5 must await both T2 and T6.',omp)
add(20,12,r'''$W=750$ and $D=450$ on $1\to2\to5\to7$. Over an ideal span-attaining execution, the average number of busy processors is $W/D=5/3\approx1.67$; for an arbitrary actual schedule it is $W/T_p$ instead. **Three threads are faster** despite that average being below two. They execute T2,T3,T4 concurrently on 100–200 (T2 continues to 250), T6 on 200–300, T5 on 250–350, and T7 on 350–450. With two threads the best makespan is 500: run T2 100–250 and T3 100–200, T4 200–300, T5 250–350, T6 300–400, then T7 400–500. This compares ideal task costs and ignores thread overhead.''')
add(20,13,r'''$W=200$. There are two length-100 critical paths: $1\to2\to5\to6\to11$ and $3\to7\to6\to11$, so span is 100 and parallelism is 2. Halve **T11**, from 30 to 15. Both paths shorten to 85, but $1\to2\to5\to10\to9$ then becomes critical at 90. The new span is **90**, an improvement of 10. Halving T6 only reduces span to 95; shortening a task confined to one of the two original critical paths leaves the other at 100. Thus choosing the largest task alone (T7) would not reduce span.''')

scope='`shared(x)` makes threads refer to the same original object; it does not make accesses atomic. `private(x)` supplies a separate uninitialized instance (for ordinary C scalars), so it does not copy the original value. `firstprivate(x)` additionally initializes each private copy from the original value. `default(none)` requires explicit attributes for variables without predetermined rules; `default(shared)` sets the default for eligible variables. Data scope controls which object is used; synchronization controls visibility and ordering of accesses to a shared object.'
schedule='Use the `schedule` clause on `omp for` (or `parallel for`). `static` assigns chunks in advance, with low runtime overhead and predictable ownership/locality; it suits uniform iteration costs. With an explicit chunk size, chunks are assigned round-robin. `dynamic` hands out chunks as workers finish, improving balance for irregular work but adding coordination overhead and potentially poorer locality. Larger chunks reduce scheduling cost but may worsen balance; `guided` decreases chunk sizes over time. Scheduling does not make dependent iterations independent.'
numthreads='Use `num_threads(k)` on a parallel region, `omp_set_num_threads(k)` for subsequent relevant regions, or the `OMP_NUM_THREADS` environment variable. `omp_set_num_threads` updates the calling task\'s control state; it does not resize a team already executing. The actual team also depends on dynamic adjustment, active nesting limits, thread limits and available runtime resources. Query it inside the region with `omp_get_num_threads()`. Hardware affects performance and resources, but the number is not simply capped at the number of physical cores.'
workshare='Worksharing divides work among an existing team: `for`/Fortran `do` distributes loop iterations, `sections` distributes explicitly listed blocks, and `single` selects one team thread for a block; Fortran also has `workshare`. These constructs do not themselves create a team. Participants must encounter the required constructs in a consistent order and obey nesting/loop rules. Ensure iterations/blocks are independent or use reductions/synchronization for their dependencies, and provide enough coarse work to offset overhead. Most have an implicit end barrier unless an allowed `nowait` removes it.'
reduction='A `reduction(+:sum)` creates private partial sums initialized with the operator identity (0 for addition), then combines them with the original `sum` when the reduction completes. With `parallel for`, a team is created and loop iterations are distributed among its threads. This avoids a race on a shared accumulator and usually avoids the contention of an atomic update per iteration. Initialize the original value as intended and wait for completion before reading the result. Floating-point reassociation may change rounding; signed integer overflow must remain absent.'
nested='Yes: a `parallel` region can be encountered inside another, creating nested teams when enabled and permitted by the active-level settings, for example `omp_set_max_active_levels`. Inner regions may otherwise be serialized. Nested teams can be useful for genuinely hierarchical work, but often cause oversubscription and repeated team overhead. Prefer one team with tasks or a suitably collapsed/distributed loop when that expresses the decomposition efficiently.'
add(21,1,'False. OpenMP primarily describes shared-memory multithreading, SIMD and device offloading; a plain host OpenMP team does not communicate across independent node address spaces. MPI is normally used between distributed-memory nodes, often with OpenMP within each node. Device offload extends the set of execution/memory environments but does not make ordinary OpenMP a replacement for general cluster message passing.',omp)
add(21,[2,10,20],scope,omp)
add(21,3,'For an unordered tree search that must explore branches, use one outer `parallel` team, a `single` generator and recursive tasks for child subtrees. Capture child pointers safely, keep the tree immutable, use a synchronized found/result state or a valid reduction, and await all generated tasks; an optional cooperative cancellation can stop unnecessary search. Irregular subtree sizes benefit from task scheduling, but an extremely unbalanced chain has little parallelism. If this is an ordered binary-search-tree lookup, the usual search follows one comparison-selected path, so blindly searching both subtrees increases work rather than accelerating that algorithm.',omp)
add(21,4,'False if it means a hard limit equal to the physical core count. OpenMP can oversubscribe hardware with more software threads than cores; actual team sizes depend on runtime limits, settings, nesting and resources. The hardware determines how many threads can execute simultaneously and strongly affects useful performance. More threads than available compute/memory capacity can slow the program.',omp)
add(21,5,'Yes. The compiler and runtime must implement the needed OpenMP version/features, and OpenMP must be enabled, for example with the compiler\'s appropriate option. A compiler may accept only an older feature set or lack some offload targets. Without support, ordinary OpenMP pragmas may be ignored and code can run serially, while runtime API calls still need declarations/linking. Associated loops/regions must also satisfy OpenMP syntax and canonical-form restrictions.',omp)
add(21,[6,23],workshare,omp)
add(21,7,'A pointer-linked list of unknown length is not directly an indexed canonical `omp for`. One `single` thread can traverse links and create a task per node (or per batch), capturing the node pointer with `firstprivate`; tasks search immutable node contents and publish a result safely. Pointer chasing/task creation remains a serial producer bottleneck, so batch sufficiently expensive work. Alternatively first collect node pointers into an indexed array and parallelize that search, accounting for the preprocessing cost. A mutable list needs additional synchronization.',omp)
add(21,[8,21],nested,omp)
add(21,9,'OpenMP uses fork-join: the encountering thread forms a team at a parallel region, threads execute implicit tasks, and the team synchronizes at the end. A runtime commonly keeps operating-system threads in a reusable pool, so the logical join need not destroy them. Explicit tasks are work items created within that execution; they may be deferred and run by available team threads. Creating an explicit task does not mean creating a new operating-system thread.',omp)
add(21,11,'`sections` distributes a fixed set of `section` structured blocks among the current team. Each section executes once, assigned to some team thread, and a thread may execute multiple sections. There is an implicit end barrier unless `nowait` is specified. It suits a small known set of independent operations, not an unknown recursive number of tasks. Enclose it in `parallel` or use `parallel sections` to create a team.',omp)
add(21,[12,34],'Explicit `#pragma omp barrier` is available inside a valid team context, but is not always needed. Worksharing constructs commonly already supply an implicit end barrier; `nowait` removes one where permitted. Keep a barrier when subsequent work needs all previous results; omit redundant barriers only after checking dependencies and memory visibility. All required team participants must encounter a barrier consistently, so placing it in an incompatible conditional/worksharing region can deadlock or violate the standard.',omp)
add(21,13,'The **static/lexical extent** is the source-code structured block associated with the `parallel` directive. Its **dynamic extent** also includes routines called while executing that block, transitively. A function need not be textually inside the parallel block to execute concurrently when team threads call it. Therefore shared state and thread safety of called routines matter, not just the visible statements in the lexical block.',omp)
add(21,[14,22,27,37,42,55],schedule,omp)
add(21,[15,18,35],numthreads,omp)
add(21,[16,38],reduction,omp)
add(21,17,'`single` executes its structured block once, by one arbitrary thread of the current team. Other threads skip the block and normally wait at its implicit end barrier, unless `nowait` is specified. Use it for one-time actions such as generating tasks or initializing shared data within a parallel region. It does not necessarily choose the primary thread and does not itself create a new team.',omp)
add(21,19,'`critical` gives mutual exclusion: at most one thread at a time executes critical regions with the same name (unnamed critical regions share a common name). It protects compound accesses to shared state, such as updating a shared container. All competing accesses must use compatible synchronization. It is not a barrier: other threads need not arrive before a thread proceeds, and excessive use can serialize a hot path.',omp)
add(21,24,'`#pragma omp simd` permits concurrent execution of suitable loop iterations in SIMD lanes, typically using vector instructions within a core. It does not by itself create a team of operating-system threads. The loop must obey its dependence and data-sharing requirements; reductions and appropriate SIMD clauses express supported dependencies. Combine it with `parallel for` to distribute chunks across cores and vectorize within each chunk.',omp)
add(21,25,'Assume cancellation is enabled and all numbered directives target the same valid enclosing cancellable region. **Thread 1** reaches the earliest point 1, activates cancellation and exits the canceled region immediately; it never reaches its later point 2. **Thread 3** exits when it reaches its point 1; it also never reaches its later point 2. **Threads 2 and 4** reach their point 2 after cancellation is active, detect it and exit there, without reaching their later point 1. Each transfers control to the appropriate end of the canceled region, with the required completion synchronization. If cancellation is disabled, these directives have no cancellation effect and the threads continue normally.',cancelref)
add(21,26,'Threads can access the same memory concurrently, so conflicting unsynchronized accesses can race and violate the program\'s required value/order relationships. Synchronization provides mutual exclusion, atomic updates and/or producer-to-consumer visibility. Use reductions for aggregates, locks/critical regions for compound state, atomic operations for supported individual accesses, and barriers/task dependencies for phase ordering. A `shared` declaration alone supplies none of these protections.',omp)
add(21,28,'For a pure function and separate valid arrays, each map iteration owns one output:\n\n```c\n#pragma omp parallel for\nfor (int i=0; i<n; ++i) {\n    y[i] = f(x[i]);\n}\n```\n\nThe iteration variable is private by the loop rules. Shared input reads are safe; `f` must not introduce conflicting hidden shared-state accesses. Chunking and a sufficiently large `n` help amortize startup costs.',omp)
add(21,29,'`firstprivate(x)` creates a private instance initialized from the value of `x` at the specified construct encounter. Later updates to that private copy do not update the original or the other threads\' copies. This differs from `private`, whose ordinary C scalar copy is uninitialized. Copies are initialized according to the construct/task rules, not freshly from the original before every loop iteration. Capture a loop-generated task\'s index/pointer with `firstprivate` when it must retain that encounter\'s value.',omp)
add(21,30,'Cancellation is cooperative and must be enabled. `cancel` requests cancellation of a supported enclosing construct; other executing tasks/threads notice it only at applicable cancellation points, so work between those points can continue. It is not asynchronous preemption or rollback, and already performed side effects remain. Explicit `cancellation point` directives improve responsiveness where appropriate. Code must still avoid leaving locks/resources or synchronization in an invalid state.',cancelref)
add(21,31,r'''`for simd` distributes a loop over an already existing team and allows SIMD execution within each assigned chunk. `static,5` requests static round-robin chunks; the `simd` schedule modifier adjusts interior chunk sizes to $\lceil5/w\rceil w$, where $w$ is an implementation-defined SIMD width. The first and last chunks have the specified permitted exceptions, so this does not guarantee five iterations per chunk or a particular vector instruction width. The loop still must satisfy dependence and SIMD restrictions. No new team is created by this directive alone.''',omp)
add(21,32,'Both run a block once within a team. `single` chooses an arbitrary team thread and has an implicit end barrier unless `nowait` is used. Legacy `master` runs only on the primary thread (thread number 0) and has no implicit barrier. Thus replacing one with the other can change both thread identity and synchronization. Modern OpenMP provides `masked` for primary/selected-thread execution; the exam\'s `master` terminology describes the older construct.',omp)
add(21,33,'Assume enabled cancellation of the same valid enclosing construct. **Thread 2** and **Thread 4** first pass point 2 before any cancellation request, so they continue. **Thread 1** then reaches point 1, activates cancellation and exits the region. Threads 2 and 4 later reach their own point 1 and exit there. **Thread 3** reaches its point 2 after cancellation is active and exits there. Cancellation is not retroactive: passing an earlier cancellation point does not stop a thread from doing work before its next applicable point. With cancellation disabled, all threads continue normally.',cancelref)
add(21,36,'This generates an explicit task with an `in` dependence on the storage location `status[i]`. It waits for previously generated sibling tasks whose matching dependence is `out`/`inout` (or another applicable conflicting dependence type) on that location. It does not wait for the numeric value of `status[i]` to become nonzero. A matching preceding producer must be generated in the same relevant task-dependence scope; arbitrary unrelated tasks are not linked automatically. Keep the storage alive and capture `i` appropriately when the task body uses its encounter-time value.',omp)
add(21,39,'Use `parallel for simd`: threads execute chunks on different cores, and SIMD lanes process elements within each core. For example, `#pragma omp parallel for simd reduction(+:sum)` followed by a loop accumulating `a[i]*a[i]`. The reduction avoids races on `sum`; the independent element operations support vectorization. Useful scaling still requires sufficient work and memory bandwidth, and the compiler determines the actual vector instructions.',omp)
add(21,40,'Use `cancel` when remaining work in a cancellable region is no longer needed, for example after a search finds an acceptable answer. Enable cancellation (normally with `OMP_CANCELLATION=true`) and target the correct enclosing `parallel`, `for`, `sections` or `taskgroup` region. Other threads need applicable cancellation points to notice the request; explicit points can avoid long delays. Protect publication of the found result separately. Cancellation is cooperative and does not undo work already performed.',cancelref)
add(21,41,'Tasks suit dynamically generated, irregular or recursive work, such as recursively exploring a tree whose shape is unknown. Existing team threads schedule ready tasks. `sections` lists a fixed set of blocks in source and is useful for a few known operations. A fixed `sections` block is not a direct replacement for an arbitrary recursive task graph. It is possible to parallelize a few recursion levels with additional parallel sections, but this changes team creation/nesting and is often much less efficient than tasks in one team.',omp)
add(21,43,r'''There are several defects. The printed pragma/braces must first be formatted as valid OpenMP/C. `seed` is already private because it is declared inside the parallel block; putting it in `firstprivate` on the binding worksharing loop violates the scoping restriction. Giving every worker the same initial seed also repeats/correlates random streams. Finally, `if (x*x+y*y)` tests nonzero rather than membership in the unit circle; use `<=1`.

One corrected outline is:

```c
int hits = 0;
#pragma omp parallel reduction(+:hits)
{
    unsigned int seed = make_distinct_seed(omp_get_thread_num());
    #pragma omp for
    for (int i=0; i<100; ++i) {
        float x = rand_r(&seed) / (float)RAND_MAX;
        float y = rand_r(&seed) / (float)RAND_MAX;
        if (x*x + y*y <= 1.0f) ++hits;
    }
}
float pi = 4.0f * hits / 100.0f;
```

`make_distinct_seed` denotes an appropriate seeding scheme; a quality stream-splitting or counter-based generator is preferable for serious Monte Carlo work. The reduction completes before estimating pi. `rand_r` is the POSIX routine used by the question, not portable ISO C.''','[OpenMP firstprivate restrictions](https://openmp.org/spec-html/5.2/openmpsu38.html).')
add(21,44,'Process one BFS frontier at a time using `omp for` (often dynamic/guided scheduling) over the current frontier\'s vertices, or tasks if per-vertex work is very irregular. Claim each newly visited vertex atomically or with suitable locking, and collect the next frontier in safe local/shared buffers. Finish the level before processing the next to preserve BFS shortest-distance semantics. A naive recursive task traversal without frontier ordering is generally a parallel search/DFS, not a correct level-synchronous BFS.',omp)
add(21,45,'OpenMP does not promise that every unsynchronized shared-memory access participates in one globally sequential order. Threads/compiler transformations may retain temporary views, so the program must establish the required ordering and visibility using the memory-model rules and synchronization, such as barriers, locks, atomics or task dependencies. A data race is not repaired by declaring data `shared`, nor by adding an arbitrary `flush` while retaining conflicting accesses. Properly synchronized accesses have the required happens-before relationships.',omp)
add(21,46,'`private(offset)` creates an uninitialized private scalar, so iterations do not reliably see the original 5. Use `firstprivate(offset)` to copy 5, or omit the clause and keep `offset` shared/read-only. For example:\n\n```c\n#pragma omp parallel for firstprivate(offset)\nfor (int i=0; i<N; ++i) result[i] = i + offset;\n```\n\nEach iteration owns one result element, so no other synchronization is required.',omp)
add(21,47,'Use `sections` for a small fixed list of independent coarse operations, such as loading three independent datasets or invoking three independent processing stages once. Each block executes once and the implicit end barrier waits for the phase. It is concise and avoids describing a task graph unnecessarily. Tasks are more flexible when the number of jobs is dynamic/recursive or when dependencies and irregular load balancing matter.',omp)
add(21,48,r'''Distribute iterations over cores and vectorize within each core, while reducing the scalar:

```c
#pragma omp parallel for simd reduction(+:c) schedule(static)
for (int i=0; i<N; ++i) {
    float t = a[i] + b[i];
    c += t*t + a[i]*3.0f;
}
```

Each iteration only reads its own input elements, and the reduction prevents conflicting updates to `c`. The 256-bit units shown can operate on eight 32-bit floats per vector, subject to compiler code generation. Parallel reassociation can change the final floating-point rounding.''',omp)
add(21,49,'Fuse the map into a `parallel for reduction` when intermediate values are not otherwise needed: `sum += f(a[i])`. Each thread accumulates locally and the runtime combines partial results, reducing memory traffic and synchronization. If keeping two phases, ensure mapped outputs are ready before the reduction consumes them. An `atomic update` on a shared sum prevents lost updates but can serialize on a cache line; atomics do not automatically protect hidden state inside `f` or provide a complete phase barrier. Floating-point reduction/atomic order can also change rounding.',omp)
add(21,50,'A single `sections` construct contains a fixed set of source blocks and cannot by itself generate the unknown number of recursive subtree jobs. Reusing the same worksharing sections arbitrarily inside recursive tasks also violates nesting/encounter requirements. The intended solution is tasks in one team. It is possible to create nested `parallel sections` for selected forks, so “cannot” is too absolute; that alternative creates additional teams and can oversubscribe or add substantial overhead.',omp)
add(21,51,'Use explicit **OpenMP tasks** for the child subtrees, inside one outer `parallel` region with a `single` initial call. Tasks fit the unknown, irregular recursive work and can be scheduled on idle team threads. Technically `task` is a task-generating construct, rather than an ordinary worksharing loop/sections construct. A sequential cutoff helps small subtrees.',omp)
add(21,52,r'''Create one team, let one thread initiate traversal, and spawn child work as tasks:

```c
void dfs(node *root) {
    if (!root) return;
    printf("%d\n", root->value);
    #pragma omp task firstprivate(root)
    { dfs(root->left); }
    #pragma omp task firstprivate(root)
    { dfs(root->right); }
    #pragma omp taskwait
}

int main(void) {
    node root; /* initialize complete tree */
    #pragma omp parallel
    {
        #pragma omp single
        {
            #pragma omp taskgroup
            { dfs(&root); }
        }
    }
}
```

The tree must remain alive and immutable; child tasks retain their pointer value. Recursive `taskwait` and the outer taskgroup ensure completion. Output line order is arbitrary as permitted; if the I/O implementation cannot emit each record safely, guard `printf` with a named critical region. Fix the source's `Int` typo to `int` and avoid tasks below a useful size threshold.''',omp)
add(21,53,'For the three fixed independent operations, use `sections` inside a team: each listed section runs once, and its default end barrier completes that phase. For recursive irregular subproblems, use tasks generated by one initial call; ready tasks can be balanced across the existing team as the graph grows. Enclose the recursive generation in a **taskgroup** to wait for the whole generated group including descendants. `taskwait` waits for the relevant direct child tasks, so it covers an entire recursive tree only when the recursive structure itself supplies the required waits.',omp)
add(21,54,'If “section” means the body of a `parallel` region, a plain `for` is executed independently by every thread: the work is duplicated, and shared writes can race. `omp for` distributes the iterations once among the team. If the wording literally means one `omp section` block, that block is assigned to one thread, so its ordinary loop stays serial; an `omp for` cannot simply be closely nested there. In either interpretation, ordinary C loop syntax does not automatically share the work.',omp)

result='A joinable worker returns a `void *` from its start routine or calls `pthread_exit(value)`. Another thread obtains it through `pthread_join(thread, &result)`. The pointed-to result must outlive the worker: allocate it on the heap or use caller-owned storage, never return a pointer into the terminated worker\'s stack. A worker can also write caller-provided shared output, with a join or other synchronization establishing completion. Detached threads cannot be joined, so shared output needs another completion/lifetime protocol.'
join='A joinable thread retains the information/resources needed for `pthread_join`, which waits for its termination and can retrieve its return value. A detached thread releases termination resources automatically and cannot be joined. Detachment does not prevent ordinary synchronization: detached threads may still use mutexes, condition variables, barriers or shared completion flags with proper synchronization. Arrange data lifetime and completion explicitly; “detached” does not mean independent of the process lifetime.'
barrier='A POSIX barrier is initialized for a participant count. Each `pthread_barrier_wait` waits until that many threads have arrived, then the participating threads are released and the barrier can be reused for another round. One returns `PTHREAD_BARRIER_SERIAL_THREAD`, the others return 0; that special return is not an error. A join instead waits for one target thread to terminate, so it cannot provide a reusable mid-computation rendezvous among continuing workers. Use the correct participant count and ensure every participant reaches each round.'
condition=r'''A condition variable lets threads sleep until a predicate over shared state may have changed. Protect that predicate with a mutex and check it in a loop:

```c
pthread_mutex_lock(&m);
while (!ready) pthread_cond_wait(&cv, &m);
/* predicate is true; use/update protected state */
pthread_mutex_unlock(&m);
```

`pthread_cond_wait` atomically releases the mutex while blocking and reacquires it before return. A producer changes the predicate under the mutex and calls `pthread_cond_signal` or `pthread_cond_broadcast`. Recheck because wakeups can be spurious or another consumer can use the resource first. Notifications are not a queue of saved events; the predicate is the source of truth.'''
add(22,1,result,posix)
add(22,2,'Yes. Assign one or more worker threads to each fixed stage and connect consecutive stages with bounded queues. Protect each queue with a mutex; use condition variables to wait while empty/full, checking predicates in `while` loops. A producer signals available data and a consumer signals free capacity. Propagate an end-of-stream marker or explicit completion state so stages terminate safely. Different items overlap across stages, but each item retains its required stage order; the slowest stage limits throughput.',posix)
add(22,3,'Pthreads synchronization is explicit: the programmer selects where mutex locks/unlocks, condition waits/signals, barriers and joins are needed. Protect a critical section with the same mutex for all conflicting accesses, or use a read-write lock for suitable read-heavy state. Atomics can serve supported individual operations. Creating threads does not automatically synchronize shared state, and `volatile` is not a replacement for a synchronization protocol.',posix)
add(22,4,'Use `pthread_create` to start workers, `pthread_join` to await joinable completion, barriers for phase rendezvous, mutexes/read-write locks for protected state, and condition variables for predicate-based waiting such as queues. Thread attributes control properties such as detachment. A fixed pool with a synchronized task queue separates work scheduling from thread creation. Choose the construct according to the required relationship; mutual exclusion, completion and a rendezvous are different requirements.',posix)
add(22,5,'`pthread_create` passes exactly the supplied `void *arg` to a start routine with type `void *routine(void *)`. Package multiple arguments in a struct and pass its address, then cast inside the routine. The programmer explicitly supplies this argument; arbitrary local variables are not automatically captured. The struct must remain alive until consumed, and use a distinct per-thread struct or safe immutable storage rather than a shared changing loop variable.',posix)
add(22,[6,11,14],join,posix)
add(22,[7,10],condition,posix)
add(22,8,'Yes. Create a fixed worker pool once, give it a synchronized queue of task descriptors, and have workers repeatedly remove and execute tasks. This implements **workpile** and can also implement map or task-parallel patterns. Use mutexes/condition variables for queue access and sleeping, and choose a task granularity that amortizes queue overhead. For dynamically generated work, terminate only when no queued or active task can produce more jobs, not simply when the queue happens to be empty.',posix)
add(22,[9,12,15,18],barrier,posix)
add(22,[13,17],'Pthreads exposes low-level thread creation, argument passing, joining and synchronization. OpenMP adds compiler/runtime support for teams, loop worksharing, tasks, data scoping and reductions, so common parallel structures require less manual scheduling and bookkeeping. Both support shared-memory programming and still require correct handling of dependencies and shared state. Pthreads gives explicit control and does not require OpenMP directives; OpenMP needs a supporting compiler/runtime and its construct rules must be respected.',omp)
add(22,16,'A normal return from the initial thread\'s `main` terminates the process, including other threads. To terminate only that initial thread while allowing workers to continue, call **`pthread_exit(NULL)` instead of returning from `main`**. Alternatively, join all joinable workers before returning. There is no call that makes ordinary Pthreads continue after the process itself has exited; the wording “after main returns” is therefore imprecise.',posix)

metrics={k:{'work':sum(w.values()),'span':span(w,e),'times':{str(p):opttime(w,e,p) for p in (2,3,4)}} for k,(w,e) in graphs.items()}
assert metrics['2023jan']['times']['2']>10 and metrics['2023jan']['times']['3']==10
assert metrics['2024jul']['times']['3']==750 and metrics['2024jul']['times']['4']==600,metrics['2024jul']
assert metrics['2025dec']['times']['2']==500 and metrics['2025dec']['times']['3']==450
for name in ['2024jul','2026sep']:
    w,e=graphs[name]
    metrics[name]['optimized_span']={str(v):span({**w,v:(0 if name=='2024jul' else w[v]/2)},e) for v in w}
(root/'graph-checks.json').write_text(json.dumps(metrics,indent=2)+'\n')
qs=json.loads((root/'questions.json').read_text())
expected={q['id'] for q in qs if 20<=q['section']<=22}
assert set(answers)==expected,(sorted(expected-set(answers)),sorted(set(answers)-expected))
(root/'answers-systems.json').write_text(json.dumps(answers,ensure_ascii=False,indent=2)+'\n')
print(f'Prepared {len(answers)} model answers covering sections 20–22. Graph schedules checked by exhaustive event scheduling.')
