from cassiopeia import Queue, Account, SummonersRiftArea


def test_summonersrift_map():
    a = Account(name="Kalturi", tagline="NA1", region="NA")
    summoner = a.summoner
    match = summoner.match_history(queue=Queue.ranked_solo_fives)[0]
    for frame in match.timeline.frames:
        for event in frame.events:
            if event.type == "CHAMPION_KILL":
                SummonersRiftArea.from_position(event.position)


def test_from_match():
    a = Account(name="Kalturi", tagline="NA1", region="NA")
    summoner = a.summoner
    match_history = summoner.match_history

    match = match_history[0]
    timeline = match.timeline
    for frame in timeline.frames[:-1]:
        for pf in frame.participant_frames.values():
            print(pf.position.location)
