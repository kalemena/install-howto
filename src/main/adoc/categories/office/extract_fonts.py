#!/usr/bin/env python3
"""
Extract fonts from LibreOffice documents.

Supports:
- .odt (OpenDocument Text)
- .ods (OpenDocument Spreadsheet)
- .odp (OpenDocument Presentation)

LibreOffice files are ZIP archives containing XML files.
Font information is stored in styles.xml.
"""

import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Set
import sys


# LibreOffice XML namespaces
NAMESPACES = {
    'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
    'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    'draw': 'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0',
    'svg': 'urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0',
}


def extract_fonts_from_odt(file_path: Path) -> Set[str]:
    """Extract font names from an ODT (or other ODS/ODP) file."""
    fonts: Set[str] = set()

    try:
        with zipfile.ZipFile(file_path, 'r') as zf:
            # Read styles.xml which contains font-face declarations
            if 'styles.xml' in zf.namelist():
                styles_content = zf.read('styles.xml').decode('utf-8')

                # Parse the XML
                root = ET.fromstring(styles_content)

                # Find all font-face declarations
                # The svg:font-family attribute contains the actual font name
                for font_face in root.findall('.//style:font-face', NAMESPACES):
                    family = font_face.get('{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}font-family')
                    if family:
                        # Clean up the font family name (remove quotes like 'Lucida Sans')
                        clean_name = family.strip("''\"")
                        fonts.add(clean_name)

                # Also check for text properties with font-name attribute
                for style in root.findall('.//style:style', NAMESPACES):
                    font_name = style.get('{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-name')
                    if font_name:
                        fonts.add(font_name)

    except zipfile.BadZipFile:
        print(f"Error: {file_path} is not a valid ZIP file (not a LibreOffice document)")
        sys.exit(1)
    except ET.ParseError as e:
        print(f"Error parsing {file_path}: {e}")
        sys.exit(1)

    return fonts


def extract_fonts(file_path: Path) -> Set[str]:
    """
    Extract fonts from a LibreOffice document.

    Supports .odt, .ods, .odp files.
    """
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    suffix = file_path.suffix.lower()

    if suffix in {'.odt', '.ods', '.odp', '.ott', '.ots', '.otp'}:
        return extract_fonts_from_odt(file_path)

    print(f"Error: Unsupported file format: {suffix}")
    print("Supported formats: .odt, .ods, .odp, .ott, .ots, .otp")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_fonts.py <file.odt> [file2.odt ...]")
        sys.exit(1)

    for file_arg in sys.argv[1:]:
        file_path = Path(file_arg)
        fonts = extract_fonts(file_path)

        print(f"\nFonts in {file_path.name}:")
        print("-" * 40)
        for font in sorted(fonts):
            print(f"  - {font}")
        print(f"\nTotal: {len(fonts)} font(s)")


if __name__ == "__main__":
    main()
