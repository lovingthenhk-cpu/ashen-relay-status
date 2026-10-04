# 実装ファイルの全計画

**現在のコード**と**新規ファイル案**を分けて記載する。ここに書いた新規案は未実装。Javaは動的な配置・AI・保存状態、Lost Cities JSONは静的な建築語彙、KubeJS/LootJSはloot・recipe、advancementとFTBは進行・案内を担当する。R-28以降の地区・遠征・武器更新・調整・最終検証も[完成工程](completion.html)に全件記載する。

## R-27W1〜W4：現世の街と入口

R-27W1で判明した旧 `WroughtFacilityReservation.java` は非都市のランダム候補を選び、都市と孤立していた。R-27W2で**現世のLost Cities道路縁**へ候補を移し、実歩行面から原生小屋と室へ接続した。3 seedと再起動の機械検証は通過した。R-27W4では独自中継所の新規現世生成を止め、進行用の記録箱を原生小屋の下草位置へ移した。旧worldの小屋も管理者診断で移行でき、プレイヤーが別ブロックを置いた場合は保持する。人が箱を開く操作は未確認。旧 `anchor_02.json` もlive packから外し、新規worldの固定別次元街区生成を停止した。

| ファイル | 既存/案 | 仕事 |
|---|---|---|
| `addon/.../worldgen/WroughtFacilityReservation.java` | R-27W2〜W4実装・機械検証済み | `forlorn_hut_1` と `wroughtnaut_chamber`、梯子・通路・再実行防止を保ち、街路縁候補を安全に受け入れる。原生小屋内の記録箱を配置・保全し、旧worldの下草だけ移行する |
| `addon/.../worldgen/CityFacilityConnector.java` | 新規案 | Lost Citiesの道路端、施設入口、街区・構造の衝突を調べ、配置候補と拒否理由を記録する |
| `addon/.../worldgen/CityPathWeld.java` | 塔向けの新規案 | 小屋への通路は既存classへ実装済み。塔入口と同じ道路を幅2以上の通路で接続し、帰路を検査 |
| `pack/kubejs/data/lostcities/lostcities/worldstyles/standard.json` | R-27W4改修済み | 自作外観style12種と独自中継所の新規現世生成を止める。Lost Cities原生街区は維持する |
| `pack/kubejs/data/ashen_relay/lostcities/predefinedcities/anchor_road_01.json` | R-27W2追加 | 現世のLost Cities原生style、半径160ブロック、強制独自建物0。道路縁の接合元 |
| 旧 `predefinedcities/anchor_02.json` | R-27W4生成停止 | 固定別次元街区は主進行から外れ、旧JSONを非配布の監査fixtureへ移した。旧worldの未生成chunk境界と人の景観は未検証 |
| `pack/kubejs/data/ashen_relay/lostcities/{buildings,parts,citystyles}/...` | 既存選別 | `link_entrance` / `link_hall` 等の接合片は必要に応じて残し、外観代用 `link_tower` と `vocab_*` の参照を段階的に解消 |
| `scripts/r27w2-verify.sh` | R-27W2実装・実行済み | 3 seed、新規現世、自然生成、実ブロックの経路、原生boss、再起動を検査 |
| `scripts/r27w-city-walk.py` | 後続案 | 人の目視を代用せず、塔と地下の二択・衝突と種類数を追加検査 |

**未確定の実装選択**: 固定jarから地上9家族を候補化したが、同じ街で8種類に歩いて届く配置と外観は未検証。3 Mod・8種類の景観がR-28Dで作れなければ都市は未完了。色違い、案内板、街道、独自箱建物は種類に数えない。

## R-27W4：原生structure-startの街道採用

`StreetNativeStructure.java`と`NativeStructureTypes.java`を実装し、隔離fixtureで火術塔の全8部品が管理者配置なしに自然生成されることを確認。元Structureの全pieceを生成段階へ返し、地形への適応・processor・可変地下室を保つ。街道近傍と全piece/都市chunkの非交差を条件にし、元Modの自然施設・lootは維持する。試験用`worldgen/structure/street_pyromancer_tower.json`と対応structure_setはlive packでまだ有効にしない。道路・帰路・保存・衝突・分布を確認してから通常生成へ移す。

## R-27W4：原生Jigsawの全体計画

