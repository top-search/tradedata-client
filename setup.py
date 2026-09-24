from setuptools import setup, find_packages

setup(
    name="tradedata-client",
    version="0.1.1",
    description="TradeData Api | Import Export Data Source — Official Developer Client for Global Customs Records",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Trade Data Pte. Ltd.",
    author_email="dev@tradedata.io",
    url="https://tradedata.io",
    project_urls={
        "Homepage": "https://tradedata.io",
        "Singapore HQ": "https://tradedata.sg",
        "Documentation": "https://top-search.github.io/tradedata-client/",
        "Source": "https://github.com/top-search/tradedata-client",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Database :: Front-Ends",
    ],
    python_requires=">=3.8",
)
