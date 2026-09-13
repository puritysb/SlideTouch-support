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

When a presentation is exported as flattened image-based slides, the text is no longer directly editable. SlideTouch helps you correct a date or phrase without rebuilding the whole slide.

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

## Content updates and release checks

- `scripts/site_content.json` owns EN/KO/JA release status, release notes, feature descriptions and support FAQ. Homepages use the same release status.
- Run `python3 scripts/refresh_content.py`, then `python3 scripts/refresh_home.py`, then `python3 scripts/check_content.py` and `git diff --check`.
- Verify the released and pending versions in App Store Connect before changing status. An uploaded build is not a released app. On approval, update the status/date in all three locale entries and remove obsolete preview wording where appropriate.
- Reconcile release notes with the app repository's `AppStore/metadata/*/whats-new-1.1.0.txt`, `AppStore/FinalUI-2026-09/*/metadata/whats-new.txt`, and current code. Latest requirements come from `SlideTouch.xcodeproj/project.pbxproj`.
- Privacy body remains in each `docs/*/privacy.html`; its search description and support-sharing paragraph are managed by the content generator. Check both visible copy and metadata.
- On 2026-09-13, ASC showed 1.1.0 released and 1.2.0 awaiting review. The site now includes both histories, clearly labels 1.2 previews, uses actual photo-background output, and marks older screenshots as such. No unsupported speed multiplier, exact restoration, fixed model-unload time or individual-page close instruction is used.
- Before publishing, inspect desktop and mobile pages, expand support FAQs, follow demo/release links, and verify public HTML/CSS against the committed output after Pages finishes.
