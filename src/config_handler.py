from importlib import import_module


def module_importer(module_path: str):
    return import_module(module_path)
