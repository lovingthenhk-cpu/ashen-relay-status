# 製作経路台帳

更新: 2026-10-23。目的: 素材から製作品・別の攻略先までを追い、未接続箇所を閉じる。状態: **G1の静的棚卸し、runtime受入は未完了**。
正本: 進行/採用設計は[攻略・製作](progression.html)、全範囲は[採用台帳](ideas.html)。本書は実IDと取得/加工依存の台帳であり、計画を別に増やさない。

## 趣旨を満たす経路

| 経路 | Mod要素の組合せ | できる操作・別圏での使い道 | 移す投資 / 残る作業 |
|---|---|---|---|
| 都市の寄り道→地下の固有武器 | Apotheosis Affix/Gem＋Mowzie固有斧/兜＋Iron's装備型呪文＋継承印 | 地下の重い近接武器へ寄り道の強化を付け、城塞や墓地の敵に合わせる | エンチャント/Affix/Gem/対応呪文を分ける。固有武器技は器に残す。供給量と費用の通し確認が残る |
| 工場回収→継承と磁気装備 | Cataclysm工場＋Alex回収材/磁石＋Iron's精髄＋空印 | 新しい武器へ投資を移す費用と、交通/追尾矢/磁気盾の準備を得る | 回収材版空印/交通レシピは設計のみ。これだけで終盤武器の代わりにはしない |
| 呪術側の剣→機械剣 | Maledictus/T.O素体＋Harbinger/Cataclysm銃＋融合 | 剣を残すか、銃を混ぜた別武器へ変えるか選び、別距離の戦いへ移る | 融合が元の剣を消費する。Affix/Gem/呪文の保持/退避を実機確認する |
| 洞窟の拳→魔法加工→都市へ | Alex古生物系素材/ボス＋Iron's魔法金属＋T.O拳 | 洞窟攻略の素材を都市の拳ビルドへ使い、設置/射線戦の対処を変える | 高位素材を全ての武器に要求しない。術式との同居と消費量を確認 |
| 海の素材→槍→垂直区画 | Alex海生物素材＋Cataclysm海武器＋Iron's部品＋T.O槍 | 水中で用意した装備を都市の高所/工業攻略へ持つ | Deepling Bruteの装備生成でcoral_bardicheを持つことは固定classで確認。装備drop条件/都市spawn/実取得は未確認。水中準備・帰還・素材経路を同時に設計 |
| 二つの任意攻略→機動槍 | BOMD Void Blossom/Obsidilith＋既存継承 | Earthdive Spearを別の器として選び、近接の距離管理を変える | 元武器の固有能力を無制限に移さない。両遠征の都市導線/実素材取得が残る |
| 敵の技→プレイヤーの技→別主体との再戦 | Iron's/T.O caster＋Cataclysm/BOMD等のpayload＋既存Host/Carrier | 敵から学んだ能力を別の武器/巻物で使い、別Hostが使う同じ規則にも対処する | T.O未収録の再演2種以上と取得/使用/再取得を作る。属性違いの弾だけで数を満たさない |

上記は実現する体験。加工を長くするための中間素材や、全ボスを順番に倒す鍵を増やすことを目標にしない。六圏18場面・全旧案と接続し、同じ5部屋の反復に縮めない。

## 九信号の原生報酬も更新候補に残す

T.O四系列を全装備の置換先にしない。以下は固定版の元Loot表にあるitem参照（条件・個数・追加modifier・実取得は別途）。既存の共鳴刻印と署名巻物は上乗せであり、この原生報酬を消さない。音楽ディスク/羽は表から省略した。

