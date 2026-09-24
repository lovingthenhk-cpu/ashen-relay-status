# Mod要素単位の縫合パターン台帳

更新日: 2026-09-25。**場所と操作まで定義した縫合は現時点で58パターン**。内訳は現行packの部品を組む **C01〜C35の35件**（道路経路の機械確認1、部品・一部ループ稼働17、計画17）と、未導入Modの **X01〜X20という20作業パッケージ内の23操作**（全件隔離試験待ち）。前版の42件は作業パッケージを数え、既存のR-01〜R-22の縫合7件を落とし、X03/X12/X13内の別操作を一件にまとめていた。58は完成数でも上限でもなく、旧資料にある未割当候補は末尾で追う。R-27W3は後続の継続指示で着手済み。街道から塔への道は実装したが、額縁の初回表示と3 seed安定生成は未受入。

照合元は `MODPACK_CONTENT_BLUEPRINT.md` の施設別の混ぜ方、`EXPANDED_GAME_VISION.md` の六圏・五縫合、`IDEA_DELIVERY_CONTRACT.md` のW/P/U/X行、`IDEA_INCLUSION_LEDGER.md` のネガティブリスト。実装証拠は `TESTING.md` と `reports/compat/` を正本とする。

## 数え方と状態

一件は「部品A × 部品B → 特定の場所でプレイヤーに生じる操作」が異なる縫合レシピ。同じ塔の色違い、同じ弾の属性違い、同じ仕組みを別seedへ置いたものは増やさない。Lost Citiesの道路とMod建築の接合、戦闘payloadと別Modのcarrier、報酬と別Modの装備更新も、プレイヤーの操作が異なれば数える。`W01〜W06`、`S01〜S05`、`G01〜G05` は圏・空間・方法の分類であり、58件に重複加算しない。X03a/b、X12a/b、X13a/bは元のX IDの枝であり、`IDEA_DELIVERY_CONTRACT.md` の20作業単位を増やした意味ではない。

状態は **機械確認**＝現行packで実ブロック/専用server等の該当接続を確認、**一部稼働**＝構成部品や片側はあるが施設内の一連の遊びは未受入、**計画**＝現行packの部品で実装予定、**隔離試験待ち**＝未導入Modの版・互換・権利・停止方法を含む候補。人の外観・操作感を機械確認に含めない。C01も外観と実player歩行は未検証。

## A. 現行packの部品で作る35パターン

