from setuptools import setup 

with open("requirements.txt") as f: 
    requirements = f.read().splitlines()

setup(
    name="pretend-api",
    version="1.0.0",
    description="A Python API wrapper for pretend api",
    author="Pretend LLC",
    url="https://github.com/PretendServices/pretend-api",
    install_requires=requirements,
    python_requires='>=3.8.0',
    project_urls = {
        "Documentation": "https://v1.pretend.bot/docs"
    }
)