# 次の作業と受入条件

目的: プレイテストから企画再編までのユーザー指示を、次のRで実際に処理する作業へ対応させる。状態: **現行の公開作業計画**（2026-09-23）。順序と受入は [完成工程](completion.html)、旧案の採否は [旧案の採用台帳](ideas.html)、全案の実装行は このページ、既存実装と検証は 内部の検証記録 を参照。物語の核心と隠し条件は本書に記さない。

## 1. 次に開始する作業

次の制作単位は **R-27W1: 原生建築・入口・権利・生成停止範囲の棚卸し**。まず `WroughtFacilityReservation.java`、Lost Citiesの街路条件、現行の `vocab_*`/接合part、固定jarの建築テンプレートとstructure setを読む。新規現世で道路から利用できる原生建築の実ID・寸法・入口・生成条件、地中埋没/通路切断の原因候補、モデルの参照可否を表にする。R-27W1は調査票の完成であり、都市接合や新Mod導入を完了した扱いにしない。

| 順 | 次の単位 | このチャットの要望へ届く具体的な成果 |
|---|---|---|
| 1 | **R-27W1** | 原生構造の候補と入口/寸法/権利、既存の独自建物の参照箇所、Lost Citiesの配置・空洞の原因を確定する。Dungeons Enhanced等の未導入候補も隔離試験の資料として載せる |
| 2 | **R-27W2** | 現世Lost Cities道路からAlex's小屋の梯子を通りMowzie's室へ降り、地上へ戻れる。Structure Void/地形上書き・通路未接続を新規3 seedで検証する |
| 3 | **R-27W3** | 同じ街道から原生Apotheosis塔へ歩ける。地下と塔の二択を同じworldで成立させる |
| 4 | **R-27W4 / R-28A〜D** | Ashen Relay製の低品質な外観建物を生成選択から外し、別Modの建物・接合元で種類を増やす。工業・城塞・水辺も含む六圏へ拡張する |
| 5 | **R-27M / R-27E1〜E3** | 中継弾の射手を固有外見+AIにし、墓地の復元床、工場の磁力と設備、城塞の歩法と縮小を異なる場所の遊びにする |
| 6 | **R-27A/B/S、R-29〜31** | 地区共鳴、継ぎ目異常、施設別報酬、複数の遠征経路、武器更新、段階的な記録と復帰を繋ぐ |
| 7 | **R-32〜36、R-37〜44以降** | 調整・検証の後、六圏/五空間/五縫合と旧案全件を このページ のID単位で実装・監査する。R-36は中間監査、R-44も未達を完了扱いにしない |

**R-27W1を先に完了してから**、実IDと配置条件に基づいてW2のコード/JSONを確定する。新規worldの検証には使い捨て環境を使い、プレイ中worldを断りなく削除しない。

## 2. プレイテストから残った修正要求

