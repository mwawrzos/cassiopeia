from collections import Counter
import datetime
import random

import cassiopeia as cass
from cassiopeia import (
    Queue,
    Summoner,
    Match,
    Champion,
    Champions,
    ChampionMastery,
    Item,
    Items,
    LanguageStrings,
    Map,
    Locales,
    Runes,
    Rune,
    ShardStatus,
    FeaturedMatches,
    SummonerSpell,
    SummonerSpells,
    GameMode,
    Role,
)

import os, pytest


def test_versions():
    versions = cass.get_versions(region="NA")
    versions[0]
    versions.region
    versions = cass.get_versions(region="NA")
    versions[0]


def test_realms():
    realms = cass.get_realms(region="NA")
    realms.latest_versions


def test_match():
    name = "Kalturi"
    region = "NA"

    a = cass.Account(name=name, tagline="NA1", region=region)
    summoner = a.summoner

    match_history = cass.get_match_history(a.continent, summoner.puuid, queue=Queue.ranked_solo_fives)
    match_history = summoner.match_history
    match_history(queue=Queue.ranked_solo_fives)

    champion_id_to_name_mapping = {
        champion.id: champion.name for champion in cass.get_champions(region=region)
    }
    played_champions = Counter()
    for match in match_history[:5]:
        champion_id = match.participants[summoner].champion.id
        champion_name = champion_id_to_name_mapping[champion_id]
        played_champions[champion_name] += 1

    for champion_name, count in played_champions.most_common(10):
        champion_name, count

    match = match_history[0]
    match.id

    p = match.participants[summoner]
    p.id, p.summoner.region, p.summoner_name, p.summoner.puuid, p.champion.id, p.champion.name,

    for p in match.participants:
        p.id, p.summoner.region, p.summoner_name, p.summoner.puuid, p.champion.id, p.champion.name, p.team.first_dragon, p.runes.keystone.name

    for p in match.participants:
        p.id, p.summoner.region, p.summoner_name, p.summoner.puuid, p.champion.id, p.champion.name, p.team.first_dragon, p.runes.keystone.name

    for p in match.participants:
        for r in p.stat_runes:
            r.name

    match.blue_team.win
    match.red_team.win
    for p in match.blue_team.participants:
        p.summoner_name


def test_champions():
    champions = Champions(region="NA")
    for champion in champions:
        champion.name, champion.id

    annie = Champion(name="Annie", region="NA")
    annie.name
    annie.title
    for spell in annie.spells:
        spell.name, spell.keywords

    annie.info.difficulty
    annie.passive.name
    annie.free_to_play
    annie._Ghost__all_loaded

    ziggs = cass.get_champion("Ziggs", region="NA")
    ziggs.name
    ziggs.region
    ziggs.free_to_play
    for spell in ziggs.spells:
        for var in spell.variables:
            spell.name, var
    ziggs._Ghost__all_loaded


def test_championmastery():
    me = cass.Account(name="Kalturi", tagline="NA1", region="NA")
    karma = Champion(name="Karma", id=43, region="NA")
    cm = ChampionMastery(champion=karma, summoner=me.summoner, region="NA")
    cm = cass.get_champion_mastery(champion=karma, summoner=me.summoner, region="NA")
    "Champion ID:", cm.champion.id
    "Mastery points:", cm.points
    "Mastery Level:", cm.level
    "Points until next level:", cm.points_until_next_level

    cms = cass.get_champion_masteries(summoner=me.summoner, region="NA")
    cms = me.summoner.champion_masteries
    cms[0].points
    cms["Karma"].points  # Does a ton of calls without a cache

    "{} has mastery level 6 or higher on:".format(me.name_with_tagline)
    pro = cms.filter(lambda cm: cm.level >= 6)
    [cm.champion.name for cm in pro]


def test_items():
    dagger = Item(name="Dagger", region="NA")
    dagger.name
    dagger.id
    items = cass.get_items(region="NA")
    for item in items:
        item.name
    items = cass.get_items(region="NA")
    items[10].name
    dagger = Item(name="Dagger", region="NA")
    dagger.name, dagger.id
    items = Items(region="NA")
    items[10].name


def test_languagestrings():
    language_strings = cass.get_language_strings(region="NA")
    assert len(language_strings.strings) > 0


def test_leagues():
    summoner_name = "Kalturi"
    region = "NA"
    a = cass.Account(name=summoner_name, tagline="NA1", region=region)
    summoner = a.summoner
    "Name:", summoner.account.name
    "PUUID:", summoner.puuid

    # entries = cass.get_league_entries(summoner, region=region)
    entries = summoner.league_entries
    if entries.fives.promos is not None:
        # If the summoner is in their promos, print some info
        "Promos progress:", entries.fives.promos.progress
        "Promos wins", entries.fives.promos.wins
        "Promos losses:", entries.fives.promos.losses
        "Games not yet played in promos:", entries.fives.promos.not_played
        "Number of wins required to win promos:", entries.fives.promos.wins_required
    else:
        "The summoner is not in their promos."

    "Name and id of fives leagues this summoner is in:"
    entries.fives.league.name
    entries.fives.league.id
    f"Listing all summoners in {entries.fives.league.id}"
    for entry in entries.fives.league.entries:
        entry.summoner.account.name, entry.league_points, entries.fives.league.tier, entry.division
        entry.league.name, entry.tier

    "Challenger League name and id:"
    challenger = cass.get_challenger_league(
        queue=Queue.ranked_solo_fives, region=region
    )
    # challenger.name
    challenger.id

    "Grandmaster League name and id:"
    grandmaster = cass.get_grandmaster_league(
        queue=Queue.ranked_solo_fives, region=region
    )
    # grandmaster.name
    grandmaster.id

    "Master League name and id:"
    master = cass.get_master_league(queue=Queue.ranked_solo_fives, region=region)
    # master.name
    master.id, master.name


