# Text edit example provenance

2026-09-12 development build. Synthetic seeded PDF fixture rendered at 2x, Apple Vision OCR, UnifiedEditorState.selectTextBox / enterTextEditMode / applyTextEdit, Page.batchInpaint, RenderingService composite.

Source: SlideTouchTests/InpaintingQualityTests.swift, testSelectedOCRTextReplacementProducesVisualDemo (SlideTouch repository). The test asserts selected observation, editor visibility, actual inpainted patch, replacement OCR, no original phrase and unchanged source image identity. Font and white color are explicit editing choices, not automatic style estimation.

PNG files are unretouched app pipeline output, not UI screenshots. The website draws a CSS outline from demo-metadata.json OCR bounds. Restoration can soften complex detail. Regenerate artifacts by running the test; copy its SlideTouchQuality/demo-* outputs. Recalculate percentage outline coordinates from metadata if the fixture changes.
