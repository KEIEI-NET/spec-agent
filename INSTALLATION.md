# Installation Guide - インストールガイド

*バージョン: v2.0.0*
*最終更新: 2025年01月25日 00:30 JST*

## 📌 概要

Spec Agent System は Claude Code CLI のサブエージェントとして動作する、自動仕様書作成システムです。7つの専門エージェントが協調して、包括的な仕様書を自動生成します。ユーザーレベル（全プロジェクト共通）またはプロジェクトレベル（特定プロジェクトのみ）でインストール可能です。

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

### 🪟 Windows

#### 方法1: 改善版インストーラー（推奨）

```cmd
# エラーハンドリング強化版
python install.py
```

#### 方法2: バッチファイルを使用

```cmd
# 管理者権限で実行推奨
install.bat
```

#### 方法3: 標準Pythonスクリプト

```cmd
python install.py
```

### 🐧 Linux / 🍎 macOS

#### 方法1: 改善版インストーラー（推奨）

```bash
# Python 3 を使用
python3 install.py
```

#### 方法2: シェルスクリプトを使用

```bash
# 実行権限を付与
chmod +x install.sh

# インストール実行
./install.sh
```

#### 方法3: 標準Pythonスクリプト

```bash
python3 install.py
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
├── agent/
│   ├── auto-spec-master-agent.md
│   ├── auto-requirement-agent.md
│   ├── auto-system-architect-agent.md
│   ├── auto-implementation-agent.md
│   ├── auto-integration-agent.md
│   ├── auto-qa-reviewer-agent.md
│   └── auto-compliance-agent.md
├── auto_coordination_rules.yaml
├── coordination_rules.yaml
├── carafter.md
├── progress.md
├── todo.md
└── CLAUDE.md
```

## 💻 使用方法

### 1. Claude Code CLIを起動
```bash
claude
```

### 2. Agentを呼び出す

#### マスターAgentを使用
```
@auto-spec-master-agent プロジェクトを開始します
```

#### 個別のAgentを使用
```
@auto-requirement-agent 要求を分析してください
@auto-system-architect-agent アーキテクチャを設計してください
@auto-implementation-agent 実装仕様を作成してください
@auto-integration-agent 統合仕様を作成してください
@auto-qa-reviewer-agent 品質レビューを実施してください
@auto-compliance-agent コンプライアンスチェックを実施してください
```

### 3. プロジェクトでの活用

新しいプロジェクトを開始する際：

1. プロジェクトディレクトリを作成
2. `claude` コマンドでClaude Codeを起動
3. `@auto-spec-master-agent` で仕様書作成を開始
4. 対話的に要件を入力
5. 各フェーズの仕様書が自動的に生成される
6. `carafter.md` に統合された仕様書が出力される

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

*最終更新: 2025年09月01日 14:40 JST*
*バージョン: v2.1.0*

**更新履歴:**
- v2.1.0 (2025年09月01日): ファイル構造を最新版に更新、7つの専門エージェント体制を反映
- v2.0.0 (2025年01月25日): セキュリティ強化版インストーラーを反映、トラブルシューティング充実、OS別詳細手順追加