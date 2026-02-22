# SPDX-FileCopyrightText: 2026 Tayra Sakurai <taira_sakurai@outlook.jp>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Secret Modules"""
from string.templatelib import Interpolation, Template, convert


def _parse_tstr(tstr: Template) -> str:
    """Parsing the template string.

    Args:
        tstr: The t-string to be parsed.

    Returns:
        The parsed string.
    """
    result: str = tstr.strings[0]
    for index, interpolation in enumerate(tstr.interpolations):
        if interpolation.format_spec == '':
            result += convert(interpolation.value, conversion=interpolation.conversion)
        else:
            result += format(interpolation.value, interpolation.format_spec)
        result += tstr.strings[index + 1]
    return result
