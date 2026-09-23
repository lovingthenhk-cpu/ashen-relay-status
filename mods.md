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
