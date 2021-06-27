from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "chiavdf==1.0.1",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.2",  # proof of space
    "clvm==0.9.6",
    "clvm_rs==0.1.7",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the greenberry processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.1",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="greenberry-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@greenberry.network",
    description="GreenBerry blockchain full node, farmer, timelord, and wallet.",
    url="https://greenberry.network/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="greenberry blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "greenberry",
        "greenberry.cmds",
        "greenberry.consensus",
        "greenberry.daemon",
        "greenberry.full_node",
        "greenberry.timelord",
        "greenberry.farmer",
        "greenberry.harvester",
        "greenberry.introducer",
        "greenberry.plotting",
        "greenberry.protocols",
        "greenberry.rpc",
        "greenberry.server",
        "greenberry.simulator",
        "greenberry.types.blockchain_format",
        "greenberry.types",
        "greenberry.util",
        "greenberry.wallet",
        "greenberry.wallet.puzzles",
        "greenberry.wallet.rl_wallet",
        "greenberry.wallet.cc_wallet",
        "greenberry.wallet.did_wallet",
        "greenberry.wallet.settings",
        "greenberry.wallet.trading",
        "greenberry.wallet.util",
        "greenberry.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "greenberry = greenberry.cmds.greenberry:main",
            "greenberry_wallet = greenberry.server.start_wallet:main",
            "greenberry_full_node = greenberry.server.start_full_node:main",
            "greenberry_harvester = greenberry.server.start_harvester:main",
            "greenberry_farmer = greenberry.server.start_farmer:main",
            "greenberry_introducer = greenberry.server.start_introducer:main",
            "greenberry_timelord = greenberry.server.start_timelord:main",
            "greenberry_timelord_launcher = greenberry.timelord.timelord_launcher:main",
            "greenberry_full_node_simulator = greenberry.simulator.start_simulator:main",
        ]
    },
    package_data={
        "greenberry": ["pyinstaller.spec"],
        "greenberry.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "greenberry.util": ["initial-*.yaml", "english.txt"],
        "greenberry.ssl": ["greenberry_ca.crt", "greenberry_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