| 攻略先 | 元Loot表の主な実ID | 装備経路での役割 |
|---|---|---|
| ferrous_wroughtnaut | `mowziesmobs:wrought_axe`, `mowziesmobs:wrought_helmet` | 固有斧/兜を器として継承し、重量近接の選択肢を残す |
| frostmaw | `mowziesmobs:ice_crystal` | 氷結道具と既存のテーマ巻物で、冷気/距離管理の選択を残す |
| umvuthi | `mowziesmobs:sol_visage` | 原生装備と太陽系の既存巻物を別ビルドへ使う |
| netherite_monstrosity | `cataclysm:infernal_forge`, `cataclysm:lava_power_cell`, `cataclysm:monstrous_horn` | 原生Forge武器/防具素材と火系巻物。既存融合の別枝も調べる |
| ender_guardian | `cataclysm:gauntlet_of_guard` | 原生拳を維持し、既存の他ボス素材との融合枝へ接続する |
| the_harbinger | `cataclysm:witherite_block` | ブロック→インゴット→銃/設備/融合。death_laser署名巻物も既存経路 |
| the_leviathan | `cataclysm:abyssal_egg`, `cataclysm:tidal_claws` | 原生の爪の操作と水中対処を保持し、海槍だけを唯一の更新先にしない |
| ancient_remnant | `cataclysm:ancient_metal_block`, `cataclysm:remnant_skull`, `cataclysm:sandstorm_in_a_bottle` | 金属/固有道具と既存の嵐系融合枝。原生素材と道中回収材を区別する |
| maledictus | `cataclysm:cursium_ingot` | 原生cursiumとT.O剣/媒体、固有技の巻物で別の更新先を選べる |

固有武器の実性能/射程/アクションは原生実装を調べ、同じ攻撃力の比較だけで下位互換として捨てない。元の印象的な技と、移植できる強化を分けて案内する。

## 判明した供給上の要点

- Harbingerの元Loot表は **witherite_blockを1個**。解体でwitherite_ingot9個。曖昧な「witherite1」とインゴット1を混同しない。gatlingに2＋機械剣3段に3なら、**既に融合設備を使える場合の武器分だけ**なら一回のブロック9から5個を使う静的予算になる。ただし素体の剣とlast_glow3個は別の依存。
- weapon_partsはmithril_ingot3＋arcane_ingot2。海槍のsteel6にarcane6、部品にarcane2で、**素体から最終までのarcane_ingotは合計8**。元文書のsteel分6だけを全工程の合計にしない。
- arcane_ingot1はarcane_essence8＋arcane_ingot_baseタグ1。固定jarのタグは鉄/銅/金。海槍経路のarcane8は精髄64＋対応金属8に相当し、別途mithrilの加工/取得が必要。
- mithril_ingotはmithril_scrap4。raw_mithrilまたはarcane_salvageの溶鉱炉経路があり、ingot→scrap4の戻しもある。鉱石のworldgen、salvageの実回収、都市移管後の供給は未受入。
- heart_of_ironの参照がblock Lootだけでも、自然配置や装置からの実取得は別途確認が必要。coral_bardicheのJSON取得元が見つからなくても、Java装備drop等があり得るため入手不能とは断定しない。
- T.Oの素体と鍛冶媒体は追加Lootの抽選。固定jarのglobal modifier一覧にHarbinger/Maledictus/Hullbreaker/Luxtructosaurusの4件を確認し、各元entity Loot→追加表の条件/参照、KeyLootModifierのaddAllまで静的確認した。最終packでの登録/死亡時発動を確認して初めて実経路として受入する。抽選weightをそのまま最終ドロップ率と説明しない。

## 終点までの材料予算（元レシピの選択経路を展開）

以下は固定レシピの静的加算。入手保証・難度・面白さの受入ではなく、余計な反復や途切れた経路を発見するための値。加工設備/燃料/継承費用は別計算し、特に融合金床の金属6個を無視しない。4系列全部を必須ノルマへ合算しない。

