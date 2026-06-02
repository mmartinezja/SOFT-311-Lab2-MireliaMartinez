from pathlib import Path


def assert_with_screenshot(
    page,
    condition,
    message,
    name="assert"
):

    screenshots_dir = Path(
        "artifacts/screenshots"
    )

    screenshots_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    if not condition:

        page.screenshot(
            path=str(
                screenshots_dir /
                f"{name}_failure.png"
            ),
            full_page=True
        )

        raise AssertionError(
            message
        )