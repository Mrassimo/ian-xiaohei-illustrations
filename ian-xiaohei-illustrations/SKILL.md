---
name: ian-xiaohei-illustrations
description: Generate Ian-style English article body illustrations. Use when a user asks for strange, Xiaohei, hand-drawn, article illustration, body illustration, illustration advice, shot list, remove title, or image edit tasks for English articles, posts, blogs, Notion documents, workflow documents, methods, processes, structures, states, metaphors, or ideas. Defaults to Xiaohei IP, pure white hand-drawn visuals, sparse red/orange/blue annotations, and a clean but imaginative visual style.
---

# Ian Xiaohei Strange Body Illustrations

## Core Positioning

Design and generate 16:9 landscape body illustrations for English articles. The goal is not commercial illustration, PPT infographics, or cute cartoons. The goal is to turn an article's key judgment, workflow, structure, state, or metaphor into a clean, strange, creative, readable hand-drawn explanation sketch that does not feel like a manual.

The default visual IP is `Xiaohei`: a small solid-black character with white dot eyes, thin legs, and a blank expression, seriously doing something absurd but coherent. Xiaohei must participate in the image's core action and must not stand beside the scene as decoration.

## Read These References First

Read only what the task needs; do not load everything into context at once:

- `references/style-dna.md`: style DNA, color, text, and prohibitions.
- `references/xiaohei-ip.md`: Xiaohei's appearance, personality, action library, and prohibitions.
- `references/composition-patterns.md`: structure types, original-metaphor method, and anti-copying rules.
- `references/prompt-template.md`: single-image generation prompt template.
- `references/qa-checklist.md`: post-generation checks and iteration rules.
- `assets/examples/`: low-frequency visual calibration only. Do not copy these examples' compositions, objects, or labels.

## Workflow

### 1. Digest The Article

Read the user-provided article, link, Notion page, Markdown file, screenshot, or theme. Extract:

- The core argument.
- Paragraphs that create a cognitive turn.
- Sections that are worth explaining visually.
- Sections that should stay as text and do not need images.

Do not distribute illustrations evenly. Prefer cognitive anchors such as a core judgment, two breakpoints, input-output loop, branching, before/after contrast, one-source-many-uses, handoff path, common trap, or role-state shift.

### 2. Create The Illustration Strategy First

If the user is only asking to analyze where illustrations should go, output a shot list first. For each image, specify:

- Placement in the article.
- Image theme.
- Core idea.
- Structure type.
- What Xiaohei is doing.
- Suggested elements.
- Suggested short English labels.

Default to 4-8 images. Use 1-3 for a short article. Even for long articles, avoid going above 9 unless there is a strong reason. Use only what helps; do not turn the article into a picture book.

### 3. Generate Single Images

If the user explicitly asks to generate, output, make, or create images, do not wait for confirmation; call the built-in `image_gen` tool for each image separately. Do not combine multiple images into one.

Each image should express one core structure. The prompt must include:

- 16:9 landscape English article body illustration.
- Pure white background.
- Black hand-drawn line art.
- A few short red/orange/blue handwritten English notes.
- Generous whitespace.
- Xiaohei as the subject carrying the core action.
- No PPT style, commercial illustration, childish cuteness, complex architecture diagram, or top-left type title.

Do not copy old examples. Examples only calibrate visual density and Xiaohei's involvement. Do not directly reuse existing compositions such as conveyor breakpoints, Xiaohei pulling wires, material fish, stamped copy toolbox, or common-traps path unless the user explicitly asks to reproduce a specific image. Invent a new strange-but-coherent metaphor from the current article each time.

### 4. Check And Iterate

After generation, check `references/qa-checklist.md`. If any of the following appear, regenerate or locally edit first:

- Xiaohei is only decorative.
- The image is too crowded.
- It looks too much like a flowchart or PPT slide.
- There is too much text or text is badly misspelled.
- The top-left contains titles such as `Common traps`, `Workflow`, or `System architecture`.
- The style is too cute, childish, or stiff.
- The background is not clean white.

### 5. Save Delivery Files

If the user is working in a workspace, copy final images to:

```text
assets/<article-slug>-illustrations/
```

Name them in order:

```text
01-topic-name.png
02-topic-name.png
```

Keep original generated files. Do not overwrite existing assets unless the user explicitly asks.

## Output Style

Pre-generation strategy output should be short and precise. After generation, delivery should include:

- How many images were generated.
- The purpose of each image.
- Save paths.
- Which images are strongest and which are optional.

Do not write a long explanation of style theory; let the images carry the point.
