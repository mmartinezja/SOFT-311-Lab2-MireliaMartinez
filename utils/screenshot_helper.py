from pathlib import Path


def screenshot_path(
    filename: str
) -> str:

    screenshots_dir = Path(
        "artifacts/screenshots"
    )

    screenshots_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    return str(
        screenshots_dir / filename
    )