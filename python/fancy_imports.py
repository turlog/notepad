from types import ModuleType

from importlib.util import LazyLoader, find_spec, module_from_spec


def lazy_import(name: str) -> ModuleType:
    module = module_from_spec(spec := find_spec(name))
    LazyLoader(spec.loader).exec_module(module)
    return module


print("lazyload")
fancy_imports_mod = lazy_import("fancy_imports_mod")

print("access")
print(fancy_imports_mod.ready)
