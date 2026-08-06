"""Import bridge for scripts/call-gemini.py (hyphenated filename).

call-gemini.py cannot be imported with a normal ``import`` statement
because of the hyphen. It has no import-time side effects (verified:
``genai.configure()`` only runs inside ``setup_gemini()``, ``main()`` is
``__name__``-guarded), so loading it via importlib is safe.

Its internal imports (``from modules.template_processor import ...``,
``from validate_summary import ...``) assume ``scripts/`` is on
``sys.path`` — replicated here before exec.
"""

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"

_MODULE_NAME = "call_gemini_eval"


def ensure_scripts_on_path() -> None:
    if str(SCRIPTS_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPTS_DIR))


def load_call_gemini():
    """Load scripts/call-gemini.py under a synthetic module name (memoized)."""
    ensure_scripts_on_path()

    if _MODULE_NAME in sys.modules:
        return sys.modules[_MODULE_NAME]

    spec = importlib.util.spec_from_file_location(
        _MODULE_NAME, SCRIPTS_DIR / "call-gemini.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[_MODULE_NAME] = module
    spec.loader.exec_module(module)
    return module