def test_locales():
    locales = cass.get_locales(region="NA")
    for locale in locales:
        locale
    assert len(locales) > 10


def test_maps():
    maps = cass.get_maps(region="NA")
    for map in maps:
        map.name, map.id

    map = Map(name="Summoner's Rift", region="NA")
    map.id


def test_profileicons():
    profile_icons = cass.get_profile_icons(region="NA")
    for pi in profile_icons:
        pi.name, pi.id
    profile_icons[10].name


def test_readme():
    summoner = cass.get_account(name="Kalturi", tagline="NA1", region="NA").summoner
    "{name} is a level {level} summoner on the {region} server.".format(
        name=summoner.account.name, level=summoner.level, region=summoner.region
    )
    champions = cass.get_champions(region="NA")
    random_champion = random.choice(champions)
    "He enjoys playing champions such as {name}.".format(name=random_champion.name)

    challenger_league = cass.get_challenger_league(
        queue=cass.Queue.ranked_solo_fives, region="NA"
    )
    best_na = challenger_league[0].summoner
    "He's not as good as {name} at League, but probably a better python programmer!".format(
        name=best_na.account.name
    )


def test_runes():
    for rune in cass.get_runes(region="NA").keystones:
        rune.name, rune.id, rune.path, rune.tier
        assert rune.is_keystone


def test_shards():
    status = cass.get_status(region="NA")
    status = ShardStatus(region="NA")
    status.name


def test_spectator():
    featured_matches = cass.get_featured_matches(region="NA")
    for match in featured_matches:
        match.region, match.id

    match = featured_matches[0]
    a_summoner = match.blue_team.participants[0].summoner
    a_summoner.account.name
    a_tagline = match.blue_team.participants[0].summoner.account.tagline
    match.queue
    summoner = cass.Summoner(puuid=a_summoner.puuid, region=match.region)
    current_match = summoner.current_match
    current_match.map.name

    for participant in current_match.blue_team.participants:
        participant.summoner.account.name


def test_summoner():
    name = "Kalturi"
    region = "NA"
    a = cass.Account(name=name, tagline="NA1", region=region)
    summoner = a.summoner
    "Name:", summoner.account.name
    "PUUID:", summoner.puuid
    "Level:", summoner.level
    "Revision date:", summoner.revision_date
    "Profile icon ID:", summoner.profile_icon.id
    "Profile icon name:", summoner.profile_icon.name
    "Profile icon URL:", summoner.profile_icon.url
    "Profile icon image:", summoner.profile_icon.image


def test_summonerspells():
    sspells = cass.get_summoner_spells(region="NA")
    for sspell in sspells:
        if set(sspell.modes) & {
            GameMode.classic,
            GameMode.aram,
            GameMode.poro_king,
            GameMode.ascension,
        }:
            "Name:", sspell.name
            "Description:", sspell.description

    sspell = SummonerSpell(name="Ghost", region="NA")
    sspell.description


def test_timeline():
    name = "Kalturi"
    region = "NA"
    a = cass.Account(name=name, tagline="NA1", region=region)
    summoner = a.summoner
    match_history = summoner.match_history
    match = match_history[0]
    "Match ID:", match.id

    match.timeline.frame_interval
    for frame in match.timeline.frames:
        for event in frame.events:
            event.type

    for p in match.participants:
        for event in p.timeline.events:
            event.type
    
    match = next(m for m in match_history if m.duration > datetime.timedelta(minutes=16))
    p = match.participants[summoner]
    p_state = p.cumulative_timeline[datetime.timedelta(minutes=15, seconds=30)]
    p_state = p.cumulative_timeline["15:30"]

    items = [item.name for item in p_state.items]
    print("Champion:", p.champion.name)
    print("Items:", items)
    print("Skills:", p_state.skills)
    print("Kills:", p_state.kills)
    print("Deaths:", p_state.deaths)
    print("Assists:", p_state.assists)
    print("KDA:", p_state.kda)
    print("Level:", p_state.level)
    print("Position:", p_state.position)
    print("Exp:", p_state.experience)
    print("Number of objectives assisted in:", p_state.objectives)
    print("Gold earned:", p_state.gold_earned)
    print("Current gold:", p_state.current_gold)
    print("CS:", p_state.creep_score)
    print("CS in jungle:", p_state.neutral_minions_killed)