| チャットで確定したこと | 現状の扱い | 作業と受入先 |
|---|---|---|
| 地中TPと出口の不便、地下通路の切断 | 目視で報告済み。原因をMowzie's単体へ決めつけない。Structure Voidは「置くべき場所にない可能性」という訂正を採る | R-27W1で配置順、空洞処理、block置換、Void/airの実NBTと地形、LC衝突を調べる。R-27W2で地上入口→梯子→室→帰路を3 seed/再起動で確認 |
| フェラスの強さは問題ない。構造物が雅ではない | 戦闘難度を下げる根拠にはしない | R-27W2/W4で外観・入口・接合を改善。原生boss AI/dropは保持 |
| 「イグルー式」の梯子入口を他Modの構造から借り、地下通路へ溶接 | 既存のAlex's `forlorn_hut_1` と原生室の実行時参照を優先する。権利未確認NBTの丸写しはしない | R-27W1で建築候補を比較し、R-27W2で入口、縦坑、水平通路、壁/床の隙間、帰路を一体で受入 |
| 水の流入は許容 | それ自体は欠陥票にしない | R-27W2と浸水圏で、流入後も窒息/通路消失/loot破壊/帰路不能がないか判定 |
| 生成はきれいでも施設が都市から孤立 | 見た目だけの生成PASSを撤回 | R-27W2/W3、R-28D。**現世**道路からの徒歩往復、施設を見つけられる輪郭、複数seedを受入 |
| 別ディメンションは物語上の理由がなければ現世へ | 固定 `lostcities:lostcity` アンカーを通常進行の正本にしない。別次元へ行く未用意の導線で進行を塞がない | R-27W3/W4で現世進行へ移し、既存world参照とadvancement/FTBを監査 |
| Ashen Relay製の建物は低品質。必要なもの以外を削り、他Modの構造物を組み合わせて種類も増やす | 独自建物の維持は接合機能が必要な場合に限る | R-27W4/R-28D/R-37/R-43。外部建築3 Mod・8種は第一波の下限。道路、色違い、独自箱を別種に数えない |
| 中継弾の射手は名前付きスケルトンをやめ、他Modのモデルと専用AIを組み合わせる | 既存の弾・予兆・lootは活かす | R-27Mで登録済みモデルの実行時参照か原生Mob hostを比較し、外見/AI/owner/報酬を一体で確認 |
| 他にも今遊べる場所を増やす | 施設が自然生成するだけで「遊べる」としない | R-29A〜C/R-37以降。街の準備→原生遠征→固有drop→都市で更新→別攻略の往復を作る |

過去のOP付与、物資支給、TP、spectator/survival切替、ワールド削除・再起動、クライアント起動は、その時の試験環境を操作する個別指示だった。将来の長期worldを削除する恒久許可や、毎Rでクライアントを自動操作する許可にはしない。テスト時に必要なら 内部の運用手順 と 内部のテスト手順 に従い、Codexが専用server/selftest/ログで検証する。Computer Useは禁止。

## 3. 企画とModの組合せについて確定したこと

| 指示 | 作業化した場所 |
|---|---|
| 「何と何」をゲーム内のどこで組み合わせるか、最小の遊び、書くクラス/JSON、Modの役割、止める要素まで列挙する | [実装ファイル](implementation.html) が第一街区、このページ が旧案全行、[完成工程](completion.html) が順序。各Rで実IDと固定版APIを確定 |
| Modから構造だけ、モデルだけ、NBT/アイテム/接合元だけを借り、不要な内容はdatapack/KubeJS/event/必要箇所のMixinで止めてよい | 旧案の各X行に「借りる/残す/抑える」を付ける。実行時参照を優先し、権利・動画条件、依存、固定版、停止スキーマを導入前に確認 |
| アイデア出しと拡張性チェック・ソース確認の成果を使う | [旧案の採用台帳](ideas.html) に旧案を原則採用対象として戻し、このページ で施設と実装単位へ割当。ソースA/B/C、EX実証、実施設検証を区別 |
| 実現困難、面白くなさそう、物語と衝突する案だけを除く | 除外は三理由の証拠、遊びへの影響、代替、反転条件を台帳/決定記録に要求。工数、旧凍結、似たModがあることでは削らない |
| 建物を入れ替えるだけでなくバリエーションを増やし、企画を小さくしない | 六圏・18場面を下限とし、外部Mod建築と五空間・五縫合、複数の武器更新を展開。R-36で打ち切らない |
| ストーリーと部品の組合せを一体のプレイループにする | 全行に入口→遭遇→原生drop+追加報酬→武器/能力更新→次の施設を要求。核心は 非公開の物語資料 の正史と開示順で検証 |
| 完成像が見えないまま小さな作業に還元しない | 毎R終了時に構想、今回遊べる範囲、実装と検証、物語/次の装備、削った案と影響、次の体験を報告。`AGENTS.md` §1.2 |
| 予定することは公開ページにも全部載せる。詳細が伝わるなら不要なネタバレは避ける | この公開サイト の世界/ゲーム/Mod/案台帳/実装/完成工程を内部正本と同じRで更新。物語の核心を作業説明のためだけに掲載しない |

