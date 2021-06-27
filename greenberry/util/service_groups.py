from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "greenberry_harvester greenberry_timelord_launcher greenberry_timelord greenberry_farmer greenberry_full_node greenberry_wallet".split(),
    "node": "greenberry_full_node".split(),
    "harvester": "greenberry_harvester".split(),
    "farmer": "greenberry_harvester greenberry_farmer greenberry_full_node greenberry_wallet".split(),
    "farmer-no-wallet": "greenberry_harvester greenberry_farmer greenberry_full_node".split(),
    "farmer-only": "greenberry_farmer".split(),
    "timelord": "greenberry_timelord_launcher greenberry_timelord greenberry_full_node".split(),
    "timelord-only": "greenberry_timelord".split(),
    "timelord-launcher-only": "greenberry_timelord_launcher".split(),
    "wallet": "greenberry_wallet greenberry_full_node".split(),
    "wallet-only": "greenberry_wallet".split(),
    "introducer": "greenberry_introducer".split(),
    "simulator": "greenberry_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
