import setuptools

setuptools.setup(
    name="timbra",
    version="0.0.1",
    py_modules=["timbra", "usertime", "timbra_cli"],
    entry_points = {
        "console_scripts": [
            "timbra = timbra_cli:main",
        ]
    }

)