| ID | 部品同士の縫合と場所 | プレイヤーがすること・次の用途 | 状態 / 受入R |
|---|---|---|---|
| C01 | Lost Cities現世道路 × Alex's `forlorn_hut_1` × Mowzie's `wroughtnaut_chamber` | 道から小屋の梯子を降り、フェラス室へ行って同じ道へ戻る。原生dropを次の武器候補にする | **機械確認**：R-27W2。外観・実歩行は未検証 |
| C02 | Lost Cities街路 × Apotheosis原生塔 | 地下との二択として道から塔へ登り、Affix/Gemを持ち帰る | **実装中**：R-27W3。道路経路と原生lootは接合済み。額縁の初回表示と3 seed安定生成は未受入 |
| C03 | 塔の射手AI × BOMD `MagicMissileProjectile` × Cataclysm `Bone Fracture` | 予兆を見て遮蔽物へ移り、弾の命中効果を読む | **一部稼働**：弾とAIは既存、実施設・外見はR-27M/R-28D |
| C04 | Cataclysm由来の外見候補 × 塔専用射手AI | 名前付きvanilla skeletonから脱し、外見と攻撃の予兆を一致させる | **計画**：R-27M。モデル/rendererと権利を確認 |
| C05 | Iron's `catacombs` × Mowzie's `EntityBlockSwapper` | 一室で床が一時変わる予兆を見て安全帯へ移り、復元後に進む | **計画**：R-27E1/R-37B。入口・箱は保護 |
| C06 | Iron's `catacombs` × Cataclysmの設置予兆攻撃 | 墓地の別室で床変化とは違うタイミングの攻撃を避ける | **一部稼働**：元施設・攻撃部品あり、実施設受入はR-28A |
| C07 | Cataclysm `ancient_factory` × Alex's磁力Effect/BlockEntity | 工場の設備周期で引かれる向きを読み、安全帯へ動く | **計画**：R-27E2/R-28B |
| C08 | Cataclysm工場 × Mowzie's復元床 | 原生装置を避けつつ一時的な足場を渡り、復元後も退路を失わない | **計画**：R-27E2/R-28B |
| C09 | Iron's `evoker_fort` × Ashen Relay `relay_step` × Pehkui縮小 | 門・狭路で敵の移動と短時間のサイズ変化に対処する | **一部稼働**：敵の移動あり、縮小との複合はR-27E3/R-28C |
| C10 | 都市の二地区境界 × Mowzie's一時床 × BOMD/塔の予兆弾 | 学んだ二規則を順番に越え、任意の一回報酬を選ぶ | **計画**：R-27E3/R-27A/R-39E |
| C11 | Lost Cities魔術地区 × Iron's巻物loot | 建物と観測票から巻物を探す地区を選び、次の呪文武器へ使う | **計画**：R-27A/R-28A |
| C12 | Lost Cities工業地区 × Cataclysm工場素材/重量装備loot | 工業区で重い武器の素材を狙い、城塞や洞窟用へ更新する | **計画**：R-27A/R-28B |
| C13 | Lost Citiesの浸水街路 × Cataclysm `sunken_city` × Alex's水中Effect | 街の水位を手掛かりに海へ向かい、水中能力で探索・帰還する | **計画**：R-29B/R-37E。原生海生成は維持 |
| C14 | Alex's六洞窟の素材 × T.O段階武器 | 都市の装備で洞窟へ行き、素材を持ち帰って別の武器種へ更新する | **一部稼働**：素材/合成は既存、案内と往復はR-29B/R-30B |
| C15 | Cataclysm工場・海の素材 × T.O段階武器 | 地下/海の原生攻略を剣・拳・機械刃・トライデント系列の更新へ結ぶ | **一部稼働**：横断レシピあり、施設別の入手順はR-29/R-30B |
| C16 | Mowzie's屋外原生拠点 × Cataclysm設置攻撃 | 地下より広い視界で予兆を読み、遮蔽物の使い方を変える | **計画**：R-29C/R-37F。原生Mob戦を保持 |
| C17 | Apotheosis Affix/Gem × Ashen Relay継承印 × T.O武器 | 塔で拾った強化を新しい器へ部分的に移し、地下や工場で試す | **一部稼働**：継承機構あり、施設別更新はR-30A/B |
| C18 | Iron's装備型呪文 × Ashen Relay継承印 × 別Mod武器 | 墓地の呪文付き装備から互換分を移し、不適合分は印に残す | **一部稼働**：部分適用あり、施設報酬の調整はR-30A/B |
| C19 | BOMD `Earthdive Spear` × Ashen Relay継承印/台帳 | 任意遠征で得た槍を次の器と比較し、旧武器への投資を移す | **一部稼働**：槍・継承あり、遠征からの導線はR-29C/R-30C |
| C20 | Mowzie's/Cataclysm固有武器の重複品 × 残響精錬 × 継承素材 | 二個目以降の戦利品を残響片にし、新しい武器へ投資を回す | **一部稼働**：精錬機構あり、複数圏の実報酬はR-30C/R-39A |
| C21 | 複数Modの異なる武器種 × Ashen Relay武器記録台帳 | 一度使った武器種を記録し、次の器や継承先を選ぶ | **一部稼働**：台帳あり、六圏での選択はR-30/R-39B |
| C22 | BOMD等の未収録ボス行動 × Player用スペル/道具 × 原生drop | 敵の技を観測後、短いPlayer用能力として別の施設で使う | **計画**：R-39D。T.O既存スペルとの重複は作らない |
| C23 | Iron's `relay_flame_strike` × Cataclysm `Flame_Strike_Entity` | 墓地で見た予兆攻撃を呪文として得て、別の施設で指定地点へ置く | **一部稼働**：R-02/R-07。spell実装・試験済み、施設横断の体験は未受入 |
| C24 | タグ付きMob Goal × Cataclysm Flame Strike、Iron's墓地 | Mobの予兆を見て安全帯へ動き、後にC23のPlayer呪文と比較する | **一部稼働**：R-01/R-14。Goal実装・試験済み、外観/実歩行は未受入 |
| C25 | Cataclysm `ancient_factory` × Ashen Relay Zone Host × Cataclysm Flame Strike | 無人の装置が同じ攻撃を周期発火する。敵の技と違い安全帯を読む | **一部稼働**：R-03/R-18C。zone/工場配置は実装、実player体験は未受入 |
| C26 | Iron's `relay_bone_bolt` × BOMD Magic Missile × Cataclysm Bone Fracture | 塔で受けた弾をPlayerが別施設で撃ち、ownerと効果を使い分ける | **一部稼働**：R-06/R-07。spell/弾は試験済み、獲得後の往復は未受入 |
| C27 | Iron's `relay_shrink` × Pehkui BASE scale | 短時間だけ自分のサイズを変え、城塞の狭路を別ルートで通る | **一部稼働**：R-05。spell実装・試験済み、城塞の実ルートは未受入 |
| C28 | Iron's `relay_step` のPlayer版 × 城塞の敵側Goal | 自分が使った短距離移動を敵も予兆つきで使うため、着地点を読む | **一部稼働**：R-19D。enemy mirror実装・専用server試験済み、実player操作は未受入 |
| C29 | 異なる2地区の攻略記録 × Ashen Relay連鎖state × Apo/Iron's強化継承 | 攻略順を選び、両地区後に旧武器のAffix/Gem/装備呪文を移す | **一部稼働**：R-22A/B。状態/永続のproxy受入済み、実player操作は未受入 |
| C30 | BOMD Magic Missile命中 × Mowzie's BlockSwapper、都市境界 | 命中地点に一時床を作り、弾を避けるだけでなく足場を読み直す | **計画**：R-38G/R-39E。owner・復元・保護blockを隔離試験 |
| C31 | BOMD Magic Missile命中 × Cataclysm Flame Strike、塔の上層 | 弾の着弾予兆の後に遅れて床攻撃が来るため、二段階で移動する | **計画**：R-38G。遅延、miss cleanup、元塔lootを保護 |
| C32 | Mowzie's Sunstrike × 日光で起動する都市外縁設備 | 設備の照射予兆を見て遮蔽物に入る。夜は別の通路を選べる | **計画**：R-37F/R-38H。固定版B候補、設備と原生Mob戦を分離 |
| C33 | Alex's MAGNETIZING Effect × 工場の武装Mob | 敵の装備に引かれる方向を見て退路を選び、C07の固定設備と比較する | **計画**：R-37C/R-38F。Effectの対象・同期を隔離試験 |
| C34 | Pehkui BASE scale × Projectile命中、城塞の狭路 | 被弾による短時間縮小を利用または回避し、終了後に元サイズへ戻る | **計画**：R-38G。EX-06は四Host実証、実施設と復帰は未検証 |
| C35 | BOMD RiftBurst × Mowzie's BlockSwapper、外縁の屋外戦 | 裂け目の遅延予兆を見て、短時間だけ変わる地面から退避する | **計画**：R-37F/R-38G。固定版B候補、原生屋外戦を保持 |

