import pytest
import re
from pathlib import Path

# ── Helpers ──────────────────────────────────────────────────────────────────

def run_task(filename, var_name, value):
    """Execute a task file with the boolean variable forced to a specific value."""
    source = Path(filename).read_text()
    modified = re.sub(
        rf'^{var_name}\s*=\s*(True|False)',
        f'{var_name} = {value}',
        source,
        flags=re.MULTILINE
    )
    namespace = {}
    exec(modified, namespace)
    return namespace

def has_enough_text(outcome):
    """Check that at least 10 characters follow the colon in outcome."""
    return bool(re.search(r':\s*.{10,}', outcome))

def count_if_not():
    """Count if not patterns across all task files."""
    pattern = re.compile(r'if\s+not\s+\w+\s*:')
    total = 0
    for i in range(1, 6):
        source = Path(f'task{i}.py').read_text()
        total += len(pattern.findall(source))
    return total

# ── Global ────────────────────────────────────────────────────────────────────

def test_if_not_used_exactly_twice():
    count = count_if_not()
    assert count == 2, (
        f"Found {count} use(s) of 'if not' across all tasks. "
        "The 'not' operator must be used exactly twice — check your reference sheet."
    )

# ── Task 1 — torch_lit ────────────────────────────────────────────────────────

def test_task1_torch_lit_is_bool():
    ns = run_task('task1.py', 'torch_lit', 'True')
    assert isinstance(ns.get('torch_lit'), bool), (
        "torch_lit should be a boolean. "
        "Check your reference sheet — what are the only two values a boolean can hold?"
    )

def test_task1_flicker_when_true():
    ns = run_task('task1.py', 'torch_lit', 'True')
    outcome = ns.get('outcome', '')
    assert outcome.startswith('Flicker:'), (
        "When torch_lit is True, outcome should begin with 'Flicker:'. "
        "Check which branch runs when a boolean is True."
    )

def test_task1_doom_when_false():
    ns = run_task('task1.py', 'torch_lit', 'False')
    outcome = ns.get('outcome', '')
    assert outcome.startswith('Doom:'), (
        "When torch_lit is False, outcome should begin with 'Doom:'. "
        "Check your else branch."
    )

def test_task1_flicker_has_text():
    ns = run_task('task1.py', 'torch_lit', 'True')
    outcome = ns.get('outcome', '')
    assert has_enough_text(outcome), (
        "Your Flicker: outcome needs more creative text after the prefix."
    )

def test_task1_doom_has_text():
    ns = run_task('task1.py', 'torch_lit', 'False')
    outcome = ns.get('outcome', '')
    assert has_enough_text(outcome), (
        "Your Doom: outcome needs more creative text after the prefix."
    )

# ── Task 2 — has_key ─────────────────────────────────────────────────────────

def test_task2_has_key_is_bool():
    ns = run_task('task2.py', 'has_key', 'True')
    assert isinstance(ns.get('has_key'), bool), (
        "has_key should be a boolean. "
        "Check your reference sheet — what are the only two values a boolean can hold?"
    )

def test_task2_click_when_true():
    ns = run_task('task2.py', 'has_key', 'True')
    outcome = ns.get('outcome', '')
    assert outcome.startswith('Click:'), (
        "When has_key is True, outcome should begin with 'Click:'. "
        "Check which branch runs when a boolean is True."
    )

def test_task2_doom_when_false():
    ns = run_task('task2.py', 'has_key', 'False')
    outcome = ns.get('outcome', '')
    assert outcome.startswith('Doom:'), (
        "When has_key is False, outcome should begin with 'Doom:'. "
        "Check your else branch."
    )

def test_task2_click_has_text():
    ns = run_task('task2.py', 'has_key', 'True')
    outcome = ns.get('outcome', '')
    assert has_enough_text(outcome), (
        "Your Click: outcome needs more creative text after the prefix."
    )

def test_task2_doom_has_text():
    ns = run_task('task2.py', 'has_key', 'False')
    outcome = ns.get('outcome', '')
    assert has_enough_text(outcome), (
        "Your Doom: outcome needs more creative text after the prefix."
    )

# ── Task 3 — guard_awake ──────────────────────────────────────────────────────