| 完成品 | 素体以外も展開した最終までの必要量 | 別に用意する設備/操作 | 調整上の懸念 |
|---|---|---|---|
| Cursed Wraithblade III | 素体1、echo_winglet3、cursium_ingot3 | 鍛冶台、既存武器の強化退避/戻し | 素体/媒体の両方が同ボス追加抽選。単純な周回数増加で終盤を作らない |
| Mechanized Wraithblade III | Cursed素体1、last_glow3、witherite_ingot5、鉄3、赤石1、赤石block1 | gatling製作→機械融合金床→3段鍛冶。剣側の強化を事前抽出 | 既存の融合設備を利用するなら武器分5。私設金床の6を加えると計11で一回のblock9では足りない。別ボス素体と媒体の抽選も別依存 |
| Gauntlet of Extinction III | 素体1、amber_curiosity12、tectonic_shard6、arcane_essence96、arcane_ingot用の鉄/銅/金計12 | 作業台で合金、3段鍛冶 | 欲しいのは拳の別操作。精髄96や同ボス素材6を集める作業だけで間を埋めない |
| Trident of Eternal Maelstrom III | coral_bardiche1、hullbreaker_scales24、immortal_embryo3、arcane_essence64、arcane用金属8、ミスリルingot3 | steel6/weapon_parts1を製作、3段鍛冶。ミスリル3はscrap12、raw/salvageの経路は別確認 | 海生物/海武器/魔法加工を横断する意味を残し、scale/embryoの同一戦反復に偏らせない |
| Earthdive Spear | void_thorn1、obsidian_heart1、棒1 | 作業台、抽出印の既存強化を適合範囲で装着 | 単純な二素材合成でも、異なる攻略と機動操作をつなぐ点が価値。無意味な中間材を増やさない |

### 加工設備も含めた最初の製作目標

機械融合金床の元レシピはwitherite_ingot6＋赤石block2＋金床1。12個の原生factory templateのpaletteを調べた範囲では同設備の配置参照は0（processor/runtimeによる配置や実worldは未確認）。工場に入れば最初から使える、と案内してはいけない。

既存レシピを変えずに、Harbingerのblock1→ingot9から**自分の融合金床6＋gatling2＋機械剣の第一強化1**という最初の更新が組める。必要な別ボス剣/last_glowは別途取得し、剣側の強化を先に退避する。IIIまでの武器5＋設備6は11なので、後続の供給/設備共用の導線を別に示す。共有設備を用意する場合は都市施設の実配置・所有物保護・誰でも使える帰路を検証してから採用し、未設置の設備を前提に金属を削らない。

### 抽選を踏まえて先に決めること

製作費用のうち「初回に新しい武器を触るための素材」「同じ武器を伸ばす媒体」「別武器へ投資を移す費用」を分離する。媒体を3個使う事実が、そのまま同じボスを3回以上倒す義務を意味しないよう、地区共鳴(U03)・境界選択(U05)・台帳(U02)の報酬を対応する供給へ割り当てる。どのボスを一回倒すとどの候補を選べるか、どの別圏の観測/攻略で次の媒体を得るかを先に記す。数量だけのpity追加を実装の既定にしない。

次の設計票では、上記の高額依存ごとに「初回素体の保証または選択経路」「2段目を別の場所で使って得る媒体」「最終更新で複合攻略を使う経路」を候補として比較する。未確認の実IDや原生drop率を穴埋めに使わず、元の合成/再戦で集める自由も残す。現時点ではその追加供給は未実装・未確定であり、表の量だけを達成目標としてクエストへ流し込まない。

## 継承の原要求に直接関係するリスク

`WeaponfusionRecipe`のassembleはresultをcopyし、slot0（base）のtagだけをcopyする。`WeaponfusionMenu`は機械融合金床を使い、取得時にslot0/slot1を各1個消費する。T.Oの機械剣レシピはbase=laser_gatling、addition=cursed_wraithbladeなので、**銃側のNBTを引き継ぐ処理はあるが、剣側のNBTを自動統合する処理はない**（静的確認、最終packでの実メニュー/互換性は未確認）。

本パックでは、追加側の強化を持った剣を無告知で消費させない。融合前に「銃側を引継ぎ、剣側の強化は先に空印へ退避」と表示し、既存継承の抽出→融合→再装着を一本の製作票にする。器に残る固有能力と移せる特性を区別する。互換のない特性は部分継承の残余として保持できるか確認する。新たな全NBTの無差別mergeを既定の解決にしない。


## 現行工場Lootを製作目標に照合

12容器（樽6/箱の半分6）に現在の表を各1回適用する**理論上の平均**。外部Loot注入を含めず、乱数が一様な場合の重み/個数から算出した値で、本人が得た量や実測成功率ではない。

