# Installation Guide - インストールガイド

*バージョン: v2.0.0*
*最終更新: 2025年01月25日 00:30 JST*

## 📌 概要

Spec Agent System は Claude Code CLI のサブエージェントとして動作する、汎用仕様書作成システムです。ユーザーレベル（全プロジェクト共通）またはプロジェクトレベル（特定プロジェクトのみ）でインストール可能です。

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
python install_fixed.py
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
python3 install_fixed.py
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
├── spec-master-agent.md
├── requirement-analyst-agent.md
├── system-architect-agent.md
├── implementation-spec-agent.md
├── technical-writer-agent.md
├── qa-reviewer-agent.md
├── coordination_rules.yaml
├── spec-agent-config.json
└── templates/
    ├── progress.md
    └── todo.md
```

## 💻 使用方法

### 1. Claude Code CLIを起動
```bash
claude
```

### 2. Agentを呼び出す

#### マスターAgentを使用
```
@spec-master-agent プロジェクトを開始します
```

#### 個別のAgentを使用
```
@requirement-analyst-agent 要求を分析してください
@system-architect-agent アーキテクチャを設計してください
@implementation-spec-agent 実装仕様を作成してください
```

### 3. プロジェクトでの活用

新しいプロジェクトを開始する際：

1. プロジェクトディレクトリを作成
2. `claude` コマンドでClaude Codeを起動
3. `@spec-master-agent` で仕様書作成を開始
4. 対話的に要件を入力
5. 各フェーズの仕様書が `specifications/` に生成される

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
~/.claude/agents/spec-agent/[agent-name].md

# プロジェクトレベルの場合
./.claude/agents/[agent-name].md
```

### テンプレートのカスタマイズ

プロジェクト固有のテンプレートを使用する場合：

```bash
# templatesディレクトリ内のファイルを編集
templates/progress.md
templates/todo.md
```

## 📞 サポート

問題が発生した場合は、以下の方法でサポートを受けられます：

- **GitHub Issues**: https://github.com/KEIEI-NET/spec-agent/issues
- **メール**: support@keiei.net
- **Discord**: [Spec Agent Community](https://discord.gg/spec-agent)

---

*最終更新: 2025年01月25日 00:30 JST*
*バージョン: v2.0.0*

**更新履歴:**
- v2.0.0 (2025年01月25日): install_fixed.py の内容を反映、トラブルシューティング充実、OS別詳細手順追加