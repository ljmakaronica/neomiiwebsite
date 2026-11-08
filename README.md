# Neomii Barron — original portfolio recreation

Open `index.html` in a browser. This is a static, local website with no install or build step.

The page was rebuilt from the published reference at https://neomiii.my.canva.site/ on November 7, 2026. It now uses the original downloaded artwork, portrait, resume preview, contact icons, Lovelace display font, and Tenor Sans body font. The desktop composition uses the original 1366 × 768 design coordinates, colors, image crops, rotations, text sizes, and line breaks. Text remains editable HTML. Phone layouts reflow the content at widths of 650px and below.

## Files

- `index.html`: content, links, and original desktop placement values.
- `styles.css`: shared layout, typography, and phone adaptations.
- `script.js`: muted video autoplay while visible, explicit pause handling, reduced-motion support, and the original 11.21-second trim on the second matcha video.
- `assets/original/`: recovered original artwork, fonts, and icons. `SOURCES.md` records their source URLs.
- `assets/*.mp4`: the previously downloaded original videos, now assigned to the correct positions. The prior build had the two matcha filenames reversed.
- `NB Resume26.pdf`: the supplied resume, opened by the resume preview.

The font bytes are also embedded in `assets/original/fonts.css` so Safari can display the original fonts when opening the site directly from disk. The only remote resource required by the page is the existing Google Docs paper preview. Its direct link remains available below the embed.

## Verification

- Inspected the live original and recovered its published design data and assets through Safari.
- Visually compared the recreated desktop hero, introduction, work, video layout, and contact section. Corrected original font loading and artwork stacking during that review.
- Checked every local asset reference, internal anchor, unique heading ID, video file container, and font file length.
- Passed JavaScript syntax and behavior checks in JavaScriptCore for visible playback, explicit pause preservation, offscreen pause/resume, the clip trim, and reduced motion.
- Opened 390px phone previews and confirmed their content and controls through Safari's accessibility tree. Final phone screenshots could not be verified because browser captures began returning blank images.
- Video controls responded, but captured playback frames were black. A native decoding probe also failed in this environment, so actual playback is not conclusively verified. The local MP4s retain their original bytes, with the two matcha files correctly reassigned and the published trim restored.
- The sandbox prevented starting an HTTP preview server. Browser review used `file://` instead.

Nothing was deployed. Previous source files and generated approximations are preserved in `tmp/previous-rebuild/`; the downloaded reference archives and inspection files are under `tmp/`. Neither directory is required to run the site.
