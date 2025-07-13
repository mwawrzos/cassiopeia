import arrow

import cassiopeia as cass
from cassiopeia import Queue, Summoner


def test_match_history_1():
    a = cass.Account(name="Jankos", tagline="MYBAD", region="EUW")
    summoner = a.summoner
    match_history = cass.get_match_history(
        puuid=summoner.puuid, continent=cass.data.Continent.europe, queue=Queue.ranked_solo_fives
    )
    assert len(match_history) > 40


def test_match_history_2():
    a = cass.Account(name="Jankos", tagline="MYBAD", region="EUW")
    summoner = a.summoner
    match_history = cass.get_match_history(
        puuid=summoner.puuid,
        continent=cass.data.Continent.europe,
        queue=Queue.ranked_solo_fives,
        start_time=arrow.now().shift(days=-140),
        end_time=arrow.now(),
    )
    assert len(match_history) > 0


def test_match_history_3():
    a = cass.Account(name="Jankos", tagline="MYBAD", region="EUW")
    summoner = a.summoner
    match_history = cass.get_match_history(
        puuid=summoner.puuid,
        continent=cass.data.Continent.europe,
        queue=Queue.ranked_solo_fives,
        start_time=arrow.get(2025, 6, 1),
        end_time=arrow.get(2025, 6, 30),
    )
    assert len(match_history) == 168


def test_match_history_5():
    a = cass.Account(name="Jankos", tagline="MYBAD", region="EUW")
    summoner = a.summoner
    match_history = cass.get_match_history(
        puuid=summoner.puuid,
        continent=cass.data.Continent.europe,
        queue=Queue.ranked_solo_fives,
        start_time=arrow.get(2024, 1, 1),
        end_time=arrow.now(),
    )
    assert len(match_history) > 0


def test_match_history_6():
    a = cass.Account(name="Jankos", tagline="MYBAD", region="EUW")
    summoner = a.summoner
    match_history = cass.get_match_history(
        puuid=summoner.puuid,
        continent=cass.data.Continent.europe,
        queue=Queue.ranked_solo_fives,
        start_time=arrow.get(2025, 6, 1),
        end_time=arrow.get(2025, 6, 30),
    )
    assert len(match_history) > 0


def test_match_history_7():
    a = cass.Account(name="Jankos", tagline="MYBAD", region="EUW")
    summoner = a.summoner
    match_history = cass.get_match_history(
        puuid=summoner.puuid,
        continent=cass.data.Continent.europe,
        queue=Queue.ranked_solo_fives,
        start_time=arrow.get(2025, 6, 1),
    )
    assert len(match_history) > 0


def test_match_history_8():
    a = cass.Account(name="chowdog", tagline="peso", region="NA")
    summoner = a.summoner
    mh = cass.get_match_history(
        puuid=summoner.puuid,
        continent=cass.data.Continent.americas,
        start=0,
        count=20,
        queue=Queue.ranked_solo_fives,
    )
    match = mh[0]
    assert len(match.participants) == 10
