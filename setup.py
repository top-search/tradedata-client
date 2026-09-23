from setuptools import setup, find_packages

setup(
    name="tradedata-client",
    version="0.1.0",
    description="Official Developer Client for TradeData.io & TradeInt Customs Big Data API",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Top Search Developer Team",
    author_email="dev@tradedata.io",
    url="https://tradedata.io",
    project_urls={
        "Homepage": "https://tradedata.io",
        "TradeInt Flagship": "https://tradeint.com",
        "Vietnam Hub": "https://tradeint.vn",
        "Documentation": "https://tradedata.io/docs",
        "Source": "https://github.com/top-search/tradedata-client",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
)
