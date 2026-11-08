# CLAUDE.md

This repo holds the RevealJS lecture decks, lecture notes, exercises, practice notebooks and planning files for **Học tăng cường** (Reinforcement Learning), semester 1 of 2026–2027 (`2627-1/`). Source decks come from the 2025–2026 semester in `RL-hk2-2025-2026/`.

The workspace file `../CLAUDE.md` carries the rules shared by every course: environment, static-site rules, shared CSS, writing style, `no-ai-slop`/`quill`, the sub-agent policy, visual verification and git basics. This file holds only what is specific to this course. `AGENTS.md` is the full, authoritative specification, written in Vietnamese. `prompt_lecture_note_deck.md` is the `/goal` workflow (lecture note first, then slide deck, then optional exercises) and extends `AGENTS.md` for materials and the index. Precedence: the user's instructions first, then `AGENTS.md` (and `prompt_lecture_note_deck.md` when that workflow is running), then this file, then `../CLAUDE.md`. Read the relevant section of `AGENTS.md` before any deck or materials work.

The presentation rules were aligned on 2026-10-12 with the sibling course `../math-4-AI` (its `AGENTS.md`, `CLAUDE.md`, finished deck 07, note 07 and exercises 07), with the author's MAT1101 slides in `../MAT1101/` and with the author's textbook *Học máy thống kê* in `../SML-textbook-main.zip`. Those three are style models only, never content sources.

## Repo map

| Path | Contents |
|---|---|
| `2627-1/lecture-NN-<ten-bai>.html` | One RevealJS deck per lecture (01–12 exist; the `.pdf` exports beside them are untracked) |
| `2627-1/lecture-style.css` | Shared stylesheet, identical in every course; synced from `../shared/css/`, never edited here |
| `2627-1/lecture-course.css` | This course's deck styles (holds `.strand-title`), loaded after `lecture-style.css` |
| `2627-1/lecture-template.html` | Structural and visual base for new decks (untracked; copy structure, never content) |
| `2627-1/revealjs/`, `plugin/`, `vendor/{katex,marked,dompurify}/` | Local runtime; decks must not load anything from the network |
| `2627-1/img/lec-NN/` | SVG assets for each lecture |
| `2627-1/planning/lec-NN/` | `outline.md`, `storyboard.md`, `review-log.md` (plus older analysis files in some lectures) |
| `2627-1/materials/lec-NN/` | `lecture-note.md`, `exercises.md`, `thuc-hanh-<chu-de>.ipynb`; templates in `materials/_templates/` |
| `2627-1/material-viewer.{html,css,js}`, `material-index.css` | Static Markdown viewer (14 block types, `DIRECTIVE_LABELS` in the JS); course overrides in the `*-course.css` beside them |
| `2627-1/index.html` | Course index: one card per finished lecture with four resource groups |
| `RL-hk2-2025-2026/` | Source decks (PPTX/PDF) and `resources/` (homework PDFs). Untracked. |
| `.codex/` | Historical Codex setup (the OpenRouter bridge now lives in `../tools/`). Not used by the current workflow. |

## Commands

```bash
../.venv/bin/python -m reloadserver 8765          # from repo root
# deck:  http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html
# note:  http://localhost:8765/2627-1/material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html
# exercises: same URL with doc=materials/lec-NN/exercises.md
git diff --check
```

There is no build step and no materials sync script in this repo.

## Course-specific rules

- **Choosing a lecture:** if the user hasn't named a source file, stop after listing `RL-hk2-2025-2026/` and ask. If the lecture number or title can't be inferred from the file name and content, ask before drafting.
- **CSS:** every deck, including the template, links `lecture-style.css` then `lecture-course.css`.
  - Reusable course rules go in `lecture-course.css`. Local CSS in a deck only for a one-slide need the course file can't meet, and it must not override the shared system.
  - No per-lecture CSS files.
  - Editing `lecture-course.css` means checking the template and every existing deck at wide and narrow sizes.
- **RevealJS config:** `lang="vi"`, 1280×720; outer `<section>` = one strand, inner `<section>` = one slide; footer at the end of `.slides` with course name, semester and lecture number.
  - Settings: `controlsLayout: "edges"`, `slideNumber: true`, `hash: true`, `hashOneBasedIndex: true`.
  - Plugins: `RevealMath.KaTeX`, `RevealNotes`, `RevealHighlight`, all local.
