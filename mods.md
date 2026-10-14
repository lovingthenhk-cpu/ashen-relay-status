# Modと部品の採用表

## 2026-10-11 最新方針：都市へ集約・元生成停止・物語を一本化

Lost Cities外の独立構造物はなるべく生成させず、都市内に多数・多様な施設を配置する。元Modの建築・敵・技・アイテムを部品として参照し、元Mod独自の物語・案内・攻略順はAshen Relayの進行へ組み替える。旧「原生生成/元ストーリーを維持」の記述は変更前の方針。

**実装した設定**：Iron’s城塞・山岳塔・火術塔、Mowzie寺院・フェラス室、水術塔、湿地小屋、Apotheosis塔4型の元structure set、計11setをfrequency=0に変更。都市wrapperまたは都市の直接template配置と必要な原生登録は維持。砂のApotheosis塔は都市での通常抽選・自動街道接合・冷保存を確認。既存の建築は消去しない。全種・全seedでの停止と移管後分布は未測定。

**未完了の必須作業**：残る35構造setとAlex’s小屋の元生成依存、ピラミッド・墓地・工場・地下祠などの都市移管/元生成停止を対にする。Apotheosis葉/トウヒ塔の自然配置・元Loot/Gem/地区戦闘も確認する。各Modの不要なspawn・loot流入・recipe・旧物語の案内/実績/locatorを実ID別に監査し停止/移管する。必要な戦闘・技・武器更新や企画の種類は削らない。海・次元等の必要環境は都市の対応地区または管理遠征へ移し、不可避の市外例外だけ理由と都市からの導線を明記する。

**都市調整は必須**：疎な都市設定を完成形とせず、市街の広さ・密度・街区接続を調整。固定profileを確認し、同じ3seed/同じ範囲で市街面積・連結面積・都市間隔・施設の実生成/種類/徒歩帰路/負荷を比較する。施設別Lootも魔術・工業・水辺と攻略段階へ合わせて調整する。R-27W4/MからR-28Dの受入に含める。具体値未確定、密度調整と全施設Loot/物語移管は未実装。


固定版のModを丸ごと「有効」または「削除」と扱わない。各行で**原生攻略として残すもの、Ashen Relayへ借りるもの、止める/調整するもの**を対応させる。停止欄は計画であり、現在すでに停止したという意味ではない。採用する実行時参照、動画利用、将来配布の条件は別途R-31で再監査する。

## 世界・施設・ボス

| Mod | パック内の仕事 | 借りる具体物 | 残すもの | 停止・調整するもの / 時期 |
|---|---|---|---|---|
| The Lost Cities `7.5.2` | 現世の道路と街区の基盤 | city/road判定、原生standard citystyle、worldstyle、building/part、接合語彙 | 道路と自然な区画 | 見た目を支配している独自 `vocab_*` 12棟と `link_tower` のselector参照をR-27Wで解消。`anchor_02` は主導線から外す。既存worldの建物は消さない |
| Alex's Caves `2.0.2` | 六洞窟の探索、異なる環境素材 | `alexscaves:forlorn_hut_1` 9×9×9、`MAGNETIZING`、`BUBBLED`、`DEEPSIGHT` | 六洞窟、tablet導線、固有武器・drop | 洞窟全体は止めない。外部施設でのEffectは限定区画・短時間だけ |
| Mowzie's Mobs `1.8.2` | フェラスを最初の強敵にする | `mowziesmobs:wroughtnaut_chamber` 19×7×19、`EntityBlockSwapper.swapBlock` | ボスAI、斧・兜、都市接合室の原生template | 寺院とフェラス室の元生成停止設定を追加。他の移管拠点も元生成停止/都市移管へ。変換床から梯子・箱・出口を除外 |
| Apotheosis `7.4.8` | 拾った装備のAffix/Socket/Gemで更新動機を作る | `tower_main/leaf/sand/spruce`、Affix/Gem装備 | 塔4型の原生template/pool、強化入手 | 射手を変更した場合、その1体だけ元AI/dropの重複を止める。塔4型の元setは停止設定済み。Affix/Gemは維持 |
| Iron's Spells 'n Spellbooks `3.16.3` | 呪文、巻物、詠唱、装備型呪文、地下と城塞 | `catacombs`、`evoker_fort`、LivingEntity caster | 原生施設、呪文、原生loot | 追加敵/追加lootは指定施設内だけ。城塞/山岳塔/火術塔の元生成停止設定を追加。不要要素は実ID別に監査 |
| L_Ender's Cataclysm `3.16` | 大型ボス、工場、海と固有武器 | `ancient_factory`、`sunken_city`、`bone_fracture`、予兆攻撃 | 原生施設・ボス・固有drop | 工場の装置室1室だけに追加遭遇を置き、元装置・保護ブロックを上書きしない |
| Bosses of Mass Destruction `1.1.2` | 寒冷地・地下・Nether・Endの四遠征 | `MagicMissileProjectile` と命中callback、Earthdive Spear素材 | 四施設、ボス、原生drop、通常レシピ | Ashen Relay追加報酬の二重支給のみ一回性状態で防ぐ |
| T.O Magic 'n Extras `6.3.0` | ボス技の呪文化、4系列×3段階の武器、横断合成 | `aqua_mage_tower` / `echo_shrine` / `void_cathedral`、Cataclysm/Alex's素材を使う合成 | 原生施設・武器・通常レシピ | 都市へ施設配置を移管し、元生成/不要loot/recipeを停止。必要環境と寸法を確認 |
| Dungeons Enhanced（未導入） | 都市の小型接合元として隔離試験する候補 | `watch_tower` / `ruined_building` 候補 | 採用する施設だけ、原生攻略としての価値を個別判断 | 不要なstructure setを固定jarの実IDごと停止する案。依存、権利、動画、性能のゲート通過前は導入しない |

