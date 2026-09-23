# 実装ファイルの全計画

**現在のコード**と**新規ファイル案**を分けて記載する。ここに書いた新規案は未実装。Javaは動的な配置・AI・保存状態、Lost Cities JSONは静的な建築語彙、KubeJS/LootJSはloot・recipe、advancementとFTBは進行・案内を担当する。R-27後の調整・最終検証も[完成工程](completion.html)に全件記載する。

## R-27W：現世の街と入口

現在の `WroughtFacilityReservation.java` は `PostGenOutsideChunkEvent` から小屋と室を置くが、対象2×2を**すべて非都市chunk**に限定する。64×64 chunk領域に候補1件なので、都市と孤立する。旧 `anchor_02.json` は `lostcities:lostcity` 次元の固定座標で、現世の施設を追跡できない。

| ファイル | 既存/案 | 仕事 |
|---|---|---|
| `addon/.../worldgen/WroughtFacilityReservation.java` | 既存改修 | `forlorn_hut_1` と `wroughtnaut_chamber`、梯子・通路・再実行防止を保ち、街路縁候補を安全に受け入れる |
| `addon/.../worldgen/CityFacilityConnector.java` | 新規案 | Lost Citiesの道路端、施設入口、街区・構造の衝突を調べ、配置候補と拒否理由を記録する |
| `addon/.../worldgen/CityPathWeld.java` | 新規案 | 道路端と小屋/塔入口を幅2以上の歩ける通路で接続。段差・照明・帰路・保護ブロックを検査 |
| `pack/kubejs/data/lostcities/lostcities/worldstyles/standard.json` | 既存改修 | 都市に出す建物の参照を更新し、外観用 `vocab_*` の主役化を止める |
| `pack/kubejs/data/ashen_relay/lostcities/predefinedcities/anchor_02.json` | 既存見直し | 固定別次元街区を主進行から外す。既存worldとadvancement参照を確認後に生成停止を判断 |
| `pack/kubejs/data/ashen_relay/lostcities/{buildings,parts,citystyles}/...` | 既存選別 | `link_entrance` / `link_hall` 等の接合片は必要に応じて残し、外観代用 `link_tower` と `vocab_*` の参照を段階的に解消 |
| `scripts/r27w-city-walk.py` | 新規案 | 3 seed、新規現世、道→入口→戦闘室→帰路、再起動後の同一性、衝突と種類数を検査 |

**未確定の実装選択**: 外部建築8種類の候補IDと実寸。固定jarを棚卸しして決める。3 Mod・8種類の景観が作れなければR-27Wは未完了。色違い、案内板、街道、独自箱建物は種類に数えない。

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

## R-27E：異なる二つの環境遭遇

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

## R-27S以降の実装・検証

R-27Sでは通常進行とは独立した条件付き追加経路の状態、排他、一回報酬、再取得、再起動、管理者の反転を実装する。物語の成立条件や結末はここに載せない。R-28は戦術・報酬密度・数値調整、R-29は世界生成と90分試験、R-30はビルド・起動・保存の最終マトリクス、R-31は原要求と権利の監査、R-33は完成判定。どれも省略可能な後片付けではない。全unitの成果物と受入は[完成工程](completion.html)に載せる。