- **IDs:** every slide has a unique `data-slide-id`. It appears only in HTML and planning files, never on the slide face or in speaker notes.
- **Figures:** keep labels, arrow directions, legends, data and meaningful proportions exactly as in the source. Never embed rasters extracted from PDF or PPTX; without the user's explicit approval, stop that part and ask.
- **Code demos:** convert only what the source contains. Don't invent notebooks or programs unless the user asks for a practice notebook (see Materials).
- **Index:** never link `note-for-author.md` either. Only finished lectures appear.
  - Each card has four groups: **Bài giảng** (deck), **Ghi chú bài giảng** and **Bài tập** (viewer links, only once the Markdown has passed review), **Thực hành** ("Mở trên Colab" link to `https://colab.research.google.com/github/uet-iai-course/reinforcement-learning-planning/blob/main/2627-1/materials/lec-NN/<file>.ipynb` plus a download link; several notebooks get several buttons named by environment). Missing items show `Chưa có` as a status, never a fake link.

## Writing (in addition to `../CLAUDE.md`)

- **Terminology:** define or recall ("Nhắc lại:") every symbol, assumption and result before its first use on a slide or in a section; never rely on memory of an earlier lecture. The lecture's Vietnamese–English term table lives in `outline.md`.
- **Questions in lecture notes:** a genuine research question that the section answers immediately is allowed ("Ước lượng này tốt đến mức nào? Định lý sau cho biết…"); a question left unanswered is rhetorical.
- **Titles** repeat across slides when an example continues.
- **Off the slide face:** internal codes from other lectures ("T7", "VD1"). A note result number such as "(Định lý 04.3)" may follow the verbal statement at most once per slide. Sources go in the notes or on a references slide, not in a per-slide footer.
- **Speaker notes** (`<aside class="notes">`): usually 40–150 syllables, up to ~250 for proofs or solutions (longer is only a `nhẹ` finding); never only metadata.
- **Voice of lecture notes (user instruction 2026-10-11, from *Học máy thống kê*):** "chúng ta" for plans, needs, method choices and limits; "ta" inside calculations; the document is never the subject ("Mục này định nghĩa…" is banned); objective sentences inside definition/theorem/algorithm blocks; no "hãy" outside exercise statements. See `AGENTS.md` §"Ngôn ngữ và biên tập".
- **`no-ai-slop`:** record the scope and result of the check in `review-log.md`. Keep definitions, result labels, assessment questions and summaries that have a learning function.
- **`quill`:** use the relevant parts of `~/.claude/skills/quill/references/workflows.md` (Outline, Threads, Character / Concept, Revise) as a checklist against `outline.md` and `storyboard.md`.

## Deck structure and content

- **Strands:** 5–7 outer sections, including an opening and a conclusion.
  - Each strand has its own function, an input from the strand before, and an output the next one uses.
  - Going outside 5–7 needs a source or user reason, recorded in `storyboard.md` and `review-log.md`.
- **Opening strand, in order:** cover with a one-sentence thesis of the lecture; "Tiên quyết và quy ước" (a "Nhắc lại:" line for results reused from earlier lectures, a "Ký hiệu:" line for domains, time indices and expectation conventions); objectives; "Nội dung" (numbered strands matching the strand title slides and `#/N`, optional pre-reading line); "Vấn đề trung tâm" (the lecture's problem in one line plus each strand's conditional answer in one line, or a merged "Nhắc lại / Ví dụ / Nhu cầu" slide as in math-4-AI deck 04); a short frame slide when every method of the lecture shares one structure; "Ngữ cảnh" (≤ 4 lines) when a shared frame exists, may merge with the prerequisites slide.
- **Strand title slides (`AGENTS.md` §"Trang tiêu đề mạch"):** every strand except the opening starts with a `section.strand-title` slide, `id="mach-N"`, `data-slide-id` `<prefix>00` (or `<prefix>T` if taken).
  - Face: number in digits in `span.strand-number` ("2.", "3.", …, matching "Nội dung" and `#/N`), a noun-phrase name that differs from the first content slide's title, one declarative lead `p.strand-lead` (≤ 25 syllables, "Muốn <đích>, phải <việc>" or "Nhu cầu:"), optional `p.strand-keys` (≤ 5 noun phrases joined by " · "). Markup: `div.strand-title-body` > `h2` + `p.strand-lead` + `p.strand-keys`; styles live in `lecture-course.css`.
  - No definitions, formulas, figures, "Đầu vào/Đầu ra" or codes on the face. Notes of 40–100 syllables: inherited result, the strand's task, the output handed on. One storyboard entry each. Letter labels A, B, C stay in planning files and codes, never on the face.
  - Existing decks get strand title slides only in a logged revision pass requested by the user.