## 4. 旧案の取りこぼしを防ぐ確認

Rの開始時に このページ の対象IDを列挙し、元資料の該当箇所を一度確認する。Rの終了時、IDごとに「調査待ち／隔離試作／施設統合／検証済み／三理由で除外」を記録する。採用試験を実施しただけで案を閉じない。使える部品は施設へ、使えない部品は狙った操作を別経路へ引き継ぐ。公開Pagesと 内部の引き継ぎ に未完了のIDを残す。

旧資料の全案を単一Rの巨大な実装にまとめない。X01〜X20は `R-40A〜D`、`R-41A〜E`、`R-42A〜F`、`R-43A〜E` にそれぞれ割り当てた。必要なModは1つずつ隔離し、固定jar/権利/stop対象/原生施設を調べた後に本番へ導入する。X15の二Modなど一単位に異なる体験が残る場合は分割する。R-44で全行を監査し、未達があれば次のRを作る。


---

# 旧案を実装へ届ける受入台帳

20件の未導入Mod案は、ソース調査・隔離試作で終えず、指定施設の入口、遭遇、持ち帰りまで追跡します。表のクラス名とJSONは未実装の責務案です。固定版のAPI・実IDを確認して確定します。

## 1. 採用対象が完了する条件

一案の状態は **採用対象 → 固定版調査 → 隔離試作 → 施設へ統合 → 検証済み** と進める。固定版の版・依存・権利・動画条件・不要要素の停止が未確認なら「調査中」と記す。隔離試作の成功だけで「実装済み」としない。除外は台帳の三理由と証拠、代替案、反転条件が揃った場合だけ別の状態として認める。外部Modの一部が使えなくても、その行の**プレイヤー操作**は別の部品へ引き継ぐ。

施設への統合には次の6点を一枚の受入票で揃える。

1. **入口**: どの圏のどの原生/接合構造へ入り、退路と再挑戦をどう残すか。
2. **予兆と操作**: Playerが何を見て、どの武器・呪文・環境操作で対処/利用するか。単なるEffect付与や登録数を成果に数えない。
3. **持ち帰り**: 原生dropを保ち、追加loot/レシピ/能力がどの別施設で役立つか。
4. **借用と抑制**: 実行時に借りるBlock/Entity/API/NBTと、止める自然生成・recipe・AIの実IDと方法。未確認IDを上書きしない。
5. **証拠**: Javaならbuild、構成/worldgen/lootなら隔離専用server、selftestとログ、必要ならclient起動ログ、生成/保存/再起動/元drop。外観・歩行感・楽しさは人の確認まで未検証。
6. **追跡**: 下のID、R、変更ファイル、内部の検証記録/report、公開Pagesの行を相互に参照する。R終了時に「未調査・試作のみ・施設で稼働・検証済み・三理由で除外」のいずれかを残す。

版のないソース調査結果は実行可能性の証明ではない。jarを追加する場合は 内部の権利・データ監査 と 内部のMod拡張計画 の隔離ゲートを通す。選択的採用は「Mod全体の進行を一括で増やす」ことを意味しない。設定→同ID datapack/KubeJS→Forge event→対象限定Mixinの順で不要要素を止める。ただし原生攻略に価値がある場合は残す。Mixinの採用も実クラス・競合・復旧を確認するまで確定しない。

## 2. 場所・空間・進行の行

以下の行は全て採用対象。R-27〜36は第一波、R-37以降は六圏の拡張と旧案の回収である。同じ圏の三場面を同じ敵・同じ箱の色違いにしない。

