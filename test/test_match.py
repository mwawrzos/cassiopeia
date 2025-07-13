import cassiopeia
import pytest

from merakicommons.container import SearchableList
from datapipelines.common import NotFoundError

from .constants import SUMMONER_NAME, UNKNOWN_SUMMONER_NAME


def test_matches_return_type():
    a = cassiopeia.Account(name=SUMMONER_NAME, tagline="NA1", region="NA")
    summoner = a.summoner
    match_history = cassiopeia.get_match_history(puuid=summoner.puuid, continent=cassiopeia.data.Continent.americas)

    assert isinstance(match_history, SearchableList)
    assert all(isinstance(m, cassiopeia.Match) for m in match_history)


def test_matches_raises_with_unknown_summoner():
    with pytest.raises(NotFoundError):
        a = cassiopeia.Account(name=UNKNOWN_SUMMONER_NAME, tagline="NA1", region="NA")
        summoner = a.summoner
        match_history = cassiopeia.get_match_history(puuid=summoner.puuid, continent=cassiopeia.data.Continent.americas)
        match = match_history[0]


def test_match_correct_return():
    a = cassiopeia.Account(name=SUMMONER_NAME, tagline="NA1", region="NA")
    summoner = a.summoner
    match_history = cassiopeia.get_match_history(puuid=summoner.puuid, continent=cassiopeia.data.Continent.americas)
    first_match = match_history[0]

    match_from_id = cassiopeia.get_match(id=first_match.id, region="NA")

    assert isinstance(match_from_id, cassiopeia.Match)
    assert first_match.id == match_from_id.id
    assert first_match == match_from_id


def test_match_participant_search():
    a = cassiopeia.Account(name="Kejorn", tagline="VeigR", region="NA")
    summoner = a.summoner
    match = summoner.match_history[0]
    p = match.participants[summoner]
