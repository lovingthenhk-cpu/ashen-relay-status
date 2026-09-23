# Mod要素単位の縫合パターン台帳

更新日: 2026-09-24。**企画上42パターン**。内訳は現行packに入っているModとAshen Relayの部品を組む **C01〜C22の22件**、未導入Modの部品を隔離試験して採用可否を決める **X01〜X20の20件**。これは完成数でも、42種類のModや42棟の建物を入れる約束でもない。R-27W3はユーザー指示により未着手のまま。

## 数え方と状態

一件は「部品A × 部品B → 特定の場所でプレイヤーに生じる操作」が異なる縫合レシピ。同じ塔の色違い、同じ弾の属性違い、同じ仕組みを別seedへ置いたものは増やさない。Lost Citiesの道路とMod建築の接合、戦闘payloadと別Modのcarrier、報酬と別Modの装備更新も、プレイヤーの操作が異なれば数える。`W01〜W06`、`S01〜S05`、`G01〜G05` は圏・空間・方法の分類であり、42件に重複加算しない。

状態は **機械確認**＝現行packで実ブロック/専用server等の該当接続を確認、**一部稼働**＝構成部品や片側はあるが施設内の一連の遊びは未受入、**計画**＝現行packの部品で実装予定、**隔離試験待ち**＝未導入Modの版・互換・権利・停止方法を含む候補。人の外観・操作感を機械確認に含めない。C01も外観と実player歩行は未検証。

## A. 現行packの部品で作る22パターン

| ID | 部品同士の縫合と場所 | プレイヤーがすること・次の用途 | 状態 / 受入R |
|---|---|---|---|
| C01 | Lost Cities現世道路 × Alex's `forlorn_hut_1` × Mowzie's `wroughtnaut_chamber` | 道から小屋の梯子を降り、フェラス室へ行って同じ道へ戻る。原生dropを次の武器候補にする | **機械確認**：R-27W2。外観・実歩行は未検証 |
| C02 | Lost Cities街路 × Apotheosis原生塔 | 地下との二択として道から塔へ登り、Affix/Gemを持ち帰る | **計画**：R-27W3。現在は着手停止 |
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

## B. 未導入Modの部品を試す20パターン

この20件は**実験と採否判断を含む企画範囲**であり、20 Modをそのままpackへ追加する決定ではない。各件で部品の固定版・依存・動画利用条件・元Modで残す内容・不要な生成/レシピ/AIを止める手段を試す。部品が使えない場合も、狙ったプレイヤー操作は別経路で追う。X番号は `IDEA_DELIVERY_CONTRACT.md` と一致する。

| ID | 部品同士の縫合と場所 | プレイヤーがすること | 受入R |
|---|---|---|---|
| X01 | Apoli Action/Condition × Mob/設備/Player、地区境界 | 同じ条件付き効果を三主体で見比べる | R-40A |
| X02 | Ars Nouveau turret/Form × Player caster、高層魔術 | 設備と自分で同じEffectの射線/範囲を変える | R-40B |
| X03 | Immersive Engineering Chemthrower/Railgun × 他Modの液体・弾、工場 | 液体のEntity/Block別反応と別ownerの弾を読む | R-40C |
| X04 | Occultism Ritual × Ashen Relay武器継承、地区核 | 素材を払い、準備・中断・完成できる継承を行う | R-40D |
| X05 | Mekanismの汚染/化学 × 別Modの耐性装備、工場 | 時間制限の危険を装備選択で越える | R-41A |
| X06 | Hex Castingの座標/ベクトル × 弾/設置攻撃 | 弾道や置き場所を計算して変える | R-41B |
| X07 | PneumaticCraft Drone × 他Modのアイテム、工業設備 | 対象を指定し、Droneに別Mod品を使わせる | R-41C |
| X08 | Create Deployer/Fan/Arm × 他Modの部品、工場 | 機械の応答で経路を開き、報酬へ届く | R-41D |
| X09 | Industrial Foregoing設備 × 他ModのMob/素材/液体、工場 | 加工と戦闘の資源を結び、無限lootなしで更新する | R-41E |
| X10 | Twilight Forest NatureBolt/復元室 × 都市外縁 | 一時的に環境を変えて道を開き、元へ戻す | R-42A |
| X11 | Botania mana × 地区境界の別Mod攻撃 | manaを準備資源にして任意戦を起動・中断する | R-42B |
| X12 | Aether Zephyr弾/浮遊Block × 別owner/街への帰還 | 空の遠征で得た一時足場の使い方を街で変える | R-42C |
| X13 | Ice and Fire breath/石化 × 気候別のMob/罠 | 敵と罠の両方から石化を学び、復帰を含め対処する | R-42D |
| X14 | EvilCraftの血・魂資源 × 別Mod武器/継承、地下 | 旧装備を次の器へ移す際に資源の使い方を選ぶ | R-42E |
| X15 | CC:Tweaked / Integrated Dynamicsの観測 × 工場設備 | 状態を読んで安全な通路を開く。手動の別解も残す | R-42F |
| X16 | Dungeons Enhanced原生小塔等 × Lost Cities道路 | 異なる外観の小型建築を街へ接合して攻略する | R-43A |
| X17 | Simply Swords系武器 × Affix/Better Combat/継承 | 武器種を試し、別圏に合う器を選ぶ | R-43B |
| X18 | The Graveyard原生墓所 × Iron's墓地の寄り道 | 地下で別の敵・空間・報酬を選ぶ | R-43C |
| X19 | When Dungeons Arise大型建築 × Lost Cities外縁 | 都市の遠景から歩いて入口と原生室へ行く | R-43D |
| X20 | Integrated Dungeons AriseのMob/loot × X19原生建築 | 同じ大型施設に異なる攻略・報酬の寄り道を作る | R-43E |

## 全体での数え直し

- **42レシピ = C22 + X20**。現行packだけで完成した42の遊びという意味ではない。
- **六圏・18場面**は配置と体験の下限。42レシピの複数件を一場面に組み、同じレシピを複数場面で使う場合もある。従って42と18を足さない。
- **五縫合**（敵・弾・場所・道具・連鎖）は実装方法の分類。C/Xの件数と足さない。
- **X15**は二Modを一つの操作の代替候補として数える。両者で別の操作が成立した場合は分割して増やす。
- 今後、部品や施設を追加して異なる操作が確定したら新IDを付け、`IDEA_DELIVERY_CONTRACT.md`、`REVISED_COMPLETION_PLAN.md`、公開Pagesに同じ作業単位で反映する。除外は `IDEA_INCLUSION_LEDGER.md` の三理由と証拠に限る。
