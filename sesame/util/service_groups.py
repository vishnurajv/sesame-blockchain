from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "sesame_harvester sesame_timelord_launcher sesame_timelord sesame_farmer sesame_full_node sesame_wallet".split(),
    "node": "sesame_full_node".split(),
    "harvester": "sesame_harvester".split(),
    "farmer": "sesame_harvester sesame_farmer sesame_full_node sesame_wallet".split(),
    "farmer-no-wallet": "sesame_harvester sesame_farmer sesame_full_node".split(),
    "farmer-only": "sesame_farmer".split(),
    "timelord": "sesame_timelord_launcher sesame_timelord sesame_full_node".split(),
    "timelord-only": "sesame_timelord".split(),
    "timelord-launcher-only": "sesame_timelord_launcher".split(),
    "wallet": "sesame_wallet sesame_full_node".split(),
    "wallet-only": "sesame_wallet".split(),
    "introducer": "sesame_introducer".split(),
    "simulator": "sesame_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