`NativeStructurePlanner.java`と管理者`structureplan`を追加し、元biomeで火術塔の全8部品と反復一致を確認。`structureparcels`で道路近傍の元biome・全piece/都市chunkの非交差候補を検証済み。広域は11候補、標準範囲は近い1候補。広域scanの停止時間を実測して標準radius24/明示最大96へ分け、自然spawnへ広域scanを組み込まない。`structureplan ... protection`は未ロードなら棄却し、loadedの全pieceで建材・箱・原生構造物・居住時間を保護する。隔離worldだけで保護条件を通した全8部品を管理者配置したが、この管理者配置の時点では自然追加や道路接合は未受入で、後続のfixtureで別に検証した。元Modの生成器から塔・階段・可変地下室の全pieceと占有範囲を取得し、block/entityを配置せずに表示する。元biomeを標準とし、明示的なbiome無視は隔離診断用。`NativeRouteProbe.java`と管理者`routeprobe`を使い、未接続のMob proxyとMCの経路探索で入口候補を調べる。クライアント入力やblock編集は行わず、人の実歩行の代わりにはしない。火術塔本体だけを完成建築へ数えず、保護条件と接合入口を全体で確認してから配置する。

## R-27W4：水辺の出会い方

`AquaTowerConnector.java`は砂浜＋seedで割り当てた川、`MangroveHutConnector.java`は沼＋残りの川を担当する改修を実装。seed424242の自然接合、道路・原生loot/敵、再起動後の重複0、旧world小屋の保全を機械確認。同じ割当で競合を防ぎ、既存施設と保護・地形条件を維持する。物理的な水辺判定と新規小屋の候補判定を分け、旧施設の診断とentity ticketを保つ。8建築の下限の代わりには数えない。

## R-27M：射手の外見と専用AI

| ファイル | 既存/案 | 仕事 |
|---|---|---|
| `addon/.../district/RelayTowerDistrict.java` | R-27M途中実装 | 新規塔seedをCataclysm登録済み `koboleton` EntityTypeへ変更。旧worldのタグ付きスケルトンは読込互換として維持 |
| `addon/.../mob/RelayMarksman.java` | R-27M途中実装 | 原生Hostの近接Goalと骨・古代金属dropを個体限定で止め、予兆弾の専用AIを付与。一回出現と再起動後のGoal再装着をサーバー確認 |
| `addon/.../mob/RelayBoltSentryGoal.java` | 既存再利用 | 30 tick予兆、射線、70–110 tick再装填を新しい外見で維持 |
| `addon/.../projectile/RelayMissileCarrier.java`、`RelayMissileHost.java` | 既存保全 | BOMD弾のownerと命中callback、Cataclysm `bone_fracture` |
| `addon/.../mob/RelayMarksmanEntity.java` と `addon/.../client/RelayMarksmanRenderer.java` | **条件付き新規案** | 固定jarでmodel/rendererを実行時参照できる場合の専用Entity。使えなければ原生Mobホスト案を検証 |
| `pack/kubejs/data/ashen_relay/loot_tables/chests/relay_tower_reward.json` | 既存監査 | 原生塔lootとAffix/Gem/空印が重複せず届くか確認 |

原生モデルとrendererは実行時参照し、コピーしない。固定版クライアントはリソースロードまでログ確認済みだが、専用Goalの30tick射撃、最終tickの標的喪失による中断、再装填、重複発射防止、原生Hostでの塔報酬をサーバーselftestで確認した。モデルの実表示、塔内の当たり判定、実戦と死亡から進捗までの経路は未検証。R-27Mは未完了。

## R-27E1〜E3：異なる環境遭遇

| ファイル | 既存/案 | 仕事 |
|---|---|---|
| `addon/.../zone/CatacombFloorCycle.java` | 新規案 | Mowzie's `EntityBlockSwapper.swapBlock` で墓地一室の床を一時変化・復元。入口、箱、梯子は保護 |
| `addon/.../zone/FactoryMagnetCycle.java` | 新規案 | Alex's `MAGNETIZING` を工場一室の短い周期に限定。常時安全な帯を残す |
| `addon/.../zone/FlameZoneHost.java`、`FlameZonePayload.java` | 既存調整 | 工場の既存予兆装置と磁力・足場の順序を組む |
| `addon/.../district/RelayDistrictPlacement.java`、`RelayFactoryDistrict.java` | 既存改修 | 実在するcatacombs/factoryのstructure start内だけ追加遭遇を起動 |
| `addon/.../zone/SeamEncounter.java` | 新規案、R-27Aで統合 | 地区境界の任意起動、床→弾の順、退路・再挑戦・一回報酬 |

2種類が実際に異なる対処を要求し、保護ブロックや入口が壊れず、再入場・再起動で床が戻ることを専用サーバーで検査する。

## R-27A/B：loot、進行、合成、案内

