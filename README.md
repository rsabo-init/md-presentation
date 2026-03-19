# SCADA Water Management Presentation

A professional HTML presentation system with SCADA-themed design for water management topics.

## Quick Start

### 🚀 Recommended: Start with Python Server (Auto-reload enabled)

**Windows:**
1. Double-click `start-server.bat` or `start-server.ps1`
2. Browser opens automatically at http://localhost:8000/presentation.html
3. Edit `presentation.md` and save - changes appear within 2 seconds!
4. Press Ctrl+C in the terminal to stop

**Manual start:**
```powershell
python -m http.server 8000
```
Then open http://localhost:8000/presentation.html

### Option 2: Direct Open (No auto-reload)
1. Just double-click `presentation.html` to open it in your browser
2. Use arrow keys ← → to navigate slides
3. Press F11 for fullscreen mode
4. After editing MD, refresh browser manually

## Editing the Presentation

### Edit Content
1. Open `presentation.md` in any text editor
2. Edit the text, add/remove slides
3. Slides are separated by `---`
4. Use markdown formatting:
   - `# Heading 1`
   - `## Heading 2`
   - `**bold text**`
   - `- bullet point`
   - `| Col | Col |` / `|---|---|` / `| Cell | Cell |` — tables

### Hidden Notes Syntax (visible in MD, invisible in HTML)

All `<!-- ... -->` HTML comment blocks are stripped before rendering. Use them for speaker notes and slide markers.

#### Slide marker (page counter)
Place at the very top of each slide, before the heading:
```
<!-- slide: 3/26 — Slide Title -->
```

#### Talk track (speaker notes)
Place at the bottom of each slide, after the visible content:
```
<!-- talk:
- First talking point
- Second talking point
- What to watch for in the audience
-->
```

Both are fully visible in your markdown editor and completely hidden in the HTML presentation.

### After Editing (if not using Live Server)
Run the sync script to update the HTML:
```powershell
.\sync-presentation.ps1
```

## Keyboard Shortcuts
- **→ / Space** - Next slide
- **← / Backspace** - Previous slide  
- **Home** - First slide
- **End** - Last slide
- **F11** - Fullscreen mode

## Files
- `presentation.md` - Your presentation content (edit this!)
- `presentation.html` - The presentation viewer (auto-generated)
- `sync-presentation.ps1` - Sync script to update HTML from MD
- `images/` - Put your images here

## Adding Images
1. Place image files in the `images/` folder
2. Reference in markdown: `![Description](images/your-image.png)`
3. Run sync script or refresh if using Live Server

## Troubleshooting

**Blank page when opening HTML?**
- The presentation is now embedded, so it should work directly
- If you see a blank page, try refreshing (Ctrl+R)
- Make sure the HTML file is up to date (run sync script)

**Changes not appearing?**
- If using Live Server: just save the MD file
- If opening directly: run `sync-presentation.ps1` after editing

**Need to customize colors/theme?**
- Edit the `<style>` section in `presentation.html`
- Main colors: `#00d9ff` (cyan), `#4fc3f7` (light blue)

## Design Theme
Industrial SCADA theme with:
- Dark blue gradient background
- Cyan/teal accent colors
- Clean, professional typography
- Water-themed decorative elements
- Smooth slide transitions

---
Created with ❤️ for water management professionals
