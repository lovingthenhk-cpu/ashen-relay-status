# 実装ファイルの全計画

**現在のコード**と**新規ファイル案**を分けて記載する。ここに書いた新規案は未実装。Javaは動的な配置・AI・保存状態、Lost Cities JSONは静的な建築語彙、KubeJS/LootJSはloot・recipe、advancementとFTBは進行・案内を担当する。R-28以降の地区・遠征・武器更新・調整・最終検証も[完成工程](completion.html)に全件記載する。

## R-27W1〜W4：現世の街と入口

R-27W1で判明した旧 `WroughtFacilityReservation.java` は非都市のランダム候補を選び、都市と孤立していた。R-27W2で**現世のLost Cities道路縁**へ候補を移し、実歩行面から原生小屋と室へ接続した。3 seedと再起動の機械検証は通過した。旧 `anchor_02.json` は `lostcities:lostcity` 次元の固定座標で、現世の施設を追跡できない。

| ファイル | 既存/案 | 仕事 |
|---|---|---|
| `addon/.../worldgen/WroughtFacilityReservation.java` | R-27W2実装・機械検証済み | `forlorn_hut_1` と `wroughtnaut_chamber`、梯子・通路・再実行防止を保ち、街路縁候補を安全に受け入れる |
| `addon/.../worldgen/CityFacilityConnector.java` | 新規案 | Lost Citiesの道路端、施設入口、街区・構造の衝突を調べ、配置候補と拒否理由を記録する |
| `addon/.../worldgen/CityPathWeld.java` | 塔向けの新規案 | 小屋への通路は既存classへ実装済み。塔入口と同じ道路を幅2以上の通路で接続し、帰路を検査 |
| `pack/kubejs/data/lostcities/lostcities/worldstyles/standard.json` | 既存改修 | 都市に出す建物の参照を更新し、外観用 `vocab_*` の主役化を止める |
| `pack/kubejs/data/ashen_relay/lostcities/predefinedcities/anchor_road_01.json` | R-27W2追加 | 現世のLost Cities原生style、半径160ブロック、強制独自建物0。道路縁の接合元 |
| `pack/kubejs/data/ashen_relay/lostcities/predefinedcities/anchor_02.json` | 既存見直し | 固定別次元街区を主進行から外す。既存worldとadvancement参照を確認後に生成停止を判断 |
| `pack/kubejs/data/ashen_relay/lostcities/{buildings,parts,citystyles}/...` | 既存選別 | `link_entrance` / `link_hall` 等の接合片は必要に応じて残し、外観代用 `link_tower` と `vocab_*` の参照を段階的に解消 |
| `scripts/r27w2-verify.sh` | R-27W2実装・実行済み | 3 seed、新規現世、自然生成、実ブロックの経路、原生boss、再起動を検査 |
| `scripts/r27w-city-walk.py` | 後続案 | 人の目視を代用せず、塔と地下の二択・衝突と種類数を追加検査 |

**未確定の実装選択**: 固定jarから地上9家族を候補化したが、同じ街で8種類に歩いて届く配置と外観は未検証。3 Mod・8種類の景観がR-28Dで作れなければ都市は未完了。色違い、案内板、街道、独自箱建物は種類に数えない。

## R-27M：射手の外見と専用AI

| ファイル | 既存/案 | 仕事 |
|---|---|---|
| `addon/.../district/RelayTowerDistrict.java` | 既存改修 | `EntityType.SKELETON` を置く現行seedを専用射手へ移す |
| `addon/.../mob/RelayMarksman.java` | 既存改修 | 名前付きスケルトンの経路をなくし、専用AIの付与と一回出現を管理 |
| `addon/.../mob/RelayBoltSentryGoal.java` | 既存再利用 | 30 tick予兆、射線、70–110 tick再装填を新しい外見で維持 |
| `addon/.../projectile/RelayMissileCarrier.java`、`RelayMissileHost.java` | 既存保全 | BOMD弾のownerと命中callback、Cataclysm `bone_fracture` |
| `addon/.../mob/RelayMarksmanEntity.java` と `addon/.../client/RelayMarksmanRenderer.java` | **条件付き新規案** | 固定jarでmodel/rendererを実行時参照できる場合の専用Entity。使えなければ原生Mobホスト案を検証 |
| `pack/kubejs/data/ashen_relay/loot_tables/chests/relay_tower_reward.json` | 既存監査 | 原生塔lootとAffix/Gem/空印が重複せず届くか確認 |

モデルの直接コピーは決定していない。候補のEntityType、renderer公開範囲、AI差し替え、安全なhitbox、動画利用を調べてホストを決める。候補が決まらなければR-27Mは未完了。

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