| ファイル | 既存/案 | 仕事 |
|---|---|---|
| `pack/kubejs/server_scripts/ashen_relay_loot.js` | 既存改修 | 墓地の巻物、工場の重量素材、水辺の水・雷素材を元dropに追加。構造/テーブル限定 |
| `pack/kubejs/data/ashen_relay/loot_tables/chests/relay_district_reward.json`、`relay_factory_reward.json`、`relay_tower_reward.json` | 既存改修 | 場所ごとの個数・傾向と一回性を調整 |
| `pack/kubejs/data/ashen_relay/loot_tables/chests/seam_reward.json` | 新規案 | 地区境界の選択報酬。元の箱は消さない |
| `pack/kubejs/data/ashen_relay/advancements/progress/reach_*.json` | 既存改修 | 実施設到着→記録→FTB表示の依存を固定別次元から現世へ移す |
| `pack/config/ftbquests/quests/chapters/ashen_relay.snbt` | 既存改修 | 入口、危険、報酬の用途、次の候補を段階表示 |
| `pack/kubejs/server_scripts/ashen_relay_recipes.js` | 既存監査・改修 | T.O段階武器、Alex's/Cataclysm素材、BOMD槍、継承印の合成経路と重複を確認 |
| `addon/.../item/ImprintItem.java`、`ledger/RelayWeaponLedger.java` | 既存保全 | Affix/Gem/装備型呪文の移設、部分適用、素材の消失・増殖防止 |

## R-28以降の編集面

| unit | 主な既存ファイル/新規案 | プレイヤーへ届く内容 |
|---|---|---|
| R-28A〜D | `pack/kubejs/data/ashen_relay/lostcities/{citystyles,buildings,parts}/*.json`、`worldstyles/standard.json`、`CityFacilityConnector.java`、`CityPathWeld.java`、`RelayDistrictPlacement.java`、`RelayFactoryDistrict.java`、`RelayFortDistrict.java` | 四地区で外部建築、徒歩の入口・帰路、異なる遭遇と報酬を一組ずつ増やす |
| R-29A〜C | `ashen_relay_recipes.js`、`ashen_relay_loot.js`、`advancements/progress/reach_*.json`、`ashen_relay.snbt`、施設ごとの新規案 `route_*.json` | T.O施設、洞窟・海、自然拠点・BOMD遠征を街での装備更新へつなぐ |
| R-30A〜C | `ashen_relay_loot.js`、`ashen_relay_recipes.js`、`ImprintItem.java`、`EchoRefiningItem.java`、`RelayWeaponLedger.java`、九ボス用loot JSON | 序盤・中盤・後半の別武器更新と継承費用を成立させる |
| R-31A/B | `SealedRecordItem.java`、`ashen_relay.snbt`、`advancements/progress/*.json`、ja/en lang | 発見後の記録、複数の次の候補、死亡や再ログインからの復帰を案内 |
| R-32A/B | loot/recipe/config調整、計測scriptと報告 | 場所ごとの戦術、TTK、被ダメージ、報酬密度の調整と再測定 |
| R-33A/B | 生成標本script、非idle 90分負荷script、`docs/TESTING.md` | 生成・衝突・性能・再起動の保全 |
| R-34/35/36 | build/audit/backup script、`RELEASE_MANIFEST.md`、`docs/COMPLETION.md`、権利監査、引き継ぎ | 最終treeの技術・権利・原要求を判定。R-36は期限ではなく判定点 |

R-27Sでは通常進行とは独立した条件付き追加経路の状態、排他、一回報酬、再取得、再起動、管理者の反転を実装する。物語の成立条件や結末はここに載せない。第一波30 unitと第二波R-37〜44の成果物と受入は[完成工程](completion.html)に載せる。

## R-37〜44の実装面と採用試験

