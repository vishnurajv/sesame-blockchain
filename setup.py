from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "sesamevdf==1.0.1",  # timelord and vdf verification
    "sesamebip158==1.0",  # bip158-style wallet filters
    "sesamepos==1.0.2",  # proof of space
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
    "setproctitle==1.2.2",  # Gives the sesame processes readable names
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
    name="sesame-blockchain",
    author="Sesame Dev",
    author_email="sesamedev@sesamechain.network",
    description="Sesame blockchain full node, farmer, timelord, and wallet.",
    url="https://sesamechain.network/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="sesame blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "sesame",
        "sesame.cmds",
        "sesame.consensus",
        "sesame.daemon",
        "sesame.full_node",
        "sesame.timelord",
        "sesame.farmer",
        "sesame.harvester",
        "sesame.introducer",
        "sesame.plotting",
        "sesame.protocols",
        "sesame.rpc",
        "sesame.server",
        "sesame.simulator",
        "sesame.types.blockchain_format",
        "sesame.types",
        "sesame.util",
        "sesame.wallet",
        "sesame.wallet.puzzles",
        "sesame.wallet.rl_wallet",
        "sesame.wallet.cc_wallet",
        "sesame.wallet.did_wallet",
        "sesame.wallet.settings",
        "sesame.wallet.trading",
        "sesame.wallet.util",
        "sesame.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "sesame = sesame.cmds.sesame:main",
            "sesame_wallet = sesame.server.start_wallet:main",
            "sesame_full_node = sesame.server.start_full_node:main",
            "sesame_harvester = sesame.server.start_harvester:main",
            "sesame_farmer = sesame.server.start_farmer:main",
            "sesame_introducer = sesame.server.start_introducer:main",
            "sesame_timelord = sesame.server.start_timelord:main",
            "sesame_timelord_launcher = sesame.timelord.timelord_launcher:main",
            "sesame_full_node_simulator = sesame.simulator.start_simulator:main",
        ]
    },
    package_data={
        "sesame": ["pyinstaller.spec"],
        "sesame.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "sesame.util": ["initial-*.yaml", "english.txt"],
        "sesame.ssl": ["sesame_ca.crt", "sesame_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
