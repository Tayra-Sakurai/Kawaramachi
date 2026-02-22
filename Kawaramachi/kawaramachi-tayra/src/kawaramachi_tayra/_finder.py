# SPDX-FileCopyrightText: 2026 Tayra Sakurai <taira_sakurai@outlook.jp>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Finder module."""
from pathlib import Path
import mimetypes
from os import PathLike
from typing import List


def find_by_mimetypes(dirname: PathLike, mimetype: str) -> List[Path]:
    """Finds all files with matched mimetype.

    Args:
        dirname: The path or string which reresents the path of target directory.
        mimetype: The MIME type identifier of the searched file type.

    Returns:
        The list of the Path object.
    """
    extensions: List[str] = mimetypes.guess_all_extensions(mimetype)
    