| 作業群 | 新規ファイル/編集面の案 | 受入する操作 |
|---|---|---|
| R-37 | `CityFacilityConnector.java`、`CityPathWeld.java`、`lostcities/{buildings,parts,citystyles}/*.json`、施設別入口データ | 六圏から各施設へ歩いて入り帰還する |
| R-38 | Host別Goal/Projectile/Zone adapter、`seam_*.json`、selftest | 五空間×五縫合を別Hostでも読み解く |
| R-39 | `BossTechnique*.java`、`ashen_relay_loot.js`、`ashen_relay_recipes.js`、施設別chest/advancement JSON | ボス技を獲得し別圏の武器へ継承する |
| R-40 | `ApoliActionAdapter.java`、`ArsCasterAdapter.java`、`IndustrialPayloadAdapter.java`、`RitualBridge.java`、該当ModのAction/recipe/structure JSON | Player・Mob・設備で同じpayloadを使う |
| R-41 | `FactoryHazardAdapter.java`、`CoordinatePayload.java`、`DroneTargetAdapter.java`、機械別recipe/tag JSON | 汚染・計算弾・Drone・装置を工場で使い分ける |
| R-42 | `OuterExpeditionAdapter.java`、原生Entity/BlockEntity参照、外縁のloot/route JSON | 自然弾・復元室・元素攻撃・資源を外縁攻略へ接続する |
| R-43 | 各候補Modの固定jar NBT/structure set/lootを棚卸しし、採用分だけ`lostcities`とlootへ接続 | 建築種類と武器種を増やし、街路と報酬に意味を持たせる |
| R-44 | `IDEA_INCLUSION_LEDGER.md`相当の公開台帳、生成/保存/権利/遊びの証拠 | 旧案の全件に実装・検証・除外理由を付ける |

表のクラス名は作業の責務を示す**新規案**。固定版APIを確認して実名を決める。各Modの用途と停止対象は[旧案の採用台帳](ideas.html)に全件掲載。

R-40A〜D、R-41A〜E、R-42A〜F、R-43A〜Eの**20行それぞれ**の作業面と施設受入は[次の作業と実装受入](delivery.html)に掲載。隔離試作後に施設の入口・遭遇・報酬へ繋げる。


### 原生建築の共通接合基盤（R-27W4、途中）

`NativeStreetProfile.java`が`data/<namespace>/native_street_profiles/<structure>.json`から元template、入口座標・向き、改変を許すgateway範囲を読み、`NativeStreetConnector.java`が保存された原生全pieceと街道・保護条件を照合する。`NativeStreetRoadPlanner.java`は幅3の道路と高低差・gatewayの全書込を事前計画する。元gatewayの状態は元ModのNBTを実行時に参照し、assetを複製しない。管理者`streetweld <structure>`は計画表示のみ、明示`apply`だけ試験worldへ編集する。最初のJSONは火術塔の隔離fixtureのみで、通常worldの自動配置は未有効。全回転、既存world境界、施設間予約、支柱・外観、再起動後の再実行と往復経路の検証を進める。元の地下室・敵・lootを共通化のために削らない。既存4施設を一括置換せず、新規方式を受け入れてから必要な部分を統合する。


接合作業は`ashen-relay-structure-seams` skillへ手順化した。原生施設全体の調査→入口契約→共通道路preflight→保護負例→往復→再実行・再起動を同じ基準で回す。skill登録は施設の実装完了を意味しない。外観・実歩行の未検証を残し、元の部屋やlootを縮小しない。


反復検査scriptは計画表示→明示接合→道路/入口の往復proxy→再適用で変更0を一括検査し、試験結果を保存する。原生RuleProcessorの位置付き変換を再現して誤棄却を減らす。敵/lootへ作用するprocessorを計画表示で再実行しない。保護負例、clean restart、全回転と人の外観/実歩行は別に受け入れる。


火術塔の西向きfixtureで共通接合を初回機械確認した。通行頭上へ置いた保護ブロックは書込0で拒否。原生の全8部品を残した接合後、街道と入口外の往復proxyは到達、再実行の変更は0。入口の内側までの往復proxyと原生loot2個の保持、全体selftestも通過。clean restart後も全8部品・原生loot・戸口内外と街道の経路が残り、再実行の変更0を確認。全回転・自動接合・旧world境界・施設間予約・支柱と人の外観/実歩行は未受入。通常worldにはまだ生成しない。


## 原生建築の残りと個別実装（2026-10-04）

地上の接合候補は9家族、通常導入済みはAlex小屋・Apotheosis塔・Iron’s湿地小屋・T.O水術塔の4家族。残る5家族は下表。地下のフェラス室・墓地・工場・地下祠は別に数え、見た目8種類の受入を地下室や色違いで満たさない。未導入Dungeons Enhancedの監視塔・廃屋も追加候補。この台帳を開発範囲の上限としない。

| 施設 | 個別に実装・確認すること |
|---|---|
| Iron’s火術塔 | 全Jigsaw・地下室・分岐を保持。入口JSON、四回転の経路、自動接合と保存を受け入れる |
| Iron’s城塞 | 正門と大型敷地の全piece調査、道路進入路、建築間の予約と衝突保護 |
| Iron’s山岳塔 | 高所入口と山の高低差、内部梯子の経路。平地へ置き長階段だけを足す方式は既定にしない |
| Mowzie寺院 | 独自生成器と全体入口に対応するadapter。敷地、原生戦闘と周囲の保護 |
| Cataclysmピラミッド | 独自生成器の全体/入口、砂漠条件、大型敷地と原生内部経路を保持 |
| Iron’s墓地・Cataclysm工場 | 地表入口/縦坑adapter、原生部屋/装置保護、局所の復元床・磁力など既存企画の遭遇 |
| T.O地下祠 | 原生Deep Darkを維持し、都市からの遠征案内と帰還先を接続 |