| 素材 | 一棟の理論平均 | 既存/予定の用途との関係 |
|---|---:|---|
| metal_swarf | 25.2 | 回収材版空印2個に8（レシピ予定）。残りを全て空印へ変える前提にせず、足場/板/設備と次の器への投資へ |
| 青ネオジム | 約13.76 | 元レシピの浮上レール、磁石、盾の選択。交通用と戦闘用のどちらに使うか見せる |
| 赤ネオジム | 約6.86 | 追尾矢/磁石/盾。攻撃に使う消耗品と恒久装備で用途を分ける |
| 古代金属 | 12（保証範囲6～18） | 古代槍は「金属4個で槍1本」。序中盤の武器候補を得るが、製作の強制ノルマにしない |
| arcane_essence | 約15.43 | 空印2個に4（予定）。拳IIIの96や海槍IIIの64を工場だけで集める目標にしない。墓地/魔術攻略と接続 |

回収材が目立つという本人の指摘は量からも説明できるが、平均値だけで受入/不合格にしない。最初に作れる物を案内し、他圏の材料との役割差、新しい武器/技を試す頻度、余剰材を持ち帰る負担を確認してLootを決める。紙はこの二表にないため、空印製作を工場単独で閉じると説明しない。


## 対象素材の静的索引

固定jar＋addon/data＋pack/kubejs/dataの直接参照。タグ経由の全消費・Java drop・KubeJS生成レシピ・実registryの存在/到達はこの数字に含まない。0は「この索引で直接のJSON経路がない」の意味。スクリプト経路は次節に記す。

