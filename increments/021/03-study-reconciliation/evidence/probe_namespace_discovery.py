"""Evidence probe only: a namespace spec is not an installed scientific engine.

Uses Python's standard library; never imports or executes Gemmi.
The temporary directory is external to any project repository.
"""
import importlib.machinery
import importlib.metadata
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory


def summarize(spec):
    if spec is None:
        return None
    return {
        "origin_present": spec.origin is not None,
        "loader_type": type(spec.loader).__name__,
        "namespace_locations_count": len(list(spec.submodule_search_locations or [])),
    }


with TemporaryDirectory(prefix="tbmp021_namespace_") as directory:
    Path(directory, "gemmi").mkdir()
    namespace = importlib.machinery.PathFinder.find_spec("gemmi", [directory])
    assert namespace is not None and namespace.loader is None and namespace.origin is None
    synthetic = summarize(namespace)

try:
    version = importlib.metadata.version("gemmi")
except importlib.metadata.PackageNotFoundError:
    version = None

print(json.dumps({
    "probe": "module_discovery_not_engine_execution",
    "empty_source_directory_spec": synthetic,
    "current_context_spec": summarize(importlib.util.find_spec("gemmi")),
    "current_distribution_version": version,
    "historical_distribution_version_proved": False,
    "gemmi_imported_or_executed": False,
    "pytest_executed": False,
}, indent=2))