- **Conclusion strand:** its own strand title ("Tổng kết và chuyển tiếp"); a summary table `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán` with one row per main result; for multi-algorithm lectures also `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng` and `Phương pháp | Giả thiết không được bỏ | Kết luận` for convergence theorems; a slide answering the central problem conditionally with a "Nguồn:" line; one synthesis exercise with its solution on the face; "Câu hỏi tự kiểm tra" opening with "Câu hỏi: trả lời và nêu kết quả đã dùng." and 2–4 short questions; "Bài tập về nhà và tài liệu đọc" with a `Mạch | Bài tập` table mapping `exercises.md` to strands, a "Tài liệu đọc:" line and a "Ghi chú bài giảng · Bài tập" viewer link; a one-line link to the next lecture. No new concepts.
- **Common theoretical frame:** one per lecture, fixed in `outline.md` and `storyboard.md` before slides are finalised: central problem, shared objects and notation, assumptions, the chain definition → result → method, limits of applicability.
- **Timing:** three 50-minute periods = 150 min; the deck covers 120 min, the other 30 are exercises and code demos.
- **Follow the source:** keep the order, flow and main ideas of the chosen source deck. Merge, split, add, cut or reorder only locally to fix errors, reduce overload, restore prerequisites or complete the learning flow, and log every deviation.
- **Concept journey for every core concept:** problem → intuition → example → formal statement/algorithm → application → check.
  - A lead-in example may sit with the problem, before intuition; the storyboard says which problem it makes concrete.
  - Steps may share a slide, but may not be reordered or silently dropped. Never open a core concept with a definition or notation.
  - Algorithms: hand-compute one step or iteration with initial values first; then give inputs, outputs, assumptions, initialisation, parameters, update rule, order of operations and stopping rule. Hand example, formula and pseudocode must agree. A new method opens with the concrete limit of the previous one in one line, never with its name or pseudocode.
- **One central point per slide.** Split long derivations, pseudocode or tables; never shrink text to fit.
  - Body text ≥ 0.75em; below 0.65em only for short captions the student-perspective reviewer confirmed are readable.
- **Density (from MAT1101, `AGENTS.md` §"Văn phong và mật độ mặt trang chiếu"):** count syllables as whitespace tokens, excluding title, KaTeX, table numbers, figure labels and notes.
  - Aim for ≤ 40 per content slide, hard cap 60 (80 for objectives, contents, summary, comparison tables).
  - Hard caps: ≤ 6 content lines, ≤ 20 syllables per line, ≤ 3 display formulas (pseudocode over 8 lines gets its own slide), ≤ 1 text box of ≤ 2 sentences.
  - Over the cap means split or move prose to notes; never shrink fonts.
  - An exception needs a reason recorded in `storyboard.md` (with syllable counts before and after for fixed slides). Reviewers rate an over-cap slide without one `trung bình`, and one over 1.5× the cap `nghiêm trọng`.
- **Slide sentences:** terse math prose ("Đặt …", "Suy ra …", "Thế vào được …", "Với mỗi mẫu chuyển, cập nhật …"). No "ta thấy", "rõ ràng", "chúng ta", or "=" used for "là". At most one closing line, which must be a conditional result or a number, never a slogan or arrow chain.
- **Opening a concept:** the problem slide starts with "Muốn …" or "Nhu cầu:", then 1–3 concrete lead-in examples with numbers (in RL: a small hand-computable environment, a logged episode). The formal slide may keep the same title. "Ý nghĩa:" after a result never replaces the intuition step.
- **Result slides:** statement with assumptions, then optional "Ý nghĩa:" line, then optional one-line "Chứng minh.". Longer proofs go on their own "Chứng minh: <kết quả>" slide, one result per slide. Convergence results name the deciding assumptions on the face.
- **Example and exercise slides:**
  - "Ví dụ: <đối tượng>": data with numbers → "Tính …" → one step per line (for updates: target, error, new value) → result with "Diễn giải:" or a check. Continuations add the step name after a comma.
  - "Bài tập: <chủ đề>": "Câu hỏi:" typed (no screenshots), data tables in the same layout as the lead-in example. Each major cluster has one exercise whose "Lời giải:" is on the face (fragment or next slide, one reasoning step per line, ending in a short conclusion); self-study answers stay in notes. When `exercises.md` repeats a slide exercise, both solutions give the same result and the file links to the question and solution slides.