| 実ID | JSON製作元数 | 直接の加工先数 | Loot参照数 | 最初に調べる取得/加工元 |
|---|---:|---:|---:|---|
| `alexscaves:metal_swarf` | 1 | 2 | 4 | `data/alexscaves/recipes/metal_swarf.json` |
| `alexscaves:scrap_metal` | 2 | 7 | 6 | `data/alexscaves/recipes/furnace/scrap_metal_blasting.json` |
| `alexscaves:scrap_metal_plate` | 2 | 1 | 1 | `data/alexscaves/recipes/scrap_metal_plate.json` |
| `alexscaves:azure_neodymium_ingot` | 2 | 8 | 6 | `data/alexscaves/recipes/azure_neodymium_ingot.json` |
| `alexscaves:scarlet_neodymium_ingot` | 2 | 7 | 5 | `data/alexscaves/recipes/scarlet_neodymium_ingot.json` |
| `alexscaves:heart_of_iron` | 0 | 5 | 1 | `data/alexscaves/loot_tables/blocks/heart_of_iron.json` |
| `alexscaves:tectonic_shard` | 0 | 7 | 1 | `data/alexscaves/loot_tables/entities/luxtructosaurus.json` |
| `alexscaves:amber_curiosity` | 0 | 6 | 1 | `data/alexscaves/loot_tables/blocks/amber.json` |
| `alexscaves:immortal_embryo` | 0 | 4 | 1 | `data/alexscaves/loot_tables/entities/hullbreaker.json` |
| `cataclysm:ancient_metal_ingot` | 2 | 12 | 6 | `data/cataclysm/recipes/ancient_metal_ingot.json` |
| `cataclysm:witherite_ingot` | 1 | 17 | 0 | `data/cataclysm/recipes/witherite_ingot.json` |
| `cataclysm:cursium_ingot` | 1 | 16 | 1 | `data/cataclysm/recipes/cursium_ingot.json` |
| `cataclysm:laser_gatling` | 1 | 1 | 0 | `data/cataclysm/recipes/laser_gatling.json` |
| `cataclysm:coral_bardiche` | 0 | 1 | 0 | `スクリプト/Java/実取得を確認` |
| `cataclysm:witherite_block` | 1 | 1 | 2 | `data/cataclysm/recipes/witherite_block.json` |
| `cataclysm:cursium_block` | 1 | 1 | 1 | `data/cataclysm/recipes/cursium_block.json` |
| `traveloptics:cursed_wraithblade` | 0 | 2 | 1 | `data/traveloptics/loot_tables/entities/maledictus_additions_new.json` |
| `traveloptics:echo_winglet` | 0 | 3 | 1 | `data/traveloptics/loot_tables/entities/maledictus_additions_new.json` |
| `traveloptics:last_glow` | 0 | 7 | 1 | `data/traveloptics/loot_tables/entities/harbinger_additions_new.json` |
| `traveloptics:gauntlet_of_extinction` | 0 | 1 | 1 | `data/traveloptics/loot_tables/entities/luxtructosaurus_additions_new.json` |
| `traveloptics:tectonic_ingot` | 1 | 7 | 0 | `data/traveloptics/recipes/tectonic_ingot.json` |
| `traveloptics:hullbreaker_scales` | 0 | 2 | 1 | `data/traveloptics/loot_tables/entities/hullbreaker_additions_new.json` |
| `traveloptics:hullbreaker_steel` | 1 | 4 | 0 | `data/traveloptics/recipes/hullbreaker_steel.json` |
| `traveloptics:mechanized_wraithblade` | 1 | 1 | 0 | `data/traveloptics/recipes/weapon_infusion/mechanized_wraithblade.json` |
| `traveloptics:trident_of_the_eternal_maelstrom` | 1 | 1 | 0 | `data/traveloptics/recipes/trident_of_the_eternal_maelstrom.json` |
| `bosses_of_mass_destruction:void_thorn` | 0 | 2 | 1 | `data/bosses_of_mass_destruction/loot_tables/entities/void_blossom.json` |
| `bosses_of_mass_destruction:obsidian_heart` | 0 | 3 | 1 | `data/bosses_of_mass_destruction/loot_tables/chests/obsidilith.json` |
| `bosses_of_mass_destruction:earthdive_spear` | 1 | 0 | 0 | `data/bosses_of_mass_destruction/recipes/earthdive_spear.json` |
| `irons_spellbooks:arcane_essence` | 0 | 90 | 67 | `data/irons_spellbooks/loot_tables/chests/additional_ancient_city_loot.json` |
| `irons_spellbooks:arcane_ingot` | 1 | 19 | 2 | `data/irons_spellbooks/recipes/arcane_ingot.json` |
| `irons_spellbooks:weapon_parts` | 1 | 6 | 1 | `data/irons_spellbooks/recipes/weapon_parts.json` |
| `irons_spellbooks:mithril_ingot` | 1 | 2 | 0 | `data/irons_spellbooks/recipes/mithril_ingot_from_scrap.json` |
| `irons_spellbooks:raw_mithril` | 0 | 1 | 2 | `data/irons_spellbooks/loot_tables/blocks/deepslate_mithril_ore.json` |
| `irons_spellbooks:mithril_scrap` | 3 | 13 | 1 | `data/irons_spellbooks/recipes/mithril_scrap_from_ingot.json` |
| `irons_spellbooks:arcane_salvage` | 1 | 1 | 2 | `data/irons_spellbooks/recipes/arcane_salvage_from_debris.json` |
| `apotheosis:gem_dust` | 0 | 8 | 8 | `data/ashen_relay/loot_tables/chests/factory_armory.json` |
| `ashen_relay:blank_imprint` | 0 | 0 | 8 | `data/ashen_relay/loot_tables/chests/convergence_a_reward.json` |
| `ashen_relay:resonant_imprint` | 0 | 0 | 3 | `data/ashen_relay/loot_tables/chests/convergence_a_reward.json` |
| `ashen_relay:inheritance_catalyst` | 0 | 0 | 1 | `data/ashen_relay/loot_tables/chests/convergence_b_reward.json` |

## 継承の費用と既存の解放条件（ソース確認）

| 操作 | 現在の条件/費用 | 製作経路で必要な説明 |
|---|---|---|
| 通常エンチャントの抽出/装着 | 空印。上位の地区連鎖条件/触媒は不要。完全適用時は印を1個消費 | P0/P1の基本練習に使える。上位の全特性が最初から移せると説明しない |
| Affix/Gem/装備型呪文の抽出 | 4地区中の異なる2地区clearで既存連鎖を解放。抽出時に継承触媒1個 | 触媒は共鳴刻印1＋Gem粉4＋精髄4。追加のFTB章順を設けず、任意の2地区という既存選択を保持 |
| 上位特性の完全装着 | 同じ既存連鎖条件、適合する器へ。完全適用で印1個を消費 | 抽出と装着の両方で触媒を二重消費する説明にしない。新武器が既に呪文containerを持つ場合など、適合条件を確認 |
| 部分継承 | 武器台帳tier1以上。部分適用にecho_shardをtier1/2で2、tier3で1消費。残余は印に保持 | 台帳tier閾値は異なる武器3/6/9。別武器を使う動機につなぎ、残余と費用を明示。上位特性の既存連鎖条件も満たす必要がある |

