# 自動車アフター業界システム 実装コード管理ガイド

## 目次
1. [概要](#概要)
2. [ファイル配置構造](#ファイル配置構造)
3. [仕様書への記録方法](#仕様書への記録方法)
4. [実装コードの整理](#実装コードの整理)
5. [テンプレート管理](#テンプレート管理)
6. [実装例](#実装例)

---

## 概要

本ガイドは、自動車アフター業界向けシステムの実装コードを、どのファイルにどのように記録・管理するかを説明します。

### 基本方針
1. **仕様書**には完全な実装例を含める（開発者への指針）
2. **ソースコード**は適切なディレクトリ構造で整理
3. **テンプレート**として再利用可能な形で保存
4. **テストコード**は実装と同じ場所に配置

---

## ファイル配置構造

### プロジェクト全体構造
```
auto-repair-system/
├── .claude/agents/              # Agent定義
├── specifications/              # 仕様書
│   ├── implementation_spec_auto.md    # 実装仕様書（全コード例を含む）
│   ├── coding_standards_auto.md       # コーディング規約
│   ├── test_scenarios.md              # テストシナリオ
│   └── performance_spec.md            # パフォーマンス仕様
├── src/                        # 実装コード
│   ├── domain/                 # ドメインロジック
│   ├── integration/            # 外部連携
│   ├── batch/                  # バッチ処理
│   └── common/                 # 共通処理
├── templates/                  # コードテンプレート
│   └── implementation_templates/
└── tests/                      # テストコード
```

### 実装コードの詳細配置
```
src/
├── domain/
│   ├── vehicle/
│   │   ├── VehicleInspectionCalculator.js      # 車検満了日計算
│   │   ├── VehicleInspectionCalculator.test.js
│   │   ├── VINDecoder.js                       # VINデコード
│   │   └── VINDecoder.test.js
│   │
│   ├── maintenance/
│   │   ├── LaborCalculator.js                  # 標準作業点数計算
│   │   ├── LaborCalculator.test.js
│   │   ├── MaintenanceRecordManager.js         # 整備記録管理
│   │   └── MaintenanceRecordManager.test.js
│   │
│   ├── inventory/
│   │   ├── InventoryAllocator.js               # 在庫引当処理
│   │   ├── InventoryAllocator.test.js
│   │   ├── PartNumberNormalizer.js             # 部品番号正規化
│   │   └── PartNumberNormalizer.test.js
│   │
│   └── customer/
│       ├── CustomerManager.js                  # 顧客管理
│       └── CustomerManager.test.js
│
├── integration/
│   ├── edi/
│   │   ├── JapiaEdiFormatter.js                # JAPIA-EDI形式
│   │   ├── JapiaEdiFormatter.test.js
│   │   ├── EdiClient.js                        # EDI通信クライアント
│   │   └── EdiClient.test.js
│   │
│   ├── inspection/
│   │   ├── InspectionCertificateReader.js      # 車検証読取
│   │   └── InspectionCertificateReader.test.js
│   │
│   ├── obd/
│   │   ├── OBDConnector.js                     # OBD診断機連携
│   │   └── OBDConnector.test.js
│   │
│   └── security/
│       ├── VehicleDataEncryption.js            # 車両情報暗号化
│       ├── VehicleDataEncryption.test.js
│       ├── AuditLogger.js                      # 監査ログ
│       └── AuditLogger.test.js
│
├── batch/
│   ├── daily/
│   │   ├── DailyInventorySummary.js           # 日次在庫集計
│   │   └── DailyRevenueSummary.js             # 日次売上集計
│   │
│   ├── monthly/
│   │   ├── MonthlyRevenueReport.js            # 月次売上レポート
│   │   └── MonthlyInventoryReport.js          # 月次在庫レポート
│   │
│   └── notification/
│       ├── InspectionExpiryNotification.js     # 車検満了通知
│       └── MaintenanceReminder.js              # 点検リマインダー
│
└── common/
    ├── utils/
    │   ├── DateUtils.js                        # 日付ユーティリティ
    │   ├── ValidationUtils.js                  # バリデーション
    │   └── FormatUtils.js                      # フォーマット処理
    │
    └── constants/
        ├── VehicleTypes.js                     # 車種定数
        ├── ErrorCodes.js                       # エラーコード
        └── BusinessRules.js                    # 業務ルール定数
```

---

## 仕様書への記録方法

### specifications/implementation_spec_auto.md の構成

```markdown
# 実装仕様書 - 自動車アフター業界システム

## 1. 概要
実装における技術的な詳細と、具体的なコード例を記載します。

## 2. アーキテクチャ概要
[システム構成図]

## 3. ドメインロジック実装

### 3.1 車両管理機能

#### 3.1.1 車検満了日計算
**概要**: 車種と初度登録日から車検満了日を自動計算する

**配置先**: `src/domain/vehicle/VehicleInspectionCalculator.js`

```javascript
/**
 * 車検満了日計算クラス
 * 道路運送車両法に基づく車検有効期間の計算
 */
class VehicleInspectionCalculator {
  /**
   * 車検満了日を計算
   * @param {Date} firstRegistration - 初度登録年月日
   * @param {string} vehicleType - 車種区分
   * @param {boolean} isFirstInspection - 初回車検かどうか
   * @returns {Date} 車検満了日
   */
  static calculateExpiryDate(firstRegistration, vehicleType, isFirstInspection = true) {
    const base = new Date(firstRegistration);
    let years;
    
    // 車種別の車検期間
    const inspectionPeriods = {
      'PASSENGER_PRIVATE': { first: 3, subsequent: 2 },      // 自家用乗用車
      'PASSENGER_COMMERCIAL': { first: 2, subsequent: 1 },   // 事業用乗用車
      'LIGHT_VEHICLE': { first: 3, subsequent: 2 },         // 軽自動車
      'TRUCK_SMALL': { first: 2, subsequent: 1 },           // 小型貨物
      'TRUCK_LARGE': { first: 1, subsequent: 1 },           // 大型貨物
      'SPECIAL_PURPOSE': { first: 2, subsequent: 1 }        // 特種用途
    };
    
    const period = inspectionPeriods[vehicleType] || inspectionPeriods['PASSENGER_PRIVATE'];
    years = isFirstInspection ? period.first : period.subsequent;
    
    // 満了日計算（月末調整含む）
    base.setFullYear(base.getFullYear() + years);
    
    // 2月29日の場合の調整
    if (base.getMonth() === 1 && base.getDate() === 29) {
      if (!this.isLeapYear(base.getFullYear())) {
        base.setDate(28);
      }
    }
    
    return base;
  }
  
  /**
   * うるう年判定
   * @private
   */
  static isLeapYear(year) {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
  }
  
  /**
   * 車検期限までの残日数を計算
   * @param {Date} expiryDate - 車検満了日
   * @returns {number} 残日数
   */
  static getDaysUntilExpiry(expiryDate) {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    expiryDate.setHours(0, 0, 0, 0);
    
    const diffTime = expiryDate - today;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    
    return diffDays;
  }
}

module.exports = VehicleInspectionCalculator;
```

**テストコード配置先**: `src/domain/vehicle/VehicleInspectionCalculator.test.js`

```javascript
const VehicleInspectionCalculator = require('./VehicleInspectionCalculator');

describe('VehicleInspectionCalculator', () => {
  test('新車乗用車の初回車検は3年後', () => {
    const firstRegistration = new Date('2024-01-15');
    const expiryDate = VehicleInspectionCalculator.calculateExpiryDate(
      firstRegistration,
      'PASSENGER_PRIVATE',
      true
    );
    expect(expiryDate).toEqual(new Date('2027-01-15'));
  });
  
  test('中古乗用車の継続車検は2年後', () => {
    const firstRegistration = new Date('2024-01-15');
    const expiryDate = VehicleInspectionCalculator.calculateExpiryDate(
      firstRegistration,
      'PASSENGER_PRIVATE',
      false
    );
    expect(expiryDate).toEqual(new Date('2026-01-15'));
  });
  
  test('うるう年の2月29日の処理', () => {
    const firstRegistration = new Date('2024-02-29'); // 2024年はうるう年
    const expiryDate = VehicleInspectionCalculator.calculateExpiryDate(
      firstRegistration,
      'PASSENGER_PRIVATE',
      false
    );
    // 2026年は平年なので2月28日になる
    expect(expiryDate).toEqual(new Date('2026-02-28'));
  });
});
```

#### 3.1.2 VINデコード処理
[同様の形式で記載]

### 3.2 整備業務機能

#### 3.2.1 標準作業点数計算
**概要**: 日整連標準作業点数表に基づく工賃計算

**配置先**: `src/domain/maintenance/LaborCalculator.js`

```javascript
/**
 * 標準作業点数による工賃計算クラス
 */
class LaborCalculator {
  constructor(config = {}) {
    this.hourlyRate = config.hourlyRate || 8000; // 時間あたり工賃（デフォルト8,000円）
    this.pointToHour = 0.1; // 1点 = 0.1時間
    
    // 作業項目別の標準点数（サンプル）
    this.standardPoints = {
      // エンジン関連
      'ENG_OIL_CHANGE': 3,           // エンジンオイル交換
      'ENG_OIL_FILTER': 2,           // オイルフィルター交換
      'ENG_AIR_FILTER': 2,           // エアフィルター交換
      'ENG_SPARK_PLUG_4': 8,         // スパークプラグ交換(4気筒)
      'ENG_SPARK_PLUG_6': 12,        // スパークプラグ交換(6気筒)
      
      // ブレーキ関連
      'BRK_PAD_FRONT': 8,            // フロントブレーキパッド交換
      'BRK_PAD_REAR': 10,            // リアブレーキパッド交換
      'BRK_DISC_FRONT': 12,          // フロントブレーキディスク交換
      'BRK_FLUID': 6,                // ブレーキフルード交換
      
      // タイヤ関連
      'TIRE_ROTATION': 4,            // タイヤローテーション
      'TIRE_CHANGE_4': 8,            // タイヤ交換(4本)
      'TIRE_BALANCE_4': 8,           // ホイールバランス(4本)
      
      // 車検・点検
      'INSPECTION_BASIC': 100,       // 車検基本点検
      'INSPECTION_12M': 60           // 12ヶ月点検
    };
  }
  
  /**
   * 作業項目から工賃を計算
   * @param {Array} workItems - 作業項目リスト
   * @returns {Object} 計算結果
   */
  calculate(workItems) {
    const details = workItems.map(item => {
      const points = this.getStandardPoints(item.code, item.customPoints);
      const hours = points * this.pointToHour;
      const laborCost = Math.floor(hours * this.hourlyRate);
      
      return {
        code: item.code,
        name: item.name,
        points: points,
        hours: hours,
        laborCost: laborCost,
        partsCost: item.partsCost || 0,
        totalCost: laborCost + (item.partsCost || 0)
      };
    });
    
    const summary = {
      totalPoints: details.reduce((sum, item) => sum + item.points, 0),
      totalHours: details.reduce((sum, item) => sum + item.hours, 0),
      totalLaborCost: details.reduce((sum, item) => sum + item.laborCost, 0),
      totalPartsCost: details.reduce((sum, item) => sum + item.partsCost, 0),
      grandTotal: details.reduce((sum, item) => sum + item.totalCost, 0)
    };
    
    return {
      details: details,
      summary: summary
    };
  }
  
  /**
   * 作業コードから標準点数を取得
   * @private
   */
  getStandardPoints(code, customPoints) {
    if (customPoints !== undefined) {
      return customPoints;
    }
    return this.standardPoints[code] || 10; // デフォルト10点
  }
  
  /**
   * 割引を適用
   * @param {number} amount - 元の金額
   * @param {number} discountRate - 割引率（0.1 = 10%）
   * @returns {number} 割引後の金額
   */
  applyDiscount(amount, discountRate) {
    const discountAmount = Math.floor(amount * discountRate);
    return amount - discountAmount;
  }
}

module.exports = LaborCalculator;
```

[以下、同様の形式で各機能の実装コードを記載]

### 3.3 在庫管理機能

#### 3.3.1 在庫引当処理
**配置先**: `src/domain/inventory/InventoryAllocator.js`

[実装コード]

## 4. 外部連携実装

### 4.1 EDI連携

#### 4.1.1 JAPIA-EDIフォーマッター
**配置先**: `src/integration/edi/JapiaEdiFormatter.js`

[実装コード]

## 5. バッチ処理実装

### 5.1 日次バッチ

#### 5.1.1 日次在庫集計
**配置先**: `src/batch/daily/DailyInventorySummary.js`

[実装コード]

## 6. セキュリティ実装

### 6.1 データ暗号化

#### 6.1.1 車両情報暗号化
**配置先**: `src/integration/security/VehicleDataEncryption.js`

[実装コード]

## 7. パフォーマンス最適化

### 7.1 キャッシュ実装
[実装コード]

### 7.2 インデックス設計
[SQL定義]
```

---

## 実装コードの整理

### コーディング規約（coding_standards_auto.md）

```markdown
# コーディング規約 - 自動車アフター業界システム

## 1. 命名規則

### 1.1 業界用語の使用
- 車検: `inspection` (checkではない)
- 整備: `maintenance` (repairは修理の意味)
- 部品: `part` (componentは避ける)
- 工賃: `labor` (workは使わない)

### 1.2 定数名
```javascript
// 車種区分
const VEHICLE_TYPES = {
  PASSENGER_PRIVATE: '自家用乗用車',
  PASSENGER_COMMERCIAL: '事業用乗用車',
  LIGHT_VEHICLE: '軽自動車'
};

// エラーコード
const ERROR_CODES = {
  INVALID_VIN: 'E001',
  INSPECTION_EXPIRED: 'E002',
  INSUFFICIENT_STOCK: 'E003'
};
```

## 2. エラーハンドリング

### 2.1 業界特有のエラー
```javascript
class InsufficientStockError extends Error {
  constructor(partNumber, required, available) {
    super(`在庫不足: 部品番号${partNumber} 必要数${required} 在庫数${available}`);
    this.partNumber = partNumber;
    this.required = required;
    this.available = available;
  }
}
```

## 3. ログ出力

### 3.1 監査ログ
```javascript
// 整備記録の変更は必ず監査ログに記録
logger.audit({
  action: 'MAINTENANCE_RECORD_UPDATE',
  vehicleId: vehicle.id,
  userId: user.id,
  before: oldRecord,
  after: newRecord,
  timestamp: new Date()
});
```
```

---

## テンプレート管理

### templates/implementation_templates/

#### vehicle_inspection_calc.js.template
```javascript
/**
 * 車検満了日計算テンプレート
 * 
 * 使用方法:
 * 1. このファイルをコピー
 * 2. 車種区分を追加・修正
 * 3. テストケースを追加
 */
class VehicleInspectionCalculator {
  static calculateExpiryDate(firstRegistration, vehicleType, isFirstInspection = true) {
    // 実装
  }
}
```

#### labor_calculator.js.template
```javascript
/**
 * 工賃計算テンプレート
 * 
 * カスタマイズポイント:
 * - hourlyRate: 時間単価
 * - standardPoints: 作業別標準点数
 */
class LaborCalculator {
  constructor(config = {}) {
    this.hourlyRate = config.hourlyRate || 8000;
    // 実装
  }
}
```

---

## 実装例

### 1. 新規機能追加の流れ

```bash
# 1. 仕様確認
You: @auto-implementation-agent 
リコール情報管理機能の実装仕様を作成してください

Claude (as auto-implementation-agent): 
specifications/implementation_spec_auto.md に以下を追加します：

### 3.4 リコール情報管理

#### 3.4.1 リコール情報取得
**配置先**: `src/domain/vehicle/RecallManager.js`

[実装コード...]

# 2. ファイル作成
mkdir -p src/domain/vehicle
touch src/domain/vehicle/RecallManager.js
touch src/domain/vehicle/RecallManager.test.js

# 3. 実装
# specifications/implementation_spec_auto.md のコードをコピー

# 4. テスト実行
npm test src/domain/vehicle/RecallManager.test.js
```

### 2. 既存機能の修正

```bash
You: @auto-implementation-agent 
車検満了日計算にリマインダー日数を追加したい

Claude: implementation_spec_auto.md の該当箇所を更新します：

#### 3.1.1 車検満了日計算（更新）
**更新内容**: リマインダー日数の設定機能を追加

```javascript
class VehicleInspectionCalculator {
  // 既存のメソッドに加えて
  
  /**
   * リマインダー日を計算
   * @param {Date} expiryDate - 車検満了日
   * @param {Array<number>} reminderDays - 通知日数配列 [60, 30, 7]
   * @returns {Array<Date>} リマインダー日付配列
   */
  static calculateReminderDates(expiryDate, reminderDays = [60, 30, 7]) {
    return reminderDays.map(days => {
      const reminderDate = new Date(expiryDate);
      reminderDate.setDate(reminderDate.getDate() - days);
      return reminderDate;
    });
  }
}
```

ファイルを更新しました。
```

### 3. パフォーマンスチューニング

```javascript
// specifications/performance_spec.md に記載
// src/domain/vehicle/VehicleSearchOptimized.js として実装

/**
 * 車両検索の最適化実装
 */
class VehicleSearchOptimized {
  constructor(db, cache) {
    this.db = db;
    this.cache = cache;
  }
  
  async searchByExpiryDate(startDate, endDate) {
    // キャッシュキー生成
    const cacheKey = `expiry:${startDate}:${endDate}`;
    
    // キャッシュ確認
    const cached = await this.cache.get(cacheKey);
    if (cached) {
      return JSON.parse(cached);
    }
    
    // DB検索（インデックス使用）
    const vehicles = await this.db.query(`
      SELECT v.*, c.name as owner_name
      FROM vehicles v
      INNER JOIN customers c ON v.owner_customer_id = c.id
      WHERE v.inspection_expiry_date BETWEEN ? AND ?
      ORDER BY v.inspection_expiry_date
    `, [startDate, endDate]);
    
    // キャッシュ保存（5分間）
    await this.cache.setex(cacheKey, 300, JSON.stringify(vehicles));
    
    return vehicles;
  }
}
```

---

## まとめ

### ファイル配置の原則

1. **仕様書** (`specifications/`)
   - すべての実装コードを含む
   - 配置先を明記
   - 実装の意図を説明

2. **ソースコード** (`src/`)
   - ドメイン別に整理
   - テストコードと同じ場所
   - 明確な責務分離

3. **テンプレート** (`templates/`)
   - 再利用可能な形式
   - カスタマイズポイント明記
   - 使用方法を含む

4. **ドキュメント**
   - 実装ガイド
   - コーディング規約
   - アーキテクチャ説明

この構造により、仕様から実装まで一貫した管理が可能となります。