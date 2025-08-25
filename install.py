#!/usr/bin/env python3
"""
Spec Agent Installer for Claude Code CLI
汎用仕様書作成Agent群のインストーラー
"""

import os
import sys
import shutil
import platform
import json
from pathlib import Path
import argparse
import subprocess

class SpecAgentInstaller:
    def __init__(self):
        self.system = platform.system()
        self.home = Path.home()
        self.script_dir = Path(__file__).parent.resolve()
        
        # Claude Code設定ディレクトリの検出
        if self.system == "Windows":
            self.claude_base = self.home / "AppData" / "Roaming" / "claude-code"
        elif self.system == "Darwin":  # macOS
            self.claude_base = self.home / "Library" / "Application Support" / "claude-code"
        else:  # Linux
            self.claude_base = self.home / ".config" / "claude-code"
        
        # エージェントファイル
        self.agent_files = [
            "spec-master-agent.md",
            "requirement-analyst-agent.md",
            "system-architect-agent.md",
            "implementation-spec-agent.md",
            "technical-writer-agent.md",
            "qa-reviewer-agent.md",
            "coordination_rules.yaml"
        ]
        
        # テンプレートファイル
        self.template_files = [
            "progress.md",
            "todo.md"
        ]

    def check_claude_code(self):
        """Claude Codeのインストール確認"""
        try:
            result = subprocess.run(["claude", "--version"], 
                                  capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                print("✅ Claude Code CLI が検出されました")
                return True
        except:
            pass
        
        print("❌ Claude Code CLI が見つかりません")
        print("   以下のコマンドでインストールしてください:")
        print("   npm install -g @anthropic-ai/claude-code")
        return False

    def select_installation_type(self):
        """インストールタイプの選択"""
        print("\nインストールタイプを選択してください:")
        print("1. ユーザーレベル（このユーザー専用）")
        print("2. プロジェクトレベル（現在のプロジェクトのみ）")
        
        while True:
            choice = input("\n選択 (1 or 2): ").strip()
            if choice == "1":
                return "user"
            elif choice == "2":
                return "project"
            else:
                print("無効な選択です。1 または 2 を入力してください。")

    def get_installation_path(self, install_type):
        """インストールパスの取得"""
        if install_type == "user":
            # ユーザーレベル: ~/.claude/agents/spec-agent/
            if self.system == "Windows":
                base = self.home / ".claude"
            else:
                base = self.home / ".claude"
            return base / "agents" / "spec-agent"
        else:
            # プロジェクトレベル: ./.claude/agents/
            return Path.cwd() / ".claude" / "agents"

    def create_config(self, install_path, install_type):
        """設定ファイルの作成"""
        config = {
            "name": "spec-agent",
            "version": "1.0.0",
            "type": install_type,
            "description": "汎用仕様書作成Agent群",
            "agents": {
                "spec-master": {
                    "file": "spec-master-agent.md",
                    "description": "仕様書作成プロセス全体を管理"
                },
                "requirement-analyst": {
                    "file": "requirement-analyst-agent.md",
                    "description": "要求分析専門"
                },
                "system-architect": {
                    "file": "system-architect-agent.md",
                    "description": "システム設計専門"
                },
                "implementation-spec": {
                    "file": "implementation-spec-agent.md",
                    "description": "実装仕様専門"
                },
                "technical-writer": {
                    "file": "technical-writer-agent.md",
                    "description": "ドキュメント整形専門"
                },
                "qa-reviewer": {
                    "file": "qa-reviewer-agent.md",
                    "description": "品質レビュー専門"
                }
            },
            "templates": {
                "progress": "progress.md",
                "todo": "todo.md"
            },
            "rules": "coordination_rules.yaml"
        }
        
        config_file = install_path / "spec-agent-config.json"
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        
        return config_file

    def copy_files(self, install_path):
        """ファイルのコピー"""
        # エージェントファイルのコピー
        for file in self.agent_files:
            src = self.script_dir / file
            dst = install_path / file
            if src.exists():
                shutil.copy2(src, dst)
                print(f"  ✅ {file}")
            else:
                print(f"  ⚠️  {file} が見つかりません")
        
        # テンプレートファイルのコピー
        templates_dir = install_path / "templates"
        templates_dir.mkdir(exist_ok=True)
        
        for file in self.template_files:
            src = self.script_dir / file
            dst = templates_dir / file
            if src.exists():
                shutil.copy2(src, dst)
                print(f"  ✅ templates/{file}")

    def create_activation_script(self, install_path, install_type):
        """アクティベーションスクリプトの作成"""
        if install_type == "user":
            # ユーザーレベルの場合、グローバル設定に追加
            claude_config = self.claude_base / "config.json"
            
            if claude_config.exists():
                with open(claude_config, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            else:
                config = {}
            
            if "agents" not in config:
                config["agents"] = {}
            
            config["agents"]["spec-agent"] = {
                "path": str(install_path),
                "enabled": True
            }
            
            claude_config.parent.mkdir(parents=True, exist_ok=True)
            with open(claude_config, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            
            print(f"\n✅ ユーザー設定に追加されました: {claude_config}")
        
        else:
            # プロジェクトレベルの場合、プロジェクト設定を作成
            project_config = Path.cwd() / ".claude" / "project.json"
            
            if project_config.exists():
                with open(project_config, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            else:
                config = {"name": Path.cwd().name}
            
            config["agents"] = {
                "spec-agent": {
                    "path": "./agents",
                    "enabled": True
                }
            }
            
            project_config.parent.mkdir(parents=True, exist_ok=True)
            with open(project_config, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            
            print(f"\n✅ プロジェクト設定に追加されました: {project_config}")

    def install(self):
        """インストール実行"""
        print("=" * 60)
        print("Spec Agent Installer for Claude Code CLI")
        print("汎用仕様書作成Agent群 インストーラー")
        print("=" * 60)
        
        # Claude Code確認
        if not self.check_claude_code():
            return False
        
        # インストールタイプ選択
        install_type = self.select_installation_type()
        
        # インストールパス決定
        install_path = self.get_installation_path(install_type)
        
        print(f"\nインストール先: {install_path}")
        
        # 既存インストールの確認
        if install_path.exists():
            response = input("\n既にインストールされています。上書きしますか？ (y/n): ")
            if response.lower() != 'y':
                print("インストールをキャンセルしました。")
                return False
            shutil.rmtree(install_path)
        
        # ディレクトリ作成
        install_path.mkdir(parents=True, exist_ok=True)
        
        print("\nファイルをコピー中...")
        
        # ファイルコピー
        self.copy_files(install_path)
        
        # 設定ファイル作成
        config_file = self.create_config(install_path, install_type)
        print(f"\n設定ファイル作成: {config_file}")
        
        # アクティベーションスクリプト作成
        self.create_activation_script(install_path, install_type)
        
        print("\n" + "=" * 60)
        print("✅ インストール完了！")
        print("\n使用方法:")
        print("1. Claude Codeを起動: claude")
        print("2. 以下のコマンドでAgent を呼び出し:")
        print("   @spec-master-agent プロジェクトを開始します")
        print("\n詳細は manual.md を参照してください。")
        print("=" * 60)
        
        return True

def main():
    parser = argparse.ArgumentParser(
        description='Spec Agent installer for Claude Code CLI'
    )
    parser.add_argument('--uninstall', action='store_true',
                       help='Uninstall spec agents')
    
    args = parser.parse_args()
    
    installer = SpecAgentInstaller()
    
    if args.uninstall:
        print("アンインストール機能は別途 uninstall.py を使用してください。")
    else:
        installer.install()

if __name__ == "__main__":
    main()