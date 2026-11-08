# Neomii Barron — rebuilt marketing portfolio

Open `index.html` directly in a browser. No server, install, or build required. Nothing has been published.

## Implementation

The previous screenshot-panel implementation has been replaced. The page now uses real headings and paragraphs, individual transparent botanical illustrations and lace ornaments, CSS layout, independently positioned portrait and media, and native video controls. `Neomii Barron.png` is retained only as a design reference and is **not used by the website**.

- `index.html`: editable content and links.
- `styles.css`: desktop collage composition, colors, typography, and independent mobile layouts.
- `script.js`: plays muted reels when in view, pauses them off screen, respects explicit pause and reduced motion.
- `assets/`: ten separately generated artwork files, original portrait, rendered resume preview, original downloaded videos, and a small SVG paper-grain texture.

The desktop composition follows the supplied screenshot and the original Canva preview inspected in Safari. Artwork has been independently recreated; it is not identical to Canva's original illustrations. Display typography uses local Didot, Bodoni, or Times fallbacks.

## Original content

The three original videos were downloaded from the user's Canva preview and saved locally as `oud-story.mp4`, `banana-matcha.mp4`, and `matcha-moments.mp4`. The supplied portrait is used without generative alterations. The resume image is rendered from the supplied PDF and opens that PDF.

The verified LinkedIn and email links work. The paper preview and full-paper link point to the original Google document discovered in the Canva preview. This is the only embedded remote resource and requires internet access and the document's existing permissions. No content has been uploaded or published.

The introduction intentionally preserves the student wording from the requested old-site reference.

## Verification

The rebuilt page was opened in Safari for visual inspection of the hero, about, work, and contact sections. Local media paths and video file formats were checked. The automation environment did not display video frames consistently, so playback rendering could not be conclusively verified, though playback controls responded. Browser mobile review uses `tmp/mobile-preview.html`.

Generated artwork descriptions and prompts are in `assets/ARTWORK.md`.
