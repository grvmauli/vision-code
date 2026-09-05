from playwright.sync_api import Page, expect


def test_frame_content(page: Page):

    page.set_content("""
    <!DOCTYPE html>
    <html>
    <body>

        <h1>Frame Verification Demo</h1>

        <iframe
            srcdoc="<html><body><h2 id='status'>Frame Loaded Successfully</h2></body></html>"
            title="verification-frame">
        </iframe>

    </body>
    </html>
    """)

    frame = page.frame_locator(
        "iframe[title='verification-frame']"
    )

    expect(frame.locator("#status")).to_have_text(
        "Frame Loaded Successfully"
    )