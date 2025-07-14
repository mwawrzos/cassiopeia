import os
import unittest

import cassiopeia

from .constants import SUMMONER_NAME, UNKNOWN_SUMMONER_NAME


class TestSummoner(unittest.TestCase):
    def setUp(self):
        cassiopeia.apply_settings(cassiopeia.get_default_config())
        cassiopeia.set_riot_api_key(os.environ.get("RIOT_API_KEY"))

    def test_unknown_summoner(self):
        for e in cassiopeia.get_account(name="Kalturi", tagline="NA1", region="NA").summoner.league_entries:
            print(e.league.name)
        self.assertFalse(
            cassiopeia.get_account(name=UNKNOWN_SUMMONER_NAME, tagline="NA1", region="NA").exists
        )

    def test_ranks(self):
        a = cassiopeia.get_account(name=SUMMONER_NAME, tagline="NA1", region="NA")
        s = a.summoner
        ranks = s.ranks
        for key in ranks:
            self.assertIsInstance(key, cassiopeia.Queue)
            self.assertIsInstance(ranks[key], cassiopeia.data.Rank)

    def test_access_properties(self):
        a = cassiopeia.get_account(name=SUMMONER_NAME, tagline="NA1", region="NA")
        s = a.summoner
        self.assertIsNotNone(s.region)
        self.assertIsNotNone(s.platform)
        self.assertIsNotNone(s.puuid)
        self.assertIsNotNone(s.account.name)
        self.assertIsNotNone(s.level)
        self.assertIsNotNone(s.profile_icon)
        self.assertIsNotNone(s.revision_date)
        self.assertIsNotNone(s.champion_masteries)
        self.assertIsNotNone(s.match_history)
        self.assertIsNotNone(s.league_entries)

    def test_get_summoner(self):
        # Get a known summoner via account
        a = cassiopeia.get_account(name=SUMMONER_NAME, tagline="NA1", region="NA")
        s = a.summoner
        # Test get_summoner by puuid
        s_by_puuid = cassiopeia.get_summoner(puuid=s.puuid, region="NA")
        self.assertTrue(s_by_puuid.exists)
        self.assertEqual(s_by_puuid.puuid, s.puuid)


if __name__ == "__main__":
    unittest.main()