- **Running examples:** 1–2 hand-computable environments reused across concepts. Each reuse answers a new question or compares two tools on the same numbers (MC vs TD(0) on one episode, Sarsa vs Q-learning on one transition). Name them by object ("dãy bốn ô"), never "VD1". Prefer a scaled-down version of the practice-notebook environment when one exists.
- **Tables:** comparison tables for 2–4 methods on the same criteria; repeated computations use one fixed table layout with the same column names through the lecture.
- **Allowed labels:**
  - with a period: Định nghĩa. Định lý. Mệnh đề. Bổ đề. Hệ quả. Nhận xét. Thuật toán. Chứng minh. Trực quan. Ví dụ.
  - with a colon: Nhu cầu: Ý nghĩa: Diễn giải: Lưu ý: Nhắc lại: Cách khác: Dạng khác: Ký hiệu: Giả thiết: Kết luận: Đầu vào: Đầu ra: Câu hỏi: Gợi ý: Lời giải:
- **Not copied from MAT1101:** space before "?", unlabelled questions, "Bài tập" titles without a topic, question screenshots, "=" for "là", unexplained English or abbreviations, URLs on the face, year–name history lists, slides without notes.
- **Slide links** say which result is inherited, which assumption changes, and which limit creates the next need. Signposts like "tiếp theo chúng ta…" don't count.
- **RL content standards:** distinguish agent, environment, state, observation, action, reward, policy, model and value function.
  - State domains, types, sizes, time indices, expectation conventions and termination before use.
  - Keep prediction vs control, on- vs off-policy, model-based vs model-free, $V$ vs $Q$ apart where relevant.
  - For MDPs state the Markov assumption, spaces, dynamics, reward and discount. For Bellman equations and updates check indices, conditioning, signs, discount, target and what is held fixed.
  - For deep RL distinguish online and target networks, replay buffer, bootstrap target, exploration behaviour and evaluation policy.
  - No claims of convergence, optimality, unbiasedness or stability without the deciding assumptions.
  - Recompute every numeric example, probability, expectation, value update and important tensor shape.
- **Sources:** traceable by source page or slide number. External sources only to correct or verify a claim, cited specifically.
- **Storyboard:** a section map (type, function, input, output, contribution to the central problem, strand title slide code) plus one entry per slide with its reason to exist, the need it fills, links to the previous and next slide, the objective it supports, and a decision (`giữ | sửa | gộp | tách | thêm | bỏ`) with a reason. Strand title slides get an entry whose position reads "điểm vào mạch N". Each concept cluster records the slide IDs per step, what passes from example to formula, merged or `không áp dụng` steps, and timing toward 120 minutes.

## Materials: lecture notes, exercises, practice notebooks