def test_task3_guard_awake_is_bool():
    ns = run_task('task3.py', 'guard_awake', 'True')
    assert isinstance(ns.get('guard_awake'), bool), (
        "guard_awake should be a boolean. "
        "Check your reference sheet — what are the only two values a boolean can hold?"
    )

def test_task3_shadow_when_false():
    ns = run_task('task3.py', 'guard_awake', 'False')
    outcome = ns.get('outcome', '')
    assert outcome.startswith('Shadow:'), (
        "When guard_awake is False, outcome should begin with 'Shadow:'. "
        "Think carefully — is this a case where 'not' would help?"
    )

def test_task3_doom_when_true():
    ns = run_task('task3.py', 'guard_awake', 'True')
    outcome = ns.get('outcome', '')
    assert outcome.startswith('Doom:'), (
        "When guard_awake is True, outcome should begin with 'Doom:'. "
        "Check your else branch."
    )

def test_task3_shadow_has_text():
    ns = run_task('task3.py', 'guard_awake', 'False')
    outcome = ns.get('outcome', '')
    assert has_enough_text(outcome), (
        "Your Shadow: outcome needs more creative text after the prefix."
    )

def test_task3_doom_has_text():
    ns = run_task('task3.py', 'guard_awake', 'True')
    outcome = ns.get('outcome', '')
    assert has_enough_text(outcome), (
        "Your Doom: outcome needs more creative text after the prefix."
    )

# ── Task 4 — drawbridge_raised ────────────────────────────────────────────────

def test_task4_drawbridge_raised_is_bool():
    ns = run_task('task4.py', 'drawbridge_raised', 'True')
    assert isinstance(ns.get('drawbridge_raised'), bool), (
        "drawbridge_raised should be a boolean. "
        "Check your reference sheet — what are the only two values a boolean can hold?"
    )

def test_task4_thunder_when_false():
    ns = run_task('task4.py', 'drawbridge_raised', 'False')
    outcome = ns.get('outcome', '')
    assert outcome.startswith('Thunder:'), (
        "When drawbridge_raised is False, outcome should begin with 'Thunder:'. "
        "Think carefully — is this a case where 'not' would help?"
    )

def test_task4_doom_when_true():
    ns = run_task('task4.py', 'drawbridge_raised', 'True')
    outcome = ns.get('outcome', '')
    assert outcome.startswith('Doom:'), (
        "When drawbridge_raised is True, outcome should begin with 'Doom:'. "
        "Check your else branch."
    )

def test_task4_thunder_has_text():
    ns = run_task('task4.py', 'drawbridge_raised', 'False')
    outcome = ns.get('outcome', '')
    assert has_enough_text(outcome), (
        "Your Thunder: outcome needs more creative text after the prefix."
    )

def test_task4_doom_has_text():
    ns = run_task('task4.py', 'drawbridge_raised', 'True')
    outcome = ns.get('outcome', '')
    assert has_enough_text(outcome), (
        "Your Doom: outcome needs more creative text after the prefix."
    )

# ── Task 5 — escaped ──────────────────────────────────────────────────────────

def test_task5_escaped_is_bool():
    ns = run_task('task5.py', 'escaped', 'True')
    assert isinstance(ns.get('escaped'), bool), (
        "escaped should be a boolean. "
        "Check your reference sheet — what are the only two values a boolean can hold?"
    )

def test_task5_legend_when_true():
    ns = run_task('task5.py', 'escaped', 'True')
    outcome = ns.get('outcome', '')
    assert outcome.startswith('Legend:'), (
        "When escaped is True, outcome should begin with 'Legend:'. "
        "Check which branch runs when a boolean is True."
    )

def test_task5_doom_when_false():
    ns = run_task('task5.py', 'escaped', 'False')
    outcome = ns.get('outcome', '')
    assert outcome.startswith('Doom:'), (
        "When escaped is False, outcome should begin with 'Doom:'. "
        "Check your else branch."
    )

def test_task5_legend_has_text():
    ns = run_task('task5.py', 'escaped', 'True')
    outcome = ns.get('outcome', '')
    assert has_enough_text(outcome), (
        "Your Legend: outcome needs more creative text after the prefix."
    )

def test_task5_doom_has_text():
    ns = run_task('task5.py', 'escaped', 'False')
    outcome = ns.get('outcome', '')
    assert has_enough_text(outcome), (
        "Your Doom: outcome needs more creative text after the prefix."
    )