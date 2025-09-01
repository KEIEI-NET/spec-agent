# Installation Guide - インストールガイド

*バージョン: v1.1.0*
*最終更新: 2025年09月01日 18:20 JST*

## 📌 概要

Spec Agent After は、自動車アフターマーケット業界に特化した仕様書自動作成システムです。部品商社、ガラス専門店、リサイクル業界の各セクターに対応した専門エージェントが、法規制準拠と業界標準に基づいた仕様書を自動生成します。

## ✅ 前提条件

### 必須要件

| 要件 | バージョン | 確認コマンド |
|------|---------|------------|
| Node.js | 14.0以上 | `node --version` |
| npm/yarn | 最新版推奨 | `npm --version` |
| Python | 3.7以上 | `python --version` |
| Claude Code CLI | 最新版 | `claude --version` |

### Claude Code CLI のインストール

```bash
# npm を使用する場合
npm install -g @anthropic-ai/claude-code

# yarn を使用する場合
yarn global add @anthropic-ai/claude-code

# インストール確認
claude --version
```

## 🚀 インストール方法

### 📋 検証済みインストーラー使用（推奨）

新しい `install_new.py` は全機能テスト済みで、エラーハンドリングが強化されています。

#### 🪟 Windows

```cmd
# 新インストーラーを使用
python install_new.py

# または旧版（互換性維持）
python install.py
```

#### 🐧 Linux / 🍎 macOS

```bash
# 新インストーラーを使用（推奨）
python3 install_new.py

# テストモードで確認
python3 install_new.py --test

# 本番インストール
python3 install_new.py --type user
```

### 🧪 インストール前テスト

インストール前に仮想環境でテストすることを推奨します：

```bash
# 仮想環境でテスト実行
python3 install_new.py --test

# 成功メッセージ確認
# ✅ テストインストール成功！
# 📊 39/39 ファイルが正常にインストールされました
```

## 📝 インストールタイプ

### 1. ユーザーレベル
- **インストール先**: `~/.claude/agents/spec-agent/`
- **対象**: 現在のユーザーのすべてのプロジェクト
- **用途**: 複数のプロジェクトで spec-agent を使用する場合

### 2. プロジェクトレベル
- **インストール先**: `./.claude/agents/`
- **対象**: 現在のプロジェクトのみ
- **用途**: 特定のプロジェクト専用に設定をカスタマイズする場合

## ✅ インストール後の確認

インストールが成功すると、以下のファイル構造が作成されます：

```
[インストール先]/
├── agent/                          # 基本エージェント（7ファイル）
│   ├── auto-spec-master-agent.md
│   ├── auto-requirement-agent.md
│   ├── auto-system-architect-agent.md
│   ├── auto-implementation-agent.md
│   ├── auto-integration-agent.md
│   ├── auto-qa-reviewer-agent.md
│   └── auto-compliance-agent.md
├── sector-modules/
│   ├── sector-coordinator.yaml
│   ├── parts-commerce/            # 部品商社セクター（拡張版）
│   │   ├── agents/
│   │   │   ├── parts-catalog-agent.md
│   │   │   ├── inventory-forecast-agent.md
│   │   │   ├── compliance-verification-agent.md
│   │   │   ├── commercial-vehicle-parts-agent.md  # 🆕 大型車両対応
│   │   │   └── european-vehicle-parts-agent.md    # 🆕 欧州車対応
│   │   ├── regulations/
│   │   │   ├── pl-law.yaml
│   │   │   └── iatf16949.yaml
│   │   └── multi-brand-compatibility.yaml         # 🆕 全メーカー対応
│   ├── glass-specialty/
│   │   ├── agents/
│   │   │   ├── adas-calibration-agent.md
│   │   │   ├── glass-specification-agent.md
│   │   │   └── insurance-integration-agent.md
│   │   └── regulations/
│   │       ├── adas-regulation.yaml
│   │       └── ece-r43.yaml
│   └── recycling-compliance/
│       ├── agents/
│       │   ├── dismantling-process-agent.md
│       │   ├── circular-economy-agent.md
│       │   └── manifest-management-agent.md
│       └── regulations/
│           ├── auto-recycling-law.yaml
│           ├── freon-law.yaml
│           └── ev-battery-law.yaml
├── cross-sector-functions/
│   ├── supply-chain-integration.yaml
│   ├── carbon-footprint-tracker.yaml
│   └── circular-economy-metrics.yaml
├── coordination_rules.yaml
├── auto_coordination_rules.yaml
├── ドキュメント/
│   ├── README.md
│   ├── CLAUDE.md
│   ├── INSTALLATION.md
│   ├── USAGE.md
│   ├── DOCUMENTATION_STATUS.md
│   ├── progress.md
│   └── todo.md
```