## 戦闘、進行、制作を支えるMod

| Mod | パック内の具体的な役割 | 扱い |
|---|---|---|
| Better Combat `1.9.0` | 斧、槍、魔術武器などの手触りを変え、施設ごとの武器選択に意味を持たせる | モーションを維持。新しい武器数の代用にはしない |
| Pehkui `3.8.2` | 敵や通路のサイズ条件、時間制限付きscale | 城塞など限定遭遇へ。プレイヤー恒久縮小や帰路を塞ぐ使い方はしない |
| KubeJS `2001.6.5` | 横断レシピ、進行、場所限定lootの配線 | `ashen_relay_recipes.js` と `ashen_relay_loot.js` を主要編集点にする |
| LootJS `2.13.1` | 他Modの元lootを消さず、指定テーブルへ追加分を注入する | 原生dropの全面置換はしない |
| FTB Quests `2001.4.22` | 入口、危険、報酬用途、次の候補を段階的に示す | 未訪問の核心は早期表示しない。章は `ashen_relay.snbt` |
| JEI | T.OやAshen Relayの合成先を確認するUI | 維持 |
| Patchouli | 導入Modの既存ガイド | 維持。独自ガイドへの文面転用は権利確認が必要 |
| Ashen Relay addon | 構造物検出、戦闘のHost/Payload、報酬一回性、継承、記録 | Javaが必要な動的処理のみを担当。単純なloot/recipeはデータとスクリプトへ |

Iron's Lib、Lionfish API、Citadel、Cerbons API、Apothic Attributes、Placebo、Curios、GeckoLib、Player Animation Lib、Rhino、Architectury、Cloth Config、FTB Library、FTB Teamsは、上表のModを動かす固定依存。独立した新攻略先を約束するものではない。版の正本は `pack/mods/*.pw.toml`。

## 未導入Modの案（すべて採用対象・隔離試験待ち）

この表は**pack採用の宣言ではなく、旧ソース調査をゲーム制作の作業へ変える台帳**。各行で「部品を借りるか」「原生の何を残すか」「不要な自然生成・レシピ・AIをどこで止めるか」を調べる。初回試験に失敗した場合は同じ遊びの別経路を試す。

