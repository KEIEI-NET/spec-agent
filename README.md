# 汎用仕様書作成Agent群

ソフトウェア開発プロジェクトの仕様書を体系的に作成するためのマルチエージェントシステムです。

## 概要

6つの専門Agentが協調して、要求分析から実装仕様、品質レビューまでを一貫してサポートします。

## 特徴

- 🤖 **6つの専門Agent** による分業体制
- 📝 **段階的な詳細化** プロセス
- ✅ **品質保証** を組み込んだワークフロー
- 🎯 **あらゆる種類のソフトウェア開発** に対応

## Agent構成

1. **spec-master-agent** - 全体プロセスを管理するマスターAgent
2. **requirement-analyst-agent** - 要求分析専門Agent
3. **system-architect-agent** - システム設計専門Agent
4. **implementation-spec-agent** - 実装仕様専門Agent
5. **technical-writer-agent** - ドキュメント整形専門Agent
6. **qa-reviewer-agent** - 品質レビュー専門Agent

## 使用方法

詳細な使用方法は [manual.md](manual.md) を参照してください。

## ディレクトリ構成

```
spec-agent/
├── *.md                    # 各Agent定義ファイル
├── coordination_rules.yaml # Agent間連携ルール
├── progress.md            # 進捗管理ファイル
├── todo.md               # タスク管理ファイル
├── manual.md             # 詳細マニュアル
├── CLAUDE.md             # Claude Code用ガイド
└── specifications/       # 生成される仕様書（作成時）
```

## クイックスタート

1. Claude Codeでプロジェクトディレクトリを開く
2. `@spec-master-agent` でマスターAgentを呼び出す
3. プロジェクト要件を伝える
4. 段階的に仕様書を作成

## ライセンス

MIT License

## 貢献

Issue や Pull Request を歓迎します。