### 📊 インストール統計
- **総ファイル数**: 39ファイル
- **エージェント数**: 18個（基本7 + セクター別11）
- **対応メーカー**: 20社以上

## 💻 使用方法

### 1. Claude Code CLIを起動
```bash
claude
```

### 2. エージェントを呼び出す

#### 統括エージェントを使用
```
@spec-master-agent 部品商社向けの在庫管理システムの仕様書を作成します
```

#### セクター別エージェントの使用

##### 🔧 部品商社セクター
```
@parts-catalog-agent 部品マスターデータ管理システムの仕様を作成
@inventory-forecast-agent AI需要予測システムの仕様を作成  
@compliance-verification-agent PL法準拠の品質管理システム仕様を作成
```

##### 🪟 ガラス専門セクター
```
@adas-calibration-agent ADAS校正作業管理システムの仕様を作成
@glass-specification-agent ガラス型式データベースシステムの仕様を作成
@insurance-integration-agent 保険会社直接請求システムの仕様を作成
```

##### ♻️ リサイクルセクター
```
@dismantling-process-agent 解体工程最適化システムの仕様を作成
@circular-economy-agent 資源循環追跡システムの仕様を作成
@manifest-management-agent 電子マニフェスト管理システムの仕様を作成
```

### 3. プロジェクトでの活用

新しい業界特化プロジェクトを開始する際：

1. プロジェクトディレクトリを作成
2. `claude` コマンドでClaude Codeを起動
3. `@spec-master-agent` で対象セクターを指定
4. 業界固有の要件を入力（法規制、業界標準等）
5. 各エージェントが協調して仕様書を生成
6. `specifications/` ディレクトリに成果物が出力される

## 🗑️ アンインストール

### Pythonスクリプトを使用
```bash
python uninstall.py
# または
python3 uninstall.py
```

### 強制アンインストール（すべて削除）
```bash
python uninstall.py --all --force
```

## 🔧 トラブルシューティング

### Claude Code CLIが見つからない場合
```bash
npm install -g @anthropic-ai/claude-code
```

### Pythonが見つからない場合（Windows）
- Python公式サイトからインストール: https://www.python.org/
- またはバッチファイル（install.bat）を使用

### 権限エラーが発生する場合（Linux/macOS）
```bash
sudo ./install.sh
```

### Agentが認識されない場合

1. Claude Codeを再起動
2. 設定ファイルを確認：
   - ユーザーレベル: `~/.claude/agents/spec-agent/spec-agent-config.json`
   - プロジェクトレベル: `./.claude/project.json`

## 🎨 カスタマイズ

### Agent定義の編集

インストール後、各Agentファイル（.md）を編集して動作をカスタマイズできます：

```bash
# ユーザーレベルの場合
~/.claude/agents/spec-agent/agent/[agent-name].md

# プロジェクトレベルの場合
./agent/[agent-name].md
```

### 利用可能なエージェント

- **auto-spec-master-agent**: 全体のコーディネーション
- **auto-requirement-agent**: 要求分析と定義
- **auto-system-architect-agent**: システム設計とアーキテクチャ
- **auto-implementation-agent**: 実装仕様の詳細化
- **auto-integration-agent**: 統合とインターフェース設計
- **auto-qa-reviewer-agent**: 品質保証とレビュー
- **auto-compliance-agent**: コンプライアンスとセキュリティ

### 設定ファイルのカスタマイズ

プロジェクト固有の設定を使用する場合：

```bash
# コーディネーションルールの編集
auto_coordination_rules.yaml
coordination_rules.yaml

# 進捗とタスク管理
progress.md
todo.md

# 統合仕様書
carafter.md
```

## 📞 サポート

問題が発生した場合は、以下の方法でサポートを受けられます：

- **GitHub Issues**: https://github.com/KEIEI-NET/spec-agent/issues
- **メール**: support@keiei.net
- **Discord**: [Spec Agent Community](https://discord.gg/spec-agent)

---

*最終更新: 2025年09月01日 18:20 JST*
*バージョン: v1.1.0*

**更新履歴:**
- v1.1.0 (2025年09月01日): 全メーカー対応版に更新、新インストーラー追加、テスト機能実装
- v1.0.0 (2025年01月25日): 自動車アフターマーケット業界特化版として初版リリース