### C23〜C35で借りるものと止める範囲

| ID | 借りる部品・実装入口 | 残す原生要素 | 抑える範囲と受入 |
|---|---|---|---|
| C23 | Iron's caster、Cataclysm Flame Strike、`RelayFlameStrikeSpell` | Iron'sのmana/cooldownとCataclysm原生ボス | 呪文の一回発火、ボス攻撃との差、施設別入手を確認。元ボスAIを変更しない |
| C24 | Cataclysm Flame Strike、`FlameboundSentinel` のタグ限定Goal | 墓地の原生室と元Mobの通常戦 | タグ対象以外へGoalを広げず、元dropを置換しない |
| C25 | Cataclysm Flame Strike、`FlameZoneHost` の保存付きZone | 工場の原生装置・ボスdrop | Zoneは限定室だけ。原生装置、入口、安全帯への重ね置きを拒否 |
| C26 | Iron's caster、BOMD弾、Cataclysm効果、`RelayBoneBoltSpell` | BOMD原生遠征、弾の外見、Iron's詠唱資源 | owner消失・dimension変更・missで弾を消し、追加報酬の二重支給を防ぐ |
| C27 | Iron's caster、Pehkui BASE scale、`RelayShrinkSpell` | Iron's原生呪文体系とPehkuiの通常サイズ | 恒久縮小を避け、死亡/再ログイン/狭路復帰で元サイズを確認 |
| C28 | `RelayStepPayload` と `RelayEchoHunter` の個体限定Goal | 城塞原生MobとPlayer用 `relay_step` | 特殊個体以外へ移動Goalを広げず、壁内着地を拒否 |
| C29 | 二地区の攻略記録、`RelayChainSuture`、`ImprintItem` | Apo Affix/GemとIron's装備型呪文の本来の入手 | 継承解禁はプレイヤー別・一回。再ログイン、逆順攻略、不正受取を検査 |
| C30 | BOMD命中callback、Mowzie's `EntityBlockSwapper` | 両Modの原生弾/床能力 | 箱・梯子・入口を変換せず、命中時一回と復元を検査 |
| C31 | BOMD命中callback、Cataclysm Flame Strike | 塔の原生構造・loot、BOMD原生遠征 | 弾missの残存と床攻撃の二重発火を防ぎ、安全帯を残す |
| C32 | Mowzie's `EntitySunstrike`、都市外縁の起動設備 | Mowzie's原生日光攻撃と自然拠点 | 設備限定で発火。夜/悪天候条件、owner、街路通行を隔離検査 |
| C33 | Alex's `MAGNETIZING` Effect、工場Mobの装備条件 | Alex's洞窟と原生磁力設備 | 全Mobへの常時付与を避け、効果切れ・死亡・chunk unloadを検査 |
| C34 | Pehkui BASE scale、Projectile hit | Pehkui原生サイズと城塞の原生通路 | 対象個体と短時間に限定し、壁内/乗り物/死亡時の復帰を検査 |
| C35 | BOMD `RiftBurst`、Mowzie's `EntityBlockSwapper` | BOMD/Mowzie'sの原生施設とdrop | 屋外限定で地形復元、離脱時のcleanup、建築保護を検査 |