| Mod・旧資料の案 | 実際に試す場面と操作 | 取得・停止の試験 |
|---|---|---|
| Origins Forge / Apoli | 境界で同じEffectをMob・設備・Playerに条件つきで発火 | Action/Condition JSONとaddon Action、種族選択等の不要内容の停止 |
| Ars Nouveau | 高層魔術のturretとPlayerが同じpayloadをFormだけ変えて撃つ | Effect/Augment登録、施設に不要なレシピ/worldgen停止 |
| Immersive Engineering | 工場で液体のEntity/Block別反応と弾の複数ownerを読む | Chemthrower/Railgun API、巨大な機械進行を必要箇所に限定 |
| Occultism | 地区核の準備・継続・中断できる継承儀式 | Ritual lifecycle、不要な召喚/生成/レシピの停止 |
| Mekanism | 工場の時間制限つき汚染源と耐性装備、化学弾/レーザー | radiation/chemical API、汚染の永続化と機械連鎖の制御 |
| Hex Casting | 座標・ベクトルをPlayerの弾道/設置攻撃へ渡す | Action登録、暴走計算と広範囲改変の制限 |
| PneumaticCraft | 工業地区のDroneが別Modのアイテムを使用し、対象で行動を変える | Drone widget/API、圧力進行の導入範囲 |
| Twilight Forest | 外縁のNatureBoltによる一時的な環境変化、Anti-builderの復元室 | 原生BlockEntity実行時参照、構造物/音の複製なし、次元進行の扱い |
| Create | 工業地区のDeployer/Fan/Armが他Mod品を処理し、街の設備を動かす | Behaviour/Recipe/API、過剰な自動生産と自然生成の制御 |
| Botania | 境界のmanaを別Mod攻撃の準備資源に変える | APIと利用条件、コード・アセット複製を避ける経路 |
| The Aether | 外縁のZephyr弾/浮遊Blockを別ownerで使い、原生遠征を案内 | Projectile/BlockEntity、次元追加と不要進行の制御 |
| Ice and Fire | 気候別外縁のbreath/石化/誘引を施設罠とMobに渡す | Citadel互換版の隔離起動、Dragon自然生成と地形破壊の制御 |
| Industrial Foregoing | 工場設備が別ModのMob/loot/液体を処理する | 公開APIと装置の独立性、資源無限化の制御 |
| EvilCraft | 地下の血・魂系資源を別Modの武器更新の選択肢にする | 固定版の公開部品と権利確認、余剰レシピ停止 |
| CC:Tweaked / Integrated Dynamics | 工業施設の観測・条件分岐をPlayerの解法へ変える | peripheral/ネットワークAPI、操作が必須パズルにならない導入 |
| Dungeons Enhanced + Structure Gel | 都市の小塔・迷路・城・寺院を道路と原生施設の接合元にする | 実NBT/入口/寸法、使わないstructure set停止、既確認の隔離起動を再評価 |
| Simply Swords + Integrated Simply Swords | 六圏ごとに別の武器種・横断素材を置き継承の器にする | loot希釈とBetter Combat/Affix/呪文適合を測り、余剰武器loot停止 |
| The Graveyard | 地下の背景墓所・寄り道・任意ボスをIron's墓地と役割分離 | 原生構造参照、自然生成密度と報酬重複の制御 |
| When Dungeons Arise | 都市遠景と外縁の大型ランドマークを少数使う | NBT複製なしの実行時参照、動画条件、自然生成の間引き |
| Integrated Dungeons Arise | 上の大型施設と既存ModのMob・lootを結ぶ寄り道にする | 依存/起動、過密生成と重複lootの停止 |


## 停止手段の順序

1. 固定版Modの設定で、狙う機能だけ止められるか確認。
2. 実在する `data/<namespace>/worldgen/structure_set/<id>.json`、loot table、recipe等を同IDのdatapackまたはKubeJSで個別上書き。空配列を未検証で置かない。
3. Forge eventで特定個体・構造・場所にだけ条件をかける。
4. 上記でできない処理だけ対象メソッドを固定したMixinを検討。現在、採用確定のMixinはない。

外部ModのNBT、テクスチャ、モデルをpackへ複製する前に権利を監査する。可能な場合は公式jar内の登録済みIDとアセットを実行時に参照する。


## 2026-10-13 原生構造set全46件の移管・停止対象

固定版の46setを全件作業化。11件はfrequency=0設定済み、35件は移管/停止未完了。フェラス室の設定は隔離全Mod起動とselftestを確認したが、新規都市接合と全seedの元生成停止は未実測。市外例外はまだ確定していない。必要な部品・戦闘AI・固有素材を残して都市へ集約し、案内/locator/進捗/元物語をパック側へ再構成する。既存建築を消去せず新規生成へ適用。表の都市側用途は実装済みと計画を含むため状態欄と合わせて読む。

