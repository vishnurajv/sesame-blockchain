from pathlib import Path
from typing import Dict


def public_ssl_paths(path: Path, config: Dict):
    return (
        path / config["ssl"]["public_crt"],
        path / config["ssl"]["public_key"],
    )


def private_ssl_paths(path: Path, config: Dict):
    return (
        path / config["ssl"]["private_crt"],
        path / config["ssl"]["private_key"],
    )


def private_ssl_ca_paths(path: Path, config: Dict):
    return (
        path / config["private_ssl_ca"]["crt"],
        path / config["private_ssl_ca"]["key"],
    )


def sesame_ssl_ca_paths(path: Path, config: Dict):
    return (
        path / config["sesame_ssl_ca"]["crt"],
        path / config["sesame_ssl_ca"]["key"],
    )