## B. 未導入Modの部品を試す23パターン（20作業パッケージ）

X01〜X20の20作業パッケージを、プレイヤーの操作が違うX03/X12/X13だけ分けて**23パターン**として数える。これらは**実験と採否判断を含む企画範囲**であり、20 Modをそのままpackへ追加する決定ではない。各件で部品の固定版・依存・動画利用条件・元Modで残す内容・不要な生成/レシピ/AIを止める手段を試す。部品が使えない場合も、狙ったプレイヤー操作は別経路で追う。枝番号の親X番号と受入Rは `IDEA_DELIVERY_CONTRACT.md` に一致する。

| ID | 部品同士の縫合と場所 | プレイヤーがすること | 受入R |
|---|---|---|---|
| X01 | Apoli Action/Condition × Mob/設備/Player、地区境界 | 同じ条件付き効果を三主体で見比べる | R-40A |
| X02 | Ars Nouveau turret/Form × Player caster、高層魔術 | 設備と自分で同じEffectの射線/範囲を変える | R-40B |
| X03a | Immersive Engineering Chemthrower × 他Modの液体、工場 | 同じ液体をEntityとBlockへ吹き分ける | R-40C |
| X03b | Immersive Engineering Railgun × 他Modの弾/owner、工場 | 設備とPlayerの二つの発射者から来る弾道を読む | R-40C |
| X04 | Occultism Ritual × Ashen Relay武器継承、地区核 | 素材を払い、準備・中断・完成できる継承を行う | R-40D |
| X05 | Mekanismの汚染/化学 × 別Modの耐性装備、工場 | 時間制限の危険を装備選択で越える | R-41A |
| X06 | Hex Castingの座標/ベクトル × 弾/設置攻撃 | 弾道や置き場所を計算して変える | R-41B |
| X07 | PneumaticCraft Drone × 他Modのアイテム、工業設備 | 対象を指定し、Droneに別Mod品を使わせる | R-41C |
| X08 | Create Deployer/Fan/Arm × 他Modの部品、工場 | 機械の応答で経路を開き、報酬へ届く | R-41D |
| X09 | Industrial Foregoing設備 × 他ModのMob/素材/液体、工場 | 加工と戦闘の資源を結び、無限lootなしで更新する | R-41E |
| X10 | Twilight Forest NatureBolt/復元室 × 都市外縁 | 一時的に環境を変えて道を開き、元へ戻す | R-42A |
| X11 | Botania mana × 地区境界の別Mod攻撃 | manaを準備資源にして任意戦を起動・中断する | R-42B |
| X12a | Aether Zephyr弾 × 別owner、空の遠征 | 弾の発射者を読み、街の塔とは違う射線に対処する | R-42C |
| X12b | Aether浮遊Block × 街への帰還 | 一時足場を遠征で学び、街の高所で使う | R-42C |
| X13a | Ice and Fire breath × 気候別のMob/罠 | 広がる攻撃の射線と遮蔽物を読む | R-42D |
| X13b | Ice and Fire石化 × 気候別のMob/罠 | 石化の予兆と解除・復帰を扱う | R-42D |
| X14 | EvilCraftの血・魂資源 × 別Mod武器/継承、地下 | 旧装備を次の器へ移す際に資源の使い方を選ぶ | R-42E |
| X15 | CC:Tweaked / Integrated Dynamicsの観測 × 工場設備 | 状態を読んで安全な通路を開く。手動の別解も残す | R-42F |
| X16 | Dungeons Enhanced原生小塔等 × Lost Cities道路 | 異なる外観の小型建築を街へ接合して攻略する | R-43A |
| X17 | Simply Swords系武器 × Affix/Better Combat/継承 | 武器種を試し、別圏に合う器を選ぶ | R-43B |
| X18 | The Graveyard原生墓所 × Iron's墓地の寄り道 | 地下で別の敵・空間・報酬を選ぶ | R-43C |
| X19 | When Dungeons Arise大型建築 × Lost Cities外縁 | 都市の遠景から歩いて入口と原生室へ行く | R-43D |
| X20 | Integrated Dungeons AriseのMob/loot × X19原生建築 | 同じ大型施設に異なる攻略・報酬の寄り道を作る | R-43E |