- **Viewer contract:** `material-viewer.html?doc=materials/lec-NN/{lecture-note,exercises}.md&deck=lecture-NN-<ten-bai>.html`, both naming the same lecture. Pipeline: protect maths → Marked → DOMPurify → restore maths → KaTeX. No build step.
- **Blocks:** `::: definition|theorem|proposition|lemma|corollary|remark|algorithm|example|application|derivation|proof|exercise|hint|solution Optional title`, closed by `:::`, not nested. A title replaces the default label. `proof`, `hint`, `solution` are collapsed by default. The list lives only in `DIRECTIVE_LABELS` in `material-viewer.js`.
- **Lecture note = self-contained textbook chapter** (`AGENTS.md` §"Tiêu chuẩn giáo trình cho ghi chú bài giảng", binding). The deck is the summary of the note, not the reverse; on conflict fix the note first. Reading test: a prepared student reads it top to bottom without the deck and understands every sentence where it stands.
  - Problem before tool; every formula wrapped in prose; every symbol named at first appearance; every derivation step justified; verbal reading after each definition and theorem with the role of each assumption and counterexamples ("Hai giả thiết có vai trò riêng… Bỏ <giả thiết>: <phản ví dụ>"); concrete example before the general statement; section endings in prose (result obtained, what is missing, how the next section fixes it), no "Kết mục" labels; no "xem trang chiếu"; full sentences; common confusions named; figures read in text; 8 000–20 000 words (under 6 000 needs a logged reason).
  - Self-contained examples, situations and exercises: restate the data inside the block.
  - Numbered environments: one counter for Định nghĩa/Định lý/Mệnh đề/Bổ đề/Hệ quả/Nhận xét/Thuật toán (`Định lý 05.2`), separate counters for Ví dụ and Bài tập; label in the block title; four-part theorems (Giả thiết, Kết luận, Điều kiện áp dụng, Phạm vi); proofs in labelled steps, `aligned` one relation per line, ending with $\square$.
  - Linking paragraphs: concept–concept, result–result, algorithm–variant, reasoning chain in the section ending, **"Trong thực hành."** after each main result (what the objects are in an implementation, which assumptions hold or break with function approximation / off-policy data / non-Markov observations, what the result explains), applications back to theory, previous and next lecture.
  - Chapter structure: title; ≤ 1 short intro paragraph; objectives; prerequisites (bold group name + numbers + restated statement); notation table (~20 rows, one meaning per letter, reading conventions after it, correspondence to the textbook's notation once); no topic map in the note (user decision 2026-11-04, all notes from 2026-11-08: the four-group classification lives in `planning/lec-NN/outline.md`, section "Phân loại chủ đề"; the note keeps only the `note-topic-id` comments); numbered sections `## 1.` … matching strands (section 1 opens with the inherited result, the concrete problem, what the chapter builds, and a figure); application situations (≥ 2, one with a violated assumption, one tied to the practice notebook when it exists); chapter summary (5–8 sentence narrative with numbers, then results by section, formulas to remember, forgotten assumptions); exercises in three level subsections with hint and solution; references.
  - Consult the standard textbooks for how they motivate, order and interpret each concept and log the sections in `review-log.md`: Sutton & Barto (2018); Puterman (1994) and Bertsekas (2019) for MDPs and DP; Szepesvári (2010); Bertsekas & Tsitsiklis (1996) for function approximation; Goodfellow et al. (2016) for networks; the RL chapter of *Học máy thống kê* for voice and Vietnamese terms. Never translate or copy passages. Use `materials/_templates/lecture-note.md`.
  - Review checklist before publishing: `AGENTS.md` §"Kiểm định ghi chú bài giảng".
- **Exercises (`exercises.md`):** the official assignment set in three levels (nhận biết; tính toán hoặc chứng minh; vận dụng vào bài toán Học tăng cường). Opening paragraph on the relation to the note; table `Mạch | Mở phần | Bài tập` linking to strand title slides (`#/N/1`); "Hướng dẫn và ký hiệu" restating shared data; per exercise a `### Bài tập NN.k. Title` header, a "Mức độ:" line, "Trùng trang chiếu" links to the question and solution slides when applicable, `exercise`/`hint`/`solution` blocks, solutions with "**Câu (a).**" stages and a "**Kiểm tra lại.**" naming common mistakes. One Bài tập counter shared with the note; never repeat the note's "Bài tập củng cố". Use `materials/_templates/exercises.md`. Produced in Stage III of `prompt_lecture_note_deck.md` when the user asks.
- **Practice notebooks (user requirements from 2026-10-03):** `thuc-hanh-<chu-de>.ipynb` only when the user asks; continues the lecture: build environment → evaluation over many episodes (shared seeds; mean, sd, SE; paired comparison) → the lecture's algorithms, each with a hand-computed step checked by `assert` before the full run → evaluation in the real environment → open-ended extensions. Standalone (`%pip install -q …` in the first cell, runs on local Jupyter and Colab, tested in an empty venv — a throwaway one, not the workspace `.venv`). Markdown cell before each main code cell using the note's notation with a symbol → variable map and array shapes; comments in code. Visualise reference and learned policies with a light `<canvas>` player drawn from state arrays, plus static plots and a frame strip. No `assert` against package-version-dependent numbers. Publish every preliminary experiment used to pick a configuration. Review: author → three read-only reviews (RL/maths; student view + standalone test; pedagogy + `no-ai-slop` Detect) → fix → recheck → final check; log in `review-log.md`.
- **Sync:** when a deck changes notation, assumptions, examples or concept order, review the note, exercises and notebook too.

## Sub-agents (course settings)

The policy in `../CLAUDE.md` applies (sub-agents: standing user instruction 2026-10-07, given for `../math-4-AI` and adopted here; master: 2026-10-22; matches `AGENTS.md` §"Điều phối mô hình trong dự án"):

- **Effort:** every sub-agent runs at `high`.
- The lecture-note writer and the deck writer never run together.
- **Checks the master runs on written files:** visual check, viewer check, `git diff --check`.
- **Review scope:** for a local change give the reviewer the changed part, two slides either side and the section map when flow is involved. Math reviews keep the cluster's notation, assumptions, examples and sources. If a review fails for size, split it and retry with the same model. The storyline reviewer also states `vai trò trong mạch`, `kết nối vào` and `kết nối ra`.

| Stage | Role(s) | Writes files? |
|---|---|---|
| Plan | Planning agent: goals, scope, theoretical frame, concept list and journeys, task split, risks | No |
| Source analysis | Source-to-target slide map with decisions, figure inventory, gaps and inconsistencies | No |
| Draft | Authoring agent: outline, storyboard, deck, SVGs, notes; `no-ai-slop` Edit + `eval.md`; `quill` continuity check | Yes |
| Storyboard gate | Every slide's reason to exist, six-step journeys, section functions, strand title slides, 120-min timing | No |
| Review | Five independent roles on one frozen draft: student (also measures density), RL expert, math/algorithm accuracy, academic/pedagogical critique (also `no-ai-slop` Detect), linking and storyline | No |
| Revise | One editor merges the reports, fixes HTML, SVG, outline, storyboard and notes in sequence, records rejected suggestions | Yes |
| Recheck | Math on changed content. Storyline on changed slides, ±2 neighbours and section boundaries; the whole deck if the opening, conclusion or thesis changed | No |
| Final check | Opus 5.5 verifier: technical, density count, strand titles, visual, planning sync, materials consistency, index, git; the master reviews the evidence and signs off | — |

## Visual verification (course notes)

For a new deck visit every horizontal and vertical slide; check every strand title slide at both sizes and that its number matches `#/N`. For lecture notes and exercises, open the viewer URL and check that the Markdown renders, every `:::` block is recognised, KaTeX has no errors, and nothing loads from the network.

## Lecture notes workflow (`prompt_lecture_note_deck.md`)

- Stage I produces `2627-1/materials/lec-NN/lecture-note.md` and must pass review, commit and push before Stage II edits the deck. Stage III (optional, on request) produces `exercises.md` after the deck is committed.
- Each topic has a unique `note-topic-id`; decks map back with `data-slide-id`. Notes follow the same six-step concept journey at textbook depth.
- The topic classification has four groups: `cốt lõi`, `cầu nối`, `bổ sung`, `đọc thêm`. It lives in `outline.md` ("Phân loại chủ đề"), never as a section of the lecture note. Add bridge or supplementary items only for a named gap with a specific source.

## Git (course settings)

- **Standing permission:** within the `prompt_lecture_note_deck.md` workflow, the user allows commit **and push** after each stage gate passes, without asking again. Outside that workflow, ask before committing.
- **Commit scope:** for a deck: the deck HTML, `img/lec-NN/`, `planning/lec-NN/`, the related `index.html` entry, and shared files that truly had to change. Never mix two lectures in one commit.
- **Commit messages:** `feat(materials-NN)` / `fix(materials-NN)` for lecture notes, exercises and notebooks; `feat(lecture-NN)` / `fix(lecture-NN)` for decks; `docs:` for `AGENTS.md`, `CLAUDE.md`, workflow files, templates and viewer infrastructure.

## Done means

- The deck keeps the source's main ideas and flow; every deviation is logged.
- Every blocking and serious finding from the five reviews is resolved and logged.
- `outline.md`, `storyboard.md` and `review-log.md` in `planning/lec-NN/` match the current deck, including `data-slide-id`s and strand title slides.
- No slide exceeds the density caps without a storyboard exception; all figures are SVG or have an approved raster exception.
- The browser check passed at both sizes; no broken resources.
- `no-ai-slop` scope and self-check result are recorded in `review-log.md`.
- Materials of the lecture (note, exercises, notebook, if any) are consistent with the deck and pass their own checks.
- `index.html` is updated for completed lectures only, with four resource groups and no links to planning files.

The handoff lists: deck file and local URL, source file, redrawn figures and raster exceptions, checks run, intended deviations, remaining limits, and (when committed) commit hash and push verification.