水術塔・湿地小屋・地下フェラス室・Apotheosis tower_mainは既存Javaがtemplateを直接参照して配置するため、原生setの自然配置と独立している。Apotheosis別3型は都市wrapperへ登録し、砂型の自然接合だけ確認。Alex小屋templateを選ぶsetの対応、全locatorは未完了。

**46setの外にある生成経路**：フェラス室の地上入口に使う`alexscaves:forlorn_hut_1`は`underground_cabin` setから出ない。`forlorn_hollows` biomeの`forlorn_ruins` featureが小屋7型とidolを選ぶ。小屋0/2/3/5に戦利品marker各1、小屋4/6に各2があり、元featureは原生の樽へ専用LootTableを後付けする。都市で原生templateを参照するときもこの処理を移管し、残りの小屋/像を都市で生かしてからfeatureだけ停止する。8型の参照poolとLoot移管processorを隔離試作し、実配置で元の対象8樽だけにLootが付き、非対象空樽1個が空のままと確認。原生NBTは複製せず参照し、小屋ごとの向きを保つ。小屋0/3/4/5の街路定義を隔離試作し、3と5では通常saltの自然生成→照明付き道路47/32ブロックのauto接合→入口往復/専用Loot→冷保存を確認。最初の別候補は道上限/鉄格子保護で工事を拒否し、小屋0/4でも通常saltの自然auto接合22/38ブロック・入口往復・原生Loot・再preview変更0を確認し、4型の成功例が揃った。コピーの新ビルドcold起動で4型の旧成功応答が完全一致。共通街路選択は最初の候補が保護/距離で失敗した場合に別候補も全保護条件で試す処理へ変更し、既存成功/selftest/箱保護の負例は確認したが、別候補で改善した実例は未確認。小屋2/6の上階扉と原生階段を使う契約6JSONを隔離に追加し検証中。都市の本番採用・idol広場・元feature停止は未実装。`underground_cabin`7型は別施設家族として扱う。

