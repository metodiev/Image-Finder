# tests/test_finder.py

import os
import tempfile
from pathlib import Path
from image_finder.finder import ImageFinder


def create_test_file(path: Path, name: str, content: str = "test") -> None:
    file_path = path / name
    file_path.write_text(content)


def test_finds_image_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # Create image files
        create_test_file(tmp_path, "photo1.jpg")
        create_test_file(tmp_path, "graphic.PNG")
        create_test_file(tmp_path, "image.jpeg")

        finder = ImageFinder(str(tmp_path))
        results = finder.find_images()

        # Should find 3 images
        assert len(results) == 3
        assert any("photo1.jpg" in f for f in results)
        assert any("graphic.PNG" in f for f in results)
        assert any("image.jpeg" in f for f in results)


def test_ignores_non_image_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # Create files
        create_test_file(tmp_path, "document.txt")
        create_test_file(tmp_path, "notes.md")

        finder = ImageFinder(str(tmp_path))
        results = finder.find_images()

        # Should find no images
        assert len(results) == 0


def test_recursively_finds_images():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        subfolder = tmp_path / "nested"
        subfolder.mkdir()

        create_test_file(subfolder, "deep.jpg")
        create_test_file(tmp_path, "top.png")

        finder = ImageFinder(str(tmp_path))
        results = finder.find_images()

        # Should find 2 images
        assert len(results) == 2
        assert any("deep.jpg" in f for f in results)
        assert any("top.png" in f for f in results)


def test_empty_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        finder = ImageFinder(tmpdir)
        results = finder.find_images()

        assert results == []