| ID / R | プレイヤーが遊ぶもの | 主な作業面と受入 |
|---|---|---|
| W01 / R-27W3〜R-28A、R-37A | 高層魔術。街路→原生塔/魔術施設→屋上橋→帰還。高所の射線と魔法設備を使い分ける | `CityFacilityConnector.java`案、LC building/part/citystyle JSON、塔loot。異なる入口と報酬、帰路を3 seedで確認 |
| W02 / R-27W2・E1、R-37B | 地下継ぎ目。小屋の梯子、フェラス室、Iron's墓地、一時床を歩いてつなぐ | `WroughtFacilityReservation.java`既存、`CatacombFloorCycle.java`案、接合parts。入口/箱/梯子を守り再起動後に床を復元 |
| W03 / R-27E2・R-28B、R-37C | 工業。工場と都市の設備をつなぎ、磁力、液体、弾、機械主体の戦いを順に覚える | `RelayFactoryDistrict.java`既存、`FactoryMagnetCycle.java`案、設備adapter、loot/recipe JSON。安全帯と原生装置を維持 |
| W04 / R-27E3・R-28C、R-37D | 城塞。門、狭路、広間で敵の歩法と短時間縮小を対処し、後に自分で使う | `RelayFortDistrict.java`、Pehkui接続、Iron's原生施設、移動報酬。閉じ込めなし・元サイズ復帰 |
| W05 / R-29B、R-37E | 浸水。都市の堤防を手掛かりに海の原生施設へ遠征し、水中能力を帰りの街でも使う | LC水辺parts、route advancement/FTB、Cataclysm/Alex's/T.Oのloot/recipe。水中の原生生成を壊さない |
| W06 / R-29C、R-37F | 外縁。寒冷・自然拠点・洞窟・Nether/Endを装備の持ち替えで巡る | 原生structureの生成維持、route/loot/recipe。遠征の固有drop→都市で更新→別環境への帰還を二経路以上 |
| S01 / R-38A | 狭路。城塞の短距離移動と一時縮小を、退路のある幅で読む | `RelayFortDistrict.java`、Pehkui。失敗後と効果終了後に元の通路へ戻れる |
| S02 / R-38B | 閉鎖室。墓地と工場で床/装置の予兆から安全帯を選ぶ | `CatacombFloorCycle.java`案、`FlameZoneHost.java`。入口と箱を保護 |
| S03 / R-38C | 屋外。自然拠点で広い射線の弾/設置攻撃を避ける | 原生屋外施設、Projectile cleanup。施設外へ弾が残らない |
| S04 / R-38D | 垂直。塔・梯子・縦坑で上下移動し、落下後も復帰する | `CityPathWeld.java`案、塔と小屋の入口。上下両方向の帰路 |
| S05 / R-38E | 境界。二圏の規則を順番に越える任意戦 | `SeamEncounter.java`案、一回報酬JSON。二規則を初見で同時最大強度にしない |
| G01 / R-38F | 敵の縫合。原生外見のMobへ別Mod技を付け、後に別Hostで再提示 | Goal/tag、`RelayContext.java`。モデル/AI/lootと予兆が一致 |
| G02 / R-38G | 弾の縫合。BOMD/Cataclysm等の弾を別owner・命中payloadで使う | `RelayMissileHost.java`等。owner、hit、cleanup、再起動 |
| G03 / R-38H | 場所の縫合。Mowzie's復元床、Alex's磁力、工場zoneを場面へ | Zone/structure判定、保存。保護blockを壊さず復元 |
| G04 / R-38I | 道具の縫合。敵で見た技をIron's/T.O/独自装備へ結び直す | spell/item/recipe/loot JSON。Playerが別施設で使う |
| G05 / R-38J | 連鎖の縫合。異なる二圏の素材・記録・勝利を一つの選択へ繋ぐ | advancement/FTB/台帳。保存、一回性、別順攻略 |
| N01 / R-27S、R-31A/B、R-39F | 段階的な記録、複数の次の候補、条件付き経路。失敗/死亡から戻れる | advancement/FTB/ja lang/保存状態。核心の条件は非公開正本と照合し、公開上は状態・操作のみ |

## 3. 現行packの部品を必ず使い切る行