| 元structure set ID | 現在の状態 | 都市側の用途/移管計画 |
|---|---|---|
| `apotheosis:tower_leaf` | 停止設定済み・自然接合未検証 | 都市塔の別外観wrapper |
| `apotheosis:tower_main` | 停止設定済み | 都市街路の射手塔 |
| `apotheosis:tower_sand` | 停止設定済み・都市自然接合確認 | 都市塔の別外観wrapper |
| `apotheosis:tower_spruce` | 停止設定済み・自然接合未検証 | 都市塔の別外観wrapper |
| `bosses_of_mass_destruction:gauntlet_arena` | 移管/停止未完了 | 都市から到達する管理遠征/必要な攻略環境 |
| `bosses_of_mass_destruction:lich_tower` | 移管/停止未完了 | 都市から到達する管理遠征/必要な攻略環境 |
| `bosses_of_mass_destruction:obsidilith_arena` | 移管/停止未完了 | 都市から到達する管理遠征/必要な攻略環境 |
| `bosses_of_mass_destruction:void_blossom` | 移管/停止未完了 | 都市から到達する管理遠征/必要な攻略環境 |
| `cataclysm:acropolis` | 移管/停止未完了 | 都市の地上/地下/工業/水辺または管理遠征 |
| `cataclysm:ancient_factory` | 移管/停止未完了 | 都市の地上/地下/工業/水辺または管理遠征 |
| `cataclysm:burning_arena` | 移管/停止未完了 | 都市の地上/地下/工業/水辺または管理遠征 |
| `cataclysm:cursed_pyramid` | 移管/停止未完了 | 都市の地上/地下/工業/水辺または管理遠征 |
| `cataclysm:frosted_prison` | 移管/停止未完了 | 都市の地上/地下/工業/水辺または管理遠征 |
| `cataclysm:ruined_citadel` | 移管/停止未完了 | 都市の地上/地下/工業/水辺または管理遠征 |
| `cataclysm:soul_black_smith` | 移管/停止未完了 | 都市の地上/地下/工業/水辺または管理遠征 |
| `cataclysm:sunken_city` | 移管/停止未完了 | 都市の地上/地下/工業/水辺または管理遠征 |
| `alexscaves:abyssal_ruins` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:acid_pit` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:cake_cave` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:dino_bowl` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:donut_arch` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:ferrocave` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:forlorn_bridge` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:forlorn_canyon` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:gingerbread_town` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:licowitch_tower` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:ocean_trench` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:soda_bottle` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:underground_cabin` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `alexscaves:volcano` | 移管/停止未完了 | 都市地下/水辺の洞窟施設または都市からの管理遠征 |
| `irons_spellbooks:ancient_battleground` | 移管/停止未完了 | 都市の魔術施設/地下攻略先 |
| `irons_spellbooks:catacombs` | 移管/停止未完了 | 都市の魔術施設/地下攻略先 |
| `irons_spellbooks:citadel` | 移管/停止未完了 | 都市の魔術施設/地下攻略先 |
| `irons_spellbooks:evoker_fort` | 停止設定済み・自然停止未実測 | 独立wrapperの街路施設 |
| `irons_spellbooks:ice_spider_den` | 移管/停止未完了 | 都市の魔術施設/地下攻略先 |
| `irons_spellbooks:impaled_icebreaker` | 移管/停止未完了 | 都市の魔術施設/地下攻略先 |
| `irons_spellbooks:mangrove_hut` | 停止設定追加・都市接合再検証中 | 湿地の街路小屋 |
| `irons_spellbooks:mountain_tower` | 停止設定済み・自然停止未実測 | 独立wrapperの街路施設 |
| `irons_spellbooks:pyromancer_tower` | 停止設定済み・自然停止未実測 | 独立wrapperの街路施設 |
| `mowziesmobs:frostmaw_spawns` | 移管/停止未完了 | 都市周辺の管理戦闘区画/環境対応区画 |
| `mowziesmobs:monasteries` | 停止設定済み・自然停止未実測 | 独立wrapperの街路施設 |
| `mowziesmobs:umvuthana_groves` | 移管/停止未完了 | 都市周辺の管理戦闘区画/環境対応区画 |
| `mowziesmobs:wrought_chambers` | 停止設定済み・新規都市接合未検証 | 都市地下のフェラス室。原生template/ボス/lootは維持 |
| `traveloptics:aqua_mage_tower` | 停止設定追加・都市接合再検証中 | 水辺の水術塔 |
| `traveloptics:echo_shrine` | 移管/停止未完了 | 都市の魔術施設/必要環境への管理遠征 |
| `traveloptics:void_cathedral` | 移管/停止未完了 | 都市の魔術施設/必要環境への管理遠征 |

全件で固定placement/type/biome/生成step、都市側依存、元registry/template/processor/AI/dropの保持、撤回方法を記録。通常seedでの停止・都市遭遇・攻略・素材更新・保存を確認する。必要環境の市外例外はID/理由/都市からの導線/代替/見直し条件を明示する。recipe/loot/spawn/実績/説明本の全件監査は別の残件。


第二波の水術塔/湿地小屋は、全Mod起動と固定Minecraftのfrequency gateで0棄却/1対照採択を確認。中断した検証ワールドでは建築/通路/Lootが存在した一方、固有NPCが0で未受入となり、新規ワールドで再検証している。[K-060](known-issues.html)に記録。既存プレイ/展示ワールドへ停止設定を同期したり建築を消去したりしていない。


### 2026-10-12 第二波の代表受入と普通街区の多様化

水術塔/湿地小屋は新規worldで管理者配置なしの接合が成功、固有敵/NPC・箱・入口/道路と冷再起動を確認。実稼働registryで元6set頻度0・独立都市wrapper4件頻度1を確認した。残る40setと元locator/実績/案内/物語・builtin vanillaや独自生成hookの整理は未完了。

本人採用の普通建築32をLCの建物選択へ追加し、全32登録/代表自然橋の196セルと往復を確認。既存の原生施設とは別枠。さらにGLM最大設定で凝ったMod建材の温室・水処理施設1件を制作中。途中自己集計4Mod/28建材/Mod比率98%は監督前の数値で、新1件の自然採用は未決定。
