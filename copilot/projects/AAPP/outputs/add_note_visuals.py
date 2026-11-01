from pathlib import Path
import re
import shutil
import struct
import sys

COURSE = Path('/home/matteo/Documents/Obsidian/University/Advanced Algorithms and Parallel Programming')
TEMP = Path('/tmp/aapp-all-visuals')

# note, source PDF, page, filename stem, insertion anchor, caption
VISUALS = [
    ('Course Introduction', 'lecture1-Intro-Course2026-2027.pdf', 4, 'aapp-lecture1-algorithm-roadmap',
     'Source: [[lecture1-Intro-Course2026-2027.pdf#page=4|Algorithm syllabus, pp. 4–5]].',
     'A visual roadmap of the first algorithm topics announced in the course introduction.'),
    ('Course Introduction', 'lecture1-Intro-Course2026-2027.pdf', 7, 'aapp-lecture1-prerequisites',
     'The stated prerequisites are operations research, basic data structures, and computational complexity; C/C++ knowledge is helpful.',
     'The background knowledge the course expects you to bring to the algorithm and programming material.'),
    ('Divide and Conquer', 'lecture3-DandC.pdf', 12, 'aapp-lecture3-binary-search',
     'For $[3,5,7,8,9,12,15]$ and target $9$, compare with $8$, then search $[9,12,15]$; compare with $12$, then find $9$.',
     'After discarding the left half, binary search compares the target 9 with the middle of the remaining region, 12.'),
    ('Divide and Conquer', 'lecture3-DandC.pdf', 23, 'aapp-lecture3-matrix-blocks',
     'Since $n^{\\log_2 8}=n^3$, Case 1 gives $\\Theta(n^3)$. The algorithm reorganizes the computation without improving its asymptotic arithmetic count.',
     'Each output block is a sum of two block products: ordinary recursion still needs eight recursive multiplications.'),
    ('Divide and Conquer', 'lecture3-DandC.pdf', 43, 'aapp-lecture3-tree-layout',
     'Thus its bounding area is $H(n)W(n)=\\Theta(n\\log n)$.',
     'The straightforward tree layout grows linearly in width and logarithmically in height.'),
    ('Divide and Conquer', 'lecture3-DandC.pdf', 46, 'aapp-lecture3-h-tree',
     '![[lecture3-DandC.pdf#page=46]]',
     'The H-tree packs four smaller subtrees into a square-like region, reducing the area to linear growth.'),
    ('PRAM', 'lecture4-PRAM.pdf', 4, 'aapp-lecture4-ram-pram',
     'The model idealizes shared-memory access as unit-time. It does not charge realistic cache, network, bandwidth, or synchronization overhead.',
     'RAM has one processor; PRAM has several processors communicating through shared memory in synchronous rounds.'),
    ('PRAM', 'lecture4-PRAM.pdf', 20, 'aapp-lecture4-map-rows',
     'Different output entries are independent. They read common vector entries but write distinct $y_i$, making the natural row-based schedule CREW.',
     'Partition the matrix by rows: processors share the input vector but own independent output entries.'),
    ('PRAM', 'lecture4-PRAM.pdf', 21, 'aapp-lecture4-reduction-tree',
     'This is work-efficient but not cost-optimal at that processor allocation: more processors become idle at each level.',
     'Eight values become four partial sums, then two, then one: tree depth is logarithmic while the number of additions is linear.'),
    ('PRAM', 'lecture4-PRAM.pdf', 23, 'aapp-lecture4-prefix-sum',
     'Example: $[3,1,4,2]\\mapsto[3,4,8,10]$.',
     'The slide illustrates computing every prefix through staged combinations; the CR labels mark concurrent reads. The pseudocode below gives a separate explicit construction.'),
    ('PRAM', 'lecture4-PRAM.pdf', 28, 'aapp-lecture4-scaling',
     'The growing problem can expose communication and global synchronization costs even when local work remains constant.',
     'Strong scaling fixes total problem size; weak scaling fixes work per processor. Compare results only when the experiment is clear.'),
    ('ISPC', 'lecture4b-ISPC.pdf', 5, 'aapp-lecture4b-multicore-architecture',
     'This distinction matters: creating eight logical instances does not mean creating eight operating-system threads. Conversely, one gang\'s vectorized execution does not by itself spread work across all CPU cores.',
     'A simplified multicore architecture: cores have local caches and share lower-level memory resources.'),
    ('ISPC', 'lecture4b-ISPC.pdf', 10, 'aapp-lecture4b-compilation',
     'This lets the application delegate computational kernels while retaining its surrounding C/C++ structure. The compilation diagram is in [[lecture4b-ISPC.pdf#page=10|page 10]].',
     'Compile the ISPC kernel and C/C++ application separately, then link their object files into one application.'),
    ('ISPC', 'lecture4b-ISPC.pdf', 17, 'aapp-lecture4b-gang-execution',
     'Do not hard-code a gang size into an algorithm unless the target-specific assumption is intentional. Logical gang size and hardware vector width are related but should not be casually equated for every target.',
     'A gang handles successive groups of array elements; the colors distinguish logical program instances, rather than separate OS threads.'),
    ('ISPC', 'lecture4b-ISPC.pdf', 41, 'aapp-lecture4b-task-utilization',
     'Page 41 illustrates broader CPU utilization with tasks. Utilization alone is not a speedup measurement: use the metrics in [[PRAM#Performance quantities]] to evaluate whether the extra resources reduce time efficiently.',
     'The slide screenshot contrasts one busy worker with broad CPU utilization after enabling multicore tasks; it does not by itself measure speedup.'),
    ('Randomized Algorithms', 'lecture5-Randomization.pdf', 2, 'aapp-lecture5-randomness-sources',
     'A strong expected-time guarantee holds for **every fixed input**, averaging only over $R$. For example, the algorithm can randomize a candidate order rather than assume it was random initially.',
     'Separate a random input model from random choices made by the algorithm on a fixed input.'),
    ('Randomized Algorithms', 'lecture5-Randomization.pdf', 8, 'aapp-lecture5-hiring-worst-case',
     'Every applicant is still interviewed in either case.',
     'Increasing applicant quality forces a replacement at every step: this execution makes n hires.'),
    ('Randomized Algorithms', 'lecture5-Randomization.pdf', 12, 'aapp-lecture5-hiring-indicators',
     'Assume all $n!$ permutations of the distinct applicants are equally likely. Let $X_i$ indicate that the applicant at **position $i$** is hired. The subscript is an arrival position, not a fixed applicant identity.',
     'Represent each hiring event by 1 and each non-hiring event by 0; their sum is the total number of hires.'),
    ('Randomized Algorithms', 'lecture5-Randomization.pdf', 21, 'aapp-lecture5-las-vegas-monte-carlo',
     'Source: [[lecture5-Randomization.pdf#page=21|Families and efficiency, pp. 21–24]].',
     'Las Vegas preserves correctness with a random runtime; Monte Carlo bounds runtime while allowing controlled error or failure.'),
    ('Randomized Algorithms', 'lecture5-Randomization.pdf', 25, 'aapp-lecture5-sampling-array',
     'The input contains $n$ symbols, exactly half `a` and half `b`, and the goal is to find any position containing `a`. Assume each trial independently samples a uniform index **with replacement**. Each trial succeeds with probability $1/2$.',
     'Five of these ten entries are a: a uniform random lookup succeeds with probability one half.'),
]