内部のソース調査 のAはソース/固定jarで入口を確認した意味。以下の「試す」は本番施設への投入を保証しないが、成功した試作は受入票へ移し、未採用なら三理由と代替を記す。既存の実装は再利用し、登録だけを成果にしない。

| ID / R | 部品→ゲーム内の操作 | 既存/予定の作業面と保護 |
|---|---|---|
| P01 / R-27E2、R-38G | Alex's Effect/Magnet/Waveを工場・浸水・境界の局所周期へ。NuclearExplosionは保護領域を壊さない方法を隔離試験 | `FactoryMagnetCycle.java`案、zone/接合ブロック、効果終了と地形保持。無制限破壊方式は受入れない |
| P02 / R-27M/E、R-38F/G、R-39D | Cataclysm Effect/Flame Strike/Lightning Storm/Ignis Fireballを塔・工場・城塞の異なる予兆とPlayer用能力へ | `RelayMissileCarrier.java`、`FlameZonePayload.java`既存、戦技案、spells/loot。原生ボスAI/dropを置換しない |
| P03 / R-27E1、R-38H、R-39D | Mowzie's BlockSwapper/Sunstrike/IceBallを復元床・屋外予兆・寒冷装備へ | `CatacombFloorCycle.java`案、保護block tag、再起動復元。原生フェラスの戦いは残す |
| P04 / R-27M、R-38G、R-39D | BOMD Magic Missile/RiftBurst/Spikes/SporeBallを塔・境界・獲得戦技で別ownerへ | 既存 `RelayMissileHost.java`、戦技adapter案、loot。owner/命中/cleanup/再取得と四原生施設を検査 |
| P05 / R-27E3、R-30、R-39 | Iron's caster、T.Oスペル、Apo Affix/Gem、Pehkuiを城塞と武器移行へ | `ImprintItem.java`・`RelayWeaponLedger.java`既存、recipe/loot。既存T.Oスペルの重複と恒久縮小を防ぐ |

## 4. 独自ギミックと装備の行

| ID / R | 状態と残る制作 | 完成を示す操作 |
|---|---|---|
| U01 残響精錬 / R-25、R-39A | `EchoRefiningItem.java` 実装済み。六圏の重複dropへ施設別の用途を接続 | 重複品→残響片→別武器の部分継承を二圏で使う |
| U02 武器記録台帳 / R-25、R-39B | `RelayWeaponLedger.java` 実装済み。拾う武器種とボス技を地区の選択へ表示 | 台帳tierが施設での次の器・能力を変え、再ログイン後も残る |
| U03 地区共鳴 / R-27A、R-39C | 未実装。構造限定lootと観測票、原生箱の保持 | 地区で探す品が異なり、別圏で用途を発見する |
| U04 戦技再演 / R-39D | 未実装。T.Oにないボス技を少なくとも二つ、原生報酬からPlayer用へ変換 | 予兆を受けた後に同じ技を別の武器/スペルで使う。同型弾の属性違いは二つに数えない |
| U05 継ぎ目異常 / R-27E3/A、R-39E | 未実装。任意起動、二規則の順序、一回報酬と再挑戦 | 二地区を学んだ後に境界戦へ入り、選択報酬を次の圏へ持つ |
| U06 継承の選択損失 / R-25、R-39F | `ImprintItem.java` 部分適用を実装済み。失う/残す特性と費用をプレイヤーへ明示 | 不適合分が印に残り、別の器に再利用でき、素材増殖がない |
| U07 横断装備 / R-29〜30、R-39G | 九ボス固有drop、Apo Affix/Gem、Iron's装備型呪文、T.O四系列、BOMD槍を六圏の報酬表へ配置 | 序・中・後の各段階で距離/操作の違う二つ以上の更新先があり、旧装備の投資を移せる |

## 5. 未導入Modを施設へ組み込む作業単位

