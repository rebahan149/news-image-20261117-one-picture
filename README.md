[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/rebahan149/news-image-20261117-one-picture/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/rebahan149/news-image-20261117-one-picture/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# The World's News in One Picture — Tuesday 17 November 2026

Entry for the make.fun bounty [news-image-20261117](https://make.fun/bounty/news-image-20261117): sum up 17 November 2026's world news in one image.

A single front page that sums up one full day of world news — Tuesday 17 November 2026: **40 stories, six continents, one day.**

## What the page shows

- **10 illustrated panels**: Ukraine strikes the Kerch Bridge; Moscow counts 1,441 drones downed in a single night; Iran says tankers hit naval mines in Hormuz; a US base struck in Bahrain; Ebola in DR Congo; Trump travels to Asia; Nvidia tops $115.8bn quarterly revenue; cyclone threats in the Pacific; five EU states plan migrant return hubs in Rwanda; Japan scrambles jets.
- **A "Where it happened" map** with the panels pinned, plus key developments of the day.
- **30 more stories** (numbered 11–40): Serbia's student list, the lost US measles status, UK settlement sanctions, Mondlane on trial in Mozambique, the UN weapons deadlock, Khurelsukh's party revolt in Mongolia, Sudan's 2,230 civilian toll, the Siberia plane crash, the Knesset Kahana bill, Sözcü TV seized in Türkiye, France's 100,000-strong pay march, Xi–Carney tariff cuts, the IMF's Ukraine tranche, FIFA's 2026 expansion and the G20 climate call.

## How it was made

The front-page artwork was created by the entrant. It was then repaired and completed in-session with Muse (`build/repair.py`, source art in `assets/source-frontpage.png`):

- the generated "30 More Stories" list contained corrupted, duplicated entries (a garbled duplicate #22 and a doubled FIFA item) — the whole list was redrawn clean;
- generic filler items were replaced with verified stories from the day's record (Siberia crash, Knesset Kahana bill, Sözcü TV, Mondlane trial, Sudan toll, France pay march, Xi–Carney tariffs, IMF Ukraine);
- panel 2's region tag was corrected (Kyiv is not the Middle East) and its headline replaced with the verified Moscow drone-count story; panel 4's headline was replaced with the verified Bahrain story;
- `build/fit.py` fits the page to the 1024×1024 / 1 MiB gate.

Referred by [@anjars](https://make.fun/r/eskhvp8c) — join make.fun: https://make.fun/r/eskhvp8c
