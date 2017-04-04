import imp

def _pymysql():
    import importlib
    try:
        importlib.import_module("pymysql")
    except ImportError:
        import pip
        pip.main(['install', "pymysql"])
    finally:
        globals()["pymysql"] = importlib.import_module("pymysql")
        imp.reload(pymysql)