## 全体での数え直し

- **現時点で場所と操作を特定した58件 = C35 + X23**。現行packだけで完成した58の遊びという意味ではない。42件の旧版から既存実装の見落とし7件と現行pack候補6件を加え、Xの別操作3件を分けた。
- **六圏・18場面**は配置と体験の下限。58パターンの複数件を一場面に組み、同じパターンを複数場面で使う場合もある。従って58と18を足さない。
- **五縫合**（敵・弾・場所・道具・連鎖）は実装方法の分類。C/Xの件数と足さない。
- **X15**は二Modを一つの操作の代替候補として数える。両者で別の操作が成立した場合は分割して増やす。
- **まだ件数に入れていない旧資料候補**: Alex's Wave/Nuclear Explosion、Cataclysm Lightning Storm/Ignis Fireball/Void Rune、Mowzie's IceBall/Earth Spike/Boulder、BOMD Spikes/SporeBall、Iron'sのMob casterを他Mod Mobへ渡す方式。`CROSS_MOD_PARTS_CATALOG.md` のA/B/C確度と `IDEA_DELIVERY_CONTRACT.md` のP01〜P05で採用対象として追跡する。技術・権利、遊び、物語の三理由を示さず除外しない。場所・操作・受入Rを確定した時点でC番号を追加する。
- 今後、部品や施設を追加して異なる操作が確定したら新IDを付け、`IDEA_DELIVERY_CONTRACT.md`、`REVISED_COMPLETION_PLAN.md`、公開Pagesに同じ作業単位で反映する。除外は `IDEA_INCLUSION_LEDGER.md` の三理由と証拠に限る。