接合skillは調査・実装・検証の手順を再利用する。施設の入口実測、特殊移動、生成adapter、原生敵/装置/loot、施設固有の戦闘・報酬・次の用途、人の外観/歩行受入は施設ごとに残る。

火術塔の隔離試験では西・北・東・南の全8pieceと街道↔入口外の経路proxyが通過。北/東は再起動後も往復、戸口、loot2個、再接合変更0を確認。南の再起動後20cellsは自然砂利の天井落下が原因だった。安定木材の天井で支える修正後、新規worldで管理者applyなしの798cells自動接合、読み取り専用の往復114/115nodes・変更0、再起動後も変更0・戸口・原生loot保持を確認した。外観・人の実歩行は全方向未受入。

`NativeStreetJobs.java`を実装し、隔離試験で保留→保存/再起動→ロード後自動完了→完了保存を確認した。入口profileの`automatic:true`、新規chunk来歴、全piece/道路ロード待ち、一秒一件の処理、SavedDataによる保留/完了/棄却を担当する。旧施設読込から工事を始めず、自動道路は新規来歴のあるchunkだけを使う。先に生成・保存した旧道路へ新規塔が接合しようとする負例は変更0で拒否し、再起動後も棄却状態を保持。未訪問のchunkは任意の期限で永久棄却せず、古いdue順に処理する。自然砂利/砂の天井直下は木材で支え、落下による通路閉塞を防ぐ。`streetjobs`は管理者の状態診断。通常packへ火術塔の定義はまだ導入していない。施設間の全body予約、支柱・造形、複数seed分布と人の受入は引き続き残る。


### 本体の生成前予約（実装・隔離検証中）

旧い密な火術塔の試験では、隣の塔本体と地下部品の箱が3組交差していた。`NativeStreetReservations.java`を追加し、同wrapper群の近隣random-spread候補を全pieceとseed/頻度/exclusionで比較する。structure IDとanchor座標の固定優先順で交差する低優先候補を生成前に拒否し、ロード順へ依存しない。`StreetNativeStructure`の`reservation_radius`は全pieceを包む契約で、部屋を切り捨てる上限ではない。現在はbuild通過・同じ密な条件の新規worldで検証中。通常pack未導入。他Mod原生本体、旧FULL境界、優先候補の連鎖棄却が分布へ与える影響は残る。保存データ監査はpiece箱の交差とFULL不足を示す補助で、実block/外観の合格とはしない。


本体予約の密な再現試験では、残した火術塔が原生8部品・道路往復81/82nodes・lootを保持し、低優先の隣接候補は生成前に拒否された。保存全pieceの箱交差0、再起動後も経路・変更0を確認。元Modの同座標計画は全11部品で有効なので、部屋の縮小で回避した結果ではない。

通常生成の原生施設を守るため、wrapper JSONのavoid_structuresへ実IDと全pieceの範囲を指定する対応も追加・build通過。登録済み原生typeの元placement/頻度/exclusion/biome/全部品を計画し、重なるwrapper候補を避ける。元Modの自然生成/lootを止めない。現在は原生火術塔を隣接させた隔離試験中で、全他Modを対応済みとはしない。未監査の独自生成器は計画の副作用や範囲も個別確認する。


旧chunk境界には`NativeFullChunkGuard.java`を追加・build通過。新しい施設の全pieceと地形調整の周囲を、完成chunkへまたがらないよう生成前に検査する。完成座標と保存NBTのStatusを使い、未ロードchunkを強制生成しない。読取失敗も拒否する。管理者fullchunkplanはpiece数と拒否理由を読み取りで確認する診断で、既存施設を再配置する機能ではない。隔離試験では新規地形に接合塔8部品と離れた原生塔9部品が自然生成し、両者のloot・保存・再起動後の経路と変更0を確認。未ロードの保存済みFULLと読込済みFULLは、元の8部品計画を保持したまま新規候補を拒否し、保護ブロックも保持。原生を近づけた負例では原生11部品を残し、接合塔を避けた。全他Mod・複数seed・人の外観をこれだけで合格にしない。