originals = {}
updates = {}
assets = []
blocks = {}
replacement = None
for name, pdf, page, stem, anchor, caption in VISUALS:
    if name not in originals:
        originals[name] = (COURSE / 'Notes' / (name + '.md')).read_text()
        updates[name] = originals[name]
        blocks[name] = []
    assert originals[name].count(anchor) == 1, f'Missing or duplicated anchor: {name}, {stem}'
    filename = stem + '.png'
    image = TEMP / f'{pdf}-page{page}.png'
    destination = COURSE / 'Attachments' / name / filename
    assert not destination.exists(), f'Image already exists: {destination}'
    assert image.read_bytes().startswith(b'\x89PNG\r\n\x1a\n')
    block = f'![[{filename}|720]]\n\n*{caption}* [[{pdf}#page={page}|Source slide {page}]].'
    if anchor.startswith('![['):
        updates[name] = updates[name].replace(anchor, block, 1)
        replacement = (name, block, anchor)
    else:
        addition = '\n\n' + block
        updates[name] = updates[name].replace(anchor, anchor + addition, 1)
        blocks[name].append(addition)
    assets.append((image, destination))

web_filename = 'aapp-lecture4b-mandelbrot-complex-plane.png'
web_source = 'https://commons.wikimedia.org/wiki/File:Mandelbrot_Set_in_Complex_Plane.png'
web_anchor = 'A renderer assigns each pixel a complex parameter and records an escape iteration, or a maximum iteration count. Different pixels are independent, making the exercise suitable for SIMD and task decomposition.'
assert originals['ISPC'].count(web_anchor) == 1
web_block = (f'\n\n![[{web_filename}|600]]\n\n'
             '*A rendered view of the Mandelbrot set in the complex plane: black depicts the set, with colored bands outside it.* '
             f'[Image: Lars H. Rohwedder / Wikimedia Commons, public domain]({web_source}).')
updates['ISPC'] = updates['ISPC'].replace(web_anchor, web_anchor + web_block, 1)
blocks['ISPC'].append(web_block)
web_destination = COURSE / 'Attachments/ISPC' / web_filename
assert not web_destination.exists()
assets.append((TEMP / 'mandelbrot-complex-plane.png', web_destination))

# Confirm that the changes consist solely of the chosen embeds and captions.
for name, updated in updates.items():
    recovered = updated
    for block in blocks[name]:
        recovered = recovered.replace(block, '', 1)
    if replacement and replacement[0] == name:
        recovered = recovered.replace(replacement[1], replacement[2], 1)
    assert recovered == originals[name], f'Unexpected text changes: {name}'
    assert updated.count('[[') == updated.count(']]'), f'Unbalanced links: {name}'
    print(name, 'image embeds:', len(re.findall(r'!\[\[[^\]]+\.png\|\d+\]\]', updated)))

for source, destination in assets:
    data = source.read_bytes()
    assert data.startswith(b'\x89PNG\r\n\x1a\n')
    width, height = struct.unpack('>II', data[16:24])
    assert width >= 700 and height >= 500, f'Unexpected dimensions: {source}'
print('Prepared 21 local images across five notes, including replacement of one PDF embed.')

if '--install' in sys.argv:
    for name, original in originals.items():
        assert (COURSE / 'Notes' / (name + '.md')).read_text() == original, f'Note changed: {name}'
    for source, destination in assets:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    for name, updated in updates.items():
        (COURSE / 'Notes' / (name + '.md')).write_text(updated)
    asset_names = {destination.name: destination for _, destination in assets}
    for name, updated in updates.items():
        saved = (COURSE / 'Notes' / (name + '.md')).read_text()
        assert saved == updated
        for filename in re.findall(r'!\[\[([^\]|]+\.png)\|\d+\]\]', saved):
            assert asset_names[filename].is_file(), f'Missing embed: {filename}'
    print('Installed and verified all images and note edits. Existing prose and properties preserved.')