根拠は`ImprintItem.java` use/requiresCatalyst/consumeCatalyst、`RelayChainSuture.java` REQUIRED_DISTRICTS/DISTRICT_ADVANCEMENTS、`RelayWeaponLedger.java`の閾値/費用。ソース上の現行動作を確認したもので今回のsurvival実操作ではない。融合前の退避を案内する際は、空印だけで十分か、触媒/既存連鎖/部分継承が必要かを対象武器の実データで判定する。

## 案内と記録を出す順序（G3へ渡す仕様）

素材/レシピの通常利用は先に可能とし、P0～P5の段階表を製作禁止条件にしない。未来の核心は出さず、下記のように実際に見た場所/得た品/使った操作に説明を付ける。

| 経路 | 環境で示すこと | 得た品の用途説明 | 使用・攻略後に示すもの |
|---|---|---|---|
| 塔→地下の器 | 異質な建材、塔の箱と地下への帰路 | Affix/Gemと空印の対応。固有技が器に残ること | 最初の抽出/再装着の確認後、別武器を拾う価値と別の圏の候補を示す |
| 工場回収 | 磁性装置/安全帯と帰還路 | swarfの精錬、空印材料、磁気道具の選択 | 最初の製作/使用後、磁性を別の場所で使う候補を示す。工場だけの素材集めを次クエストにしない |
| 機械剣 | 原生工場設備と別文化の剣の存在 | 金床/融合の二入力、銃側NBT、剣側は事前退避 | 実際の融合/再装着後に組合せの使用記録を出す。未確認の強化保持を約束しない |
| 拳/洞窟 | 都市から環境へ行き戻る準備 | 洞窟素材と魔法金属を合わせる用途/必要量 | 拳を別圏で使う目標、観測済み技の再利用候補を示す |
| 海の槍 | 水辺の入口、呼吸/視界/移動の準備 | 海武器/生物素材/魔法部品の3系統 | 帰還後に高所/工業で槍を使う選択を示す。元Modの独自物語へ案内しない |
| BOMD槍 | 二つの異なる遠征の手掛かり | 片方の素材だけでも次の取得先と用途が分かる | 槍を手に入れた後、機動能力と以前の強化の移し方へ接続 |
| 技の再演/境界 | 元の学習場面で予兆と対処を見せる | 観測済み術式をどの器で使えるか説明 | 使用記録→別Hostからの再提示→複合攻略の順に、既存の開示段階へ割り当てる |

記録の具体的な文面/条件は既存進捗・spoilersの正史へ照合してから実装する。ここでは物語の真相を追加せず、能力を使う行動に説明を結ぶ責務を定める。FTBは次の複数候補を示す案内とし、通常の素材製作を章順でロックしない。

## スクリプト経路と通常取得の受入

- `ashen_relay_recipes.js`：空印（アメジスト4/精髄4/紙1）、継承触媒（共鳴刻印1/Gem粉4/精髄4）、Forlorn研究石板。JSON製作元0と矛盾しない。
- `ashen_relay_loot.js`：九信号ボスの署名巻物/共鳴刻印、地区巻物と再取得条件。一般のボス追加Lootと各地区の一回性を分ける。
- 原生生成停止後の取得を「元の場所にあるから大丈夫」と扱わない。実構造/環境、locator、到達条件、再戦・固有drop、製作設備、帰路の一組で確認する。
- 次のG1受入は、上の供給/加工の実registryとrecipe-manager、T.O modifierの対象、融合NBT、coral_bardiche/heart_of_iron/mithrilの実取得経路。さらに出力から原料へ戻せる循環を調べる。未確認素材のために他の全経路を止めず、行ごとに状態を付ける。


## 検証の範囲

固定版jarとパックデータの直接参照・入力数・Loot内容、融合処理の固定classを静的確認しています。39素材の全経路の実入手/実craft/最終registryの確認は未完了です。
