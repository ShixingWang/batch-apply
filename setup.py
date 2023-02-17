from setuptools import setup

setup(
    name="batch_apply",
    version="0.0.1",
    description="Given a function and a pandas.DataFrame, execute the function with each row of DF as kwargs.",
    author="Shixing Simon Wang",
    author_email="ShixingWang@users.noreply.github.com",
    url="https://github.com/ShixingWang/batch-apply",
    py_modules=["batch_apply"],
    install_requires=[
        "pandas"
    ]
)