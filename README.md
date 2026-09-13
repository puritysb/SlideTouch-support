# SlideTouch Support

**SlideTouch** is a macOS-native app for pixel-level editing of image-based PDF slides.

**SlideTouch**는 이미지 기반 PDF 슬라이드를 픽셀 단위로 편집할 수 있는 macOS 네이티브 앱입니다.

---

## Links

| | English | 한국어 | 日本語 |
|---|---|---|---|
| Home | [Landing Page](https://puritysb.github.io/SlideTouch-support/) | [랜딩 페이지](https://puritysb.github.io/SlideTouch-support/ko/) | [ランディング](https://puritysb.github.io/SlideTouch-support/ja/) |
| Features | [Features](https://puritysb.github.io/SlideTouch-support/features.html) | [기능](https://puritysb.github.io/SlideTouch-support/ko/features.html) | [機能](https://puritysb.github.io/SlideTouch-support/ja/features.html) |
| Support | [Support & FAQ](https://puritysb.github.io/SlideTouch-support/support.html) | [지원 & FAQ](https://puritysb.github.io/SlideTouch-support/ko/support.html) | [サポート](https://puritysb.github.io/SlideTouch-support/ja/support.html) |
| Privacy | [Privacy Policy](https://puritysb.github.io/SlideTouch-support/privacy.html) | [개인정보처리방침](https://puritysb.github.io/SlideTouch-support/ko/privacy.html) | [プライバシー](https://puritysb.github.io/SlideTouch-support/ja/privacy.html) |
| Releases | [Release Notes](https://puritysb.github.io/SlideTouch-support/releases.html) | [릴리즈 노트](https://puritysb.github.io/SlideTouch-support/ko/releases.html) | [リリース](https://puritysb.github.io/SlideTouch-support/ja/releases.html) |

---

## About SlideTouch

Slides from NotebookLM, Canva, and similar tools are beautiful but entirely flattened images. Fixing a single typo requires regenerating the whole deck.

SlideTouch solves this with on-device OCR + AI inpainting + text rendering:

- **On-Device OCR**: Apple Vision detects text in image slides
- **AI Inpainting**: LaMa model restores backgrounds behind removed text
- **Non-Destructive Editing**: Layer-based edits with undo/redo
- **Object Selection**: SAM2 segmentation for precise object removal
- **Shape Drawing**: Rectangles, ellipses, arrows, freeform curves
- **Rich Text**: Fonts, sizes, colors, alignment per text run
- **Flexible Export**: PDF, PNG, JPEG, video, GIF

### Requirements

- macOS 15.1+ (Sequoia)
- Apple Silicon (M1+)
- 8GB+ RAM recommended

### Privacy

Document OCR and image processing run on-device. Optional purchases use Apple services.

---

## Bug Reports & Feature Requests

Please use [GitHub Issues](https://github.com/puritysb/SlideTouch-support/issues) to report bugs or request features.

---

## License

Support materials in this repository are licensed under the [MIT License](LICENSE). SlideTouch app itself is proprietary software.

## Landing page updates

Run `python3 scripts/refresh_home.py` to rebuild EN/KO/JA homepages. These retain the existing page head, navigation and footer. The script owns landing page copy; `docs/site.css` and `docs/landing.js` own layout and interactions. See `docs/media/1.2/README.md` for media provenance. The 1.2 demo is labeled as submitted for review until release is confirmed.

All 15 EN/KO/JA pages use the same `site-theme` shell and `docs/site.css`. Subpage navigation marks the current page with `aria-current`. Check home → features → releases → support → privacy on desktop and mobile when changing shared styles.
