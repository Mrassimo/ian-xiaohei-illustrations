# Image Generation Prompt Template

Generate each image separately. Replace variables according to the article content. Do not combine multiple images into a single image.

```text
Create a 16:9 landscape English article body illustration.

Style:
Pure white background. Black hand-drawn line art, thin slightly wobbly strokes, sparse and clean. No paper texture, no beige background, no shadow, no gradient.

Character:
Xiaohei, a small solid-black absurd creature with white dot eyes, tiny thin legs, blank serious expression, and slightly uneven hand-drawn body shape. Xiaohei must perform the core conceptual action, not decorate the scene. Make Xiaohei serious, deadpan, and slightly bizarre, not cute.

Theme:
{body illustration theme}

Structure type:
{structure type: workflow / system fragment / before-after contrast / role state / concept metaphor / method layering / map route / mini comic panels}

Core meaning:
{the core idea this image should express}

Scene:
{specific scene: where Xiaohei is, what Xiaohei is doing, main objects, and how information or material moves}

Elements:
{element 1} / {element 2} / {element 3} / {element 4}

Text labels:
Use only these short English handwritten labels if needed: {label 1} / {label 2} / {label 3} / {label 4} / {optional label 5}

Color rules:
Black for main line art and Xiaohei. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state.

Avoid:
No PPT infographic, no formal flowchart, no commercial illustration, no cute mascot, no children's cartoon, no complex architecture diagram, no UI screenshot, no top-left title such as Workflow or System Architecture, no dense text, no copied composition from previous examples.
```

## Image Edit Prompts

Remove a top-left title:

```text
Edit the provided image. Remove only the handwritten title "{text to remove}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

Increase strangeness:

```text
Regenerate this illustration with the same core meaning and simple layout, but make Xiaohei more central to the conceptual action. Xiaohei should be doing the strange work that explains the idea, not standing beside the diagram. Keep it clean, sparse, hand-drawn, and not cute.
```