各行は一つの**実装候補パッケージ**。まず固定版と実ID/APIを確認し、隔離世界で一つの操作を作る。通れば指定施設の入口・遭遇・持ち帰りへ接続し、不要要素の停止と原生要素の保持を確認する。パッケージ全体が進められない場合も、同じ操作を別部品で実現する作業を同じRへ残す。以下のファイルは予定名であり既存ファイルと混同しない。

| ID / R | Playerがすることと借りる部品 | 新規クラス/データ案、残す/止めるもの | 施設統合の受入 |
|---|---|---|---|
| X01 / R-40A Apoli | 境界でMob/設備/Playerが同じ条件付きpayloadを使う。Action/Condition/Raycast | `compat/apoli/RelayActionBridge.java`、`data/ashen_relay/powers/*.json`案。種族選択と不要なpower配布を抑える方法を確認 | 三主体が同じ条件で発火し、境界でPlayerが規則を読み返せる |
| X02 / R-40B Ars Nouveau | 高層魔術のturretとPlayerが同じEffectをFormで撃ち分ける | `compat/ars/RelayEffect.java`、glyph/recipe JSON案。原生魔術設備を残し、余剰レシピ/生成を選別 | 射線/範囲の選択が塔攻略と次の施設で役立つ |
| X03 / R-40C Immersive Engineering | 工場でChemthrowerの液体をBlock/Entityへ使い分け、Railgunの弾を別ownerで撃つ | `compat/ie/FactoryPayloadHandlers.java`、液体/弾/recipe JSON案。原生設備を残し、無関係な機械進行を調整 | Playerと設備で同じ資源を使い、工場報酬が弾/液体の更新へ繋がる |
| X04 / R-40D Occultism | 地区核で準備・中断・完成を選ぶ継承儀式 | `compat/occultism/RelayRitualBridge.java`、ritual/loot JSON案。原生Ritualを残し、余剰召喚/レシピを選別 | 中断して再開可能、旧装備と素材の支払いが保存後も一回だけ |
| X05 / R-41A Mekanism | 工場の時間制限つき汚染を耐性装備で越え、化学/レーザーを別の使い道にする | `compat/mekanism/FactoryHazardAdapter.java`、耐性tag/recipe JSON案。原生機械は採用範囲を決め、永久汚染を防ぐ | 汚染終了・chunk unload・再起動で安全に戻り、装備選択に意味がある |
| X06 / R-41B Hex Casting | 座標・ベクトルで弾道/設置位置を指定する | `compat/hex/RelayHexAction.java`、action JSON案。原生Hexの操作を残し、無制限な広域改変を抑える | 同じpayloadを敵の予兆とPlayerの計算行動で異なる角度から使う |
| X07 / R-41C PneumaticCraft | Droneが対象を判定し、別Modのアイテムを施設設備として使用する | `compat/pneumatic/DroneTargetBridge.java`、widget/recipe JSON案。原生Droneを残し、圧力進行の必要範囲を測る | Droneの対象/失敗/停止が見え、Playerが回収した部品を次の工場で使う |
| X08 / R-41D Create | Deployer/Fan/Armが他Mod品を処理し、工場の通路/設備を動かす | `compat/create/FactoryBehaviourBridge.java`、processing/recipe JSON案。原生機械を残し、資源の無限化を防ぐ | Player操作→機械応答→開いた経路→報酬の一連が再起動後も保たれる |
| X09 / R-41E Industrial Foregoing | 工場設備へ他ModのMob/素材/液体を入力する | `compat/industrial/FactoryMachineBridge.java`、条件tag/recipe JSON案。原生装置を残し、Mob複製と資源循環を制限 | 加工と戦闘の資源がつながり、無限lootや施設外の悪用がない |
| X10 / R-42A Twilight Forest | 外縁のNatureBoltと復元室で、環境を一時変化させて道を開く | `compat/twilight/OuterNatureBridge.java`、Block/loot tag案。原生BlockEntityを実行時参照、ARR構造/音は複製しない | 元の道へ戻せ、原生次元の攻略と都市の持ち帰りに用途がある |
| X11 / R-42B Botania | manaを境界攻撃の準備資源へ変える | `compat/botania/ManaSeamBridge.java`、mana/recipe JSON案。公開APIと権利を先に確認し、コード/アセット複製を避ける | mana消費、予兆、成功/中断、報酬が一つの任意戦になる |
| X12 / R-42C The Aether | Zephyr弾と浮遊Blockを別ownerで使い、空の外縁遠征から街へ持ち帰る | `compat/aether/OuterProjectileBridge.java`、route/loot JSON案。原生遠征を残し、ARRアセットは複製しない | 弾のowner/消滅と一時足場の復元を確認。別環境で操作が変わる |
| X13 / R-42D Ice and Fire | 気候別外縁でbreath/石化/誘引を敵と罠から学ぶ | `compat/icefire/ClimateAttackBridge.java`、biome/loot JSON案。Citadel互換を先に隔離起動し、Dragon生成/地形破壊を制御 | 石化からの復帰と原生Mobの報酬を保ち、別圏の対処に使う |
| X14 / R-42E EvilCraft | 地下の血・魂系資源を旧装備から次の器へ変換する | `compat/evilcraft/UndergroundResourceBridge.java`、recipe/loot JSON案。権利と第三者素材を確認し、余剰レシピを選別 | 資源の入手・消費・上限が明示され、継承と独立の選択になる |
| X15 / R-42F CC:Tweaked / Integrated Dynamics | 工業区で設備の状態を観測し、条件を組んで安全な通路を開く | `compat/automation/FactorySignalBridge.java`、peripheral/logic APIと案内JSON案。原生自動化は残し、必須進行をプログラミング技能へ固定しない | 自動化による別解があり、手動でも攻略可能。状態/保存/報酬が一致 |
| X16 / R-43A Dungeons Enhanced | 小塔・迷路・城・寺院の原生建築を道路へ溶接する | `CityFacilityConnector.java`案、LC parts/structure_set JSON案。Structure Gel依存、実NBT/入口、不要生成の停止を確認 | 最低二つの外観差とそれぞれ別の攻略・原生loot/帰路。実行時参照 |
| X17 / R-43B Simply Swords + Integrated | 六圏で武器種・素材を見つけ、継承先として選ぶ | `ashen_relay_loot.js`/recipes、weapon tag JSON案。原生武器の操作を残し、全lootへの一括注入を止める | Better Combat/Affix/呪文互換、入手頻度と既存武器の価値を測る |
| X18 / R-43C The Graveyard | 地下の背景墓所と任意ボスをIron's墓地の寄り道として攻略 | 原生structure参照、LC connector、chest/route JSON案。自然生成密度と重複lootを調整 | 同じ墓地に見えず、別の空間・敵・報酬・帰路を持つ |
| X19 / R-43D When Dungeons Arise | 都市遠景の大型ランドマークへ向かい、外縁攻略と繋ぐ | 原生structureの実行時参照、LC connector、route JSON案。ARR NBT複製を避け、生成頻度/動画条件を確認 | 道路から見え、入口と原生室に行ける。周辺街路を潰さない |
| X20 / R-43E Integrated Dungeons Arise | 上の大型施設で他ModのMob/lootを使う寄り道 | 原生structure/loot参照、限定loot JSON案。依存jarと重複生成を隔離試験 | X19と異なる攻略操作・報酬があり、原生の遊びを損ねない |

X15は二Modを一つの**体験**で比べる。両方のソース案を試し、両方が異なる操作を成立させる場合はR-42Fを分割する。X16〜X20は建築や武器の数だけを増やすための枠ではない。入口・遭遇・持ち帰りの三点が揃わなければ試作止まりにする。R-44はX01〜X20とW/S/G/U/P/N全行の状態・除外証拠・公開Pagesの一致を監査し、未達行の後続Rを作る。


[旧案の採用・除外規則](ideas.html) · [全工程](completion.html)
