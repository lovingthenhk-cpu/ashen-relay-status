# Modと部品の採用表

固定版のModを丸ごと「有効」または「削除」と扱わない。各行で**原生攻略として残すもの、Ashen Relayへ借りるもの、止める/調整するもの**を対応させる。停止欄は計画であり、現在すでに停止したという意味ではない。採用する実行時参照、動画利用、将来配布の条件は別途R-31で再監査する。

## 世界・施設・ボス

| Mod | パック内の仕事 | 借りる具体物 | 残すもの | 停止・調整するもの / 時期 |
|---|---|---|---|---|
| The Lost Cities `7.5.2` | 現世の道路と街区の基盤 | city/road判定、worldstyle、building/part、接合語彙 | 道路と自然な区画 | 見た目を支配している独自 `vocab_*` 12棟と `link_tower` のselector参照をR-27Wで解消。`anchor_02` は主導線から外す。既存worldの建物は消さない |
| Alex's Caves `2.0.2` | 六洞窟の探索、異なる環境素材 | `alexscaves:forlorn_hut_1` 9×9×9、`MAGNETIZING`、`BUBBLED`、`DEEPSIGHT` | 六洞窟、tablet導線、固有武器・drop | 洞窟全体は止めない。外部施設でのEffectは限定区画・短時間だけ |
| Mowzie's Mobs `1.8.2` | フェラスを最初の強敵にする | `mowziesmobs:wroughtnaut_chamber` 19×7×19、`EntityBlockSwapper.swapBlock` | ボスAI、斧・兜、自然拠点 | 接合施設が重複すると実測された場所だけ頻度調整。変換床から梯子・箱・出口を除外 |
| Apotheosis `7.4.8` | 拾った装備のAffix/Socket/Gemで更新動機を作る | `tower_main/leaf/sand/spruce`、Affix/Gem装備 | 原生塔と強化入手 | 射手を変更した場合、その1体だけ元AI/dropの重複を止める。塔やAffix全体は止めない |
| Iron's Spells 'n Spellbooks `3.16.3` | 呪文、巻物、詠唱、装備型呪文、地下と城塞 | `catacombs`、`evoker_fort`、LivingEntity caster | 原生施設、呪文、原生loot | 追加敵/追加lootは指定施設内だけ。Mobやスペル全体の停止なし |
| L_Ender's Cataclysm `3.16` | 大型ボス、工場、海と固有武器 | `ancient_factory`、`sunken_city`、`bone_fracture`、予兆攻撃 | 原生施設・ボス・固有drop | 工場の装置室1室だけに追加遭遇を置き、元装置・保護ブロックを上書きしない |
| Bosses of Mass Destruction `1.1.2` | 寒冷地・地下・Nether・Endの四遠征 | `MagicMissileProjectile` と命中callback、Earthdive Spear素材 | 四施設、ボス、原生drop、通常レシピ | Ashen Relay追加報酬の二重支給のみ一回性状態で防ぐ |
| T.O Magic 'n Extras `6.3.0` | ボス技の呪文化、4系列×3段階の武器、横断合成 | `aqua_mage_tower` / `echo_shrine` / `void_cathedral`、Cataclysm/Alex's素材を使う合成 | 原生施設・武器・通常レシピ | 確認された重複loot/recipeだけ局所調整。都市へ強制移植する施設は寸法と生成条件を確認 |
| Dungeons Enhanced（未導入） | 建築が不足した場合の小型接合元 | `watch_tower` / `ruined_building` 候補 | 採用する施設だけ、原生攻略としての価値を個別判断 | 不要なstructure setを固定jarの実IDごと停止する案。依存、権利、動画、性能のゲート通過前は導入しない |

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

## 未導入候補の扱いも計画に含める

現行の施設で不足が具体的に見つかった場合だけ、部品価値・止める要素・導入負荷・権利・動画条件・検証場所を記録し、隔離試験から判断する。調査棚にはApoliのEntity/Block/Item Action、Ars Nouveauのcaster/設備、Immersive Engineeringの弾薬/液体、Occultismの儀式、Mekanismの放射線/レーザー、Hex Castingの座標操作などがある。**ソースで可能性を見つけた段階であり、導入やR作業は未決定**。現行の不足が確認されない限り、これらを黙って追加する予定はない。

## 停止手段の順序

1. 固定版Modの設定で、狙う機能だけ止められるか確認。
2. 実在する `data/<namespace>/worldgen/structure_set/<id>.json`、loot table、recipe等を同IDのdatapackまたはKubeJSで個別上書き。空配列を未検証で置かない。
3. Forge eventで特定個体・構造・場所にだけ条件をかける。
4. 上記でできない処理だけ対象メソッドを固定したMixinを検討。現在、採用確定のMixinはない。

外部ModのNBT、テクスチャ、モデルをpackへ複製する前に権利を監査する。可能な場合は公式jar内の登録済みIDとアセットを実行時に参照する。
